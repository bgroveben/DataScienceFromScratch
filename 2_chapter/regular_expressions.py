# We're going to be searching through quite a bit of text; regular expressions to the rescue!
import re

print all([
      not re.match("a", "cat"),  # 'cat' doesn't start with 'a'
      re.search("a", "cat"),  # 'cat' does have an 'a' in it
      not re.search("c", "dog"),  # 'dog' doesn't have a 'c' in it
      3 == len(re.split("[ab]", "carbs")),  # split on a or b to ['c','r','s']
      "R-D-" == re.sub("[0-9]", "-", "R2D2")  # replace digits with dashes
])

# The terminal output will be True when the above code is run.
# Regexes are fun; here are some docs when you get confused:
# https://docs.python.org/2/library/re.html
# https://docs.python.org/2/howto/regex.html#regex-howto
