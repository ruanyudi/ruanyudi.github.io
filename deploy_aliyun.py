import socket
import argparse

def start_client(host='127.0.0.1', port=8888):
    # 创建TCP/IP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")

    # 发送数据
    message = "Deploy!"
    client_socket.send(message.encode('utf-8'))
    print(f"Sent data to server: {message}")

    # 接收响应
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received response from server: {response}")

    # 关闭连接
    client_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TCP Server')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host address to bind')
    parser.add_argument('--port', type=int, default=12345, help='Port to bind')

    args = parser.parse_args()
    start_client(args.host, args.port)
