import time
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x150")
root.title("Easy Timer")
hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("00")
minute.set("00")
second.set("00")
Label(root, text="Hours").place(x=30, y=20)
Label(root, text="Minutes").place(x=120, y=20)
Label(root, text="Seconds").place(x=210, y=20)
hour_entry = Entry(root, width=3, textvariable=hour, font=("Arial", 18))
hour_entry.place(x=30, y=50)
minute_entry = Entry(root, width=3, textvariable=minute, font=("Arial", 18))
minute_entry.place(x=120, y=50)
second_entry = Entry(root, width=3, textvariable=second, font=("Arial", 18))
second_entry.place(x=210, y=50)
def start_countdown():
    try:
        total_seconds = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showerror("Error", "Enter numbers only!")
        return
    while total_seconds >= 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        hour.set(f"{h:02}")
        minute.set(f"{m:02}")
        second.set(f"{s:02}")
        root.update()
        time.sleep(1)
        if total_seconds == 0:
            messagebox.showinfo("Done!", "Time is up!")
        total_seconds -= 1
start_button = Button(root, text="Start", command=start_countdown)
start_button.place(x=120, y=100)
root.mainloop()
