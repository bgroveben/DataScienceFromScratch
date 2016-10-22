# A Counter turns a sequence of values into a defaultdict(int)-like object mapping keys to counts.
# We will primarily use Counter to create histograms.
from collections import Counter
c = Counter([0, 1, 2, 0])
print c
print

# This gives us a simple way to solve our letter_counts problem.
document = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sollicitudin arcu vel ullamcorper tincidunt. Proin convallis faucibus erat, ut mattis eros euismod at.")
letter_counts = Counter(document)
print "A count of all of the letters in our lorem ipsum text document:"
print letter_counts
print

# A Counter instance has a most_common method that frequently comes in handy.
# The following command prints the 10 most common letters in document and their counts.
print "A count of the 10 most common letters in our lorem ipsum text document:"
for letter, count in letter_counts.most_common(10):
    print letter, count
print 
