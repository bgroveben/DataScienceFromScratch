# https://docs.python.org/2/tutorial/datastructures.html#functional-programming-tools
# https://docs.python.org/2/library/functions.html#filter
# https://docs.python.org/2/library/functions.html#map
# https://docs.python.org/2/library/functions.html#reduce 

# When passing functions around, sometimes we want to partially apply (or curry) functions to create new functions.
# For example, imagine that we have a function with two variables:
def exp(base, power):
    return base ** power
# and we want to use it to create a function of one variable called two_to_the whose input is a power and
# whose output is the result of exp(2, power).
# We can do this with def, but it can be a bit clumsy:
def two_to_the(power):
    return exp(2, power)

# A different approach is to use functools.partial:
from functools import partial
two_to_the = partial(exp, 2)  # is now a function of one variable
print two_to_the(3)
print

# You can also use partial to fill in later arguments if you specify their names:
square_of = partial(exp, power=2)
print square_of(3)
print

# It starts to get messy if you curry arguments in the middle of the function, so try to avoid that.

# We will also use map, reduce, and filter, which provide functional alternatives to list comprehensions.
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
print twice_xs
map_twice_xs = map(double, xs)
print map_twice_xs
list_doubler = partial(map, double)
print list_doubler
again_twice_xs = list_doubler(xs)
print again_twice_xs
print

# Confused yet? Good.
# You can also use map with multiple argument functions if you provide multiple lists:
def multiply(x, y): return x * y

products = map(multiply, [1, 2], [4, 5])
print products
print

# Similarly, filter does the work of if in a list-comprehension:
def is_even(x):
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
print x_evens
filter_x_evens = filter(is_even, xs)
print filter_x_evens
list_evener = partial(filter, is_even)
print list_evener
again_x_evens = list_evener(xs)
print again_x_evens
print

# And finally, reduce combines the first two elements of a list, then that result with a third,
# that result with a fourth, and so on until a single result is produced.
x_product = reduce(multiply, xs)
print x_product
list_product = partial(reduce, multiply)
print list_product
final_product = list_product(xs)
print final_product
print
