# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:51:43 2018

@author: michal-siwek
"""

import sys
import hashlib

# checking hash function

# check hash length
sys.getsizeof(hash('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla')) # 36
sys.getsizeof(hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).hexdigest()) # 81
sys.getsizeof(hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).digest()) # 49 <--- best digest

# check has speed
from timeit import timeit
timeit(stmt="hash('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla')") # super fast
timeit(stmt="hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).hexdigest()", setup="import hashlib")
timeit(stmt="hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).digest()", setup="import hashlib")

