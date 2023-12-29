import numpy as np
from numpy.testing import assert_array_equal


def sort_evens(A: np.ndarray):
    filtered_array = A[A%2==0]
    filtered_array.sort()
    A[A%2==0] = filtered_array
    return A


######################################################
assert_array_equal(sort_evens(np.array([])), np.array([]))
######################################################
assert_array_equal(sort_evens(np.array([2, 0])), np.array([0, 2]))
######################################################
assert_array_equal(sort_evens(np.array([9, 3, 1, 5, 7])), np.array([9, 3, 1, 5, 7]))
######################################################
assert_array_equal(sort_evens(np.array([8, 12, 4, 10, 6, 2])), np.array([2, 4, 6, 8, 10, 12]))
######################################################

print("success")