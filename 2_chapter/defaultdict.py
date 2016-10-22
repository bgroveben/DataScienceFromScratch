# Imagine that you're trying to count the letters in a document.
# A obvious approach is to create a dicitonary in which the keys are letters and the values are counts.
# As you check each letter, you can increment its count if it's already in the dictionary and add it if not.

# Sample document
document = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sollicitudin arcu vel ullamcorper tincidunt. Proin convallis faucibus erat, ut mattis eros euismod at.")

letter_counts = {}
for letter in document:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1
print "Letters in document using a dictionary:"
print letter_counts
print

# You could also use the "forgiveness is better than permission" approach and just handle the exception
# from trying to look up a missing key.
letter_counts = {}
for letter in document:
    try:
        letter_counts[letter] += 1
    except KeyError:
        letter_counts[letter] = 1

# A third approach is to use get, which behaves gracefully for missing keys.
letter_counts = {}
for letter in document:
    previous_count = letter_counts.get(letter, 0)
    letter_counts[letter] = previous_count + 1


# Or we can skip all of that nonsense above and use a defaultdict.

# A defaultdict is like a regular dictionary, except that when you look up a key it doesn't contain,
# it first adds a value for it using a zero-argument function you provided when you created it.

# defaultdicts must be imported from collections.
from collections import defaultdict

letter_counts = defaultdict(int)
for letter in document:
    letter_counts[letter] += 1
print "Letters in document using a defaultdict:"
print letter_counts
print

# defaultdicts can also be useful with list, dict, or even your own function.
dd_list = defaultdict(list)
print dd_list
dd_list[2].append(1)
print dd_list
print
dd_dict = defaultdict(dict)
print dd_dict
dd_dict["Joel"]["City"] = "Seattle"
print dd_dict
print
dd_pair = defaultdict(lambda: [0,0])
print dd_pair
dd_pair[2][1] = 1
print dd_pair
print

# defaultdicts will be useful when we're using dictionaries to 'collect' results by some key
# and we don't want to have to check every time to see if the key exists yet.
