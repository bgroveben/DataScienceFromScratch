# The VP of Revenue wants to understand which users pay for accounts and which don't.
# You notice a correlation between years of experience and paid accounts in the data.

0.7, 'paid',
1.9, 'unpaid',
2.5, 'paid',
4.2, 'unpaid',
6,   'unpaid',
6.5, 'unpaid',
7.5, 'unpaid',
8.1, 'unpaid',
8.7, 'paid',
10,  'paid',

# Users with vary few and very many years of experience tend to pay.
# Users with average amounts of experience don't.
# We could generate a very basic model based on our observations:
def predict_paid_or_unpaid(years_experience):
    """ (number) -> str
    Return a result of 'paid' or 'unpaid' based on the number of years entered as the function argument.

    >>> predict_paid_or_unpaid(6)
    unpaid
    """
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

print(predict_paid_or_unpaid(2))
print(predict_paid_or_unpaid(6))
print(predict_paid_or_unpaid(10))
# Not very scientific, and there is not enough data to base a model on, but it makes for a nice example.
