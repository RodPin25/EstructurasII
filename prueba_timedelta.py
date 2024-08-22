from datetime import datetime
import time

def calculate_time(hours, minutes):
    return (hours + minutes // 60) % 24, minutes % 60 #Se calculan las horas que se deben agregar a la hora actual

def add_time(minutes_placed): #Se le agregan los minutos que ingreso el usuario
    hours, minutes = calculate_time(0, minutes_placed) #Se calculan las horas y los minutos
    return hours, minutes #Se retornan las horas y los minutos calculados

hours, minutes = add_time(60) #Mando a llamar a la funcion

current_time = datetime.now() #Obtengo la hora actual.

"""
    Se sabe que la hora esta en formato datetime, lo que significa que la hora actual se podria tratar como un string.
    Eso quiere decir que se pueden utilizar funciones propias de los strings como los son el replace, reemplanzando los datos
    a cada segundo para que se vaya actualizando la hora.

    Para poder actualizar a cada segundo  la hora, se debe utilizar un bucle while que se repita y tenga un sleep de 1 segundo,
    aunque, eso funcionaria para una aplicacion en consola, al utilizar librerias como Tkinter podriamos usar funciones como 
    after que se encargan de llamar a una funcion despues de un tiempo determinado
"""
while True:
    current_time = datetime.now()
    print(f"{current_time.replace(hour=(current_time.hour + hours) % 24, minute=(current_time.minute + minutes) % 60, second=current_time.second).strftime("%H:%M:%S")} \r")
    time.sleep(1)  