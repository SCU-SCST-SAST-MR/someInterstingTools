import os
import time
from pynput.keyboard import Controller, Key, Listener
import random
import win32con
import win32clipboard as wincld

# 监听按压
TIMES = 50
TIME_SLEEP = 0.5

class listener():
    def __init__(self,TIMES,TIME_SLEEP):
        self.kb = Controller()
        self.TIMES = TIMES
        self.TIME_SLEEP = TIME_SLEEP
        pass
    def on_press(self,key):
        if not os.path.exists(os.path.abspath(os.path.dirname(__file__) + '\\hello.txt')):
            path = os.path.abspath(os.path.dirname(__file__) + '\\hello.txt')
            fd = open(path, mode="w", encoding="utf-8")
            fd.write('这是个demo')
            fd.close()
            pass
        try:
            if key.char == 'c':
                # 队友
                k = Controller()
                k.press(Key.enter)
                k.release(Key.enter)
                del k
                self.ma()
                pass
            if key.char == '/':
                # 全局
                k = Controller()
                k.press(Key.shift)
                k.press(Key.enter)
                k.release(Key.shift)
                k.release(Key.enter)
                del k
                self.ma()
                pass
        except AttributeError:
            # print("正在按压:", format(key))
            pass


    # 监听释放
    def on_release(self,key):
        # print("已经释放:", format(key))
        pass

        if key == Key.end:
            # 按住end停止监听
            print('停止监听')
            del self.kb

            return False


    # 开始监听
    def start_listen(self):
        print('开始监听')
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


    def clicpBoard(self,text):
        time.sleep(self.TIME_SLEEP)
        # 打开粘贴板
        wincld.OpenClipboard()
        # 清空粘贴板
        wincld.EmptyClipboard()
        wincld.SetClipboardData(win32con.CF_UNICODETEXT, text)
        wincld.CloseClipboard()
        pass


    def ma(self):
        path = os.path.abspath(os.path.dirname(__file__) + '\\hello.txt')
        for i in range(self.TIMES):
            with open(path, encoding='UTF-8') as f:
                line = f.readlines()
                line = [x.strip('\n') for x in line]
                self.clicpBoard(random.choice(line))
                f.close()
                pass

            k = Controller()
            k.press(Key.ctrl_l)
            k.press('v')
            k.release(Key.ctrl_l)
            k.release('v')
            k.press(Key.enter)
            k.release(Key.enter)
            del k
        pass


if __name__ == '__main__':
    # 实例化键盘

    # 开始监听,按end退出监听
    demo = listener(TIMES,TIME_SLEEP)
    demo.start_listen()
