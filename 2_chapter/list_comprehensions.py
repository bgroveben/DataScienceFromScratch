# Frequently, you'll want to transform a list into another list by choosing only certain elements,
# or by transforming elements, or both.
# List comprehensions are a Pythonic way of doing this.
even_numbers = [x for x in range(5) if x % 2 == 0]
print even_numbers
squares = [x * x for x in range(5)]
print squares
even_squares = [x * x for x in even_numbers]
print even_squares
print

# You can turn lists into dictionaries or sets:
square_dict = { x : x * x for x in range(5)}
print square_dict
square_set = { x * x for x in [1, -1, 2]}
print square_set
print

# If you don't need the value from the list, it's conventional to use an underscore as the (throwaway) variable:
zeroes = [0 for _ in even_numbers]  # has the same length as even numbers
print zeroes
print

# A list comprehension can include multiple fors:
pairs = [(x, y)
         for x in range(5)
         for y in range(5)]
print pairs
print
# and later fors can use the results of earlier ones:
increasing_pairs = [(x, y)    # only pairs with x < y
                    for x in range(10)  # range(low, high) equals
                    for y in range(x + 1, 10)]  # [low, low + 1, ..., high - 1]
print increasing_pairs
print

# We will use list comprehensions a lot.
