import numpy as np
from numpy.testing import assert_array_equal

def sum_digits(num):
    return num%10 + sum_digits(num//10) if num > 9 else num
def num_sum(a: np.ndarray):
    new_func = np.vectorize(sum_digits)
    result = new_func(a)
    return result

######################################################
assert_array_equal(num_sum(np.array([82])), np.array([10]))
######################################################
assert_array_equal(num_sum(np.array([1241, 354, 121])), np.array([ 8, 12, 4]))
######################################################
assert_array_equal(num_sum(np.array([1, 22, 333, 4444, 55555])), np.array([1, 4, 9, 16, 25]))
######################################################