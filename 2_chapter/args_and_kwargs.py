# https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
# http://book.pythontips.com/en/latest/args_and_kwargs.html

# Let's say we want to create a higher order function that takes as input some function f
# and returns a new function that for any input returns twice the value of f:
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

# This works in some cases:
def f1(x):
    return x + 1

g = doubler(f1)
print g(3)
print g(-1)
print

# However, it breaks down with functions that take more than a single argument:
def f2(x, y):
    return x + y

"""
g = doubler(f2)
print g(1, 2)
>>> TypeError: g() takes exactly 1 argument (2 given)
"""

# What we need is a way to specify a function that takes an arbitrary number of arguments.
# We can do this with argument unpacking and a little bit of magic:
def magic(*args, **kwargs):
    print "unnamed args: ", args
    print "keyword args: ", kwargs

magic(1, 2, key="word", key2="word2")
print

# When we define a function like this, args is a tuple of its unnamed arguments
# and kwargs is a dict of its named arguments.

# Conversely, if you want to use a list (or tuple) and dict to supply arguments to a function:
def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = { "z" : 3 }
print other_way_magic(*x_y_list, **z_dict)
print

# You can do all sorts of neat tricks like this.
# We will use it to produce higher-order functions whose inputs can accept arbitrary arguments.

def doubler_correct(f):
    """
    Works no matter what kind of inputs f expects.
    """
    def g(*args, **kwargs):
        """
        Take the arguments supplied to g and pass them on to f.
        """
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print g(1, 2)
