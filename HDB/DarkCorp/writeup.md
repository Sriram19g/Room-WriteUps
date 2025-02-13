###nmap scan :

Open 10.10.11.54:22
Open 10.10.11.54:80 --> drip.htb 

PORT   STATE SERVICE REASON          VERSION
22/tcp open  ssh     syn-ack ttl 127 OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey: 
|   256 33:41:ed:0a:a5:1a:86:d0:cc:2a:a6:2b:8d:8d:b2:ad (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPM91a70VJCxg10WFerhkQv207077raOCX9rTMPBeEbHqGHO954XaFtpqjoofHOQWi2syh7IoOV5+APBOoJ60k0=
|   256 04:ad:7e:ba:11:0e:e0:fb:d0:80:d3:24:c2:3e:2c:c5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHquJFnMIhX9y8Ea87tDtRWPtxThlpE2Y1WxGzsyvQQM
80/tcp open  http    syn-ack ttl 127 nginx 1.22.1
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: nginx/1.22.1

drip.htb --> mail.drip.htb
