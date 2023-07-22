
from colorist import Color




# Do you want to enable debug mode?

DEBUG = True

def good(string):
	print(f"{Color.GREEN}[+] {string}{Color.OFF}")

def fatal(string, exit_code=1):
	print(f"{Color.RED}[!] {string}{Color.OFF}")
	exit(exit_code)

def info(string):
	print(f"{Color.BLUE}[*] {string}{Color.OFF}")
	

def debug(string):
	if DEBUG:
		print(f"{Color.YELLOW}[?] {string}{Color.OFF}")


