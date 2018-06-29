#Basic Socket/Port Scanner
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('cls', shell=True)

remServ = input("What is the name of the machine you would like to scan?: ")
remServIP = socket.gethostbyname("www.yahoo.com")

print("=") * 60
print("Please wait while I scan the host", remServIP)
print("=") * 60

t1 = datetime.now()

try:
    for port in range(1, 1500):
        sock = (socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remServIP, port))
        if result == 0:
            print("Port {}:     Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("You interrupted the operation")
    sys.exit

except socket.error:
    print("Couldn't connect to the server, please try again.")
    sys.exit()

t2 = datetime.now()

time = t2 - t1
print("Scan Completed in: ", time)