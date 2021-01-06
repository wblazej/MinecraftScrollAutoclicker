from pynput.mouse import Listener, Button, Controller
from time import sleep
import sys

class AutoClicker:
    def __init__(self, right_button: bool = True):
        self.mouse = Controller()
        self.right_button = right_button
        self.listener = None

        print("Started autoclicker. Press Ctrl + C to terminate the program.")

        try:
            with Listener(on_scroll=self.on_scroll) as self.listener:
                self.listener.join()
        except KeyboardInterrupt:
            print("Ctrl + C has been pressed. Stoping program...")
            sys.exit()

    def on_scroll(self, x, y, dx, dy):
        if dy == 1:
            self.do_click()
            self.mouse.scroll(0, -1)

    def do_click(self):
        if self.right_button:
            self.right_click()
        else:
            self.left_click()

    def right_click(self):
        self.mouse.press(Button.right)
        self.mouse.release(Button.right)

    def left_click(self):
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)