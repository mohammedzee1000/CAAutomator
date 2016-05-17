#!/bin/python

from ca import CA

class RootCA(CA):
    """This class defines a root CA"""

    def __init__(self, cadir, country = None, stateorprovince = None, locality = None, orgname = None, ou = None, email = None,cn = None):

        self.priv_ca_dir = cadir
        self.priv_child_init()
        self.priv_set_subj_defauls(country, stateorprovince, locality, orgname, ou, email)

        return

    def create_config(self):

        self.priv_set_config_common()

        currsec = "CA_default"

        self.priv_config.set(currsec, "private_key", "$dir/"
                                   + CA.d_private
                                   + "/"
                                   + "ca"
                                   + CA.f_key)

        self.priv_config.set(currsec, "certificate", "$dir/"
                                   + CA.d_certs
                                   + "/"
                                   + "ca"
                                   + CA.f_cert)

        self.priv_config.set(currsec, "crlnumber", "$dir/"
                                   + CA.f_crlnumber)

        self.priv_config.set(currsec, "policy", "policy_strict")

        self.priv_write_config()

        return

