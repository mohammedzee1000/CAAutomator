#!/bin/python

from ConfigParser import RawConfigParser

class CA:
    """Abstract class defines a CA."""
    # Consts
    d_certs = "certs"
    d_crl = "crl"
    d_newcerts = "newcerts"
    d_private = "private"
    d_csr = "csr"

    f_index = "index.txt"
    f_serial = "serial"
    f_crlnumber = "crlnumber"
    f_cnf = "openssl.cnf"

    def __init__(self):

        self.ca_dir = "/root/ca"
        self.ca_loc_certs = ""
        self.ca_loc_crl = ""
        self.ca_loc_newcerts = ""
        self.ca_loc_private = ""
        self.ca_loc_csr = ""

        return

    def child_init(self):

        self.ca_loc_certs = self.ca_dir + "/" + CA.d_certs
        self.ca_loc_crl = self.ca_dir + "/" + CA.d_crl


        return