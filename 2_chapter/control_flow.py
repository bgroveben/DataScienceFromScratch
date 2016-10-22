# As in most programming languages, you can perform an action conditionally using if.
if 1 > 2:
    message = "if only one were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'."
else:
    message = "when all else fails use else (if you want to)."

# We can also write a ternary if-then-else on one line, which we will do occasionally.
x = 5
parity = "even" if x % 2 == 0 else "odd"

# Python has a while loop:
x = 0
while x < 10:
    print x, "is less than 10"
    x += 1  # Don't forget the incrementor, lest you run an infinite loop.

# although more often we will use for and in:
for x in range(10):
    print x, "is less than 10"

# If you need more complex logic, you can use continue and break:
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break  # quit the loop entirely
    print x
