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


listbox = Listbox(root, listvariable=hours_var, height=5, selectmode='extended')

listbox.grid(row=0, column=6)

hour = StringVar()
min = StringVar()
    
def muzyczka(evt):

    while  True:    
        if evt.isSet():
            return()   
        winsound.Beep(500, 200)
        sleep(0.2)



# metoda do alarmu, czyli wyskakujacego okna itp
def Alarm():
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        # global drzemka
        # drzemka=current_time+timedelta(minutes=0.1)
        now = current_time.strftime("%H:%M")
        
        for h in hours:
            
            if h == now:
                x=Event()
                music=Thread(target = muzyczka, args = (x, ))
                
                music.start()
                    
                alarm = messagebox.askyesno('notification', 'Turn off alarm?')
                if alarm == False:
                    x.set()
                    # hours=timedelta(minutes=0.1)
                    messagebox.showinfo('alarm', 'to se spij')
                    
                elif alarm == True:
                    x.set()
                    listbox.delete(hours.index(h),END)
                    hours.remove(h)
                break
            
Checker=Thread(target=Alarm,daemon=True)
Checker.start()
        
# metoda do pobierania godziny alarmu
def actual_time():
    

    set_alarm_timer = f"{hour.get()}:{min.get()}"
    setted_alarm = set_alarm_timer
    listbox.insert(END, setted_alarm)
    hours.append(setted_alarm)
    print(set_alarm_timer)
    sort_list()


def sort_list():
    hours.sort()
    temp_list=hours
    
    print (temp_list)
    listbox.delete(0,END)
    for item in hours:
        listbox.insert(END,item)

def delete_alarm():
    try:
        asd=listbox.curselection()
        for index in listbox.curselection():
            hours.remove(listbox.get(index))
            listbox.delete(asd)
            print(index)
    except IndexError:
        pass



hourTime = Entry(root, textvariable=hour, bg="cornflower blue", width=5)

# hourTime.config
hourTime.grid(row=1, column=1)
minTime = Entry(root, textvariable=min, bg="cornflower blue", width=5)
minTime.grid(row=1, column=2)

# minTime.config
submit = Button(root, text="Set Alarm", fg="red", width=10, command=actual_time)
submit.grid(row=1, column=3)
delete = Button(root, text="Delete Alarm", fg="red", width=10, command=delete_alarm)
delete.grid(row=2, column=3)
root.mainloop()