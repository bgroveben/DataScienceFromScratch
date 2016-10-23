# https://en.wikipedia.org/wiki/Object-oriented_programming
# Python allows you to define classes that encapsulate data and the functions that operate on them.
# We'll use them sometimes to make our code cleaner and simpler.
# What follows is a heavily annotated example of creating a class.
# Imagine that we didn't have the built-in Python set -- we are going to create our own Set class.

# What behavior should our class have?
# Given an instance of Set, we want to be able to add and remove items as well as see if it contains a certain value.
# Once we create these member functions, we can access them with a dot after the Set object.

# By convention, we give classes PascalCase names.
class Set:
    # these are the member functions
    # each one takes a first parameter 'self' (another convention)
    # that refers to the particular Set object being used
    def __init__(self, values=None):
        """
        This is the constructor.
        It gets called when you create a new Set.
        You can use it like so:
        s1 = Set()  # empty set
        s2 = Set([1,2,2,3])  # set initialized with values
        """
        self.dict = {}  # each instance of Set has its own dict property used to track memberships

        if values is not None:
            for value in values:
                self.add(value)

        def __repr__(self):
            """
            This is the string representation of a Set object if you type it at the prompt or pass it to a string.
            """
            return "Set: " + str(self.dict.keys())

        # we can represent memebership by being a key in self.dict with value True
        def add(self, value):
            self.dict[value] = True

        # value is in the set if it's a key in the dictionary
        def contains(self, value):
            return value in self.dict

        def remove(self, value):
            del self.dict[value]

# Let's see if our Set class works:
s = Set([1,2,3])
print s
s.add(4)
print s
print s.contains(4)
s.remove(3)
print s.contains(3)
print s
print
