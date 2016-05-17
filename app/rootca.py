#!/bin/python

from ca import CA

class RootCA(CA):
    """This class defines a root CA"""

    def __init__(self, cadir):

        self.ca_dir = cadir

        self.child_init();

        return