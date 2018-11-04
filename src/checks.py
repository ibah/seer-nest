# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:51:43 2018

@author: michal-siwek
"""

import os
import sys

# Get the path of the root folder of the project,
# this a reference for all other paths.
PROJ_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)
PROJ_ROOT = os.path.abspath(PROJ_ROOT)

# Replace the current folder with the path to src folder of the project,
# this is to setup the reference folder for all imports in the project.
src_dir = os.path.join(PROJ_ROOT, "src")
sys.path[0] = src_dir

# checking hash function

import hashlib

# check hash length
sys.getsizeof(hash('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla')) # 36
sys.getsizeof(hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).hexdigest()) # 81
sys.getsizeof(hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).digest()) # 49 <--- best digest

# check has speed
from timeit import timeit
timeit(stmt="hash('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla')") # super fast
timeit(stmt="hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).hexdigest()", setup="import hashlib")
timeit(stmt="hashlib.md5('lahflkajg;kjalkdjgkljalkjlakjglkjgalkjalkjdla'.encode('utf-8')).digest()", setup="import hashlib")

# checking yaml

import yaml
import io

yaml_folder = os.path.join(PROJ_ROOT, 'library', 'test')

# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}

# Write YAML file
yaml_file = os.path.join(yaml_folder, 'data.yaml')
with io.open(yaml_file, 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=False)

# note:
# default_flow_style=False is the human-readable choice
# allow_unicode=False, less readable but allows for better handling of special characters (independent of system encoding or whatever)

# Read YAML file
with open(yaml_file, 'r') as stream:
    data_loaded = yaml.load(stream)

print(data)
print(data_loaded)
print(data == data_loaded) # this test failed on my computer when allow_unicode=True
