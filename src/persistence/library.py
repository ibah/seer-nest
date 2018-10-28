# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 00:31:37 2018

@author: michal-siwek
"""

import hashlib
from warnings import warn

class Catalog:
    """
    Catalog
    """
    
    def __init__(self, library_folder, catalog_file, memory_cache):
        self.library_folder = library_folder
        self.catalog_file = catalog_file
        self.memory_cache = memory_cache
        self.catalog = {}
        # read the catalog file from HDD
        if memory_cache:
            # read the objects from the catalog
            self.catalog['prediction'] = {}
        else:
            self.catalog['prediction'] = {}
    
    def add_object(self, hash_code, stage, object_to_store):
        if stage not in self.catalog.keys():
            # Error: wrong stage
            pass
        if hash_code in self.catalog[stage]:
            warn("Object %s already present in catalog at stage %s" % (hash_code, stage))
        self.catalog[stage][hash_code] = object_to_store
                
    def get_object(self, hash_code, stage):
        if stage not in self.catalog.keys():
            # Error: wrong stage
            pass
        object_to_retrieve = self.catalog[stage].get(hash_code, None)
        return object_to_retrieve

class Librarian:
    """
    Librarian
    """
    
    def __init__(self, catalog, hash_function):
        """
        hash - fast but possible collisions, definition may change with implementation/version
        md5 - slow, collisions is unlikely, fixed definition
        """
        self.catalog = catalog
        return None

    def get_hash(self, description):
#        return hashlib.md5(description.encode('utf-8')).hexdigest()
        return hashlib.md5(description.encode('utf-8')).digest()
