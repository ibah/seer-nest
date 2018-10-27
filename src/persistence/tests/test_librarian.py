# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 00:33:51 2018

@author: michal-siwek
"""
import numpy as np
import os
import sys

# Get the path of the root folder of the project,
# this a reference for all other paths.
PROJ_ROOT = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir)
PROJ_ROOT = os.path.abspath(PROJ_ROOT)

# Replace the current folder with the path to src folder of the project,
# this is to setup the reference folder for all imports in the project.
src_dir = os.path.join(PROJ_ROOT, "src")
sys.path[0] = src_dir

#from sklearn.utils.testing import assert_raise_message
#from sklearn.utils.testing import assert_almost_equal
#from sklearn.utils.testing import clean_warning_registry
#from sklearn.utils.testing import assert_array_almost_equal
#from sklearn.utils.testing import assert_array_equal
#from sklearn.utils.testing import assert_array_less
from sklearn.utils.testing import assert_equal
#from sklearn.utils.testing import assert_greater_equal
#from sklearn.utils.testing import assert_less_equal
#from sklearn.utils.testing import assert_raises
#from sklearn.utils.testing import assert_raises_regex
#from sklearn.utils.testing import assert_true
#from sklearn.utils.testing import assert_false
#from sklearn.utils.testing import assert_warns_message
#from sklearn.utils.testing import assert_no_warnings
#from sklearn.utils.testing import assert_allclose
#from sklearn.utils.testing import assert_allclose_dense_sparse
#from sklearn.utils.testing import skip_if_32bit

from persistence import Librarian

# Example data
from sklearn import datasets
iris = datasets.load_iris()

# Toy data (source: scikit-learn)
rng = np.random.RandomState(0)
n_features = 30
n_samples = 1000
offsets = rng.uniform(-1, 1, size=n_features)
scales = rng.uniform(1, 10, size=n_features)
X_2d = rng.randn(n_samples, n_features) * scales + offsets
X_1row = X_2d[0, :].reshape(1, n_features)
X_1col = X_2d[:, 0].reshape(n_samples, 1)
X_list_1row = X_1row.tolist()
X_list_1col = X_1col.tolist()

def test_Librarian():
    # case
    librarian = Librarian()
    # test
    x = librarian.add1(3)
    # assertions
    assert_equal(x, 4)
    assert np.all((0,0) == (0,0))
    assert np.allclose((.1,.1), (.1,.1))
