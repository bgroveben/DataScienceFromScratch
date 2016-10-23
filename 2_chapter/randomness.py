# Import the random module if you need to generate random numbers.
import random

four_uniform_randoms = [random.random() for _ in range(4)]
print four_uniform_randoms  # print 4 random numbers between 0 and 1
print

# The random module actually produces pseudorandom (aka deterministic) numbers based on an
# internal state that you can set with random.seed if you want to get reproducible results.
random.seed(10)
print random.random()
print random.random()
random.seed(10)
print random.random()
print

# We'll sometimes use random.randrange(), which takes either 1 or 2 arguments and returns
# an element chosen randomly (!?!) from the corresponding range():
print random.randrange(10)
print random.randrange(3, 6)
print

# random.shuffle() randomly reorders the elements of a list:
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten
print

# You can use random.choice to randomly pick one element froma list:
my_best_friend = random.choice(["Alice", "Bob", "Charlie", "Daria"])
print my_best_friend
print

# If you need to randomly choose a sample of elements without replacement (no duplicates), use random.sample()
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print winning_numbers
print

# To choose a sample of elements with replacement, make multiple calls to random.choice()
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]
print four_with_replacement
print
