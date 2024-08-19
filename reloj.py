import tkinter as tk
from tkinter import ttk
import time
import datetime
from datetime import datetime,timedelta

#Variables de los colores de la aplicacion
bg_color="#3a3c51"

#Variable que lleva el control de que funcion esta activa
clock_running=True

current_time=time.strftime("%H:%M:%S") #obtengo la hora actual en formato de Hora:Minuto:Segundo
current_sec=time.strftime("%S") #Obtengo los segundos actuales
current_min=time.strftime("%M") #Obtengo los minutos actuales
current_hour=time.strftime("%H") #Obtengo la hora actual

#Funcion que actualizara el reloj
def update_clock():
    global current_time, current_hour, current_min, current_sec

    if not clock_running:
        return
    
    #current_time=time.strftime("%H:%M:%S") #obtengo la hora actual en formato de Hora:Minuto:Segundo
    #current_sec=time.strftime("%S") #Obtengo los segundos actuales
    #current_min=time.strftime("%M") #Obtengo los minutos actuales
    #current_hour=time.strftime("%H") #Obtengo la hora actual

    current_time = datetime.strptime(current_time, "%H:%M:%S") # CONVERTIR A OBJETO DATETIME
    current_time = current_time + timedelta(seconds=1) # SUMAR 1 SEGUNDO PARA QUE AVANCE EL RELOJ
    
    current_sec = int(datetime.strftime(current_time, "%S"))
    current_min = int(datetime.strftime(current_time, "%M"))
    current_hour = int(datetime.strftime(current_time, "%H"))
    
    current_time = datetime.strftime(current_time, "%H:%M:%S") # CONVERTIR DE OBJETO DATETIME A TEXTO

    if int(current_sec)!=0: #Si los segundos actuales no son cero
        current_sec_binary=convert_binary(int(current_sec)) #Entonces convierto esos segundos a binarios y hexadecimales
        current_sec_hexadecimal=hexa_conversion(int(current_sec))
    else: #Si son cero en ambos sistemas de numeracion seran cero, por lo cual muestro una cadena con dos ceros
        current_sec_binary="00"
        current_sec_hexadecimal="00"

    if int(current_min)!=0: #Aplico la misma logica que en los segundos a los minutos
        current_min_binary=convert_binary(int(current_min))
        current_min_hexadecimal=hexa_conversion(int(current_min))
    else:
        current_min_binary="00"
        current_min_hexadecimal="00"

    if int(current_hour)!=0: #Por ultimo aplico la misma logica de conversion a 
        current_hour_binary=convert_binary(int(current_hour))
        current_hour_hexadecimal=hexa_conversion(int(current_hour))
    else:
        current_hour_binary="00"
        current_hour_hexadecimal="00"

    current_binary_hour=f"{current_hour_binary}:{current_min_binary}:{current_sec_binary}" #Ahora uno todos los valores convertidos a una cadena para ser mostrada en un Label
    current_hexadecimal_hour=f"{current_hour_hexadecimal}:{current_min_hexadecimal}:{current_sec_hexadecimal}" #Aplico la misma logica que en el sistema binario

#Intercambio los textos de los label por el texto de cada variable
    label.configure(text=current_time) #Hora en decimal
    label2.configure(text=current_binary_hour) #Hora en binario 
    label3.configure(text=current_hexadecimal_hour) #Hora en hexadecimal
    root.after(1000, update_clock) 
    """
        la funcion root.after() sirve para que la funcion sea recursiva y se mande a 
        llamar pasado un periodo de tiempo, en este caso 1 segundo
    """

config=1
def change_config():
    global config
    config+=1
    if config==1:
        label.place(relx=0.5, rely=0.5, anchor='center')
        label.configure(background=bg_color,foreground="white",font=("Montserrat ExtraBold Italic",120))
        label2.place(relx=0.5, rely=0.7, anchor='center')
        label2.configure(background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
        label3.place(relx=0.5, rely=0.31, anchor="center")
        label3.configure(background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
    elif config==2:
        label.place(relx=0.5, rely=0.7, anchor='center')
        label.configure(background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
        label2.place(relx=0.5, rely=0.31, anchor='center')
        label2.configure(background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
        label3.place(relx=0.5, rely=0.5, anchor="center", )
        label3.configure(background=bg_color,foreground="white",font=("Montserrat ExtraBold Italic",120))
    elif config==3:
        label.place(relx=0.5, rely=0.31, anchor='center')
        label.configure(background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
        label2.place(relx=0.5, rely=0.5, anchor='center')
        label2.configure(background=bg_color,foreground="white",font=("Montserrat ExtraBold Italic",110))
        label3.place(relx=0.5, rely=0.7, anchor="center")
        label3.configure(background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
        config=0

#Funcion que encuentra la nueva hora
def new_hour():
    global clock_running, current_time, current_sec, current_min, current_hour
    
    clock_running = False  # Detiene la función update_clock

    new_time = None  
    current_time = datetime.strptime(current_time, '%H:%M:%S')
    
    minutes_placed = textBox1.get("1.0", "end-1c")  # Obtengo los minutos que ingresó el usuario
    textBox1.delete("1.0","end-1c") # LIMPIAR EL TEXTBOX1 PARA QUE QUEDE VACIO
    
    try:  # Si es posible hacer la conversión de los números ingresados de string a int, realiza el siguiente código
        minutes_placed = int(minutes_placed)
        new_time = current_time + timedelta(minutes=minutes_placed)  # Sumo los minutos
        #if new_time is None:
            #new_time = current_time + timedelta(minutes=minutes_placed)  # Sumo los minutos
        #else:
            #new_time = new_time + timedelta(minutes=minutes_placed)
        
        #new_time = new_time + timedelta(seconds=1)
        
        # La nueva hora convertida a binario
        seconds_binary = convert_binary(new_time.second)
        minutes_binary = convert_binary(new_time.minute)
        hours_binary = convert_binary(new_time.hour)

        # La nueva hora convertida a hexadecimal
        seconds_hexadecimal = hexa_conversion(new_time.second)
        minutes_hexadecimal = hexa_conversion(new_time.minute)
        hours_hexadecimal = hexa_conversion(new_time.hour)

        current_time = datetime.strftime(new_time, '%H:%M:%S') # SE REASIGNA LA NUEVA HORA

        # Agrupo en un string las horas convertidas
        new_binary_hour = f"{hours_binary}:{minutes_binary}:{seconds_binary}"
        new_hexadecimal_hour = f"{hours_hexadecimal}:{minutes_hexadecimal}:{seconds_hexadecimal}"

        label.configure(text=current_time)
        label2.configure(text=new_binary_hour)
        label3.configure(text=new_hexadecimal_hour)

        clock_running = True
        minutes_placed=0
        #root.after(1000, update_clock)  # A cada segundo la función se vuelve recursiva
        
    except ValueError:  # En caso de que no se pueda realizar algo del código anterior, realiza esto
        #print("No se pudo realizar la conversión")
        #return
        current_time = datetime.strftime(current_time, '%H:%M:%S') # SE CONVIERTE A TEXTO NUEVAMENTE
        clock_running = True

#Funcion que convertira los nuemeros de decimales a binarios por medio de la division sucesiva por dos
def convert_binary(num):
    binary="" #Inicializo una variable vacia que contendra el numero binario encontrado
    while True: #Un ciclo infinito que se ejecute mientras se pueda ir dividiendo el numero
        if num!=0: #Si el numero no es cero, quiere decir que aun es divisible
            residuo=num%2 #Encuentro el residuo de la division
            binary+=str(residuo) #Convierto el residuo a string y lo almaceno en la variable binary
            num//=2 #Realizo la respectiva division del numero
        else: 
            break #Si el numero llega a ser 0 quiere decir que ya no se puede seguir diviendo, por lo tanto rompe el ciclo

    return binary[::-1] #Retorno la cadena de residuos que ya encontramos pero del reves, para que se pueda representar como binario

#Funcion que convierte de numero decimal a numero hexadecimal
def hexa_conversion(num):
    """
        Como sabemos los numeros en el sistema decimal van desde el 0 al 9,
        en el sistema hexadecimal van desde el 0 hasta el 9 y de la letra A a la F.
        Para ello necesitaremos un diccionario para poder convertir los numeros decimales
        mayores o iguales a 10 y menores a 16 que nos topemos a la hora de realizar 
        divisiones sucesivas por 16 
    """
    hexa_dictionary={
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }

    hexadecimal="" #Inicializo una variable String vacia que contendra el valor que retornora al final cuando encuentr el hexadecimal
    
    while True: #Ciclo infinito que se ejecutara mientras que el numero sea divisible
        if num!=0:
            res=num%16 #Encuentro el residuo de la division
            if res>=10: #Si el residuo es mayor o igual a 10 necesito convertirlo a un valor alpha numerico
                hexadecimal+=hexa_dictionary[res] #Encuentro el valor que le toca dentro del diccionario
            else:
                hexadecimal+=str(res) #Si no es mayor o igual a 10 simplemente convierto a String el residuo y lo almaceno
            num//=16 #Realizo la division entre 16 para la siguiente vuelta
        else: 
            break #El ciclo se rompe si ya no se puede seguir dividiendo, es decir si el numero ya llego a ser 0

    return hexadecimal[::-1] #Retorno la cadena de texto que ya encontramos del reves para poder representar el numero en el sistema

#Inicializo la ventana
root=tk.Tk()
root.title("Reloj Binario-Hexadecimal")
root.state("zoomed")
root.config(bg=bg_color)

#Inicializo los temas
style=ttk.Style()
style.theme_use("clam")

#Inicializo el label
label=ttk.Label(root,text="",style="TLabel")
label.place(relx=0.5, rely=0.5, anchor='center')
style.configure("TLabel",background=bg_color,foreground="white",font=("Montserrat ExtraBold Italic",120))

#Label que me va  a servir para probar los demas tiempos
label2=ttk.Label(root,text="",background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
label2.place(relx=0.5, rely=0.7, anchor='center')

#Inicializo y configuro el label que me servira para mostrar los hexadecimales
label3=ttk.Label(root,text="", background=bg_color,foreground="white",font=("Montserrat Light Italic", 40))
label3.place(relx=0.5, rely=0.35, anchor="center")

#Label que servira para guiar al usuario
label4=ttk.Label(root,text="Inserte aca el tiempo en minutos que desea agregar o disminuir (+/-)", background=bg_color,foreground="white",font=("Fira Code",15))
label4.place(relx=0.55, rely=0.85,anchor="e")

#Inicializo y cofiguro el textbox que recibira el tiempo agregado 
textBox1=tk.Text(root, height=1,width=50,padx=10,pady=10,background="#3a3c51",border=2,foreground='white',font=("Fira Code",20))
textBox1.place(relx=0.3, rely=0.9, anchor="center")
textBox1.bind("<Return>",lambda event:new_hour())

#Inicializo el boton que cambiara los labels
label_button=ttk.Button(root,text="Cambiar el reloj",command=change_config)
label_button.place(relx=0.7,rely=0.9,anchor="center")

#Mando a llamar a la funcion que actualiza el tiempo
update_clock()

#El mainloop de la ventana para que se mantenaga abierta
root.mainloop() 

