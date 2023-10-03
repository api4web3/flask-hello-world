import socket

def getIp():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    data = str(IPAddr) + " " + str(hostname)
    return data

if __name__ == '__main__':
    getIp()
