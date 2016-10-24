# Frequently, you will want to iterate over a list and use both its elements and their indices.

# Not Pythonic
"""
for i in range(len(documents)):
    document = documents[i]
    do_something(i, document)
"""

# Also Not Pythonic
"""
i = 0
for document in documents:
    do_something(i, document)
    i += 1
"""

# The Pythonic solution is enumerate, which produces tuples (index, element):
"""
for i, document in enumerate(documents):
    do_something(i, document)
"""

# Similarly, if we just want the indices:
"""
for i, _ in enumerate(documents): do_something(i)  #Pythonic
# instead of
for i in range(len(documents)): do_something(i)  # Not Pythonic
"""
print

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]

print enumerate(presidents)
print

print list(enumerate(presidents))
print 

for number, name in enumerate(presidents):
    print number, name
print

for number, name in list(enumerate(presidents)):
    print number, name
print

for number, name in enumerate(presidents):
    print "President {}: {}".format(number, name)
print

for _, name in enumerate(presidents):
    print name
print
