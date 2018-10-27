# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:51:01 2017

@author: michal.siwek
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

from persistence import Librarian

def main():
    librarian = Librarian()
    print(librarian.add1(0))

if __name__ == "__main__":
    main()
