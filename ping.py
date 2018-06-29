import os

print("Please make sure you are running your console as administrator! Otherwise ping functionality will not work")

hostname = input('Please specify the host to ping: ')
response = os.system("ping -c 1 " + hostname)


#Basic Ping ability
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')