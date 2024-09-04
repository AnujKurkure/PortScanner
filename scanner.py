import socket
import sys
from datetime import datetime

target = input(str("Target IP: "))

# Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:
	
	# Scan every ports in the Target IP
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5)
		
		# Return Open Ports 
		result = s.connect_ex((target,port))
		if result == 0:
			print("[*] Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n Exiting : (")
		sys.exit()
except socket.error:
		print("\ Host not responding : (")
		sys.exit()
