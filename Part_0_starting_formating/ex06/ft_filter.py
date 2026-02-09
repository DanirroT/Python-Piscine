
#def is_digit_str(string):
# for char in string:
#  if char.isdigit() == False and char != ' ':
#      return False
# return True
#
#def is_digit_char(char):
# return char.isdigit()


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return (item for item in iterable if function(item))


#strings = ["1234 5678 919", "abcd efgh ijkl", "12ab 34cd 56ef", "!!@@ ##$$ %%^^"]
#string = "12ab 34cd 56ef"
#print("original")
#print()
#print()
#print(str(filter.__doc__))
#print()
#print()
#print(list(filter(is_digit_str, strings)))
#print()
#print()
#print(list(filter(is_digit_char, string)))

#print("Ft_filter")
#print()
#print()
#print(str(ft_filter.__doc__))
#print()
#print()
#print(list(ft_filter(is_digit_str, strings)))
#print()
#print()
#print(list(ft_filter(is_digit_char, string)))