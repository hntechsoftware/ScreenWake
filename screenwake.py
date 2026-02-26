import ttkbootstrap as tb
from pywinstyles import change_header_color
from hPyT import maximize_minimize_button
import ctypes
import time
from tktooltip import ToolTip


wakescreen = False

window = tb.Window()
window.title("")
window.iconbitmap("")
window.resizable(False, False)
window.attributes("-topmost", True)

style = tb.Style()
style.configure("red.TButton", background="#d91507", foreground="white")
style.configure("green.TButton", background="#008f00", foreground="white")

def start():
    global wakescreen
    wakescreen = True
    start_timer()
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002) #this will prevent the screen saver or sleep. 

def stop():
    global wakescreen
    wakescreen = False
    reset_timer()
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000) #set the setting back to normal

def update_label():
    global start_time
    elapsed_time = time.time() - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"  

    label.config(text=time_str)
    label.after(1000, update_label)  # Update every second

def start_timer():
    global start_time
    start_time = time.time()
    update_label()

def reset_timer():
    global start_time
    start_time = None
    label.config(text="00:00:00 (Off)")

startbutton = tb.Button(text="  Start   ", style="green.TButton", command=start)
startbutton.grid(row=0, column=0)

stopbutton = tb.Button(text="   Stop    ", style="red.TButton", command=stop)
stopbutton.grid(row=0, column=1)

label = tb.Label(text="00:00:00 (Off)")
label.grid(row=1, column=0, columnspan=2)

name0 = ToolTip(label, msg="Time since ScreenWake started", follow=True, delay=0.1, x_offset=-160, y_offset=-100)
name1 = ToolTip(startbutton, msg="Begin the ScreenWake", follow=True, delay=0.1, x_offset=-160, y_offset=-100)
name2 = ToolTip(stopbutton, msg="Stop the ScreenWake", follow=True, delay=0.1, x_offset=-160, y_offset=-100)

name0.attributes("-topmost", True)
name1.attributes("-topmost", True)
name2.attributes("-topmost", True)

change_header_color(window, color="white")
maximize_minimize_button.hide(window)

window.mainloop()