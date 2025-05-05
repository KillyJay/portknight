

import socket
import termcolor

ascii_art = '''
    ____             __  __ __       _       __    __ 
   / __ \____  _____/ /_/ //_/____  (_)___ _/ /_  / /_
  / /_/ / __ \/ ___/ __/ ,<  / __ \/ / __ `/ __ \/ __/
 / ____/ /_/ / /  / /_/ /| |/ / / / / /_/ / / / / /_  
/_/    \____/_/   \__/_/ |_/_/ /_/_/\__, /_/ /_/\__/  
                                   /____/             
	Developed by: Ayomide Kilajolu
 	https://github.com/KillyJay
'''

print (ascii_art)

def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
