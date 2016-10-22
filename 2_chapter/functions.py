# Python 2 means integer division by default; let's fix that.
from __future__ import division

# A function is a rule for taking zero or more inputs and returning a corresponding output.
def my_double(x):
    """ (number) -> number
    This is where you put an optional docstring describing what the function does.
    You can also describe what the inputs and outputs shoud be, mention preconditions (if any), and give examples.
    For example, this function multiplies its input by 2

    >>> my_double(2)
    4
    """
    return x * 2

print "Basic function:"
print my_double(2)
print ''


# Python functions are first-class, meaning we can assign them to variables and pass them into
# other functions just like any other arguments:
def apply_to_one(f):
    """ (function) -> function(1)
    Calls the function f with 1 as its argument.

    >>> apply_to_one(my_double)
    2
    """
    return f(1)

print 'First-class function:'
print apply_to_one(my_double)
print ''


# You can also create short anonymous functions, aka lambdas:
print 'Anonymous function:'
not_quite_anonymous = apply_to_one(lambda x: x + 4)
print not_quite_anonymous
print ''


# You can assign lambdas to variables, but a more common practice is to use def instead
another_double = lambda x: 2 * x   # Don't do this
def another_double(x): return 2 * x   # Do this instead


# Function parameters can also be given default arguments.
# Arguments only need to be specified when you want a value other than the default.
def my_print(message="my default message"):
    print message

print 'Functions with a default argument:'
my_print("hello")
my_print()
print ''


# Sometimes it is useful to specify arguments by name:
def subtract(a=0, b=0):
    return a - b

print 'Function with multiple named arguments'
print subtract(10, 5)
print subtract(0, 5)
print subtract(b=5)
