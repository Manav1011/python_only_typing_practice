# import keyboard

# def on_key_event(event):
#     print(f"Key {event.name} {'pressed' if event.event_type == 'down' else 'released'}")

# keyboard.on_press(on_key_event)
# keyboard.on_release(on_key_event)

# keyboard.wait() # wait for keystrokes
# Define ANSI escape codes for different colors
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_CYAN = '\033[36m'
COLOR_RESET = '\033[0m'

# Print colored text to the terminal
print(COLOR_RED + 'Hello, world!' + COLOR_RESET)
print(COLOR_GREEN + 'Hello, world!' + COLOR_RESET)
print(COLOR_YELLOW + 'Hello, world!' + COLOR_RESET)
print(COLOR_BLUE + 'Hello, world!' + COLOR_RESET)
print(COLOR_MAGENTA + 'Hello, world!' + COLOR_RESET)
print(COLOR_CYAN + 'Hello, world!' + COLOR_RESET)
