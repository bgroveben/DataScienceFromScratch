# A bar chart is a good choice when you want to show how some quantity varies among a set of discrete items.
# Let's look at some movies that have won Academy Awards.
from matplotlib import pyplot as plt

# Get some movie data:
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Bars are set to a default width of 0.8, so we'll add 0.1 to the left coordinate so that each bar is centered.
xs = [i + 0.1 for i, _ in enumerate(movies)]

# Plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("Number of Academy Awards")
plt.title("My Favorite Movies")

# Label x-axis with movie names centered on each bar.
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()
