LinkVortex HTB 

nmap result:--->
----------------

PORT      STATE    SERVICE REASON         VERSION
22/tcp    open     ssh     syn-ack ttl 63 OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:f8:b9:68:c8:eb:57:0f:cb:0b:47:b9:86:50:83:eb (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMHm4UQPajtDjitK8Adg02NRYua67JghmS5m3E+yMq2gwZZJQ/3sIDezw2DVl9trh0gUedrzkqAAG1IMi17G/HA=
|   256 a2:ea:6e:e1:b6:d7:e7:c5:86:69:ce:ba:05:9e:38:13 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKKLjX3ghPjmmBL2iV1RCQV9QELEU+NF06nbXTqqj4dz
80/tcp    open     http    syn-ack ttl 63 Apache httpd
|_http-title: Did not follow redirect to http://linkvortex.htb/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache
40770/tcp filtered unknown no-response
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

------------------------------------------------------------------------

directory ffuzzing 
------------------
[15:20:03] 200 -   15KB - /favicon.ico
[15:20:15] 200 -    1KB - /LICENSE
[15:20:36] 200 -  103B  - /robots.txt
[15:20:40] 200 -  255B  - /sitemap.xml

-------------------------------------------------------------------------

/robots.txt
-----------
User-agent: *
Sitemap: http://linkvortex.htb/sitemap.xml
Disallow: /ghost/
Disallow: /p/
Disallow: /email/
Disallow: /r/

----------------------------------------------------------------------------

/ghost --> sign page 

dev.linkvortex.htb  --> found may git files while search for dire search

[16:58:47] Starting: 
[16:58:53] 200 -   73B  - /.git/description
[16:58:53] 200 -  201B  - /.git/config
[16:58:53] 200 -  557B  - /.git/
[16:58:53] 200 -   41B  - /.git/HEAD
[16:58:53] 200 -  620B  - /.git/hooks/
[16:58:53] 200 -  402B  - /.git/info/
[16:58:53] 200 -  240B  - /.git/info/exclude
[16:58:53] 200 -  401B  - /.git/logs/
[16:58:53] 200 -  175B  - /.git/logs/HEAD
[16:58:53] 200 -  418B  - /.git/objects/
[16:58:53] 200 -  147B  - /.git/packed-refs
[16:58:53] 200 -  393B  - /.git/refs/
[16:58:54] 200 -  691KB - /.git/index

gitdumper  tool --> user to dump the exposed .git folders and file

passwords obtained :
--------------------
thisissupersafe
OctopiFociPilfer45
Sl1m3rson99
superSecure

/ghost --> sign page:
---------------------
[Username] : admin@linkvortex.htb 
[Password] : OctopiFociPilfer45

exploit:
--------
[github] : https://github.com/0xyassine/CVE-2023-40028/blob/master/CVE-2023-40028.sh

Dockerfile.ghost --> var/lib/ghost/config.production.json

ssh credentials:
----------------
[Username] : bob@linkvortex.htb 
[password] : fibber-talented-worth

user.text --> b46699611ac5c7d32b28f18a94e9ddf3
==========
