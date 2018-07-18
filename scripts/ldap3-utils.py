#!/usr/bin/env python
#version: 0.0.2
#date: 07/17/2018
#Author: Mohan T

import os
from subprocess import Popen, PIPE, call 
import argparse
import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

ldapserver = 'ned-ldap.int.example.com'
admindn = os.getenv('USER')

parser=argparse.ArgumentParser(description='LDAP User and Group management utility')
#parser.add_argument('--dn', '-d', help='Your LDAP DN [UID]')
parser.add_argument('--userid', '-u', help='LDAP account to which group membership to be added; To be used with -g or -f')
parser.add_argument('--filename', '-f', help='Provide group list file to modify User\'s group membership ')
parser.add_argument('--groups', '-g', nargs='+', help='provide space separated list of groups on command line')
parser.add_argument('--adduser', '-n', help='Creates a new ldap user account', action='store_true')
parser.add_argument('--modattr', '-m', help='Modify users email address', action='store_true')
parser.add_argument('--deletehost', '-d', help='Delete Host entry from LDAP', action='store_true')
parser.add_argument('--notify', '-s', help='Send password reset link to the User', action='store_true')
parser.add_argument('--addGroup', '-G', help='Add new LDAP group', action='store_true')
parser.add_argument('--deleteGroup', '-D', help='Delete LDAP group; to be used as/with -D -g <space separated group(s)>', action='store_true')
parser.add_argument('--locate', '-l', help='Locate LDAP User or Group; to be used as/with -l -u <uid> or -g <gid>', action='store_true')

args = parser.parse_args()

# Function to find last ldap userid
# Note this is using legacy script /usr/local/bin/lnumber
def find_lastuid():
	L = Popen(['ldapsearch', '-xZZLh', '{}'.format(ldapserver), '-b', 'ou=People,dc=int,dc=example,dc=com'], stdout=PIPE)
	L1 = Popen(["grep", "uidNumber"], stdin=L.stdout, stdout=PIPE)
	L2 = Popen(["sort", "-k", "1", "-n"], stdin=L1.stdout, stdout=PIPE)
	L.stdout.close()
	L1.stdout.close()
	L3 = Popen(["tail", "-n", "1"], stdin=L2.stdout, stdout=PIPE)
	L2.stdout.close()
	N = L3.communicate()[0].strip().split()
    	lstuid = N[1]
	nxtuid = int(lstuid) + 1
	return nxtuid
	#else:
		#print("Check if /usr/local/bin/lnumber is exist")


def find_last_gid():
	L = Popen(['ldapsearch', '-xZZLh', '{}'.format(ldapserver), '-b', 'ou=Group,dc=int,dc=example,dc=com'], stdout=PIPE)
	L1 = Popen(["grep", "gidNumber"], stdin=L.stdout, stdout=PIPE)
	L2 = Popen(["sort", "-k", "2", "-n"], stdin=L1.stdout, stdout=PIPE)
	L.stdout.close()
	L1.stdout.close()
	L3 = Popen(["tail", "-n", "1"], stdin=L2.stdout, stdout=PIPE)
	L2.stdout.close()
	N = L3.communicate()[0].strip().split()
	lstgid = N[1]
	nxtgid = int(lstgid) + 1
	return nxtgid
# Function for User Inputs
def user_inputs():
	U = find_lastuid()
	# Handle blank inputs
	try:
		uidnum = int(raw_input("Please enter UID number (default is: %s)" % U))
	except ValueError:
	    	uidnum = U
		print("Default UID is used: %s" % U)	
	   # print("defualt uid is used: %s" % uidnum)	    
	fname = raw_input("Please enter user's First Name: ")
	cfname = fname.lower()
	lname = raw_input("Please enter user's Last Name: ")
	clname = lname.lower()
	global userid
	userid = "{}.{}".format(cfname, clname)
	maildomain = 'example.com'
	global mail
	mail = "{}.{}@{}".format(cfname, clname, maildomain)
	userhome = "/home/{}.{}".format(cfname, clname)
	print("\n")
	print("Note: email id formation is based on firstname and last name; e.g firstname.lastname@example.com")
	custom_uid = str(raw_input("If you wish to customize UID/email; Please enter customized UID here or press Enter to continue: "))
	if custom_uid.strip() != '':
	    userid = custom_uid
	    mail = "{}@{}".format(userid, maildomain)
	    userhome = "/home/{}".format(userid)
	else:
	    print("Using default UID")
	groupid = 100
	nixshell = '/bin/bash'
	passwd = ''.join(random.sample((string.ascii_lowercase+string.digits),8))
	
	print("-" * 80)
	#ans = raw_input("Please confirm above information is correct, Y|N : ")

	return (fname, lname, cfname, clname, userid, uidnum, mail, groupid, nixshell, userhome, passwd)

# Function to send email notification to user upon user creation

def grp_user_inputs():
	G = find_last_gid()
        try:
        	gidnum = int(raw_input("Please enter UID number (default is: %s): " % G))
        except ValueError:
                gidnum = G
                print("Default UID is used: %s" % G)
        grpname = raw_input("Please enter new LDAP Group name: ")
	print("-" * 80)
	return (gidnum, grpname)	



def send_email_notification(rmail, ruserid):
	message = """From: Linux Operations Team <LinuxOperationsTeam@example.com>
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: LDAP User Account Activation
<p class=MsoNormal>Hello,</p>
<p class=MsoNormal>Your LDAP account has been activated.</p>
UserID: %s
<p class=MsoNormal>Please follow below link to reset your LDAP password.</p>
<p class=MsoNormal><a href="http://ldap-reset-tool.nedpr.paas.example.net">http://ldap-reset-tool.nedpr.paas.example.net</a>
</p>
<p class=MsoNormal>Thank You</p>""" % (rmail, ruserid)
	try:
		server = smtplib.SMTP('glbsmtp.int.example.com',25)
		server.sendmail('LinuxOperationsTeam@example.com', rmail, message)
		print("Successfully sent email notification to %s" % rmail)
	except SMTPException:
		print("Error sending email notification to new ldap user")
		

def find_attribute():
	userid=args.userid
	try:
		output=Popen('ldapsearch -xLh dolomite.int.example.com -b "dc=int,dc=example,dc=com" "(uid=%s)"' % userid, stdout=PIPE)
	except OSError: 
		print(output)

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
                call("ldapmodify -WxZZh %s -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f " % (ldapserver, admindn)+ldfile, shell=True)
	call("rm -f %s" % ldfile, shell=True)

elif args.userid and args.groups:
	for grp in args.groups:
		with open('modify_member_uid.ldif', 'w+') as F:
			lines = ["dn: cn="+grp.strip()+",ou=Group,dc=int,dc=example,dc=com\n", "changetype: modify", "add: memberUid", "memberUid: "+args.userid]
			F.write("%s" % lines[0])
			F.write("%s\n" % lines[1])
			F.write("%s\n" % lines[2])
			F.write("%s\n" % lines[3])
			ldfile=str(F).split(',')[0].split("'")[1]
			F.seek(0)
			rline = F.readlines()
			call("ldapmodify -WxZZh %s -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f " % (ldapserver, admindn)+ldfile, shell=True)
			
	call("rm -f %s" % ldfile, shell=True)
elif args.adduser:
  flag = True
  while flag:
        V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10 = user_inputs()
        print("\n")
        print("New user details are as follow:")
        print("-" * 80)
        print("Name: \t\t\t %s %s" % (V0, V1))
	print("UID: \t\t\t %s" % (V4))
	print("uidNumber: \t\t %s" % V5)
	print("email: \t\t\t %s" % V6)
	print("gid: \t\t\t %s" % V7)
	print("shell: \t\t\t %s" % V8)
	print("home: \t\t\t %s" % V9)
	print("Temp_passwd: \t\t %s" % V10)
	print("Passwd_rest_URL: \t http://ldap-reset-tool.nedpr.paas.example.net/")
	print("-" * 80)
	ans = raw_input("Confirm if above information is correct, Y|N : ")
	
	if ans == 'Y' or ans == 'y':
		S=[V4, V10, V1, V9, V0, V1, V7, V0, V1, V5, V6, V4, V0]
		with open(V4+'.ldif', 'w+') as F:
			lines = ["dn: uid="+V4.strip()+",ou=pci_policy,ou=People,dc=int,dc=example,dc=com",
				"changetype: add",
				"userPassword: "+V10,
				"shadowWarning: 7",
				"sn: "+V1,
				"homeDirectory: "+V9,
				"gecos: "+V0+" "+V1,
				"shadowMax: -1",
				"shadowMin: -1",
				"gidNumber: "+str(V7),
				"loginShell: /bin/bash",
				"shadowInactive: -1",
				"shadowFlag: 0",
				"cn: "+V0+" "+V1,
				"uidNumber: "+str(V5),
				"mail: "+V6,
				"uid: "+V4,
				"shadowLastChange: 17711",
				"objectClass: top",
				"objectClass: person",
				"objectClass: organizationalPerson",
				"objectClass: inetorgperson",
				"objectClass: posixAccount",
				"objectClass: shadowAccount",
				"objectClass: account",
				"givenName: "+V0,
				"shadowExpire: -1"]
			for line in lines:
			    F.write("%s\n" % line)
			ldfile=str(F).split(',')[0].split("'")[1]
			F.seek(0)
			L=F.readlines()
			call("ldapmodify -WxZZh %s -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f " % (ldapserver, admindn)+ldfile, shell=True)
			sleep(3)
			retval=call("id "+V4,shell=True)
			if retval == 0:
				send_email_notification(mail, userid)
				
		flag = False
  call("rm -f %s" % ldfile, shell=True)
elif args.modattr:
	acct = raw_input("For which user account do you wish to modify email address? :")
	newattr = raw_input("Please specify new email address: ")
	with open('mod_attributes.ldif', 'w+') as F:
		lines = ["dn: uid="+acct.strip()+",ou=pci_policy,ou=People,dc=int,dc=example,dc=com",
			"changetype: modify",
			"replace: mail",
			"mail: "+newattr.strip()]
		for line in lines:
			F.write("%s\n" % line)
		ldfile=str(F).split(',')[0].split("'")[1]
		F.seek(0)
		L=F.readlines()
		call("ldapmodify -WxZZh %s -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f " % (ldapserver, admindn)+ldfile, shell=True)
		call("rm -f %s" % ldfile, shell=True)

elif args.deletehost:
	delhost = raw_input("Please specify host name you wish to delete (Use this option carefully) : ")
	with open('mod_attributes.ldif', 'w+') as F:
		lines = ["dn: cn="+delhost+",ou=Hosts,dc=int,dc=example,dc=com", "changetype: delete"]
		for line in lines:
			F.write("%s\n" % line)
		ldfile=str(F).split(',')[0].split("'")[1]
		F.seek(0)
		L=F.readlines()
		call("ldapmodify -WxZZh %s -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f " % (ldapserver, admindn)+ldfile, shell=True)
		call("rm -f %s" % ldfile, shell=True)

elif args.notify:
	email_id = raw_input("Please provide email ID to send passowrd reset URL: ")
	message = """From: Linux Operations Team <LinuxOperationsTeam@example.com>
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: LDAP Password reset link
<p class=MsoNormal>Hello,</p>
<p class=MsoNormal>Please follow below link to reset your LDAP password.</p>
<p class=MsoNormal><a href="http://ldap-reset-tool.nedpr.paas.example.net">http://ldap-reset-tool.nedpr.paas.example.net</a>
</p>
<p class=MsoNormal>Thank You</p>""" % email_id
	try:
		server = smtplib.SMTP('glbsmtp.int.example.com',25)
		server.sendmail('LinuxOperationsTeam@example.com', email_id, message)
		print("Successfully sent email notification to %s" % email_id)
	except SMTPException:
		print("Error sending email notification to new ldap user")

elif args.addGroup:
  flag = True
  while flag:
	V0, V1 = grp_user_inputs()
	print("\n")
	print("New Group details are as below")
	print("-" * 80)
	print("gidNumber:\t\t\t %s" % V0)
	print("GroupName:\t\t\t %s" % V1)
	print("-" * 80)	
	ans = raw_input("please confirm above details are correct Y|N: ")
	if ans == 'Y' or ans == 'y':
		S=[V0, V1]
		with open(V1+".ldif", 'w+') as F:
			lines = ["dn: cn="+V1.strip()+",ou=group,dc=int,dc=example,dc=com",
                                "changetype: add",
				"gidNumber: "+str(V0),
				"cn: "+V1,
				"objectClass: top",
				"objectClass: posixgroup"]
			for line in lines:
                            F.write("%s\n" % line)
                        ldfile=str(F).split(',')[0].split("'")[1]
                        F.seek(0)
                        L=F.readlines()
                        call("ldapmodify -WxZZh %s -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f " % (ldapserver, admindn)+ldfile, shell=True)
			flag = False
  call("rm -f %s" % ldfile, shell=True)

elif args.deleteGroup:
	for grp in args.groups:
                with open(grp+'.ldif', 'w+') as F:
                        lines = ["dn: cn="+grp.strip()+",ou=Group,dc=int,dc=example,dc=com", "changetype: delete"]
			for line in lines:
				F.write("%s\n" % line)
                        ldfile=str(F).split(',')[0].split("'")[1]
                        F.seek(0)
                        rline = F.readlines()
                        call("ldapmodify -WxZZh %s -D \"uid=%s,ou=pci_policy,ou=People,dc=int,dc=example,dc=com\" -f " % (ldapserver, admindn)+ldfile, shell=True)

        call("rm -f %s" % ldfile, shell=True)

	
elif args.locate:
  if args.userid:
      L = Popen(['ldapsearch', '-xZZLh', '{}'.format(ldapserver), '-b', 'ou=People,dc=int,dc=example,dc=com'], stdout=PIPE)
      L1 = Popen(["grep", "uid:"], stdin=L.stdout, stdout=PIPE)
      L.stdout.close()
      L2 = Popen(["grep", '{}'.format(args.userid)], stdin=L1.stdout, stdout=PIPE)
      L1.stdout.close()
      UID = L2.communicate()[0]
      print(UID)
  elif args.groups:
      grp = args.groups	
      G = Popen(['ldapsearch', '-xZZLh', '{}'.format(ldapserver), '-b', 'ou=Group,dc=int,dc=example,dc=com'], stdout=PIPE)
      G1 = Popen(["grep", "dn:"], stdin=G.stdout, stdout=PIPE)
      G.stdout.close()
      G2 = Popen(["grep", str(grp[0])], stdin=G1.stdout, stdout=PIPE)
      data = G2.communicate()[0]
      #for line in data:
      D1=data.split("\n")
      L1=D1[:-1]
      for i in L1:
	print(i.split(',')[0].split(' ')[1].split('=')[1])
	
else:
    print parser.print_help()
