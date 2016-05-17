#!/bin/python

from ConfigParser import RawConfigParser

class CA:
    """Abstract class defines a CA."""
    # Consts
    ca_dir_certs = "certs"
    ca_dir_crl = "crl"
    ca_dir_newcerts = "newcerts"
    ca_dir_private = "private"
    ca_dir_csr = "csr"

    ca_file_index = "index.txt"
    ca_file_serial = "serial"
    ca_file_crlnumber = "crlnumber"
    ca_file_cnf = "openssl.cnf"

    def __init__(self):

        self.ca_dir = "/root/ca"
        self.ca_certs = self.ca_dir + "/" + CA.ca_dir_certs

        return