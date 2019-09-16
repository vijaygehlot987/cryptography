import socket
host= input("Enter a remote host to scan: ")
IP= socket.gethostbyname(host)
for port in range(1,100):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((IP,port))
    if result == 0:
        print("Port {}: Open"+str(port))
    
