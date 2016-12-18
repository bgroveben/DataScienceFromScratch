from __future__ import division
from collections import Counter
from linear_algebra import distance, vector_subtract, scalar_multiply
import math, random


def step(v, direction, step_size):
    """ move step_size in the direction from v """
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]


def safe(f):
    """ define a new function that wraps f and return it """
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')   # this means "infinity" in Python
    return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """ use gradient descent to find theta that minimizes the target function """
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0               # set theta to initial value
    target_fn = safe(target_fn)   # safe version of target_fn
    value = target_fn(theta)      # value being minimized
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]
        # choose the one that minimizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)
        # stop if we're "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value


def negate(f):
    """ return a function that for any input x returns -f(x) """
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """ negate when f returns a list of numbers """
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)
