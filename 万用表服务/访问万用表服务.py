import socket
import time

arrCmd = bytearray(56)
arrCmd[0] = 114
arrCmd[1] = 101
arrCmd[2] = 97
arrCmd[3] = 100
arrCmd[4] = 63
arrCmd[5] = 13
arrCmd[6] = 10

m_tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m_strIp = '127.0.0.1'  # 服务器IP地址
server_port = 5025  # 服务器端口号
m_tcpSocket.connect((m_strIp, server_port))

m_tcpSocket.send(arrCmd[:7])
time.sleep(0.05)

arrRet = m_tcpSocket.recv(256)
strRet = arrRet[:len(arrRet)].decode('ascii')

while True:
    strV = ""
    if len(strRet) > 0:
        strV = "{:.9f}".format(float(strRet))
        print("值：",strV)

    input("请输入内容: ")
