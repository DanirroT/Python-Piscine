

def main(argc: int, argv: list):
	char_num = 0
	digit = 0
	lower_alp = 0
	upper_alp = 0
	space = 0
	ponct = 0

	if argc == 0:
		read()
		argc = 1
	elif argc > 1:
		print("AssertionError")
		return
	if argc == 1:
		s = argv[1]
		for c in s:
			char_num++
			if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				upper_alp++
			elif c in "abcdefghijklmnopqrstuvwxyz":
				lower_alp++
			elif c in "1234567890":
				digit++
			elif c in " \n\t\v\f\r":
				space++
			elif c in ".:,;!?":
				ponct++

		print(f"""The text contains {171} characters:
			{upper_alp} upper letters
			{lower_alp} lower letters
			{ponct} punctuation marks
			{space} spaces
			{digit} digits""")