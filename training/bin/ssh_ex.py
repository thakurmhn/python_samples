#!/usr/bin/python3.6
import paramiko

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='ocnode1.mhn.com',port=22,username='root',password='redhat')

stdin,stdout,stderr=ssh.exec_command('ls')
out=stdout.readlines()
print(out)

#stdin.write('')
#sftp=ssh.open_sftp()
#sftp.get('readme.txt','readme_copied.txt')
