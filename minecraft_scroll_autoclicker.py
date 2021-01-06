from pynput.mouse import Listener, Button, Controller
from pynput.keyboard import Key, Listener as KeyboardListener
import sys
import multiprocessing
import threading

RIGHT_BUTTON = True
OFF = False

mouse = Controller()

def on_scroll(x, y, dx, dy):
    global OFF
    global RIGHT_BUTTON
    
    if not OFF and dy == 1:
        if RIGHT_BUTTON:
            mouse.press(Button.right)
            mouse.release(Button.right)
        else:
            mouse.press(Button.left)
            mouse.release(Button.left)
        mouse.scroll(0, -1)

def on_press(key):
    global OFF
    global RIGHT_BUTTON

    pressed_key = ''
    try:
        pressed_key = key.char
    except AttributeError:
        pressed_key = str(key)

    if pressed_key == '[':
        if RIGHT_BUTTON:
            RIGHT_BUTTON = False
            print("Changed to LeftClick")
        else:
            RIGHT_BUTTON = True
            print("Changed to RightClick")
    elif pressed_key == ']':
        if OFF:
            OFF = False
            print("Turned on")
        else:
            OFF = True
            print("Turned off")

def handle_scroll():
    with Listener(on_scroll=on_scroll) as listener:
        listener.join()

def handle_keys():
    with KeyboardListener(on_press=on_press) as keyboard_listener:
        keyboard_listener.join()

if __name__ == "__main__":
    print("Started program... Instructions:")
    print("Press key '[' to toggle mouse button")
    print("Press key ']' to turn off or turn on scroll clicking")
    print("Press Ctrl + C to terminate the program")
    print("\n--------------\n")

    try:
        handler1 = threading.Thread(target=handle_scroll, args=())
        handler2 = threading.Thread(target=handle_keys, args=())

        handler1.start()
        handler2.start()

        handler1.join()
        handler2.join()
    except KeyboardInterrupt:
        print("Ctrl + C has been pressed. Stoping program...")
        sys.exit()