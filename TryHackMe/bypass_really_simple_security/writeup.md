bypass really simple security -writeup 
=======================================

nmap result:
------------
PORT     STATE    SERVICE
22/tcp   open     ssh
| ssh-hostkey: 
|   3072 36:ea:03:8e:a1:50:1b:c7:76:85:84:c2:46:e1:81:fe (RSA)
|   256 e6:24:00:6f:c0:19:9d:50:85:33:a9:10:57:f4:7e:ee (ECDSA)
|_  256 b6:44:3a:4e:78:ee:ff:c3:f9:00:60:b2:d6:b4:9f:fb (ED25519)
42/tcp   filtered nameserver
80/tcp   open     http
|_http-title: Error response
541/tcp  filtered uucp-rlogin
8080/tcp open     http-proxy
|_http-title: Vulnerable THM Blog
|_http-open-proxy: Proxy might be redirecting requests
|_http-generator: WordPress 6.7.1 


directory enumeration:
----------------------
Target: http://vulnerablewp.thm:8080/

[00:23:02] Starting: 
[00:24:06] 200 -    7KB - /license.txt
[00:24:22] 200 -    3KB - /phpmyadmin/doc/html/index.html
[00:24:24] 200 -    3KB - /phpmyadmin/index.php
[00:24:24] 200 -    3KB - /phpmyadmin/
[00:24:26] 200 -    3KB - /readme.html
[00:24:50] 200 -  509B  - /wp-admin/install.php
[00:24:50] 200 -    0B  - /wp-config.php
[00:24:50] 200 -    0B  - /wp-content/
[00:24:50] 200 -   84B  - /wp-content/plugins/akismet/akismet.php
[00:24:51] 200 -  479B  - /wp-content/uploads/
[00:24:51] 200 -    0B  - /wp-cron.php
[00:24:51] 200 -    2KB - /wp-login.php
[00:24:51] 200 -    0B  - /wp-includes/rss-functions.php
[00:24:51] 200 -    5KB - /wp-includes/

Q1) --> Rsssl_Two_Factor_On_Board_Api 
Q2) --> check_login_and_get_user  

Exploit.py output:
------------------

Request successful!

Cookie 1:
Cookie Name: wordpress_eb51341dc89ca85477118d98a618ef6f
Cookie Value: admin|1740803147|zSM9klQLGx6hTTarBkrqKjUVRV0GHkFl84FxmNSOGvB|5ee39e2d68626badff98b4d10dad4b335398b64e41744c48c115c7acee2bd114

Cookie 2:
Cookie Name: wordpress_logged_in_eb51341dc89ca85477118d98a618ef6f
Cookie Value: admin|1740803147|zSM9klQLGx6hTTarBkrqKjUVRV0GHkFl84FxmNSOGvB|a5a6d1c344d88a8c3ee59bc49fef45ac73b6c0eb6382bf9589cc1eef5224e125

Q3) --> admin@fake.thm 
Q4) --> jack 
Q5) --> post 

Q6) --> nay 

--------------------------------------------------------------------------------
