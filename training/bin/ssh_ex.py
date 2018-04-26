#!/bin/python3.6
import paramiko

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='test.rebex.net',port=22,username='demo',password='password')

stdin,stdout,stderr=ssh.exec_command('ls')
out=stdout.readlines()
print(out)

#stdin.write('')
sftp=ssh.open_sftp()
sftp.get('readme.txt','readme_copied.txt')
