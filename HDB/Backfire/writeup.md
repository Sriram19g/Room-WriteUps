# [HackTheBox] - [BackFire]

## Enumeration:
```bash
 rustscan -a 10.10.11.49 --range 1-65535 --tries 3 --ulimit 5000 -- -A -sCV -Pn -r -n --reason --min-rate 2000 --disable-arp-ping
```
- **Open Port** : 22(ssh), 443(https), 8000(http.server - python server)
 Supported Methods: GET HEAD POST
| http-ls: Volume /
| SIZE  TIME               FILENAME
| 1559  17-Dec-2024 11:31  disable_tls.patch
| 875   17-Dec-2024 11:34  havoc.yaotl
|_

- **havoc.yaotl**
Teamserver {
    Host = "127.0.0.1"
    Port = 40056

    Build {
        Compiler64 = "data/x86_64-w64-mingw32-cross/bin/x86_64-w64-mingw32-gcc"
        Compiler86 = "data/i686-w64-mingw32-cross/bin/i686-w64-mingw32-gcc"
        Nasm = "/usr/bin/nasm"
    }
}

Operators {
    user "ilya" {
        Password = "CobaltStr1keSuckz!"
    }

    user "sergej" {
        Password = "1w4nt2sw1tch2h4rdh4tc2"
    }
}

Demon {
    Sleep = 2
    Jitter = 15

    TrustXForwardedFor = false

    Injection {
        Spawn64 = "C:\\Windows\\System32\\notepad.exe"
        Spawn32 = "C:\\Windows\\SysWOW64\\notepad.exe"
    }
}

Listeners {
    Http {
        Name = "Demon Listener"
        Hosts = [
            "backfire.htb"
        ]
        HostBind = "127.0.0.1" 
        PortBind = 8443
        PortConn = 8443
        HostRotation = "round-robin"
        Secure = true
    }
}
- **disable_tls.patch**

Disable TLS for Websocket management port 40056, so I can prove that sergej is not doing any work Management port only allows local connections (we use ssh forwarding) so 
this will not compromize our teamserver

diff --git a/client/src/Havoc/Connector.cc b/client/src/Havoc/Connector.cc
index abdf1b5..6be76fb 100644
--- a/client/src/Havoc/Connector.cc
+++ b/client/src/Havoc/Connector.cc
@@ -8,12 +8,11 @@ Connector::Connector( Util::ConnectionInfo* ConnectionInfo )
 {
     Teamserver   = ConnectionInfo;
     Socket       = new QWebSocket();
-    auto Server  = "wss://" + Teamserver->Host + ":" + this->Teamserver->Port + "/havoc/";
+    auto Server  = "ws://" + Teamserver->Host + ":" + this->Teamserver->Port + "/havoc/";
     auto SslConf = Socket->sslConfiguration();
 
     /* ignore annoying SSL errors */
     SslConf.setPeerVerifyMode( QSslSocket::VerifyNone );
-    Socket->setSslConfiguration( SslConf );
     Socket->ignoreSslErrors();
 
     QObject::connect( Socket, &QWebSocket::binaryMessageReceived, this, [&]( const QByteArray& Message )
diff --git a/teamserver/cmd/server/teamserver.go b/teamserver/cmd/server/teamserver.go
index 9d1c21f..59d350d 100644
--- a/teamserver/cmd/server/teamserver.go
+++ b/teamserver/cmd/server/teamserver.go
@@ -151,7 +151,7 @@ func (t *Teamserver) Start() {
 		}
 
 		// start the teamserver
-		if err = t.Server.Engine.RunTLS(Host+":"+Port, certPath, keyPath); err != nil {
+		if err = t.Server.Engine.Run(Host+":"+Port); err != nil {
 			logger.Error("Failed to start websocket: " + err.Error())
 		}
 

- **Havoc Framework** 
Havoc appears to be a framework or tool that is related to cybersecurity operations or penetration testing. Based on the details you've shared from the havoc.yaotl file, it seems that Havoc might be part of a command-and-control (C2) framework or a malware/attack tool.

- **CVE Exploration**
- **CVE-2024-41570: Havoc C2 SSRF + RCE POC**
```
https://github.com/godylockz/CVE-2024-41570
```
SSRF CVE-2024-41570 This exploit works by spoofing a demon agent registration and checkins to open a TCP socket on the teamserver and read/write data from it. This allows attackers to leak origin IPs of teamservers and much more.

RCE Havoc is vulnerable to command injection enabling an authenticated user to execute commands on the Teamserver. Affects versions 0.3 up to the latest release 0.6. Havoc's default profile contains hardcoded passwords, so a C2 operator careless enough to use the default profile on a public network can immediately be exploited.

```https://github.com/sebr-dev/Havoc-C2-SSRF-to-RCE
```
This is a modified version of the CVE-2024-41570 SSRF PoC from @chebuya chained with the auth RCE exploit from @hyperreality. This exploit executes code remotely to a target due to multiple vulnerabilities in Havoc C2 Framework. where chebuya and hyperreality are the author of this room... so using this..

- **User.txt** --> 947e273a29994eafe51e5a478aa0295e

- **hardhat.txt**
Sergej said he installed HardHatC2 for testing and  not made any changes to the defaults
I hope he prefers Havoc bcoz I don't wanna learn another C2 framework, also Go > C# 

- **Checking netsat**
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:7096            0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:8443          0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:40056         0.0.0.0:*               LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
udp        0      0 0.0.0.0:68              0.0.0.0:*                          

-- **Trying port forwarding**
i got succeed for the port 7096
ssh -L 7096:127.0.0.1:7096 ilya@backfire.htb


