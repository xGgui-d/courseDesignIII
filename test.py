from PIL import Image, ImageTk
import tkinter as tk
import cv2
from tkinter import Label, PhotoImage

class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # 打开摄像头
        self.cap = cv2.VideoCapture(0)

        # 创建一个Label用于显示摄像头捕获的图像
        self.label = Label(window)
        self.label.pack(padx=10, pady=10)

        # 每隔10毫秒调用一次update函数
        self.window.after(10, self.update)

        # 点击窗口的关闭按钮时，调用on_close函数
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def update(self):
        # 读取摄像头的一帧
        ret, frame = self.cap.read()

        # 将OpenCV图像转换为Pillow图像
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)

        # 将Pillow图像转换为Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image=image)

        # 更新Label的图像
        self.label.configure(image=photo)
        self.label.image = photo

        # 每隔10毫秒调用一次update函数
        self.window.after(10, self.update)

    def on_close(self):
        # 释放摄像头资源
        self.cap.release()
        self.window.destroy()

# 创建Tkinter窗口
root = tk.Tk()
app = CameraApp(root, "Camera App")
root.mainloop()
