import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
    
print("IP Adresa e kompjuterit tuaj eshte:" + IPAddr) 

#Referenca:
#https://www.geeksforgeeks.org/python-program-find-ip-address/
