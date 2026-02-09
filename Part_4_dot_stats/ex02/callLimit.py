# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    callLimit.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 18:07:58 by dmota-ri          #+#    #+#              #
#    Updated: 2026/02/01 18:16:13 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		nonlocal count
		def limit_function(*args: any, **kwds: any):
			nonlocal count
			if count >= limit:
				print(f"Error: {function} call too many times")
				return
			count += 1
			return function(*args, **kwds)
		return limit_function
	return callLimiter



@callLimit(3)
def f():
	print ("f()")

@callLimit(1)
def g():
	print ("g()")

for i in range(3):
	f()
	g()
