Chemistry - Active Room Linux 
==============================

nmap result:
------------

Open port : 22 (ssh) , 5000 (werkzeug --> Flask)

http://chemistry.htb/dashboard --> need to upload the CIF file 

CIF --> crystallographic information file 

I found the cve for CIF  ==> `hack.cif`

i get the shell using netcat 

found db in instance/database.db 

ssh creds:
---------- 
[Username] : rosa 
[Hash]     : 63ed86ee9f624c7b14f1d4f43dc251a5 
[Password] : unicorniosrosados

user.txt ==> e5f793914eda281e5ef19e1d16f54528 
============================================== 

previledge escalation:
---------------------- 

Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN

8080  --> python server let's try port forwarding 

curl http://0.0.0.0:8080 --head
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 5971
Date: Tue, 18 Feb 2025 16:54:40 GMT
Server: Python/3.9 aiohttp/3.9.1

CVE-2024-23334:
--------------- 
A path traversal vulnerability in the python AioHTTP library =< 3.9.1

ssh private found for root ..

change the key so that the user can use..

ssh root@chemistry.htb -i key  

root.txt ==> 1e23ed7832df3ecde3a3f41fd1d4d58d
===============================================
