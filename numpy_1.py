import numpy as np
from numpy.testing import assert_equal


def nearest_value (x: np.ndarray, v:float):
    return x.flatten()[abs(x-v).argmin()]


######################################################
assert_equal(
    nearest_value(np.array([ 1,  2, 13]), 10),
    13)
######################################################
assert_equal(
    nearest_value(np.array([ -1,  0]), -0.5),
    -1)
######################################################
assert_equal(
    nearest_value(np.array([[[ 1], [2],[3]],[[4],[5],[6]]]), 4.5),
    4)
######################################################
assert_equal(
    nearest_value(np.array([[ 1,  2, 13],
                            [15,  6,  8],
                            [ 7, 18,  9]]), 7.2),
    7)
######################################################
assert_equal(
    nearest_value(np.array([[ -1,  -2],
                            [-15,  -6]]), -100),
    -15)
######################################################
assert_equal(
    nearest_value(np.array([[ 2,  2],
                            [12,  12]]), 7),
    2)
######################################################
assert_equal(
    nearest_value(np.array([[ -2,  -2],
                            [-12,  -12]]), -7),
    -12)
#abs(-2,-7)=5 == abs(-12,-7)=5
######################################################