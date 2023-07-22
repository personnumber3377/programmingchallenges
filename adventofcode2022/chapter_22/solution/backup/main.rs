
//use std::io;
use std::io::{self, BufRead};

// Thanks to https://stackoverflow.com/questions/56921637/how-do-i-split-a-string-using-a-rust-regex-and-keep-the-delimiters

use regex::Regex; // 1.1.8

fn split_keep<'a>(r: &Regex, text: &'a str) -> Vec<&'a str> {
    let mut result = Vec::new();
    let mut last = 0;
    for (index, matched) in text.match_indices(r) {
        if last != index {
            result.push(&text[last..index]);
        }
        result.push(matched);
        last = index + matched.len();
    }
    if last < text.len() {
        result.push(&text[last..]);
    }
    result
}


fn parse_input() -> (Vec<Vec<i32>>, Vec<i32>, Vec<i32>, Vec<i32>) {

    // Go through all the lines in stdin

    //let out_map: Vec<i32> = Vec::new();

    let mut out_map = Vec::new();

    let mut moves: Vec<i32> = Vec::new();

    let mut line_offsets: Vec<i32> = Vec::new();

    let stdin = io::stdin();
    //let mut lines = stdin.lock().lines();

    let mut lines = stdin.lock().lines();



    loop {
        //println!("{}", line.unwrap());

        let cur_line = lines.next().unwrap().unwrap(); 
        println!("Current line: {}\n", cur_line);
        if cur_line.eq("") {

            break;

        }




        //let current_chars: Vec<i32> = String::from(cur_line).chars(); // Get string.

        // rent_chars[offset as usize].eq(


        //let current_chars: std::str::Chars = String::from(cur_line).chars().to_vec();

        let current_chars: Vec<char> = String::from(cur_line).chars().collect();

        let mut offset: i32 = 0;

        // Calculate offset

        loop {
            
            //if !current_chars[offset as usize].eq(" ") {
            println!("{}", offset);
            if !(current_chars[offset as usize]== 32 as char) {
                break;

            }
            offset += 1;

        }

        // Append to offsets.

        line_offsets.push(offset);

        // let last3 = v.as_slice()[v.len()-3..].to_vec();
        // thanks to https://stackoverflow.com/questions/44549759/return-last-n-elements-of-vector-in-rust-without-mutating-the-vector

        let mut new_line: Vec<i32> = Vec::new();

        //for c in new_line.as_slice()[offset as usize..].to_vec() {
        for c in current_chars.as_slice()[offset as usize..].to_vec() {

            if c == 46 as char { // ascii character code of 46 is the dot character (".")
                new_line.push(0);
            } else {
                // assume "#" character.

                new_line.push(1);

            }


        }

        out_map.push(new_line);

    }


    let move_line = lines.next().unwrap().unwrap(); 

    // now the very last line is the line which tells all of the moves and stuff.

    // Extract integers and moves from string.

    //     let seperator = Regex::new(r"([ ,.]+)").expect("Invalid regex");

    let seperator = Regex::new(r"R|L").expect("Invalid regex");

    let move_stuff = split_keep(&seperator, &move_line);

    let mut move_lenghts: Vec<i32> = Vec::new();

    let mut count: i32 = 0;

    for m in move_stuff {
        if count % 2 == 0 {

            move_lenghts.push(m.parse::<i32>().unwrap());  // modulo two equals zero means length.

        } else {

            assert!(m.eq("L") || m.eq("R")); // Only left and right moves are allowed.
            if m.eq("L") {

                moves.push(0); // 0 == left
            } else {
                moves.push(1); // 1 == right
            }
            //moves.append(m);
        }

        count += 1;

        //move_lenghts.append()

    }






    //(out_map, line_offsets, moves, move_lenghts);

    (out_map, line_offsets, moves, move_lenghts)

}



fn main_loop(game_map: Vec<Vec<i32>>, line_offsets: Vec<i32>, mut moves: Vec<i32>, move_lenghts: Vec<i32>) {

    let mut cur_x: i32 = line_offsets[0]; // This must be here because we start on the top.
    let mut cur_y: i32 = 0;

    let mut distance: i32 = 0;

    let mut turn = 0;

    let mut facing = 0;  // "Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)."

    let mut counter = 0;

    let mut dx = 0;

    let mut dy = 0;

    moves.push(1); // final move does not matter

    for m in moves {

        // Mainloop

        distance = move_lenghts[counter];

        // Try to go forward

        match facing {
            0 => {
                dx = 1;
                dy = 0;
            }
            1 => {
                dx = 0;
                dy = 1;  // Y is one on the highest level and the biggest on the ground.
            }
            2 => {
                dx = -1;
                dy = 0;
            }
            3 => {
                dx = 0;
                dy = -1;
            }
            _ => {
                assert!(false); // shouldn't happen.
            }
        }

        // Try to advance
        println!("facing == {}", facing);
        println!("distance == {}", distance);
        for n in 0..distance {


            cur_x += dx;

            cur_y += dy;

            // check block

            // actual place is cur_x, (line_offsets[cur_y]+cur_x)%game_map[cur_y].len()

            println!("cur_y: {}", cur_y);
            println!("cur_x: {}", cur_x);
            //println!("game_map.len() == {}\n",game_map.len());
            if game_map[(cur_y as usize % game_map.len()) as usize][((line_offsets[(cur_y as usize % game_map.len()) as usize]+cur_x)%(game_map[(cur_y as usize % game_map.len()) as usize].len()) as i32) as usize] == 1 {
                // Blocked

                cur_y -= dy;

                cur_x -= dx;

                break


            }

        }

        if m == 0 {
            facing -= 1; // left
            facing = facing % 4;
        } else {
            // assume right
            facing += 1;
            facing = facing % 4;
        }



        
        counter += 1;



    }
    facing -= 1; // reset the facing because we add one on the last cycle
    println!("Final x: {}\n", cur_x);
    println!("Final y: {}\n", cur_y);


}



fn main() {
    
    //let (game_map: Vec<i32>, line_offsets: Vec<i32>, moves: Vec<i32>, move_lenghts: Vec<i32>) = parse_input();

    //let (game_map, line_offsets, moves, move_lenghts) = parse_input();
    let (game_map, line_offsets, moves, move_lenghts) = parse_input();


    main_loop(game_map, line_offsets, moves, move_lenghts);
}
