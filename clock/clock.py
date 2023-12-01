import time
from tkinter import *
from playsound import playsound

import winsound


sound = ('a.wav')

flags = winsound.SND_FILENAME | winsound.SND_NOWAIT


# configurar estilos de tabla
root = Tk()
root.title('Timer')
root.geometry('400x600')
root.config(bg='#000')
root.resizable(False, False)

heading = Label(root, text='Timer', font='arial 30 bold',
                bg='#000', fg='#1E90FF')
heading.pack(pady=10)

# clock
Label(root, font=('arial', 15, 'bold'), text='current time:',
      bg='papaya whip').place(x=65, y=70)


def clock():
    clock_time = time.strftime('%I:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font=('arial', 15, 'bold'),
                     text='', fg='#000', bg='#fff')
current_time.place(x=190, y=70)
clock()

# limiatr campos de entarda de horas ,minutos y segundos


def validate_hrs(P):
    if P == '' or P == '00':
        return True
    if P.isdigit():
        value = int(P)
        if 0 <= value <= 23:
            return True
    return False


def validate_mins_sec(P):
    if P == '' or P == '00':
        return True
    if P.isdigit():
        value = int(P)
        if 0 <= value <= 59:
            return True
    return False


# timer
hrs = StringVar()
hrs.trace_add('write', lambda *args: validate_hrs(hrs.get()))
Entry(root, textvariable=hrs, width=2, font='arial 50',
      bg='#000', fg='#fff', bd=0).place(x=30, y=155)
hrs.set('00')

mins = StringVar()
mins.trace_add('write', lambda *args: validate_mins_sec(mins.get()))
Entry(root, textvariable=mins, width=2, font='arial 50',
      bg='#000', fg='#fff', bd=0, ).place(x=150, y=155)
mins.set('00')

sec = StringVar()
sec.trace_add('write', lambda *args: validate_mins_sec(sec.get()))
Entry(root, textvariable=sec, width=2, font='arial 50',
      bg='#000', fg='#fff', bd=0, validatecommand=(validate_mins_sec, '%P')).place(x=270, y=155)
sec.set('00')

Label(root, text='hours', font='arial 12',
      bg='#000', fg='#fff').place(x=105, y=200)
Label(root, text='min', font='arial 12',
      bg='#000', fg='#fff').place(x=225, y=200)
Label(root, text='sec', font='arial 12',
      bg='#000', fg='#fff').place(x=345, y=200)


def Timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

    def update_timer():
        nonlocal times
        if times > 0:
            minute, second = divmod(times, 60)
            hour, minute = divmod(minute, 60)
            sec.set(f'{second:02d}')
            mins.set(f'{minute:02d}')
            hrs.set(f'{hour:02d}')
            times -= 1
            root.after(1000, update_timer)
        else:
            print('Fin')
            winsound.PlaySound(sound, flags)
            sec.set('00')
            mins.set('00')
            hrs.set('00')

    update_timer()


def brush():
    hrs.set('00')
    mins.set('02')
    sec.set('00')


def face():
    hrs.set('00')
    mins.set('15')
    sec.set('00')


def eggs():
    hrs.set('00')
    mins.set('10')
    sec.set('00')


button = Button(root, text='Start', bg='#ea3548', bd=0,
                fg='#fff', width=20, height=2, font='arial 10 bold', command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)


Image1 = PhotoImage(file='face.png')
button1 = Button(root, image=Image1, bg='#000', bd=0, command=brush)
button1.place(x=7, y=300)

Image2 = PhotoImage(file='face.png')
button2 = Button(root, image=Image2, bg='#000', bd=0, command=face)
button2.place(x=137, y=300)

Image3 = PhotoImage(file='face.png')
button3 = Button(root, image=Image3, bg='#000', bd=0, command=eggs)
button3.place(x=267, y=300)

root.mainloop()
