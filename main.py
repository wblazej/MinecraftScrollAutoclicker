from pynput.mouse import Listener, Button, Controller
from time import sleep
import threading

class AutoClicker:
    def __init__(self):
        self.mouse = Controller()
        self.last = None

    def right_click(self):
        self.mouse.press(Button.right)
        self.mouse.release(Button.right)
        sleep(0.025)
        self.mouse.press(Button.right)
        self.mouse.release(Button.right)

        self.mouse.scroll(0, -1)

    def on_scroll(self, x, y, dx, dy):
        if dy == 1:
            self.right_click()

if __name__ == "__main__":
    auto_clicker = AutoClicker()
    with Listener(on_scroll=auto_clicker.on_scroll) as listener:
        listener.join()