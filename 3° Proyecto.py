import pygame as pygame

InfoPer = """
_______________________________________________
    Insituto Tecnologico de Costa Rica         
            Computer Engineering 
            
            Formula E CE Tec
    Energy Saving and Telemetry Part II
                       

    Kenneth Fuentes Martinez 2019026305 
    Cristian Calvo Porras 2019205083              
    Curso: Taller de Programacion
    Año: 2019                             
    Prof: Milton Villegas Lemus    
    Pais: Costa Rica
    Python 3.7.2                    
    Version: 1.0.0                        
_________________________________________________
Guia basica:
                      
_________________________________________________
"""
# __________/BIBLIOTECAS
import tkinter as tk  # Se importa tkinter
from tkinter import *  # Tk(), Label, Canvas, Photo
from threading import Thread  # p.start()
import threading  #
import winsound  # Playsound
import os  # ruta = os.path.join('')
import time  # time.sleep(x)
from tkinter import messagebox  # AskYesNo ()
import random  # Biblioteca Random
from tkinter.ttk import Progressbar  # Se utiliza para hacer una progressbar
from tkinter import ttk
from pygame import mixer # Se importa mixer de pygame


# ______________________________________________
# Biblioteca para conectar con el carro
import WiFiClient
from WiFiClient import NodeMCU

# ______________________________________________
#Biblioteca para conectar con el carro
# Control del carrito por NodeMCU
from pygame import mixer

global left, right

# ______________________________________________
# Biblioteca para conectar con el carro
import WiFiClient
from WiFiClient import NodeMCU

# ______________________________________________
# Control del carrito por NodeMCU
Carrito = NodeMCU()
Carrito.start()
mixer.init()

# ______________________________________________
# Global
global left, right, NumGas, NumGas_Re, reverseON, L_rightON, L_leftON, L_backON, GasON, L_DirON, pressTecla, L_frontON, front_press, left_press, right_press, Dir_press
left = False
right = False
reverseON = False
L_rightON = False
L_leftON = False
L_frontON = False
L_DirON = False
GasON = True
L_backON = False
pressTecla = False
front_press = False
reverse_press = False
left_press = False
right_press = False
Dir_press = False
NumGas = 0
NumGas_Re = 0
num_bar = 0


# __________/Función para cargar imagenes
def cargarImg(nombre):
    ruta = os.path.join('img', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen


# __________/Música
def Song1():
    mixer.music.load('song1.wav')
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.1)


# __________/funcion para el boton mute
def pause():
    mixer.music.pause()


def play():
    mixer.music.unpause()


# __________/Ventana Principal
root = tk.Tk()
root.title('Raio Makuin')
root.minsize(1000, 562)
root.resizable(width=NO, height=NO)

# __________/Se crea un lienzo para objetos
Principal_Canvas = Canvas(root, width=1000, height=562, bg='black')
Principal_Canvas.place(x=0, y=0)

# __________/Cargar una imagen
InicioBackup = cargarImg("backup.png")
Principal_Canvas.create_image(0, 0, image=InicioBackup, anchor=NW)

# _________/Se crea la funcion que ejecuta la cancion de fondo
Play = Thread(target=Song1, args=())
Play.start()


def play1():
    pause()
    Play = Thread(target=Song1, args=())
    Play.start()

def quit():
    mixer.music.stop()
    root.destroy()


# _________/Se crea la funcion que ejecuta la cancion de fondo
Play = Thread(target=Song1, args=())
Play.start()

# __________ /Funcion para ventana about
def ventana_about():
    # Esconder la pantalla principal sin destruirla
    root.withdraw()
    # Pantalla About
    about = Toplevel()
    about.title('About')
    about.minsize(1000, 562)
    about.resizable(width=NO, height=NO)
    # __Se crea un canvas
    About_Canvas = Canvas(about, width=1000, height=562, bg='black')
    About_Canvas.place(x=0, y=0)
    # __Se crea un fondo
    Backup_aboutImg = cargarImg('backup_about.png')
    Backup_about = Label(About_Canvas, image=Backup_aboutImg)
    Backup_about.photo = Backup_aboutImg
    Backup_about.place(x=0, y=0)
    # __Se carga una imagen
    PersonalImg = cargarImg('Personalimg.gif')
    Personal = Label(About_Canvas, image=PersonalImg, bg='white')
    Personal.photo = PersonalImg
    Personal.place(x=10, y=60)
    ImgCris = cargarImg('fotoCris.gif')
    Personal1 = Label(About_Canvas, image=ImgCris, bg='white')
    Personal1.photo = ImgCris
    Personal1.place(x=230, y=60)
    # __Se crea un label con informacion crucial
    Label_about = Label(About_Canvas, text=InfoPer, font=('Britannic Bold', 16), fg='white', bg='#040521')
    Label_about.place(x=500, y=10)

    # __Se crea una funcion para volver a la pantalla principal
    def atras_about():
        global pausa
        pausa = True
        about.destroy()
        root.deiconify()

    Btn_Atras = Button(About_Canvas, text='Atras', font=('Britannic Bold', 18), command=atras_about, bg='black',
                       fg='white')
    Btn_Atras.place(x=5, y=512)

    about.mainloop()

# __________ /Funcion para ventana de Pilotos
def ventana_Pilots():
    # Esconder la pantalla principal sin destruirla
    root.withdraw()
    # Pantalla pilots
    Pilots = Toplevel()
    Pilots.title('Pilots')
    Pilots.minsize(900, 700)
    Pilots.resizable(width=NO, height=NO)
    # __Se crea un canvas y un scrollbar
    Pilots_Canvas = Canvas(Pilots, width=900, height=700, bg='white')
    scroll_y = Scrollbar(Pilots,orient = 'vertical', command = Pilots_Canvas.yview)
    Pilots_frame = Frame(Pilots_Canvas)
    listaframes = []
    for i in range(0,10):
        listaframes.append(Frame(Pilots_Canvas))

    Y1 = 40
    Y2 = 145
    Y3 = 250
    Y4 = 355
    Y5 = 460
    Y6 = 565
    Y7 = 670
    Y8 = 775
    Y9 = 880
    Y10 =985
    #Se cargan las banderas
    britanico = cargarImg("britanico.png")#en la lista cargar la imagen
    japones = cargarImg("japones.png")
    italiano = cargarImg("italiano.png")
    frances = cargarImg("frances.png")
    americano = cargarImg("americano.png")
    jonathan = cargarImg("jonathan.png")
    joseph = cargarImg("joseph.png")
    jotaro = cargarImg("jotaro.png")
    josuke = cargarImg("josuke.png")
    giorno = cargarImg("giorno.png")
    dio = cargarImg('dio.png')
    kira = cargarImg('kira.png')
    bruno = cargarImg('bruno.png')
    polnareff = cargarImg('polnareff.png')
    caesar = cargarImg('caesar.png')

    ListaPilotos = []
    listaY = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10]
    listaimg = [jonathan,joseph,jotaro,josuke,giorno,dio,kira,bruno,polnareff,caesar]
    # __Se abre el archivo de texto con la info. de los pilotos
    arch1 = open('Pilotos.txt', 'r+')
    for i in range(0,10):
        ListaPilotos.append(arch1.readline().split('@'))

    #Se calculan los RGP de los pilotos y se agregan a la lista de cada piloto
    for i in range(0,10):
        ListaPilotos[i].append(str(int(((int(ListaPilotos[i][5])+int(ListaPilotos[i][6]))/(int(ListaPilotos[i][4])-int(ListaPilotos[i][7]))*100))))

    for i in range(0,10):
        ListaPilotos[i].append(int(((int(ListaPilotos[i][5]))/(int(ListaPilotos[i][4])-int(ListaPilotos[i][7]))*100)))
    #la lista de cada piloto
    for i in range(0,10):
        ListaPilotos[i].append(listaY[i])

    print(ListaPilotos)

    ListaPilotos[0][2] = britanico
    ListaPilotos[1][2] = americano
    ListaPilotos[2][2] = japones
    ListaPilotos[3][2] = japones
    ListaPilotos[4][2] = italiano
    ListaPilotos[5][2] = britanico
    ListaPilotos[6][2] = japones
    ListaPilotos[7][2] = italiano
    ListaPilotos[8][2] = frances
    ListaPilotos[9][2] = italiano

    #ListaPilotos=(Pil0,Pil1,Pil2,Pil3,Pil4,Pil5,Pil6,Pil7,Pil8,Pil9)
    # RGP = ((V+P)/(T-A))*100
    # REP =(V/(T-A))*100
    # V = VICTORIAS, P = 2 Y 3 LUGAR, T=PARTICIPACIONES, A=ABANDONOS
    # Altura de las imagenes x = 72, y=85
    listatext = []
    listaflags = []
    listanom = []
    listaedad = []
    listatmp = []
    listargp = []
    listarep = []
    listacomp = []

    for i in range(0,10):
        listatext.append(Pilots_Canvas.create_text(5, listaY[i], anchor=NW, text=i+1, font=('Britannic Bold', 16)))

    Nombre = Pilots_Canvas.create_text(182,2,anchor=NW,text ='Nombre/Edad',font=('Britannic Bold', 16))
    Temp = Pilots_Canvas.create_text(380, 2, anchor=NW, text='Temporada', font=('Britannic Bold', 16))
    RGP = Pilots_Canvas.create_text(500, 2, anchor=NW, text='RGP', font=('Britannic Bold', 16))
    REP = Pilots_Canvas.create_text(555,2,anchor=NW,text ='REP',font=('Britannic Bold', 16))
    Comp = Pilots_Canvas.create_text(610,2,anchor=NW,text ='Competencias',font=('Britannic Bold', 16))

    for i in range(0,10):
        listaflags.append(Pilots_Canvas.create_image(108,ListaPilotos[i][10],image=ListaPilotos[i][2],anchor=NW))

    for i in range(0,10):
        listanom.append(Pilots_Canvas.create_text(182,ListaPilotos[i][10],anchor=NW,text =ListaPilotos[i][0],font=('Britannic Bold', 16)))

    for i in range(0,10):
        listaedad.append(Pilots_Canvas.create_text(182,ListaPilotos[i][10]+25,anchor=NW,text =ListaPilotos[i][1],font=('Britannic Bold', 16)))

    for i in range(0,10):
        listatmp.append(Pilots_Canvas.create_text(380,ListaPilotos[i][10],anchor=NW,text =ListaPilotos[i][3],font=('Britannic Bold', 16)))

    for i in range(0,10):
        listargp.append(Pilots_Canvas.create_text(500,ListaPilotos[i][10],anchor=NW,text =ListaPilotos[i][8],font=('Britannic Bold', 16)))

    for i in range(0,10):
        listarep.append(Pilots_Canvas.create_text(555,ListaPilotos[i][10],anchor=NW,text =ListaPilotos[i][9],font=('Britannic Bold', 16)))

    for i in range(0,10):
        listacomp.append(Pilots_Canvas.create_text(610,ListaPilotos[i][10],anchor=NW,text =ListaPilotos[i][4],font=('Britannic Bold', 16)))


    #Pilots_Canvas.delete(nomp)
    #Boton.destroy()

    def borrar():
        for flags in listaflags:
            Pilots_Canvas.delete(flags)
        for nom in listanom:
            Pilots_Canvas.delete(nom)
        for edad in listaedad:
            Pilots_Canvas.delete(edad)
        for tmp in listatmp:
            Pilots_Canvas.delete(tmp)
        for rgp in listargp:
            Pilots_Canvas.delete(rgp)
        for rep in listarep:
            Pilots_Canvas.delete(rep)
        for comp in listacomp:
            Pilots_Canvas.delete(comp)
        for btn in listabtn:
            btn.destroy()
        #Pilots_Canvas.delete(listatext)
    def mayor_RGP():
      borrar()

    def burbuja(Lista):
        return burbuja_aux(Lista, 0, 0, len(Lista), False)

    def burbuja_aux(Lista, i, j, n, Swap):
        if i == n:
            return Lista
        if j == n - i - 1:
            if Swap:
                return burbuja_aux(Lista, i + 1, 0, n, False)
            else:
                return Lista
        if Lista[j][8] > Lista[j + 1][8]:
            Tmp = Lista[j]
            Lista[j] = Lista[j + 1]
            Lista[j + 1] = Tmp
            return burbuja_aux(Lista, i, j + 1, n, True)
        else:
            return burbuja_aux(Lista, i, j + 1, n, Swap)

    # __Se carga una imagen

    # __Se crea un label con informacion crucial

    # __Se crea una funcion para volver a la pantalla principal
    def atras_Pilots():
        global pausa
        pausa = True
        Pilots.destroy()
        root.deiconify()

    Btn_Atras = Button(Pilots_frame, text='Atras', font=('Britannic Bold', 14), command=atras_Pilots, bg='black',
                       fg='white')
    Btn_Atras.pack()

    Btn_OrdenRGPM = Button(Pilots_frame,text='Mayor RGP', font=('Britannic Bold', 14), bg='black',fg='white',command = mayor_RGP)
    Btn_OrdenRGPM.pack()
    Btn_OrdenRGPm = Button(Pilots_frame, text='Menor RGP', font=('Britannic Bold', 14), bg='black', fg='white')
    Btn_OrdenRGPm.pack()
    Btn_OrdenREPM = Button(Pilots_frame, text='Mayor REP', font=('Britannic Bold', 14), bg='black', fg='white')
    Btn_OrdenREPM.pack()
    Btn_OrdenREPm = Button(Pilots_frame, text='Menor REP', font=('Britannic Bold', 14), bg='black', fg='white')
    Btn_OrdenREPm.pack()
    #Botones de los pilotos
    listabtn = []
    for i in range(0,10):
        listabtn.append(Button(listaframes[i],image=listaimg[i]))
        listabtn[i].pack()
    '''Btn_jon = Button(listaframes[0],image=jonathan)
    Btn_jon.pack()
    Btn_jsp = Button(listaframes[1], image=joseph)
    Btn_jsp.pack()
    Btn_jot = Button(listaframes[2], image=jotaro)
    Btn_jot.pack()
    Btn_jsk = Button(listaframes[3], image=josuke)
    Btn_jsk.pack()
    Btn_gio = Button(listaframes[4], image=giorno)
    Btn_gio.pack()
    Btn_dio = Button(listaframes[5], image=dio)
    Btn_dio.pack()
    Btn_kra = Button(listaframes[6], image=kira)
    Btn_kra.pack()
    Btn_brn = Button(listaframes[7], image=bruno)
    Btn_brn.pack()
    Btn_pol = Button(listaframes[8], image=polnareff)
    Btn_pol.pack()
    Btn_czs = Button(listaframes[9], image=caesar)
    Btn_czs.pack()'''

    for i in range(0,10):
        Pilots_Canvas.create_window(30, ListaPilotos[i][10], anchor=NW, window=listaframes[i])

    Pilots_Canvas.create_window(780,30,anchor=NW,window=Pilots_frame)
    Pilots_Canvas.update_idletasks()
    Pilots_Canvas.configure(scrollregion = Pilots_Canvas.bbox('all'),yscrollcommand = scroll_y.set)
    Pilots_Canvas.pack(fill =BOTH, expand = True,side = LEFT)
    scroll_y.pack(fill = Y, side= RIGHT)
    Pilots.mainloop()

    Pilots.mainloop()

# ___________/Funcion de send, para enviar mensajes al Carrito

def send(mensaje):
    if (len(mensaje) > 0 and mensaje[-1] == ";"):
        Carrito.send(mensaje)
    else:
        messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    # __________ /Funcion para ventana de TestDrive


def ventana_TestDrive():
    # Esconder la pantalla principal sin destruirla
    root.withdraw()
    # Pantalla About
    Test = Toplevel()
    Test.title('Test Drive')
    Test.minsize(1000, 720)
    Test.resizable(width=NO, height=NO)
    # __Se crea un canvas
    Test_Canvas = Canvas(Test, width=1000, height=720, bg='black')
    Test_Canvas.place(x=0, y=0)
    # __Se carga una imagen de fondo

    BackupVel = cargarImg('BackupVel.png')
    Test_Canvas.create_image(0, 300, image = BackupVel, anchor = NW)

    BackupTD = cargarImg('BackupTD.png')
    Test_Canvas.create_image(0, 0, image=BackupTD, anchor=NW)

    #__Se crea el control de vel
    velocimetro = cargarImg('velocity.png')
    Test_Canvas.create_image(200, 400, image = velocimetro, anchor = NW)

    # _Luces carrito
    # Luz front
    Luz_Front = cargarImg('luz_blanca.png')
    Test_Canvas.create_image(605, 420, image=Luz_Front, anchor=NW, tags=("L_f", "LF"), state=HIDDEN)
    Test_Canvas.create_image(650, 420, image=Luz_Front, anchor=NW, tags=("L_f2", "LF"), state=HIDDEN)
    # Luz direccion
    Luz_Direccion = cargarImg('luz_amarilla.png')
    Test_Canvas.create_image(490, 510, image=Luz_Direccion, anchor=NW, tags=("L_left", "L_dir"), state=HIDDEN)
    Test_Canvas.create_image(568, 510, image=Luz_Direccion, anchor=NW, tags=("L_right", "L_dir2"), state=HIDDEN)
    # Luz stop
    Luz_Stop = cargarImg('luz_roja.png')
    Test_Canvas.create_image(570, 610, image=Luz_Stop, anchor=NW, tags=("L_s", "LS"), state=NORMAL)
    Test_Canvas.create_image(615, 610, image=Luz_Stop, anchor=NW, tags=("L_s2", "LS"), state=NORMAL)
    # __Se carga una imagen del estado del vehiculo
    CarNone = cargarImg('none.png')
    CarLeft = cargarImg('left.png')
    CarRight = cargarImg('right.png')
    Test_Canvas.create_image(630, 450, image=CarNone, anchor=NW, tags=("none", "car"), state=NORMAL)
    Test_Canvas.create_image(630, 450, image=CarLeft, anchor=NW, tags=("left", "car"), state=HIDDEN)
    Test_Canvas.create_image(630, 450, image=CarRight, anchor=NW, tags=("right", "car"), state=HIDDEN)

    #__Se carga el texto de la velocidad
    Test_Canvas.create_text(300, 560, anchor=NW, text="o", tags = "velocidad", font = ('Britannic Bold', 20), fill = "white")

    # _Boton de reversa
    Reverse_off = cargarImg('reverse-off.png')
    Reverse_on = cargarImg('reverse-on.png')
    Test_Canvas.create_image(570, 450, image=Reverse_off, anchor=NW, tags=("R-off", "reverse"), state=NORMAL)
    Test_Canvas.create_image(570, 450, image=Reverse_on, anchor=NW, tags=("R-on", "reverse"), state=HIDDEN)

    #__Sol
    sol_off = cargarImg('sol_off.png')
    sol_on = cargarImg('sol.png')
    Test_Canvas.create_image(517, 480, image = sol_off, anchor = NW, tags = ('s-off', 'sol'), state = NORMAL)
    Test_Canvas.create_image(517, 480, image=sol_on, anchor=NW, tags=('s-on', 'sol'), state=HIDDEN)

    #__Luna
    luna_off = cargarImg('luna_off.png')
    luna_on = cargarImg('luna.png')
    Test_Canvas.create_image(458, 480, image=luna_off, anchor=NW, tags=('l-off', 'luna'), state=NORMAL)
    Test_Canvas.create_image(458, 480, image=luna_on, anchor=NW, tags=('l-on', 'luna'), state=HIDDEN)

    # __Funcionalidades principales del test drive

    # Control key press
    def Car_Control(event):
        key = event.char
        # Globales
        global left, right, NumGas, NumGas_Re, reverseON, L_rightON, L_leftON, L_backON, GasON, L_DirON, pressTecla, L_frontON, front_press, reverse_press, left_press, right_press
        global Dir_press

        # Control de direccion izquierda
        if (key == "a") and not left:
            left = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("left", state=NORMAL)
            ##send("dir:-1;")
            print ("dir:-1;")

        # Control de direccion derecha
        elif (key == "d") and not right:
            right = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("right", state=NORMAL)
            ##send("dir:1;")
            print("dir:1;")

        # Control de aceleracion

            # Reversa
        elif key == "w" and reverseON:
            if not pressTecla:
                pressTecla = True
                time.sleep(1)
                T_Pwm_Re = Thread(target=reverse_aceleration)
                T_Pwm_Re.start()
            else:
                return


            # Hacia adelante
        elif key == "w":
            if not pressTecla:
                pressTecla = True
                time.sleep(1)
                T_pwm = Thread(target=aceleracion)
                T_pwm.start()
            else:
                return


        # Control boton de stop

        # Reversa
        elif key == "s" and reverseON:
            NumGas_Re = 0
            Test_Canvas.itemconfig("velocidad", text=str(NumGas_Re))
            Test_Canvas.itemconfig("L_s", state=NORMAL)
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            return
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")

        #Hacia adelante
        elif key == "s":
            NumGas = 0
            Test_Canvas.itemconfig("velocidad", state=str(NumGas))
            Test_Canvas.itemconfig("L_s", state=NORMAL)
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            return
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")


        # Control del boton de reversa

        # Activar reversa
        elif key == "r":
            if reverse_press:
                return
            else:
                reverse_press = True
                if reverseON:
                    reverseON = False
                    Test_Canvas.itemconfig("reverse", state=HIDDEN)
                    Test_Canvas.itemconfig("R-off", state=NORMAL)
                else:
                    reverseON = True
                    NumGas = 0
                    NumGas_Re = 0
                    ##send("pwm:0;")
                    print ("pwm:0;")
                    Test_Canvas.itemconfig("velocidad", text="0")
                    Test_Canvas.itemconfig("reverse", state=HIDDEN)
                    Test_Canvas.itemconfig("R-on", state=NORMAL)


        #Control de luces

            # Frontales
        elif key == "f":
            if front_press:
                return
            else:
                front_press = True
                if L_frontON:
                    Test_Canvas.itemconfig("L_f", state=HIDDEN)
                    Test_Canvas.itemconfig("L_f2", state=HIDDEN)
                    L_frontON = False
                    ##send("lf:0;")
                    print("lf:0;")
                else:
                    Test_Canvas.itemconfig("L_f", state=NORMAL)
                    Test_Canvas.itemconfig("L_f2", state=NORMAL)
                    L_frontON = True
                    ##send("lf:1;")
                    print("lf:1;")

            # Izquierda
        elif key == "z":
            if left_press:
                return
            else:
                left_press = True
                if L_leftON:
                    Test_Canvas.itemconfig("L_dir", state=HIDDEN)
                    L_leftON = False
                    T_blinking_stop(100, "ll")
                else:
                    Test_Canvas.itemconfig("L_dir", state=NORMAL)
                    L_leftON = True
                    T_blinking(1, "ll")

            # Derecha
        elif key == "c":
            if right_press:
                return
            else:
                right_press = True
                if L_rightON:
                    Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
                    L_rightON = False
                    T_blinking_stop(100, "lr")
                    print (L_rightON)
                else:
                    Test_Canvas.itemconfig("L_dir2", state=NORMAL)
                    L_rightON = True
                    T_blinking(1, "lr")
                    print(L_rightON)

            # Ambas
        elif key == "x":
            if Dir_press:
                return
            else:
                Dir_press = True
                if L_DirON:
                    Test_Canvas.itemconfig("L_dir", state=HIDDEN)
                    Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
                    L_DirON = False
                    T_blinking_stop(100, "lr")
                    T_blinking_stop(100, "ll")
                else:
                    Test_Canvas.itemconfig("L_dir", state=NORMAL)
                    Test_Canvas.itemconfig("L_dir2", state=NORMAL)
                    L_DirON = True
                    T_blinking(1, "lr")
                    T_blinking(1, "ll")


    def T_blinking_stop(n, command):
        global L_DirON, L_rightON, L_leftON
        if L_DirON or L_leftON or L_rightON:
            T_Blink_stop = Thread(target = direccionalesON, args = [n, command])
            T_Blink_stop.start()

    def T_blinking(n, command):
        global L_DirON, L_rightON, L_leftON
        if L_DirON or L_leftON or L_rightON:
            T_Blink = Thread(target = direccionalesON, args = [n, command])
            T_Blink.start()

    def direccionalesON(n, command):
        global L_DirON, L_rightON, L_leftON
        if L_DirON or L_leftON or L_rightON:
            if n >= 100:
                Test_Canvas.itemconfig("L_dir", state=HIDDEN)
                Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
                L_DirON = False
                L_rightON = False
                L_leftON = False
                return
            else:
                if n % 2 != 0:
                    ##send(command + ":1;")
                    print(command + ":1;")
                    time.sleep(0.5)
                    return direccionalesON(n+1, command)
                else:
                    ##send(command + ":0;")
                    print (command + ":0;")
                    time.sleep(0.5)
                    return direccionalesON(n+1, command)

    def aceleracion():
        global NumGas, NumGas_Re, Reverse_on, pressTecla, GasON
        Test_Canvas.itemconfig("L_s2", state=HIDDEN)
        Test_Canvas.itemconfig("L_s", state=HIDDEN)
        if 500 <= NumGas <= 950 and pressTecla:
            if pressTecla:
                NumGas += 50
                ##send("pwm:"+str(NumGas)+":")
                print("pwm:" + str(NumGas) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(NumGas / 10))
                aceleracion()
            else:
                return

        elif 400 >= NumGas and pressTecla:
            if pressTecla:
                NumGas += 100
                ##send("pwm:"+str(NumGas)+":")
                print ("pwm:"+str(NumGas)+";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(NumGas / 10))
                aceleracion()
            else:
                return

    def reverse_aceleration():
        global NumGas_Re, Reverse_on, GasON, pressTecla
        Test_Canvas.itemconfig("L_s2", state=NORMAL)
        Test_Canvas.itemconfig("L_s", state=NORMAL)
        if -500 >= NumGas_Re >= -950 and pressTecla:
            if pressTecla:
                NumGas_Re -= 50
                ##send("pwm:"+str(NumGas_Re)+":")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(NumGas_Re / 10))
                reverse_aceleration()
            else:
                return

        elif -400 <= NumGas_Re and pressTecla:
            if pressTecla:
                NumGas_Re -= 100
                ##send("pwm:"+str(NumGas_Re)+":")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(NumGas_Re / 10))
                reverse_aceleration()
            else:
                return

    Test.bind("<KeyPress>", Car_Control)

    # Control key release
    def release_Control(event):
        key = event.char
        global right, left, GasON, reverse_press, front_press, left_press, right_press, Dir_press, pressTecla

        # Control de direccion
        if key == "a" or key == "d" and left or right:
            left = False
            right = False
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("none", state=NORMAL)
            ##send("dir:0;")
            print ("dir:0;")

        elif key == "f":
            front_press = False

        elif key == "z":
            left_press = False

        elif key == "c":
            right_press = False

        elif key == "x":
            Dir_press = False



    Test.bind("<KeyRelease>", release_Control)

    # __Se crea un label con informacion crucial

    # __Se crea una funcion para volver a la pantalla principal
    def atras_Test():
        global pausa
        pausa = True
        Test.destroy()
        root.deiconify()

    Btn_Atras = Button(Test_Canvas, text='Atras', font=('Britannic Bold', 14), command=atras_Test, bg='white',
                       fg='black')
    Btn_Atras.place(x=5, y=5)

    Test.mainloop()


# __________/Botones de ventana principal

Btn_mute = Button(Principal_Canvas, text='Mute', font=('Britannic Bold', 12), command=pause, bg='#040521', fg='#8c9fc5')
Btn_mute.place(x=483, y=490)

Btn_QuitImg = cargarImg("Btn_Quit.png")
Btn_Quit = Button(Principal_Canvas, image=Btn_QuitImg, command=root.destroy, bg='#040521')
Btn_Quit.place(x=10, y=480)

Btn_PlayMusic = Button(Principal_Canvas, text='Music', font=('Britannic Bold', 12), command=play1, bg='#040521',
                       fg='#8c9fc5')
Btn_PlayMusic.place(x=480, y=530)
Btn_mute = Button(Principal_Canvas, text='Mute', font=('Britannic Bold', 12), command=pause, bg='#040521', fg='#8c9fc5')
Btn_mute.place(x=483, y=490)

Btn_QuitImg = cargarImg("Btn_Quit.png")
Btn_Quit = Button(Principal_Canvas, image=Btn_QuitImg, command=quit, bg='#040521')
Btn_Quit.place(x=10, y=480)

Btn_PlayMusic = Button(Principal_Canvas, text='Music', font=('Britannic Bold', 12), command=play, bg='#040521',
                       fg='#8c9fc5')
Btn_PlayMusic.place(x=480, y=530)

Btn_Credits = cargarImg("Btn_Credits.png")
Btn_About = Button(Principal_Canvas, image=Btn_Credits, command=ventana_about, bg='#040521')
Btn_About.place(x=850, y=480)

Btn_Pilots = cargarImg("Btn_Pilots.png")
Btn_Puntajes = Button(Principal_Canvas, image=Btn_Pilots, command=ventana_Pilots, bg='#040521')
Btn_Puntajes.place(x=10, y=10)

Btn_Test = cargarImg("Btn_Test.png")
Btn_Test_Driver = Button(Principal_Canvas, image=Btn_Test, command=ventana_TestDrive, bg='#040521')
Btn_Test_Driver.place(x=850, y=10)

root.mainloop()