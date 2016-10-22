# A set is a data structure which represents a collection of distinct elements:
s = set()
print s
s.add(1)
print s
s.add(2)
print s
s.add(2)
print s
x = len(s)
print x
y = 2 in s
print y
z = 3 in s
print z
print

# We'll use sets for two main reasons.

# The first is that in is a very fast operation on sets.
# If we have a large collection of items that we want to use for a membership test, set is better than list.
"""
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list  # False, but every element is checked.
stopwords_set = set(stopwords_list)
"zip" in stopwords_set  # Much faster to check
"""

# The second reason is to find the distinct items in a collection.
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
print num_items
item_set = set(item_list)
print item_set
num_distinct_items = len(item_set)
print num_distinct_items
distinct_item_list = list(item_set)
print distinct_item_list
print

# We'll use sets much less frequently than dicts and lists.
