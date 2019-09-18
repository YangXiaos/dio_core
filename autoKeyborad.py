import time

import sys
from pynput import mouse
from pynput.mouse import Button
from pynput.keyboard import Controller,Key,Listener

kb = Controller()
m = mouse.Controller()

class detail(object):
    start = None
    over = None


# 监听按压
def on_press(key):
    try:
        if key.char == "l":
            # 停止监听
            detail.start = m.position
            print("正在按压:", format(key.char))
            print(detail.start )
        if key.char == ";":
            # 停止监听
            print("正在按压:", format(key.char))
            detail.over = m.position
            print(detail.over)
        if key.char == "'":
            print("正在按压:", format(key.char))
            while True:
                m.move(detail.start[0] - m.position[0], detail.start[1] - m.position[1])
                print("移动 {}", m.position)
                m.press (Button.left)

                time.sleep(1)
                m.move(detail.over[0] - m.position[0], detail.over[1] - m.position[1])
                print("移动 {} ", m.position)
                time.sleep(1)
                m.release(Button.left)
                time.sleep(1)
                m.click(Button.left, 1)
                time.sleep(1)
                if m.position != detail.over:
                    print("推出")
                    break
    except AttributeError:
        pass


# 监听释放
def on_release(key):
    pass




# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    # 实例化键盘


    kb.press(Key.space)

    # 开始监听,按esc退出监听
    start_listen()