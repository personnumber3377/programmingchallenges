

segment .data

priorities: db 0x1b,0x1c,0x1d,0x1e,0x1f,0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c,0x2d,0x2e,0x2f,0x30,0x31,0x32,0x33,0x34,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf,0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a


strings_do_not_share_char_msg: db "Strings do not share an element",0

segment .bss

inputstring1:	resb 255
inputstring2:	resb 255
inputstring3:	resb 255
len1:	resb 1
len2:	resb 1
len3:	resb 1
charcounts:	resb 52


occurredbefore:	resb	26+26

priority_sum: resb 4
outputinteger: resb 10

segment .text

global _start

itoa:		
        test    rdi, rdi                        ; value = rdi
        jz      itoa.iszero                     ; value==0 has a direct solution
        jns     itoa.notneg                     ; if(value <0 )
        mov     byte [rsi], '-'                 ;       *s = '-'
        neg     rdi                             ;       value = -value
        inc     rsi                             ;       s++
.notneg:
        mov     r9b, 1                          ; bool leftzero=true
        mov     r10, 10                         ; base = 10
        mov     rcx, 1000000000000000000        ; divisor = 1000000000000000000
        mov     r8, 19                          ; cont = 19 // Will repeat 19 times
.loop:                                          ; do{
        mov     rax, rdi                        ;   dividend[0..31] = value
        xor 	rdx, rdx                        ;   dividend[32..63] = 0
        idiv    rcx                             ;   rax=(rdx:rax)/rcx ; rdx=(rdx:rax)%rcx
        test    al, al                          ;   digit = rax[0..7]
        jnz     itoa.notdigit0                    ;   if(digit!=0)
        test    r9b, r9b                        ;        if(leftzero)                       
        jnz     itoa.nextdigit                   ;            continue
        jmp     itoa.digit0
.notdigit0:
        xor     r9b, r9b                        ;   leftzero = false
.digit0:        
        add     eax, 48                         ;   digit = '0' + digit
        mov     rdi, rdx                        ;   value %= divisor
        mov     byte [rsi], al                  ;   *p = digit
        inc     rsi                             ;   p++        
.nextdigit:
        mov     rax, rcx                        ;   dividend[0..31] = value
        xor 	rdx, rdx                        ;   dividend[32..63] = 0
        idiv    r10                             ;   rax=(rdx:rax)/10 ; rdx=(rdx:rax)%10
        mov     rcx, rax                        ;   divisor /= 10
        dec     r8                              ;   cont--
        jne     itoa.loop                       ; }while(cont!=0)
.end:             
        mov     byte [rsi], 0                   ; *p = '\0'
        ret
.iszero:
        mov     word [rsi], 0x0030              ; *p = "0" (x86 is little endian)
        ret



error_input_too_large:
	mov rax, 60
	syscall



get_input_old:
	; get input from stdin to the buffer pointed to by rax
	push rdi
	push rsi
	push rdx
	mov rdx, 256 ; maximum number of bytes to read+1
	mov rsi, rax ; rax holds the destination buffer
	mov rdi, 0 ; fd=0
	mov rax, 0 ; sys_read
	syscall
	cmp rax, 256
	jne no_error
	call error_input_too_large
	ret
no_error:
	pop rdx,
	pop rsi
	pop rdi
	ret

get_input:
	
	; the old get_input does not work when piping file input to buffer because piping input uses non canonical mode 🙃


	; push working registers

	push rdi
	push rsi
	push rdx
	push r11
	push r13 ; this is the base buffer
	mov r13, rax
	mov r11, 0 ; char_counter
read_char:
	mov rdx, 1 ; get one character
	mov rsi, rax ; buf+offset is the destination for the one character
	add rsi, r11
	push r11
	mov rdi, 0 ; fd=0=stdin
	mov rax, 0 ; sys_read
	syscall ; read character

	; check if character is newline
	pop r11
	inc r11 ; increment bytes read counter
	mov dl, byte [rsi]

	and rdx, 0xff ; get only least significant byte

	cmp rdx, 0x0a ; compare to newline
	je stringend
	;mov rax, rsi
	;sub rax, r11
	mov rax, r13
	jmp read_char

stringend:
	mov rax, r11 ; move length to rax

	; restore registers
	pop r13
	pop r11
	pop rdx
	pop rsi
	pop rdi
	ret ; return











_start:

loop_start:
	
	mov r10, 0 ; r10 is the priority sum

	; get the three lines:

	mov rax, inputstring1
	call get_input
	dec rax
	cmp rax, 0
	je end ; we read 0 bytes so we are at the end
	
	mov [len1], rax
	mov rax, inputstring2
	call get_input
	dec rax
	mov [len2], rax
	mov rax, inputstring3
	call get_input
	dec rax
	mov [len3], rax
	


	; for string in string: count how many times a specific byte occurs at which point

	; initialize loop counter

	mov r10, 0

	;initialize string counter

	mov r11, 0 ; strlen
	mov r12, 0 ; counter
	mov r8,0 ; working register
	mov r9, 0 ; another working register
loopcompare:
	mov r11, 0
	cmp r10, 3
	je end_processing_strings
	; get string length and put it into r11 and initialize r12 to zero:

	mov r11, [len1+r10] ; get length of the string
	and r11, 0xff
	mov r12, 0

	mov r14, 0



	
	mov r8, inputstring1   ; get address of input string:
	mov r9, 255
	; the multiplier must be inside the rax register
	mov rax, r10

	mul r9   ; multiply 255 by which string we are in
	mov r9, rax
	add r8, r9 ; add the string offset into the string pointer to get the start of the current string


string_loop:
	
	; first fetch byte
	mov r9, 0
	mov r9, [r8]
	and r9, 0x00000000000000ff
	cmp r9, 0x60
	jl oofshit ; if the character is lower case then we need to subtract seven from it because lower case and upper case letters are not next to each other on the ascii table
	sub r9, 6
oofshit:
	sub r9, 'A' ; get the offset into the priorities list

	mov byte r15, [charcounts+r9] ; get the byte

	; check if byte has occurred before
	; check if occurredbefore[thing] == 0

	mov r13, [occurredbefore+r9]
	and r13, 0xff
	cmp r13, 1
	je has_occurred_before ; do not increment as we have found the same character before




	add r15, 1 ; increment
	add r9, charcounts
	mov rax, r15


	mov byte [r9], al
	;mov byte [charcounts+r9], r15 ; put back
	sub r9, charcounts
	mov byte [occurredbefore+r9], 1 ; mark character as seen before

has_occurred_before:
	inc r8
	inc r14
	cmp r14, r11
	je stringdone

	jmp string_loop
stringdone:

	; need to reset the occurredbefore list for the next string.

	push r10 ; save r10
	mov r10, 26+26-1
reset_loop:

	mov byte [occurredbefore+r10], byte 0x00 ; zero out the byte from the list
	
	dec r10
	cmp r10, 0
	jne reset_loop ; if counter has not hit zero then jump to the loop


	pop r10 ; restore r10


	inc r10
	jmp loopcompare





end_processing_strings:
	; now we have gone through all of the three strings and we have made the charcounts list. Loop through every character in the list and see if there is any character which appears in each string


	; save working registers just in case

	push r10
	push r11
	push rax

	mov r10, 26+26 ; counter

check_three:
	mov rax, [charcounts+r10]
	cmp al, 3 ; compare if three
	je match_found
	cmp r10, 0
	je error_strings_do_not_share_char ; this is the case when the three strings do not have a common character
	dec r10
	jmp check_three


match_found:
	
	; now we need to first get the priority from the priorities list

	mov r10, [priorities+r10]
	and r10, 0xff ; get the byte
	add [priority_sum], r10 ; add the priority to the sum
	pop rax
	pop r11
	pop r10


	; at this point we need to reset the charcounts list


	push r10
	mov r10, 26+26-1
reset_charcounts:

	mov byte [charcounts+r10], byte 0x00 ; zero out the byte from the list
	
	dec r10
	cmp r10, 0
	jne reset_charcounts ; if counter has not hit zero then jump to the loop


	pop r10 ; restore r10


	;inc r10       no need to reset r10

	; mov byte [charcounts+r10], byte 0x00 ; zero also the charcounts list


	
	jmp loop_start



error_strings_do_not_share_char:
	
	pop rax
	pop r11
	pop r10

	mov rax, 1 ; sys_write
	mov rdi, 1 ; stdout
	mov rsi, strings_do_not_share_char_msg
	mov rdx, 32 ; length of string
	syscall ; call sys_write
	mov rax, 60
	syscall


	; pop registers and exit



end:

	mov rdi, [priority_sum]
	and rdi, 0xffffffff
	mov rsi, outputinteger
	call itoa

	; write the integer to the output
	mov rdx, 10 ; write ten characters max
	mov rax, 1 ; sys_write
	mov rdi, 1
	mov rsi, outputinteger
	syscall 


	mov rax, 60
	syscall

	




; TODO:
; the bug is that the get_input function reads the entire line including newlines.
; this is a problem since the input is passed with ./rucksack < input.txt which exhibits this behaviour.

