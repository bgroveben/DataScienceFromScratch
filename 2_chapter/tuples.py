# According to the book, tuples are lists' immutable cousins.
# https://docs.python.org/2/library/functions.html#tuple
# http://www.diveintopython.net/native_data_types/tuples.html
# You specify a tuple by using parentheses instead of square brackets.
# You actually don't even need the parens, but I'm trying to avoid that for the sake of clarity.
t = "a", "b", "c"
print t
print type(t)
print

my_list = [1, 2]
print my_list
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3
print my_list

try:
    my_tuple[1] = 3
except TypeError:
    print "You can't modify a tuple, sucka."
print

# Tuples are a convenient way to return multiple values from functions:
def sum_and_product(x, y):
    return (x + y),(x * y)

sp = sum_and_product(2, 3)
print sp
s, p = sum_and_product(5, 10)
print s, p
print

# Tuples (and lists) can also be used for multiple assignment:
x, y = 1, 2
print x, y
x, y = y, x  # Pythonic way to swap variables
print x, y
