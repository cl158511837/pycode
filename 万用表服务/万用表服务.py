import socket

def switch(context: str) -> float:
    switcher = {
        "read?": 1.2,
        "write?": 230.22,
        "Test?": 82.33,
    }
    return switcher.get(context, 0)

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口号
server_ip = '127.0.0.1'  # 服务器IP地址
server_port = 5025  # 服务器端口号
server_address = (server_ip, server_port)
server_socket.bind(server_address)

# 监听连接
server_socket.listen(10)

print("服务器启动，等待连接...")
while True:
    try:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print("客户端已连接:", client_address)

        while client_socket:
            # 接收数据
            arr_cmd = bytearray(56)
            try:
                client_socket.recv_into(arr_cmd, 7)
            except OSError as e:
                print('接收数据时发生异常:', e)
                break
                
            str_ret = arr_cmd.decode('ascii')
            print("数据内容:", str_ret)
            
            # 处理接收到的数据
            f_ret = switch(str_ret)
            
            # 构造响应数据
            str_response = format(f_ret, '.9f')
            
            try:
                # 发送响应数据
                client_socket.sendall(str_response.encode('ascii'))
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