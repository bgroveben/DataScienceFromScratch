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


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """ returns a num_rows by num_cols matrix whose (i,j)th entry is entry_fn(i,j) """
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]
