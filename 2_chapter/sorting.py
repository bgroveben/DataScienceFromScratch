# Every Python list has a sort method that sorts it in place.
# If you don't want to mess up your list, yo can use the sorted function that returns a new list.
x = [4,1,3,2]
print x
y = sorted(x)  # more convenient, and you keep the original list
print x
print y
x.sort()  # if you don't need the original list, it's slightly more efficient
print x
print

# As you can see, the default setting is to sort the list from smallest to largest.
# list.sort() -- https://docs.python.org/2.7/library/stdtypes.html#typesseq-mutable
# sorted() -- https://docs.python.org/2.7/library/functions.html#sorted
# Examples and tutorial == https://docs.python.org/2.7/howto/sorting.html#sortinghowto

# Sort the list by absolute value from largest to smallest:
x = sorted([-4,1,-2,3], key=abs, reverse=True)
print x
print

from collections import Counter
document = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sollicitudin arcu vel ullamcorper tincidunt. Proin convallis faucibus erat, ut mattis eros euismod at.")
letter_counts = Counter(document)
# Sort the words and counts from highest count to lowest:
wc = sorted(letter_counts.items(),
            key=lambda (letter,count): count,
            reverse=True)
print wc
print

# Keep in mind that the list.sort() method is only defined for lists.
# In contrast, the sorted() function accepts any iterable.
