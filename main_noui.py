import socket
from time import sleep

## IP / PUERTOS ##
portPuerto = {
  "10.10.10.10":"123",
  "11.11.11.11":"456" 
}

if __name__ == '__main__':
  for ip, port in portPuerto.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip,int(port)))
    if result == 0:
      print(f"IP: {ip} \t - PORT: {port} \t -> \033[92m {'OK'}\033[00m")
    else:
      print(f"IP: {ip} \t - PORT: {port} \t -> \033[91m {'FAIL'}\033[00m")
    sock.close()  
    sleep(5)