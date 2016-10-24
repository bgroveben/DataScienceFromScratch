from matplotlib import pyplot as plt

# If you want to play with some plots, go to http://matplotlib.org/users/pyplot_tutorial.html#pyplot-tutorial
# Here's one from the pyplot tutorial:
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

# Now the example from the book in the section titled 'matplotlib'
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Create a line chart, years on the x-axis, gdp on the y-axis.
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# Add a title.
plt.title("Nominal GDP")

# Add a labels to the x-axis and y-axis.
plt.ylabel("USD Billions")
plt.show()
