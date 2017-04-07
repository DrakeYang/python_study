import re

in_file = open('hangman.py')
out_file = open('hangman_out.py','w')
#lines=f.readlines()

try:
	for line in in_file:
	    out_file.write(line[5:])

finally:
	in_file.close()
	out_file.close()