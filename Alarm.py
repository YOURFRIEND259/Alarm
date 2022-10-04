from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime
import winsound
from threading import Thread, Event
from time import sleep
from datetime import timedelta

root = Tk()
hours = []
hours_var = StringVar(value=hours)
root.title("Alarm")
root.geometry("400x400")
frm = ttk.Frame(root, padding=10)
frm.grid()

current_time = datetime.datetime.now()

listbox = Listbox(root, listvariable=hours_var,
                  height=5, selectmode='extended')

listbox.grid(row=0, column=6)

hour = StringVar()
min = StringVar()


def muzyczka(evt):

    while True:
        if evt.isSet():
            return ()
        winsound.Beep(500, 200)
        sleep(0.2)


# metoda do alarmu, czyli wyskakujacego okna itp
def Alarm():
    while True:
        time.sleep(1)
        # current_time = datetime.datetime.now()
        # global drzemka
        # drzemka=current_time+timedelta(minutes=0.1)
        now = current_time.strftime("%H:%M")

        for h in hours:

            if h == now:
                x = Event()
                music = Thread(target=muzyczka, args=(x, ))
                music.start()

                alarm = messagebox.askyesno('notification', 'Turn off alarm?')
                if alarm == False:
                    x.set()
                    # hours=timedelta(minutes=0.1)
                    messagebox.showinfo('alarm', 'to se spij')

                elif alarm == True:
                    x.set()
                    listbox.delete(hours.index(h), END)
                    hours.remove(h)
                break


Checker = Thread(target=Alarm, daemon=True)
Checker.start()

# metoda do pobierania godziny alarmu


def actual_time():
    minute=int(min.get())
    h=int(hour.get())
    if minute<10 and h<10:
        if "0" in hour.get() and not "0"  in min.get():
            setted_alarm = f"{hour.get()}:0{min.get()}"
        if "0"  in min.get() and not "0"  in hour.get():
            setted_alarm = f"0{hour.get()}:{min.get()}"
        elif "0"  in min.get() and "0" in hour.get():
            setted_alarm = f"{hour.get()}:{min.get()}"
        else:
            setted_alarm = f"0{hour.get()}:0{min.get()}"

    elif minute<10 and h>=10 and "0" not in min.get():
        setted_alarm = f"{hour.get()}:0{min.get()}"
    elif minute>=10 and h<10 and "0"  not in hour.get():
        setted_alarm = f"0{hour.get()}:{min.get()}"    
    else:
        setted_alarm = f"{hour.get()}:{min.get()}"
    listbox.insert(END, setted_alarm)
    hours.append(setted_alarm)
    print(setted_alarm)
    sort_list()
    hour.set(current_time.strftime("%H"))
    min.set(current_time.strftime("%M"))


def sort_list():
    hours.sort()
    temp_list = hours
    print(temp_list)
    listbox.delete(0, END)

    for item in hours:
        listbox.insert(END, item)


def delete_alarm():
    try:
        asd = listbox.curselection()

        for index in listbox.curselection():
            hours.remove(listbox.get(index))
            listbox.delete(asd)
            print(index)

    except IndexError:
        pass


# hourTime.config
hourTime = Entry(root, textvariable=hour, bg="cornflower blue", width=5)
hourTime.grid(row=1, column=1)
hour.set(current_time.strftime("%H"))
minTime = Entry(root, textvariable=min, bg="cornflower blue", width=5)
minTime.grid(row=1, column=2)
min.set(current_time.strftime("%M"))

# minTime.config
submit = Button(root, text="Set Alarm", fg="red",
                width=10, command=actual_time)
submit.grid(row=1, column=3)
delete = Button(root, text="Delete Alarm", fg="red",
                width=10, command=delete_alarm)
delete.grid(row=2, column=3)
root.mainloop()
