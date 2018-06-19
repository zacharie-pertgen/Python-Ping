import os
hostname = input('Please specify the host to ping: ')
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')