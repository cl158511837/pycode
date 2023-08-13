import socket

HOST = '127.0.0.1'
PORT = 8887
print("服务器启动，等待连接...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        try:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    # 接收数据
                    arrCmd = bytearray(256)
                    try:
                        conn.recv_into(arrCmd[:len(arrCmd)])
                    except OSError as e:
                        print('接收数据时发生异常:', e)
                        break

                    strRet = arrCmd.decode("utf-8", errors="ignore")
                    strRet = strRet.replace("\r\n", "").replace("\x00", "")
                    print('Received:', strRet)

                    # 处理请求数据
                    # ...

                    str_ret = format(34.02323, '.9f')
                    # 返回响应
                    try:
                        conn.sendall(str_ret.encode('ascii'))
                    except OSError as e:
                        print('发送数据时发生异常:', e)
                        break

        except KeyboardInterrupt:
            # 捕获键盘中断信号，退出服务器
            print("服务器已停止")
            break

        except Exception as e:
            # 捕获其他异常，打印错误信息并继续运行
            print("发生异常:", e)
            continue