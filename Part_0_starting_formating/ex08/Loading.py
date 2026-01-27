# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 20:21:15 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 14:17:54 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from tqdm import tqdm

def ft_tqdm(lst: range) -> None:
	range_len = len(lst)
	range_processed = 0
	loading_bar_size = get_terminal_size().columns - 40
	loading_arrow = f"[{"=" for i in range(loading_bar_size)}>]"
	print(f"{((range_processed/range_len)*100)3i}%|{loading_arrow}| {range_processed} / {range_len}")
	return(range(range_len))

for elem in ft_tqdm(range(333)):
	sleep(0.005)
print()
for elem in tqdm(range(333)):
	sleep(0.005)