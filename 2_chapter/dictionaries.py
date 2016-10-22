# Dictionaries associate values with keys to allow the user to quickly retrieve the value corresponding to a given key.
# https://docs.python.org/2/tutorial/datastructures.html#dictionaries
# http://www.diveintopython.net/native_data_types/index.html#odbchelper.dict

empty_dict = {}  # more Pythonic
empty_dict2 = dict()  # less Pythonic

grades = { "Joel" : 80, "Ben" : 95}  # dictionary literal
# You can look up the value for a key using square brackets:
bens_grade = grades["Ben"]
print bens_grade
# You will get a KeyError if you ask for a key that is not in the dictionary:
try:
    kates_grade = grades["Kate"]
except KeyError:
    print "Kate is not in that dictionary, sucka."
print

# You can check for the existence of a key using in:
joel_has_grade = "Joel" in grades
print joel_has_grade
kate_has_grade = "Kate" in grades
print kate_has_grade
print

# Dictionaries have a get method that returns a default value instead of raising an exception when
# you look up a key that is not in the dictionary.
joels_grade = grades.get("Joel", 0)
print joels_grade
kates_grade = grades.get("Kate", 0)
print kates_grade
nobodys_grade = grades.get("Nobody")
print nobodys_grade
print

# You can assign key-value pairs using the same square brackets:
grades["Ben"] = 99  # replaces the old value
grades["Kate"] = 95  # adds a third entry, since people keep bugging me about Kate
num_students = len(grades)
print num_students
print

# We will frequently use dictionaries as a simple way to represent structured data:
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
# We can look for specific keys or we can look at all of them:
tweet_keys = tweet.keys()  # list of keys
print "Tweet Keys:"
print tweet_keys
print
tweet_values = tweet.values()  # list of values
print "Tweet Values:"
print tweet_values
print
tweet_items = tweet.items()  # list of (key, value) tuples
print "Tweet Items:"
print tweet_items
print
print "user" in tweet_keys  # Uses a slow list in
print "user" in tweet  # more Pythonic, uses faster dic in
print "joelgrus" in tweet_values
print

# Dictionary keys must be immutable; in particular, you cannot use lists as keys.
# If you need a multipart key, you should use a tuple or figure out a way to turn the key into a string.
