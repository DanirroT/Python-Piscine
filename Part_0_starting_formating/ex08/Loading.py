# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 20:21:15 by dmota-ri          #+#    #+#              #
#    Updated: 2026/02/01 19:24:29 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from time import sleep
from tqdm import tqdm

def ft_tqdm(lst: range) -> None:
	range_len = len(lst)
	range_processed = 0

	bar_width_max = os.get_terminal_size().columns - (16 + 27)
#	bar_width_max = 100
	for _elem in lst:
		progress = range_processed / range_len
		filled = int(bar_width_max * progress)
		empty = bar_width_max - filled
		bar = "=" * filled + ">" + " " * (empty - 1)
		print(f"{int(progress * 100):3d}%|[{bar}]| {range_processed}/{range_len}", end="\r", flush=True)
		range_processed += 1
	bar = "=" * bar_width_max + ">"
	print(f"{int(progress * 100):3d}%|[{bar}]| {range_processed}/{range_len}", end="\r", flush=True)
	return(range(range_len))
