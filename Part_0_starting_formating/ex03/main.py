from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>
# Zero: 0 <class 'int'>
#: <class 'str'>
# Fake: False <class 'bool'>
# Type not Found
# 1

# print("")
# print("prints:")
# print("")
# print(Nothing)
# print(Garlic)
# print(Zero)
# print(Empty)
# print(Fake)
# print(print("Brian"))


# float_nan = float("NaN")
# print(float_nan)

# print(Garlic != float("NaN"))
# print(Garlic != Garlic)
# print(Garlic != 0)
# print(Garlic != float_nan)
