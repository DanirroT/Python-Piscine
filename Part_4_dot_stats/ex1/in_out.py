# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    in_out.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 17:31:13 by dmota-ri          #+#    #+#              #
#    Updated: 2026/02/01 18:06:44 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def square(x: int | float) -> int | float:
	return x ** 2
	
def pow(x: int | float) -> int | float:
	return x ** x

def outer(x: int | float, function) -> object:
	count = 0
	def inner() -> float:
		nonlocal count
		if count == 0:
			count = x
		count = function(count)
		return count
	return inner

