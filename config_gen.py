#!/usr/bin/env python

class cisco(object):
    def __init__(self,mgmtip,hostname,snmp_community):
        self.mgmt_ip = mgmtip
        self.hostname = hostname
        self.community = snmp_community
        self.config = ''

    def intf_config(self,intfname,ipwsub):
        self.config+= 'interface '+intfname
        if '/' in ipwsub:
            subnet = ipwsub.split('/')[1]
            mask = self.prefixtomask(subnet)
        elif ' ' in ipwsub:
            self.config+='\n ip address '+ipwsub
        else:
            self.config+='\n ip address '+ipwsub+' 255.255.255.255'

rtr1 = cisco('1.1.1.1','edge','asdf')
rtr1.intf_config('Ge0/0','10.00.0.1')
print rtr1.config
