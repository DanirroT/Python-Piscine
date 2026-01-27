# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterstring.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 20:21:21 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/26 20:21:22 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



import sys
from ft_filter import ft_filter

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def main():
	argc = len(sys.argv) - 1
	argv = sys.argv

	if argc == 0:
		s = input()
		n = input()
	elif argc == 2:
		s = argv[1]
		n = argv[2]
	elif argc > 2:
		print("AssertionError: the arguments are bad")
		return
	if is_int(n) is False:
		print("AssertionError: the arguments are bad")
		return
	n = int(n)
	split_s = s.split(" ")
	print(list(ft_filter(lambda x: len(x) >= n, split_s)))
	

if __name__ == "__main__":
	main()