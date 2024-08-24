from datetime import datetime
import time

current_time = datetime.now() #Obtengo la hora actual.


def calculate_time(hours, minutes):
    global current_time
    total_minutes = hours * 60 + minutes
    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60
    if new_minutes+int(current_time.minute)>60:
        new_hours+=1
    return new_hours % 24, new_minutes #Se calculan las horas que se deben agregar a la hora actual

def add_time(minutes_placed): #Se le agregan los minutos que ingreso el usuario
    hours, minutes = calculate_time(0, minutes_placed) #Se calculan las horas y los minutos
    return hours, minutes #Se retornan las horas y los minutos calculados

def custom_timedelta(hours, minutes):
    # Calcular el tiempo actualizado
    updated_hours = (current_time.hour + hours) % 24
    updated_minutes = (current_time.minute + minutes) % 60
    updated_seconds = current_time.second
    return updated_hours, updated_minutes, updated_seconds

hours, minutes = add_time(52)

while True:
    current_time = datetime.now()
    updated_hours, updated_minutes, updated_seconds = custom_timedelta(hours, minutes)
    if updated_minutes==59 and updated_seconds==59:
        hours+=1
    print(f"{current_time.replace(hour=updated_hours, minute=updated_minutes, second=updated_seconds).strftime('%H:%M:%S')} \r")
    time.sleep(1)

"""
    Se sabe que la hora esta en formato datetime, lo que significa que la hora actual se podria tratar como un string.
    Eso quiere decir que se pueden utilizar funciones propias de los strings como los son el replace, reemplanzando los datos
    a cada segundo para que se vaya actualizando la hora.

    Para poder actualizar a cada segundo  la hora, se debe utilizar un bucle while que se repita y tenga un sleep de 1 segundo,
    aunque, eso funcionaria para una aplicacion en consola, al utilizar librerias como Tkinter podriamos usar funciones como 
    after que se encargan de llamar a una funcion despues de un tiempo determinado
"""
