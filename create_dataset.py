import os
import time
import dxcam
from PIL import Image
from game_control import get_id
from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as key_listener

import timeit

camera = dxcam.create()


def get_screenshot():
    screen = camera.grab()
    if screen is not None:
        img = Image.fromarray(screen).resize((150, 150), Image.BICUBIC)
        return img
    else:
        pass


def save_event_keyboard(data_path, event, key):
    key = get_id(key)
    if key is not None:
        data_path = f"{data_path}/0,{event},{key},{time.time()}"
        screenshot = get_screenshot()
        if screenshot is not None:
            screenshot.save(f"{data_path}.JPEG")
            return
        else:
            pass


def save_event_mouse(x, y, cm, data_path):
    data_path = f"{data_path}/1,{x},{y},{cm},{time.time()}"
    screenshot = get_screenshot()
    if screenshot is not None:
        screenshot.save(data_path + ".JPEG")
        return
    else:
        pass


def listen_mouse():
    data_path = 'Data/Train_Data/Mouse'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    def on_click(x, y):
        print("Click!")
        save_event_mouse(x, y, 1, data_path)

    '''
    def on_move(x, y):
        save_event_mouse(x, y, 0, data_path)
    '''

    mouse_listener(on_click=on_click).start()


def listen_keyboard():
    data_path = 'Data/Train_Data/Keyboard'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    def on_press(key):
        save_event_keyboard(data_path, 1, key)

    def on_release(key):
        save_event_keyboard(data_path, 2, key)

    key_listener(on_press=on_press, on_release=on_release).start()


def main():
    dataset_path = 'Data/Train_Data/'
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
    listen_keyboard()
    listen_mouse()
    return


main()
