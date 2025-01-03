import pynput
from pynput.keyboard import Key, Listener

def on_press(key):

    print(key)


def on_release(key):
    
    if key == Key.esc:
        return False


#this listener is a loop that will constantly run until it is broken out of
#on_press is a function called when a key is pressed
#on_release is a function called when a key is released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()