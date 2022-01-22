import subprocess
from time import sleep

import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()


def screen_cap():
    keyboard.press(Key.alt)
    keyboard.press('n')
    keyboard.release(Key.alt)
    keyboard.release('n')
    return


def file_save(name, counter):
    save_name = name + "_" + str(counter)
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release(Key.ctrl)
    keyboard.release('s')
    sleep(1)
    keyboard.type(save_name)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    counter += 1
    return counter


def minimize():
    keyboard.press(Key.cmd)
    keyboard.press(Key.down)
    keyboard.release(Key.cmd)
    keyboard.release(Key.down)



# location = input("Where do you want to save the files?")
name = input("File name starts with: ")
start = int(input("Start at: "))
counter = start
while True:
    subprocess.Popen("C:\\Windows\\System32\\snippingTool.exe")
    sleep(0.5)
    screen_cap()
    sleep(3)
    counter = file_save(name, counter)
    sleep(0.5)
    minimize()
    sleep(1.5)
