from __future__ import division
from collections import Counter
from linear_algebra import dot, sum_of_squares
import math


def mean(x):
    return sum(x) / len(x)


def de_mean(x):
    """ translate x by subtracting its mean so that the result has mean 0 """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def median(v):
    """ finds the 'middle-most' value of v """
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


def quantile(x, p):
    """ returns the pth-percentile value in x """
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    """ returns a list, might be ore than one mode """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]


def variance(x):
    """ assumes x has at least 2 elements """
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    return math.sqrt(variance(x))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0  # if there is no variation, correlation is zer0
