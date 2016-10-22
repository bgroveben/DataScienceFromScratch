# A list in Python is an ordered collection.
# Lists in Python are similar to Arrays in other languages, but with some added functionality.
# https://docs.python.org/2/tutorial/introduction.html#lists

integer_list = [1, 2, 3]
list_length = len(integer_list)
list_sum = sum(integer_list)
print list_length
print list_sum
print
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
length_of_lists = len(list_of_lists)
print length_of_lists
print

# You can get the nth element of a list with square brackets:
# Python indices are zero-based, meaning the first element is at 0, not 1.
x = range(10)
print x
zero = x[0]
one = x[1]
nine = x[-1]  # Last element
eight = x[-2]  # Next-to-last element
# You can also assign values using bracket notation:
x[0] = -1
print x
print

# Square brackets can also be used to slice lists:
# http://pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
first_three = x[:3]
print first_three
three_to_end = x[3:]
print three_to_end
one_to_four = x[1:5]
print one_to_four
last_three = x[-3:]
print last_three
without_first_and_last = x[1:-1]
print without_first_and_last
copy_of_x = x[:]
print copy_of_x
print

# Python has an in operator to check for list membership:
print 1 in [1, 2, 3]
print 0 in [1, 2, 3]
print

# Concatenating lists is easy.
# If you want to modify an existing list:
x = [1, 2, 3]
x.extend([4, 5, 6])
print x
print
# If you don't want to modify x you can use list addition:
x = [1, 2, 3]
y = x + [4, 5, 6]
print x
print y
print

# You can unpack lists if you know hoow many elements they contain:
x, y = [1, 2]
print x
print y
print

# It is common to use an underscore for throwaway values:
_, y = [1, 2]
print y
print
