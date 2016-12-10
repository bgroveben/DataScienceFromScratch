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
