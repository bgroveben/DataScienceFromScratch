# Often we will need to zip two or more lists together.
# The zip() function transforms multiple lists into a single list of tuples of corresponding elements.
# https://docs.python.org/2/library/functions.html#zip
print
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
pairs = zip(list1, list2)
print pairs
print
# If the lists are different lengths, zip stops as soon as the first list ends.

# You can also 'unzip' a list using a nifty trick:
letters, numbers = zip(*pairs)
print letters
print numbers
print

# The asterisk performs argument unpacking, which uses the elements of pairs as individual arguments to zip.
# The result is almost the same as if you had called:
unpacked = zip(('a', 1), ('b', 2), ('c', 3))
print unpacked
print

# You can use argument unpacking with functions:
def add(a, b): return a + b
result = add(1, 2)
print result
"""
wrong_result = add([1,2])
print wrong_result
"""
another_result = add(*[1, 2])
print another_result
print
