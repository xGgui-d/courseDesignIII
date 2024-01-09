import socket
import cv2
import pickle
import struct

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口
server_socket.bind(('127.0.0.1', 8888))
print('正在监听连接...')
# 监听连接
server_socket.listen(5)
# 接受客户端连接
client_socket, addr = server_socket.accept()
print('接受到连接请求，建立连接成功')
# 服务端模拟打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头视频流数据
    ret, frame = cap.read()
    # 对帧进行编码
    data = pickle.dumps(frame)
    # 获取帧的大小
    size = struct.pack("L", len(data))
    # 发送帧大小
    client_socket.sendall(size)
    # 发送帧数据
    client_socket.sendall(data)

# 关闭连接
client_socket.close()
server_socket.close()