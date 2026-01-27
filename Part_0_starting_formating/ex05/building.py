# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 17:41:49 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/26 20:21:26 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	argc = len(sys.argv) - 1
	argv = sys.argv
	if argc == 0:
		s = input().upper()
	elif argc == 1:
		s = argv[1].upper()
	elif argc > 1:
		print("AssertionError")
		return

	char_num = 0
	digit = 0
	lower_alp = 0
	upper_alp = 0
	space = 0
	ponct = 0

	for c in s:
		char_num += 1
		if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			upper_alp += 1
		elif c in "abcdefghijklmnopqrstuvwxyz":
			lower_alp += 1
		elif c in "1234567890":
			digit += 1
		elif c in " \n\t\v\f\r":
			space += 1
		elif c in ".:,;!?":
			ponct += 1

	print(f"""The text contains {171} characters:
		{upper_alp} upper letters
		{lower_alp} lower letters
		{ponct} punctuation marks
		{space} spaces
		{digit} digits""")
	
if __name__ == "__main__":
	main()