# created by kbkozlev 23.11.2021
import time
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Controller as MouseController

key = KeyController()
mouse = MouseController()


def f1_toggle():
    key.press(Key.f1)
    key.release(Key.f1)


def enter_toggle():
    key.press(Key.enter)
    key.release(Key.enter)


input("Press any key to start:")
time.sleep(5)
while True:

    start_position = mouse.position

    key.press(Key.ctrl_l)
    print("Ctrl pressed")
    f1_toggle()
    print("F1 toggled")
    key.release(Key.ctrl_l)
    print("Ctrl released")
    time.sleep(1)
    enter_toggle()
    print("Enter toggled")
    time.sleep(.5)

    end_position = mouse.position

    if start_position != end_position:
        input("Press any key to continue ")

