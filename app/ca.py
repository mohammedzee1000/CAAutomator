#!/bin/python

from ConfigParser import RawConfigParser
import os
from helpers import create_dir, touchfile
from subprocess import  call

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

    f_key = ".key.pem"
    f_cert = ".cert.pem"
    f_crl = ".crl.pem"

    def __init__(self):

        self.priv_ca_dir = "/root/ca" # Path of the CA directory
        self.priv_ca_loc_certs = "" # Path of certs dir
        self.priv_ca_loc_crl = "" # Path of crl dir
        self.priv_ca_loc_newcerts = "" # path of newcerts dir
        self.priv_ca_loc_private = "" # path of private dir
        self.priv_ca_loc_csr = "" # path of csr dir

        self.priv_ca_loc_index = "" # path if index file
        self.priv_ca_loc_serial = "" # path of serial file
        self.priv_ca_loc_crlnumber = "" # path of crlnumber file
        self.priv_ca_loc_cnf = "" # path of cnf file

        self.priv_subj_country = "GB"
        self.priv_subj_state_province = "England"
        self.priv_subj_locality = "EMPTY"
        self.priv_subj_orgname = "CentOS Devcloud"
        self.priv_subj_ou = "CCCP"
        self.priv_subj_email = "test@cccp.org"

        self.priv_config = None # Initialize the config parser.

        return

    # Child init usable section

    def priv_child_init(self):
        """Allows child classes to initialize variables according th their need."""

        self.priv_config = RawConfigParser()
        self.priv_config.optionxform = str

        self.priv_ca_dir = os.path.abspath(self.priv_ca_dir)
        self.priv_ca_loc_certs = self.priv_ca_dir + "/" + CA.d_certs
        self.priv_ca_loc_crl = self.priv_ca_dir + "/" + CA.d_crl
        self.priv_ca_loc_newcerts = self.priv_ca_dir + "/" + CA.d_newcerts
        self.priv_ca_loc_private = self.priv_ca_dir + "/" + CA.d_private
        self.priv_ca_loc_csr = self.priv_ca_dir + "/" + CA.d_csr

        self.priv_ca_loc_index = self.priv_ca_dir + "/" + CA.f_index
        self.priv_ca_loc_serial = self.priv_ca_dir + "/" + CA.f_serial
        self.priv_ca_loc_crlnumber = self.priv_ca_dir + "/" + CA.f_crlnumber
        self.priv_ca_loc_cnf = self.priv_ca_dir + "/" + CA.f_cnf

        self.priv_subj_country = "GB"
        self.priv_subj_state_province = "England"
        self.priv_subj_locality = "EMPTY"
        self.priv_subj_orgname = "CentOS Devcloud"
        self.priv_subj_ou = "CCCP"
        self.priv_subj_email = "test@cccp.org"

        self.priv_fs_init();

        return

    def priv_fs_init(self):
        """Creates the directories and files needed for all CA's"""

        create_dir(self.priv_ca_dir)
        create_dir(self.priv_ca_loc_certs)
        create_dir(self.priv_ca_loc_crl)
        create_dir(self.priv_ca_loc_newcerts)
        create_dir(self.priv_ca_loc_private, 700)
        create_dir(self.priv_ca_loc_csr)

        touchfile(self.priv_ca_loc_index, "")
        touchfile(self.priv_ca_loc_serial, "1000")
        touchfile(self.priv_ca_loc_crlnumber, "1000")

        return

    # Child usable

    def priv_set_subj_defauls(self, country, stateorprovince, locality, orgname, ou, email):
        """This function sets the defaults of subj parameters to be used in the config file."""

        if country != None:
            self.priv_subj_country = country

        if stateorprovince != None:
            self.priv_subj_state_province = stateorprovince

        if locality != None:
            self.priv_subj_locality = locality

        if orgname != None:
            self.priv_subj_orgname = orgname

        if ou != None:
            self.priv_subj_ou = ou

        if email != None:
            self.priv_subj_email = email

        return

    def priv_set_config_common(self):
        # type: () -> object
        """Writes the common config information to the config object
        :rtype: None
        """

        # Section ca
        currsec = "ca"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "default_ca", "CA_default")

        # Section CA_Default
        currsec = "CA_default"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "dir", self.priv_ca_dir)

        self.priv_config.set(currsec, "certs", "$dir/"
                             + CA.d_certs)

        self.priv_config.set(currsec, "crl_dir", "$dir/"
                             + CA.d_crl)

        self.priv_config.set(currsec, "new_certs_dir", "$dir/"
                             + CA.d_newcerts)

        self.priv_config.set(currsec, "database", "$dir/"
                             + CA.f_index)

        self.priv_config.set(currsec, "serial", "$dir/"
                             + CA.f_serial)

        self.priv_config.set(currsec, "RANDFILE", "$dir/"
                             + CA.d_private
                             + "/"
                             + ".rand")

        self.priv_config.set(currsec, "crl", "$dir/"
                             + CA.f_crlnumber)

        self.priv_config.set(currsec, "crl_extensions", "crl_ext")
        self.priv_config.set(currsec, "default_crl_days", "30")
        self.priv_config.set(currsec, "default_md", "sha256")
        self.priv_config.set(currsec, "name_opt", "ca_default")
        self.priv_config.set(currsec, "cert_opt", "ca_default")
        self.priv_config.set(currsec, "default_days", "375")
        self.priv_config.set(currsec, "preserve", "no")

        # Section policy_strict
        currsec = "policy_strict"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "countryName", "match")
        self.priv_config.set(currsec, "stateOrProvinceName", "match")
        self.priv_config.set(currsec, "organizationName", "match")
        self.priv_config.set(currsec, "organizationalUnitName", "optional")
        self.priv_config.set(currsec, "commonName", "supplied")
        self.priv_config.set(currsec, "emailAddress", "optional")

        # Section policy_loose
        currsec = "policy_loose"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "countryName", "optional")
        self.priv_config.set(currsec, "stateOrProvinceName", "optional")
        self.priv_config.set(currsec, "organizationName", "optional")
        self.priv_config.set(currsec, "organizationalUnitName", "optional")
        self.priv_config.set(currsec, "commonName", "supplied")
        self.priv_config.set(currsec, "emailAddress", "optional")

        # Section req
        currsec = "req"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "default_bits", "2048")
        self.priv_config.set(currsec, "distinguished_name", "req_distinguished_name")
        self.priv_config.set(currsec, "string_mask", "utf8only")
        self.priv_config.set(currsec, "default_md", "sha256")
        self.priv_config.set(currsec, "x509_extensions", "v3_ca")

        # Section req_distinguished_name
        currsec = "req_distinguished_name"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "countryName", "Country Name (2 letter code)")
        self.priv_config.set(currsec, "stateOrProvinceName", "State or Province Name")
        self.priv_config.set(currsec, "localityName", "Locality Name")
        self.priv_config.set(currsec, "0.organizationName", "Organization Name")
        self.priv_config.set(currsec, "organizationalUnitName", "organizational Unit Name")
        self.priv_config.set(currsec, "emailAddress", "Email Address")

        # Section req_distinguished_name defaults
        self.priv_config.set(currsec, "countryName_default", self.priv_subj_country)
        self.priv_config.set(currsec, "stateOrProvinceName_default", self.priv_subj_state_province)
        self.priv_config.set(currsec, "localityName_default", self.priv_subj_locality)
        self.priv_config.set(currsec, "0.organizationName_default", self.priv_subj_orgname)
        self.priv_config.set(currsec, "organizationalUnitName_default", self.priv_subj_ou)
        self.priv_config.set(currsec, "emailAddress_default", self.priv_subj_email)

        # Section v3_ca
        currsec = "v3_ca"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "subjectKeyIdentifier", "hash")
        self.priv_config.set(currsec, "authorityKeyIdentifier", "keyid:always, issuer")
        self.priv_config.set(currsec, "basicConstraints", "critical, CA:true")
        self.priv_config.set(currsec, "keyUsage", "critical, digitalSignature, cRLSign, keyCertSign")

        # Section v3_intermediate_ca
        currsec = "v3_intermediate_ca"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "subjectKeyIdentifier", "hash")
        self.priv_config.set(currsec, "authorityKeyIdentifier", "keyid:always, issuer")
        self.priv_config.set(currsec, "basicConstraints", "critical, CA:true, pathlen:0")
        self.priv_config.set(currsec, "keyUsage", "critical, digitalSignature, cRLSign, keyCertSign")

        # Section usr_cert
        currsec = "usr_cert"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "basicConstraints", "CA:false")
        self.priv_config.set(currsec, "nsCertType", "client, email")
        self.priv_config.set(currsec, "nsComment", "\"OpenSSL Generated Client Certificate\"")
        self.priv_config.set(currsec, "subjectKeyIdentifier", "hash")
        self.priv_config.set(currsec, "authorityKeyIdentifier", "keyid:always, issuer")
        self.priv_config.set(currsec, "keyUsage", "critical, nonRepudiation, digitalSignature, keyEncipherment")
        self.priv_config.set(currsec, "extendedKeyUsage", "clientAuth, emailProtection")

        # Section server_cert
        currsec = "server_cert"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "basicConstraints", "CA:false")
        self.priv_config.set(currsec, "nsCertType", "server")
        self.priv_config.set(currsec, "nsComment", "\"OpenSSL Generated Server Certificate\"")
        self.priv_config.set(currsec, "subjectKeyIdentifier", "hash")
        self.priv_config.set(currsec, "authorityKeyIdentifier", "keyid, issuer:always")
        self.priv_config.set(currsec, "keyUsage", "critical, digitalSignature, keyEncipherment")
        self.priv_config.set(currsec, "extendedKeyUsage", "serverAuth")

        # Section crl_ext
        currsec = "crl_ext"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "authorityKeyIdentifier", "keyid:always")

        # Section oscp
        currsec = "oscp"
        self.priv_config.add_section(currsec)
        self.priv_config.set(currsec, "basicConstraints", "CA:false")
        self.priv_config.set(currsec, "subjectKeyIdentifier", "hash")
        self.priv_config.set(currsec, "authorityKeyIdentifier", "keyid, issuer")
        self.priv_config.set(currsec, "keyUsage", "critical, digitalSignature")
        self.priv_config.set(currsec, "extendedKeyUsage", "OCSPSigning")

        return

    def priv_write_config(self):

        with open(self.priv_ca_loc_cnf, 'wb') as configfile:
            self.priv_config.write(configfile)

        return