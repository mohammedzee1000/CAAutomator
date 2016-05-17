#!/bin/python

from ConfigParser import RawConfigParser

class CA:

    ca_dir = "/root/ca" # The location of the CA.

    # Consts
    ca_cnf = "openssl.cnf"
    ca_dir_certs = "certs"
    ca_dir_crl = "crl"
    ca_dir_newcerts = "newcerts"
    ca_dir_private = "private"
    ca_dir_csr = "csr"

    ca_file_index = "index.txt"

