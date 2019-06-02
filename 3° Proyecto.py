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
pressS = False
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
    Frame1 = Frame(Pilots_Canvas)

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
    britanico = cargarImg("britanico.png")
    japones = cargarImg("japones.png")
    italiano = cargarImg("italiano.png")
    frances = cargarImg("frances.png")
    americano = cargarImg("americano.png")

    # __Se abre el archivo de texto con la info. de los pilotos
    arch1 = open('Pilotos.txt', 'r+')
    Pil0 = arch1.readline().split('@')
    Pil1 = arch1.readline().split('@')
    Pil2 = arch1.readline().split('@')
    Pil3 = arch1.readline().split('@')
    Pil4 = arch1.readline().split('@')
    Pil5 = arch1.readline().split('@')
    Pil6 = arch1.readline().split('@')
    Pil7 = arch1.readline().split('@')
    Pil8 = arch1.readline().split('@')
    Pil9 = arch1.readline().split('@')
    print(Y)

    #Se calculan los RGP de los pilotos y se agregan a la lista de cada piloto
    RGPjon = str(int(((int(Pil0[5])+int(Pil0[6]))/(int(Pil0[4])-int(Pil0[7]))*100)))
    Pil0.append(RGPjon)
    RGPjsp = str(int(((int(Pil1[5])+int(Pil1[6]))/(int(Pil1[4])-int(Pil1[7]))*100)))
    Pil1.append(RGPjsp)
    RGPjot = str(int(((int(Pil2[5])+int(Pil2[6]))/(int(Pil2[4])-int(Pil2[7]))*100)))
    Pil2.append(RGPjot)
    RGPjsk = str(int(((int(Pil3[5])+int(Pil3[6]))/(int(Pil3[4])-int(Pil3[7]))*100)))
    Pil3.append(RGPjsk)
    RGPgio = str(int(((int(Pil4[5])+int(Pil4[6]))/(int(Pil4[4])-int(Pil4[7]))*100)))
    Pil4.append(RGPgio)
    RGPdio = str(int(((int(Pil5[5])+int(Pil5[6]))/(int(Pil5[4])-int(Pil5[7]))*100)))
    Pil5.append(RGPdio)
    RGPkra = str(int(((int(Pil6[5])+int(Pil6[6]))/(int(Pil6[4])-int(Pil6[7]))*100)))
    Pil6.append(RGPkra)
    RGPbrn = str(int(((int(Pil7[5])+int(Pil7[6]))/(int(Pil7[4])-int(Pil7[7]))*100)))
    Pil7.append(RGPbrn)
    RGPpol = str(int(((int(Pil8[5])+int(Pil8[6]))/(int(Pil8[4])-int(Pil8[7]))*100)))
    Pil8.append(RGPpol)
    RGPcsz = str(int(((int(Pil9[5])+int(Pil9[6]))/(int(Pil9[4])-int(Pil9[7]))*100)))
    Pil9.append(RGPcsz)

    #Se calculan los REP de los pilotos
    REPjon = (int(((int(Pil0[5]))/(int(Pil0[4])-int(Pil0[7]))*100)))
    Pil0.append(REPjon)
    REPjsp = (int(((int(Pil1[5]))/(int(Pil1[4])-int(Pil1[7]))*100)))
    Pil1.append(REPjsp)
    REPjot = (int(((int(Pil2[5]))/(int(Pil2[4])-int(Pil2[7]))*100)))
    Pil2.append(REPjot)
    REPjsk = (int(((int(Pil3[5]))/(int(Pil3[4])-int(Pil3[7]))*100)))
    Pil3.append(REPjsk)
    REPgio = (int(((int(Pil4[5]))/(int(Pil4[4])-int(Pil4[7]))*100)))
    Pil4.append(REPgio)
    REPdio = (int(((int(Pil5[5]))/(int(Pil5[4])-int(Pil5[7]))*100)))
    Pil5.append(REPdio)
    REPkra = (int(((int(Pil6[5]))/(int(Pil6[4])-int(Pil6[7]))*100)))
    Pil6.append(REPkra)
    REPbrn = (int(((int(Pil7[5]))/(int(Pil7[4])-int(Pil7[7]))*100)))
    Pil7.append(REPbrn)
    REPpol = (int(((int(Pil8[5]))/(int(Pil8[4])-int(Pil8[7]))*100)))
    Pil8.append(REPpol)
    REPcsz = (int(((int(Pil9[5]))/(int(Pil9[4])-int(Pil9[7]))*100)))
    Pil9.append(REPcsz)
    #Luego se asignan las alturas a la lista de cada piloto
    Pil0.append(Y1)
    Pil1.append(Y2)
    Pil2.append(Y3)
    Pil3.append(Y4)
    Pil4.append(Y5)
    Pil5.append(Y6)
    Pil6.append(Y7)
    Pil7.append(Y8)
    Pil8.append(Y9)
    Pil9.append(Y10)
    print(Pil0)
    print(Pil0[7])
    # RGP = ((V+P)/(T-A))*100
    # REP =(V/(T-A))*100
    # V = VICTORIAS, P = 2 Y 3 LUGAR, T=PARTICIPACIONES, A=ABANDONOS
    # Altura de las imagenes x = 72, y=85
    Num1 = Pilots_Canvas.create_text(5,Y1,anchor=NW,text ='1',font=('Britannic Bold', 16))
    Num2 = Pilots_Canvas.create_text(5,Y2,anchor=NW,text ='2',font=('Britannic Bold', 16))
    Num3 = Pilots_Canvas.create_text(5,Y3,anchor=NW,text ='3',font=('Britannic Bold', 16))
    Num4 = Pilots_Canvas.create_text(5,Y4,anchor=NW,text ='4',font=('Britannic Bold', 16))
    Num5 = Pilots_Canvas.create_text(5,Y5,anchor=NW,text ='5',font=('Britannic Bold', 16))
    Num6 = Pilots_Canvas.create_text(5,Y6, anchor=NW, text='6', font=('Britannic Bold', 16))
    Num7 = Pilots_Canvas.create_text(5,Y7, anchor=NW, text='7', font=('Britannic Bold', 16))
    Num8 = Pilots_Canvas.create_text(5,Y8, anchor=NW, text='8', font=('Britannic Bold', 16))
    Num9 = Pilots_Canvas.create_text(5,Y9, anchor=NW, text='9', font=('Britannic Bold', 16))
    Num10 = Pilots_Canvas.create_text(5,Y10, anchor=NW, text='10', font=('Britannic Bold', 16))
    Nombre = Pilots_Canvas.create_text(182,2,anchor=NW,text ='Nombre/Edad',font=('Britannic Bold', 16))
    Temp = Pilots_Canvas.create_text(380, 2, anchor=NW, text='Temporada', font=('Britannic Bold', 16))
    RGP = Pilots_Canvas.create_text(500, 2, anchor=NW, text='RGP', font=('Britannic Bold', 16))
    REP = Pilots_Canvas.create_text(555,2,anchor=NW,text ='REP',font=('Britannic Bold', 16))
    Comp = Pilots_Canvas.create_text(610,2,anchor=NW,text ='Competencias',font=('Britannic Bold', 16))

    # __Se coloca la informacion de los pilotos en la pantalla
    jonathan = cargarImg("jonathan.png")
    pil1img = Pilots_Canvas.create_image(30, Pil0[10], image=jonathan, anchor=NW)
    flag1 = Pilots_Canvas.create_image(108,Pil0[10],image=britanico,anchor=NW)
    nompil1 = Pilots_Canvas.create_text(182,Pil0[10],anchor=NW,text =Pil0[0],font=('Britannic Bold', 16))
    edadpil1 = Pilots_Canvas.create_text(182,Pil0[10]+25,anchor=NW,text =Pil0[1],font=('Britannic Bold', 16))
    tmppil1 = Pilots_Canvas.create_text(380,Pil0[10],anchor=NW,text =Pil0[3],font=('Britannic Bold', 16))
    rgppil1 = Pilots_Canvas.create_text(500,Pil0[10],anchor=NW,text =RGPjon,font=('Britannic Bold', 16))
    reppil1 = Pilots_Canvas.create_text(555,Pil0[10],anchor=NW,text =REPjon,font=('Britannic Bold', 16))
    comp1 = Pilots_Canvas.create_text(610,Pil0[10],anchor=NW,text =Pil0[4],font=('Britannic Bold', 16))

    joseph = cargarImg("joseph.png")
    pil2img = Pilots_Canvas.create_image(30, Pil1[10], image=joseph, anchor=NW)
    flag2 = Pilots_Canvas.create_image(108, Pil1[10], image=americano, anchor=NW)
    nompil2 = Pilots_Canvas.create_text(182,Pil1[10],anchor=NW,text =Pil1[0],font=('Britannic Bold', 16))
    edadpil2 = Pilots_Canvas.create_text(182,Pil1[10]+25,anchor=NW,text =Pil1[1],font=('Britannic Bold', 16))
    tmppil2 = Pilots_Canvas.create_text(380,Pil1[10],anchor=NW,text =Pil1[3],font=('Britannic Bold', 16))
    rgppil2 = Pilots_Canvas.create_text(500,Pil1[10],anchor=NW,text =RGPjsp,font=('Britannic Bold', 16))
    reppil2 = Pilots_Canvas.create_text(555,Pil1[10],anchor=NW,text =REPjsp,font=('Britannic Bold', 16))
    comp2 = Pilots_Canvas.create_text(610,Pil1[10],anchor=NW,text =Pil1[4],font=('Britannic Bold', 16))

    jotaro = cargarImg("jotaro.png")
    pil3img = Pilots_Canvas.create_image(30,Pil2[10], image=jotaro, anchor=NW)
    flag3 = Pilots_Canvas.create_image(108,Pil2[10], image=japones, anchor=NW)
    nompil3 = Pilots_Canvas.create_text(182,Pil2[10], anchor=NW, text=Pil2[0], font=('Britannic Bold', 16))
    edadpil3 = Pilots_Canvas.create_text(182, Pil2[10] + 25, anchor=NW, text=Pil2[1], font=('Britannic Bold', 16))
    tmppil3 = Pilots_Canvas.create_text(380,Pil2[10], anchor=NW, text=Pil2[3], font=('Britannic Bold', 16))
    rgppil3 = Pilots_Canvas.create_text(500,Pil2[10], anchor=NW, text=RGPjot, font=('Britannic Bold', 16))
    reppil3 = Pilots_Canvas.create_text(555,Pil2[10], anchor=NW, text=REPjot, font=('Britannic Bold', 16))
    comp2 = Pilots_Canvas.create_text(610,Pil2[10], anchor=NW, text=Pil2[4], font=('Britannic Bold', 16))


    josuke = cargarImg("josuke.png")
    pil4img = Pilots_Canvas.create_image(30, Pil3[10], image=josuke, anchor=NW)
    flag4 = Pilots_Canvas.create_image(108, Pil3[10], image=japones, anchor=NW)
    nompil4 = Pilots_Canvas.create_text(182, Pil3[10], anchor=NW, text=Pil3[0], font=('Britannic Bold', 16))
    edadpil4 = Pilots_Canvas.create_text(182, Pil3[10] + 25, anchor=NW, text=Pil3[1], font=('Britannic Bold', 16))
    tmppil4 = Pilots_Canvas.create_text(380, Pil3[10], anchor=NW, text=Pil3[3], font=('Britannic Bold', 16))
    rgppil4 = Pilots_Canvas.create_text(500, Pil3[10], anchor=NW, text=RGPjsk, font=('Britannic Bold', 16))
    reppil4 = Pilots_Canvas.create_text(555, Pil3[10], anchor=NW, text=REPjsk, font=('Britannic Bold', 16))
    comp4 = Pilots_Canvas.create_text(610, Pil3[10], anchor=NW, text=Pil3[4], font=('Britannic Bold', 16))
    #nompil4.destroy()

    giorno = cargarImg("giorno.png")
    pil5img = Pilots_Canvas.create_image(30, Pil4[10], image=giorno, anchor=NW)
    flag5 = Pilots_Canvas.create_image(108, Pil4[10], image=italiano, anchor=NW)
    nompil5 = Pilots_Canvas.create_text(182, Pil4[10], anchor=NW, text=Pil4[0], font=('Britannic Bold', 16))
    edadpil5 = Pilots_Canvas.create_text(182, Pil4[10] + 25, anchor=NW, text=Pil4[1], font=('Britannic Bold', 16))
    tmppil5 = Pilots_Canvas.create_text(380, Pil4[10], anchor=NW, text=Pil4[3], font=('Britannic Bold', 16))
    rgppil5 = Pilots_Canvas.create_text(500, Pil4[10], anchor=NW, text=RGPgio, font=('Britannic Bold', 16))
    reppil5 = Pilots_Canvas.create_text(555, Pil4[10], anchor=NW, text=REPgio, font=('Britannic Bold', 16))
    comp5 = Pilots_Canvas.create_text(610, Pil4[10], anchor=NW, text=Pil4[4], font=('Britannic Bold', 16))

    dio = cargarImg('dio.png')
    pil6img = Pilots_Canvas.create_image(30, Pil5[10], image=dio, anchor=NW)
    flag6 = Pilots_Canvas.create_image(108, Pil5[10], image=britanico, anchor=NW)
    nompil6 = Pilots_Canvas.create_text(182, Pil5[10], anchor=NW, text=Pil5[0], font=('Britannic Bold', 16))
    edadpil6 = Pilots_Canvas.create_text(182, Pil5[10] + 25, anchor=NW, text=Pil5[1], font=('Britannic Bold', 16))
    tmppil6 = Pilots_Canvas.create_text(380, Pil5[10], anchor=NW, text=Pil5[3], font=('Britannic Bold', 16))
    rgppil6 = Pilots_Canvas.create_text(500, Pil5[10], anchor=NW, text=RGPdio, font=('Britannic Bold', 16))
    reppil6 = Pilots_Canvas.create_text(555, Pil5[10], anchor=NW, text=REPdio, font=('Britannic Bold', 16))
    comp6 = Pilots_Canvas.create_text(610, Pil5[10], anchor=NW, text=Pil5[4], font=('Britannic Bold', 16))

    kira = cargarImg('kira.png')
    pil7img = Pilots_Canvas.create_image(30, Pil6[10], image=kira, anchor=NW)
    flag7 = Pilots_Canvas.create_image(108, Pil6[10], image=japones, anchor=NW)
    nompil7 = Pilots_Canvas.create_text(182, Pil6[10], anchor=NW, text=Pil6[0], font=('Britannic Bold', 16))
    edadpil7 = Pilots_Canvas.create_text(182, Pil6[10]+ 25, anchor=NW, text=Pil6[1], font=('Britannic Bold', 16))
    tmppil7 = Pilots_Canvas.create_text(380, Pil6[10], anchor=NW, text=Pil6[3], font=('Britannic Bold', 16))
    rgppil7 = Pilots_Canvas.create_text(500, Pil6[10], anchor=NW, text=RGPkra, font=('Britannic Bold', 16))
    reppil7 = Pilots_Canvas.create_text(555, Pil6[10], anchor=NW, text=REPkra, font=('Britannic Bold', 16))
    comp7 = Pilots_Canvas.create_text(610, Pil6[10], anchor=NW, text=Pil6[4], font=('Britannic Bold', 16))

    bruno = cargarImg('bruno.png')
    pil8img = Pilots_Canvas.create_image(30, Pil7[10], image=bruno, anchor=NW)
    flag8 = Pilots_Canvas.create_image(108, Pil7[10], image=italiano, anchor=NW)
    nompil8 = Pilots_Canvas.create_text(182, Pil7[10], anchor=NW, text=Pil7[0], font=('Britannic Bold', 16))
    edadpil8 = Pilots_Canvas.create_text(182, Pil7[10] + 25, anchor=NW, text=Pil7[1], font=('Britannic Bold', 16))
    tmppil8 = Pilots_Canvas.create_text(380, Pil7[10], anchor=NW, text=Pil7[3], font=('Britannic Bold', 16))
    rgppil8 = Pilots_Canvas.create_text(500, Pil7[10], anchor=NW, text=RGPbrn, font=('Britannic Bold', 16))
    reppil8 = Pilots_Canvas.create_text(555, Pil7[10], anchor=NW, text=REPbrn, font=('Britannic Bold', 16))
    comp8 = Pilots_Canvas.create_text(610, Pil7[10], anchor=NW, text=Pil7[4], font=('Britannic Bold', 16))

    polnareff = cargarImg('polnareff.png')
    pil9img = Pilots_Canvas.create_image(30, Pil8[10], image=polnareff, anchor=NW)
    flag9 = Pilots_Canvas.create_image(108, Pil8[10], image=frances, anchor=NW)
    nompil9 = Pilots_Canvas.create_text(182, Pil8[10], anchor=NW, text=Pil8[0], font=('Britannic Bold', 16))
    edadpil9 = Pilots_Canvas.create_text(182, Pil8[10] + 25, anchor=NW, text=Pil8[1], font=('Britannic Bold', 16))
    tmppil9 = Pilots_Canvas.create_text(380, Pil8[10], anchor=NW, text=Pil8[3], font=('Britannic Bold', 16))
    rgppil9 = Pilots_Canvas.create_text(500, Pil8[10], anchor=NW, text=RGPpol, font=('Britannic Bold', 16))
    reppil9 = Pilots_Canvas.create_text(555, Pil8[10], anchor=NW, text=REPpol, font=('Britannic Bold', 16))
    comp9 = Pilots_Canvas.create_text(610, Pil8[10], anchor=NW, text=Pil8[4], font=('Britannic Bold', 16))

    caesar = cargarImg('caesar.png')
    pil6img = Pilots_Canvas.create_image(30, Pil9[10], image=caesar, anchor=NW)
    flag10 = Pilots_Canvas.create_image(108, Pil9[10], image=italiano, anchor=NW)
    nompil10 = Pilots_Canvas.create_text(182, Pil9[10], anchor=NW, text=Pil9[0], font=('Britannic Bold', 16))
    edadpil10 = Pilots_Canvas.create_text(182, Pil9[10] + 25, anchor=NW, text=Pil9[1], font=('Britannic Bold', 16))
    tmppil10 = Pilots_Canvas.create_text(380, Pil9[10], anchor=NW, text=Pil9[3], font=('Britannic Bold', 16))
    rgppil10 = Pilots_Canvas.create_text(500, Pil9[10], anchor=NW, text=RGPcsz, font=('Britannic Bold', 16))
    reppil10 = Pilots_Canvas.create_text(555, Pil9[10], anchor=NW, text=REPcsz, font=('Britannic Bold', 16))
    comp10 = Pilots_Canvas.create_text(610, Pil9[10], anchor=NW, text=Pil9[4], font=('Britannic Bold', 16))

    #Pilots_Canvas.delete(pil3img)

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

    Btn_OrdenRGPM = Button(Frame1,text='Mayor RGP', font=('Britannic Bold', 14), bg='black',fg='white')
    Btn_OrdenRGPM.pack()
    Btn_OrdenRGPm = Button(Frame1, text='Menor RGP', font=('Britannic Bold', 14), bg='black', fg='white')
    Btn_OrdenRGPm.pack()
    Btn_OrdenREPM = Button(Frame1, text='Mayor REP', font=('Britannic Bold', 14), bg='black', fg='white')
    Btn_OrdenREPM.pack()
    Btn_OrdenREPm = Button(Frame1, text='Menor REP', font=('Britannic Bold', 14), bg='black', fg='white')
    Btn_OrdenREPm.pack()

    Pilots_Canvas.create_window(5, 640, anchor=NW, window=Pilots_frame)
    Pilots_Canvas.create_window(780, 10, anchor=NW, window=Frame1)
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
    velocimetroImg = cargarImg('velocity.png')
    Test_Canvas.create_image(200, 400, image = velocimetroImg, anchor = NW)

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

    #__Se cargan flechas para el velocimetro
    vel0 = cargarImg('0vel.png')
    vel10 = cargarImg('10vel.png')
    vel20 = cargarImg('20vel.png')
    vel30 = cargarImg('30vel.png')
    vel40 = cargarImg('40vel.png')
    vel50 = cargarImg('50vel.png')
    vel60 = cargarImg('60vel.png')
    vel70 = cargarImg('70vel.png')
    vel80 = cargarImg('80vel.png')
    vel90 = cargarImg('90vel.png')
    vel100 = cargarImg('100vel.png')
    Test_Canvas.create_image(283, 553, image=vel0, anchor = NW, tags = ('vel0', 'vel'), state = HIDDEN)
    Test_Canvas.create_image(263, 553, image=vel10, anchor=NW, tags=('vel10', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(248, 552, image=vel20, anchor=NW, tags=('vel20', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(253, 526, image=vel30, anchor=NW, tags=('vel30', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(286, 495, image=vel40, anchor=NW, tags=('vel40', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(320, 480, image=vel50, anchor=NW, tags=('vel50', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(318, 490, image=vel60, anchor=NW, tags=('vel60', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(316, 530, image=vel70, anchor=NW, tags=('vel70', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(316, 550, image=vel80, anchor=NW, tags=('vel80', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(319, 551, image=vel90, anchor=NW, tags=('vel90', 'vel'), state=HIDDEN)
    Test_Canvas.create_image(319, 553, image=vel100, anchor=NW, tags=('vel100', 'vel'), state=HIDDEN)

    middlecircle = cargarImg('center.png')
    Test_Canvas.create_image(317, 550, image=middlecircle, anchor=NW, state=NORMAL)


    #__Se carga el texto de la velocidad
    Test_Canvas.create_text(308,602,anchor=NW, text="Km/h", font = ('Britannic Bold', 12), fill = "white")
    Test_Canvas.create_text(297, 617, anchor=NW, text="o", tags = "velocidad", font = ('Britannic Bold', 18), fill = "white")

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
        global Dir_press, pressS

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
            if not pressS:
                pressS = True
                time.sleep(1)
                T_pwm_dowm_Re = Thread(target = reverse_desaceleracion)
                T_pwm_dowm_Re.start()
            else:
                return

        #Hacia adelante
        elif key == "s":
            if not pressS:
                pressS = True
                time.sleep(1)
                T_pwm_dowm = Thread(target=desaceleracion)
                T_pwm_dowm.start()
            else:
                return


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
                    Test_Canvas.itemconfig("L_s", state=NORMAL)
                    Test_Canvas.itemconfig("L_s2", state=NORMAL)
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
        global NumGas, pressTecla
        Test_Canvas.itemconfig("L_s2", state=HIDDEN)
        Test_Canvas.itemconfig("L_s", state=HIDDEN)
        if 500 <= NumGas <= 950 and pressTecla:
            if pressTecla:
                NumGas += 50
                ##send("pwm:"+str(NumGas)+":")
                print("pwm:" + str(NumGas) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
                aceleracion()
            else:
                return

        elif 400 >= NumGas and pressTecla:
            if pressTecla:
                NumGas += 100
                ##send("pwm:"+str(NumGas)+":")
                print ("pwm:"+str(NumGas)+";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
                aceleracion()
            else:
                return

    def reverse_aceleration():
        global NumGas_Re, Reverse_on, pressTecla
        Test_Canvas.itemconfig("L_s2", state=NORMAL)
        Test_Canvas.itemconfig("L_s", state=NORMAL)
        if -500 >= NumGas_Re >= -950 and pressTecla:
            if pressTecla:
                NumGas_Re -= 50
                ##send("pwm:"+str(NumGas_Re)+":")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
                reverse_aceleration()
            else:
                return

        elif -400 <= NumGas_Re and pressTecla:
            if pressTecla:
                NumGas_Re -= 100
                ##send("pwm:"+str(NumGas_Re)+":")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
                reverse_aceleration()
            else:
                return

    def desaceleracion():
        global NumGas, pressS
        Test_Canvas.itemconfig("L_s2", state=HIDDEN)
        Test_Canvas.itemconfig("L_s", state=HIDDEN)
        if NumGas <= 0:
            return
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            Test_Canvas.itemconfig("L_s", state=NORMAL)
        elif 500 <= NumGas <= 950 and pressS:
            if pressS:
                NumGas -= 50
                ##send("pwm:"+str(NumGas)+":")
                print("pwm:" + str(NumGas) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
                desaceleracion()
            else:
                return

        elif 400 >= NumGas and pressS:
            if pressS:
                NumGas -= 100
                ##send("pwm:"+str(NumGas)+":")
                print ("pwm:"+str(NumGas)+";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
                desaceleracion()
            else:
                return

    def reverse_desaceleracion():
        global NumGas_Re, Reverse_on, pressS
        Test_Canvas.itemconfig("L_s2", state=HIDDEN)
        Test_Canvas.itemconfig("L_s", state=HIDDEN)
        if NumGas_Re >= 0:
            return
        elif -500 >= NumGas_Re >= -950 and pressS:
            if pressS:
                NumGas_Re += 50
                ##send("pwm:"+str(NumGas_Re)+":")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
                reverse_desaceleracion()
            else:
                return

        elif -400 <= NumGas_Re and pressS:
            if pressS:
                NumGas_Re += 100
                ##send("pwm:"+str(NumGas_Re)+":")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
                reverse_desaceleracion()
            else:
                return

    def velocimetro():
        global NumGas_Re, NumGas
        if NumGas_Re == -100 or NumGas == 100:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel10', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -200 or NumGas == 200:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel20', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -300 or NumGas == 300:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel30', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -400 or NumGas == 400:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel40', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -500 or NumGas == 500:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel50', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -600 or NumGas == 600:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel60', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -700 or NumGas == 700:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel70', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -800 or NumGas == 800:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel80', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -900 or NumGas == 900:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel90', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == -1000 or NumGas == 1000:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel100', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        elif NumGas_Re == 0 or NumGas == 0:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel0', state = NORMAL)
            time.sleep(0.5)
            velocimetro()
        else:
            time.sleep(0.5)
            velocimetro()

    T_velocimetro = Thread(target= velocimetro)
    T_velocimetro.start()

    Test.bind("<KeyPress>", Car_Control)

    # Control key release
    def release_Control(event):
        key = event.char
        global right, left, GasON, reverse_press, front_press, left_press, right_press, Dir_press, pressTecla, pressS

        # Control de direccion
        if key == "a" or key == "d" and left or right:
            left = False
            right = False
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("none", state=NORMAL)
            ##send("dir:0;")
            print ("dir:0;")

        elif key == "w":
            pressTecla = False

        elif key == "s":
            pressS = False

        elif key == "r":
            reverse_press = False

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