from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Controller as Keyboard

def get_keys():
    # ARK
    # return ["w", "e", "a", "s", "d", "f", "Key.space", "Key.shift", "Key.shift_r", "Key.tab", "Key.left", "Key.up", "Key.right", "Key.down"]

    # Among us
    return ["w", "e", "a", "s", "d", "v", "q", "r", "t", "Key.tab"]

def get_key(keyId):
    return get_keys()[keyId]

def get_id(key):
    try:
        print("Key Pressed:", (str(key) + ""), sep=" ")
        return get_keys().index(key.char)
    except:
        print("???")

keyboard = Keyboard()
mouse = Mouse()

# Mouse:
def click():
    mouse.press(Button.left)
    return

def position(x, y):
    mouse.position(x, y)

# Keyboard:
def press(key):
    keyboard.press(key)
    return

def release(key):
    keyboard.release(key)
    return
