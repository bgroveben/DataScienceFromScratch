# Special thanks to Stephen Colbert for making up the word 'truthiness'.

# Booleans in Python work the same as in most other languages, just remember to Capitalize them.
one_is_less_than_two = 1 < 2
print one_is_less_than_two
true_equals_false = True == False
print true_equals_false
print

# Python uses the value None to indicate a nonexistent value -- comparable to null in other languages.
x = None
print x == None  # True, but not Pythonic
print x is None  # True as well as Pythonic
print

# The following are treated as False:
"""
False
None
[] (empty list)
{} (empty dict)
""
set()
0
0.0
"""
# Pretty much everything else is treated as True.
# Now, this allows you to use if statements to test for empty lists, strings, or dictionaries;
# However, this can cause tricky bugs if you're not careful.
"""
s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

# A simpler way of doing the same is:
first_char = s and s[0]
# Because and returns the second value when the first is truthy, the first value when it's not.
"""
# Similarly, if x is either a number or possibly None:
safe_x = x or 0  # is definitely a number

# Python has an all function which takes a list and returns True when every element is truthy.
# There is also an any function that returns True when at least one element is truthy.
print all([True, 1, { 3 }])
print all([True, 1, {}])
print any([True, 1, {}])
print all([])
print all([{}])
print any([])
