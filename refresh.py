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

x = 1
xx = 5

input("Press any key to start:")
while xx > 0:
    print("Starting in " + str(xx) + " seconds")
    xx -= 1
    time.sleep(1)
while True:

    start_position = mouse.position

    print("Cycle " + str(x))
    key.press(Key.ctrl_l)
    f1_toggle()
    key.release(Key.ctrl_l)
    time.sleep(1)
    enter_toggle()
    x += 1
    time.sleep(.5)

    end_position = mouse.position

    if start_position != end_position:
        break
