#!/usr/bin/env python
#version: 0.0.1
#date: 06/12/2018
#Author: Mohan T
import os
import sys
import subprocess
import argparse

parser=argparse.ArgumentParser(description='Adds group membership to ldap user')
parser.add_argument('--dn', '-d', help='Your LDAP DN [UID]')
parser.add_argument('--userid', '-u', help='provide LDAP account to which group membership to be added')
parser.add_argument('--filename', '-f', help='provide group list file')
parser.add_argument('--groups', '-g', nargs='+', help='provide space separated list of groups on command line')

args = parser.parse_args()

if args.userid and args.filename:

    with open(args.filename, 'r') as G:
        for grp in G:
            with open('modify_member_uid.ldif', 'w+') as F:
                lines = ["dn: cn="+grp.strip()+",ou=Group,dc=int,dc=example,dc=com\n", "changetype: modify", "add: memberUid", "memberUid: "+args.userid]
                F.write("%s" % lines[0])
                F.write("%s\n" % lines[1])
                F.write("%s\n" % lines[2])
                F.write("%s\n" % lines[3])
                ldfile=str(F).split(',')[0].split("'")[1]
		F.seek(0)
		rline = F.readlines()
                subprocess.call("ldapmodify -WxZZh ldapserver.int.example.com -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f"% args.dn+ldfile, shell=True)

elif args.userid and args.groups:
	for grp in args.groups:
		with open('modify_member_uid.ldif', 'w+') as F:
			lines = ["dn: cn="+grp.strip()+",ou=Group,dc=int,dc=asuexample,dc=com\n", "changetype: modify", "add: memberUid", "memberUid: "+args.userid]
			F.write("%s" % lines[0])
			F.write("%s\n" % lines[1])
			F.write("%s\n" % lines[2])
			F.write("%s\n" % lines[3])
			ldfile=str(F).split(',')[0].split("'")[1]
			F.seek(0)
			rline = F.readlines()
			subprocess.call("ldapmodify -WxZZh dolldapserver.int.example.com -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f"% args.dn+ldfile, shell=True)

else:
    print parser.print_help()
