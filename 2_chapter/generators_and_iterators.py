# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

# One problem with lists is that they can easily grow very large.
# If you only need to deal with one list element at a time, this can become very computationally expensive.
# If you potentially need only the first few values, then calculating them all is a waste.

# Generators to the rescue!
# A generator is something that you can iterate over (for us, usually using for),
# but whose values are produced only as needed.

# One way to create generators is with functions and the yield operator:
def lazy_range(n):
    """ (int) -> generator object
    A lazy version of range.

    >>> lazy_range(10)
    <generator object lazy_range at 0x109041b90>
    """
    while i < n:
        yield i
        i += 1
print lazy_range(10)
print

# The following loop wil consume the yielded values one at a time until none remain:
"""
for i in lazy_range(10):
    do_something_with(i)
"""

# Python 2.7 comes with a lazy_range function called xrange, and in Python 3 range itself is lazy (no xrange)

# A second way to create generators is by using for comprehensions wrapped in parentheses:
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
print lazy_evens_below_20  #returns a generator object
print

# Recall that every dict has an items() method that returns a list of its key-value pairs.
# More frequently we'll use the iteritems() method, which lazily yields the key-value pairs
# one at a time as we iterate over it.


# Here is an example I found at http://www.learnpython.org/en/Generators
# This example generator function will return seven random integers:
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)
    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

print "Lottery time!"
for random_number in lottery():
    print "And the next number is... %d!" % random_number
print

# Here is a generator function that returns the numbers in a fibonacci sequence:
def fibonacci():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

print "Here are some Fibonacci numbers:"
counter = 0
for i in fibonacci():
    print i
    counter +=1
    if counter == 10:
        break
print
