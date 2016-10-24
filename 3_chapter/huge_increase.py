from matplotlib import pyplot as plt

# Be judicious when using plt.axis().
# When creating bar charts it is considered bad form for your y-axis not to start at zero.
# This is an easy way to mislead people.
# Compare this plot to not_so_huge_increase.py

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("Number of times I have heard someone say 'data science'")

# If you don't do this, matplotlib will label the x-axis 0, 1 and then add a +2.013e3 off in the corner.
plt.ticklabel_format(useOffset=False)

# Misleading y-axis only shows the part above 500.
plt.axis([2012.5,2014.5,499,506])
plt.title("Look at the 'Huge' Increase!")
plt.show()
