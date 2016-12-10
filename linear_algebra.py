from __future__ import division # want 3 / 2 == 1.5
import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot
from collections import defaultdict, Counter
from functools import partial


def dot(v, w):
    """ dot product  v_1 * w_1 + ... + v_n * w_n """
    return sum(v_i * w_i for v_i, w_i, in zip(v, w))


def sum_of_squares(v):
    """ v_1 * v_1 + ... + v_n * v_n """
    return dot(v, v)
