import numpy as np
from numpy.testing import assert_array_equal


def replace_nans(X: np.ndarray):
    medians = np.nanmedian(X)  # Find the median of each column

    nan_columns = np.isnan(X).sum() == X.shape[0]  # Find columns where all values are nan
    X[:, nan_columns] = 0  # Fill these columns with zeros

    nan_indexes = np.isnan(X)  # Find the indexes of nan values

    X[nan_indexes] = np.take(medians, np.where(nan_indexes)[1])  # Replace nan values with medians

    return X



######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan], [np.nan],  [np.nan]])),
    np.array([[0. ],[ 0. ],[ 0. ]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[0, 42,  42]])),
    np.array([[0, 42 , 42]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan], [1], [np.nan]])),
    np.array([[1.] ,[ 1.] ,[ 1. ]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[4], [1],  [np.nan]])),
    np.array([[4 ], [1] ,[ 2.5]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan, np.nan,  np.nan],
              [     4, np.nan,       5],
              [np.nan,      8,  np.nan]]).T),
    np.array([[0. , 0. , 0. ],
              [4. , 4.5, 5. ],
              [8. , 8. , 8. ]]).T
)
######################################################