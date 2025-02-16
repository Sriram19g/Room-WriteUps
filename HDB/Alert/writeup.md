Alert (Easy -Linux) writeup:  
=============================

target : 10.10.11.44

nmap report:
-------------

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))

subdomain-enumeration:
-------------------------
statistics.alert.htb 

ssh creds:
-----------
[username] : albert 
[password] : manchesterunited

user flag ---> 6bf832333b70af44cb954b4e7f2f790c
================================================

found the machine listening to port 8080 ..

root using the 8080 in the path /opt/website-monitor

monitor folder with write access 

root.txt is present in the folder but need root access 

root flag ---> d724f9f3a64c0c06964072032fd96758 
===============================================

