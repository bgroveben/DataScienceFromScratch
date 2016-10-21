# The VP of Public Relations asks you to provide some facts about how much data scientists earn.

from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]


# What follows is code for a scatterplot of the salaries_and_tenures data.
x = np.array(salaries_and_tenures)
print('')
print('Vector Containing Years of Experience:')
print(x[:,0])
print('Vector Containing Salary:')
print(x[:,1])
print('')
plt.scatter(x[:,0], x[:,1])
plt.title('Salary by Years of Experience')
plt.xlabel('Annual Salary USD')
plt.ylabel('Years of Experience')
plt.show()


# Based on the plot, it appears that people with more experience tend to earn more.
# Let's take a closer look at the average salary for each tenure.
salary_by_tenure = defaultdict(list)
# Keys are years, values are lists of salaries for each tenure.
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
print('Salary by Tenure:')
pprint(salary_by_tenure)
print('')
average_salary_by_tenure = {
# Keys are years, each value is the average salary for that tenure.
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
    }
print('Average Salary by Tenure:')
pprint(average_salary_by_tenure)
print('')

# Since none of the users have the same tenure, we are just reporting the individual users' salaries.

# Let's try to bucket the tenures instead.
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two years"
    elif tenure < 5:
        return "between two and five years"
    else:
        return "more than five years"

# Then group the salaries corresponding to each bucket:
salary_by_tenure_bucket = defaultdict(list)
# Keys are tenure buckets, values are lists of salaries for that bucket.
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
print('Salaries Grouped by Tenure Bucket')
pprint(salary_by_tenure_bucket)
print('')

# And finally, compute the average salary for each group:
average_salary_by_bucket = {
# Keys are tenure buckets, values are the average salary for that bucket.
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
print('Average Salary by Tenure Groups')
pprint(average_salary_by_bucket)
print('')
