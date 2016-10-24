from matplotlib import pyplot as plt
from collections import Counter

# A bar chart can also be a good choice for plotting histograms of bucketed numeric values.
# Then we can visually explore how the values are distributed.

# Import grade data:
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

# Create buckets for each grade to be placed into:
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)
# >>> print list(histogram.keys())
# [0, 100, 70, 80, 90, 60]
# >>> print list(histogram.values())
# [2, 1, 3, 4, 2, 1]

# Let's plot this:
plt.bar([x - 4 for x in histogram.keys()],  # shift each bar to the left by 4
         histogram.values(),  # give each bar its correct height
         8)  # give each bar a width of 8 (buckets are width 10, and we want a small gap)

# Good, but we need to fix the x- and y- axes to make it prettier:
plt.axis([-5, 105, 0, 5])  # x-axis from -5 to 105, y-axis from 0 to 5

# Put some x-axis labels at 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])

# Now some labels and a title:
plt.xlabel("Decile")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam 1 Grades")

# Showtime!
plt.show()
