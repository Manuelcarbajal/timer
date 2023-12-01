from tkinter import *
from tkinter import ttk
import time
from playsound import playsound


def validate_input(P):
    if P == "":
        return True
    if P.isdigit():
        value = int(P)
        if 0 <= value <= 23:
            return True
    return False


def validate_minutes_seconds(P):
    if P == "":
        return True
    if P.isdigit():
        value = int(P)
        if 0 <= value <= 59:
            return True
    return False


def reset_timer():
    global time_left, start_time, paused
    time_left = 0
    start_time = 0
    paused = False
    timer_label.config(text='Temporizador reiniciado')


# contorla diseno de interface
root = Tk()
root.title('Timer')
root.geometry('1000x500')  # tamano de ventana
root.config(bg='#000')
root.resizable(False, False)

# creando un titulo
heading = Label(root, text='Timer', font=('Arial', 30, 'bold'),
                bg='#000', fg='#1E90FF')
heading.pack(pady=10)

# Variables de control para los campos de entrada
hours = StringVar()
minutes = StringVar()
seconds = StringVar()

# Definir los rangos para horas, minutos y segundos
hour_values = [str(i) for i in range(24)]  # se define un rango de horas
minute_second_values = [str(i) for i in range(60)]


time_left = 0
start_time = 0
paused = False

# Configurar la validación de entrada
validate = root.register(validate_input)
validate_minutes = root.register(validate_minutes_seconds)


def start_timer():
    global time_left, start_time
    if not paused:
        hours_value = int(hours.get() if hours.get() else 0)
        minutes_value = int(minutes.get() if minutes.get() else 0)
        seconds_value = int(seconds.get() if seconds.get() else 0)
        time_left = hours_value * 3600 + minutes_value * 60 + seconds_value
    start_time = time.time()
    countdown()

# pausa el tiempo


def toggle_pause():
    global paused
    paused = not paused


def get_time_left():
    global time_left, start_time
    elapsed_time = time.time() - start_time
    time_left = max(0, time_left - elapsed_time)
    start_time = time.time()


def countdown():
    global time_left, paused, start_time
    if time_left > 0 and not paused:
        get_time_left()

        hours_value, remainder = divmod(int(time_left), 3600)
        minutes_value, seconds_value = divmod(int(remainder), 60)

        # Obtener la fracción de segundos en milisegundos
        milliseconds = int((time_left - int(time_left)) * 1000)

        timer_label.config(
            text=f'Tiempo restante: {hours_value:02d}:{minutes_value:02d}:{seconds_value:02d}.{milliseconds:03d}')

        if time_left == 0:
            timer_label.config(text='¡Tiempo terminado!')
            # playsound('audio.mp3')

        # Actualizar más frecuentemente (cada 100 ms)
        root.after(100, countdown)


entry_label = Label(root, text='Ingrese el tiempo:', font=('Arial', 16),
                    bg='#000', fg='#1E90FF')
entry_label.pack()

time_frame = Frame(root, bg='#000')
time_frame.pack()

hours_label = Label(time_frame, text='H:', font=('Arial', 30),
                    bg='#000', fg='#1E90FF',)
hours_label.grid(row=0, column=0)

hours_entry = ttk.Entry(
    time_frame, textvariable=hours, validate="key", validatecommand=(validate, '%P'), font=('Arial', 16))
hours_entry.grid(row=0, column=1)

minutes_label = Label(time_frame, text='M:', font=('Arial', 30),
                      bg='#000', fg='#1E90FF')
minutes_label.grid(row=0, column=2)

minutes_entry = ttk.Entry(
    time_frame, textvariable=minutes, validate="key", validatecommand=(validate_minutes, '%P'), font=('Arial', 16))
minutes_entry.grid(row=0, column=3)

seconds_label = Label(time_frame, text='S:', font=('Arial', 30),
                      bg='#000', fg='#1E90FF')
seconds_label.grid(row=0, column=4)

seconds_entry = ttk.Entry(
    time_frame, textvariable=seconds, validate="key", validatecommand=(validate_minutes, '%P'), font=('Arial', 16))
seconds_entry.grid(row=0, column=5)


# startbutton
start_button = Button(root, text='start', font=('Arial', 16),
                      bg='#1E90FF', fg='#000', command=start_timer)
start_button.pack(pady=10)

# puase button
pause_button = Button(root, text='Pause', font=('Arial', 16),
                      bg='#1E90FF', fg='#000', command=toggle_pause)
pause_button.pack(pady=10)


# renciar temprizador button
reset_button = Button(root, text='Reiniciar', font=('Arial', 16),
                      bg='#1E90FF', fg='#000', command=reset_timer)
reset_button.pack(pady=10)

timer_label = Label(root, text='', font=('Arial', 16),
                    bg='#000', fg='#1E90FF')
timer_label.pack()

root.mainloop()
