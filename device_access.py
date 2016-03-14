#!/usr/bin/env python

import paramiko
import os
import sys

class Device_ssh(object):
	def __init__(self,ip,username,pwd):
		self.ip = ip
		self.user = username
		self.pwd = pwd

	def connect_device(self):
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(self.ip,username=self.user,password=self.pwd)

	def rundevicecmd(self,cmd):
		(iin,out,err) = self.ssh.exec_command(cmd)
		if out: 
			for line in out.readlines():
				print line
		else: 
			print "Error:",err	
		self.ssh.close()


def main(cmd):
	device = Device_ssh('10.0.0.4','lab1','lab1')
	device.connect_device()
	device.rundevicecmd(cmd)

cmd= sys.argv[1]
if __name__ == '__main__':
	main(cmd)
