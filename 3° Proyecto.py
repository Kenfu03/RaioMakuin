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
# ______________________________________________
# Biblioteca para conectar con el carro
import WiFiClient
from WiFiClient import NodeMCU

# ______________________________________________
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
left = False
right = False
reverseON = False
L_rightON = False
L_leftON = False
L_frontON = False
L_LRON = False
GasON = False
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
    off()
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


# __________ /Funcion para ventana de Pilotos
def ventana_Pilots():
    # Esconder la pantalla principal sin destruirla
    root.withdraw()
    # Pantalla About
    Pilots = Toplevel()
    Pilots.title('Pilots')
    Pilots.minsize(918, 700)
    Pilots.resizable(width=NO, height=NO)
    # __Se crea un canvas y un scrollbar
    #w= Scrollbar(Pilots)
    #w.place(x=900,y=0)
    Pilots_Canvas = Canvas(Pilots, width=900, height=700, bg='white')
    scroll_y = Scrollbar(Pilots,orient = 'vertical', command = Pilots_Canvas.yview)
    Pilots_frame = Frame(Pilots_Canvas)
    Frame1 = Frame(Pilots_Canvas)

    #w.config(command = Pilots_Canvas.yview)

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
    jonathan = cargarImg("jonathan.gif")
    pil1img = Pilots_Canvas.create_image(30, Pil0[10], image=jonathan, anchor=NW)
    flag1 = Pilots_Canvas.create_image(108,Pil0[10],image=britanico,anchor=NW)
    nompil1 = Pilots_Canvas.create_text(182,Pil0[10],anchor=NW,text =Pil0[0],font=('Britannic Bold', 16))
    edadpil1 = Pilots_Canvas.create_text(182,Pil0[10]+25,anchor=NW,text =Pil0[1],font=('Britannic Bold', 16))
    tmppil1 = Pilots_Canvas.create_text(380,Pil0[10],anchor=NW,text =Pil0[3],font=('Britannic Bold', 16))
    rgppil1 = Pilots_Canvas.create_text(500,Pil0[10],anchor=NW,text =RGPjon,font=('Britannic Bold', 16))
    reppil1 = Pilots_Canvas.create_text(555,Pil0[10],anchor=NW,text =REPjon,font=('Britannic Bold', 16))
    comp1 = Pilots_Canvas.create_text(610,Pil0[10],anchor=NW,text =Pil0[4],font=('Britannic Bold', 16))

    joseph = cargarImg("joseph.gif")
    pil2img = Pilots_Canvas.create_image(30, Pil1[10], image=joseph, anchor=NW)
    flag2 = Pilots_Canvas.create_image(108, Pil1[10], image=americano, anchor=NW)
    nompil2 = Pilots_Canvas.create_text(182,Pil1[10],anchor=NW,text =Pil1[0],font=('Britannic Bold', 16))
    edadpil2 = Pilots_Canvas.create_text(182,Pil1[10]+25,anchor=NW,text =Pil1[1],font=('Britannic Bold', 16))
    tmppil2 = Pilots_Canvas.create_text(380,Pil1[10],anchor=NW,text =Pil1[3],font=('Britannic Bold', 16))
    rgppil2 = Pilots_Canvas.create_text(500,Pil1[10],anchor=NW,text =RGPjsp,font=('Britannic Bold', 16))
    reppil2 = Pilots_Canvas.create_text(555,Pil1[10],anchor=NW,text =REPjsp,font=('Britannic Bold', 16))
    comp2 = Pilots_Canvas.create_text(610,Pil1[10],anchor=NW,text =Pil1[4],font=('Britannic Bold', 16))

    jotaro = cargarImg("jotaro.gif")
    pil3img = Pilots_Canvas.create_image(30,Pil2[10], image=jotaro, anchor=NW)
    flag3 = Pilots_Canvas.create_image(108,Pil2[10], image=japones, anchor=NW)
    nompil3 = Pilots_Canvas.create_text(182,Pil2[10], anchor=NW, text=Pil2[0], font=('Britannic Bold', 16))
    edadpil3 = Pilots_Canvas.create_text(182, Pil2[10] + 25, anchor=NW, text=Pil2[1], font=('Britannic Bold', 16))
    tmppil3 = Pilots_Canvas.create_text(380,Pil2[10], anchor=NW, text=Pil2[3], font=('Britannic Bold', 16))
    rgppil3 = Pilots_Canvas.create_text(500,Pil2[10], anchor=NW, text=RGPjot, font=('Britannic Bold', 16))
    reppil3 = Pilots_Canvas.create_text(555,Pil2[10], anchor=NW, text=REPjot, font=('Britannic Bold', 16))
    comp2 = Pilots_Canvas.create_text(610,Pil2[10], anchor=NW, text=Pil2[4], font=('Britannic Bold', 16))


    josuke = cargarImg("josuke.gif")
    pil4img = Pilots_Canvas.create_image(30, Pil3[10], image=josuke, anchor=NW)
    flag4 = Pilots_Canvas.create_image(108, Pil3[10], image=japones, anchor=NW)
    nompil4 = Pilots_Canvas.create_text(182, Pil3[10], anchor=NW, text=Pil3[0], font=('Britannic Bold', 16))
    edadpil4 = Pilots_Canvas.create_text(182, Pil3[10] + 25, anchor=NW, text=Pil3[1], font=('Britannic Bold', 16))
    tmppil4 = Pilots_Canvas.create_text(380, Pil3[10], anchor=NW, text=Pil3[3], font=('Britannic Bold', 16))
    rgppil4 = Pilots_Canvas.create_text(500, Pil3[10], anchor=NW, text=RGPjsk, font=('Britannic Bold', 16))
    reppil4 = Pilots_Canvas.create_text(555, Pil3[10], anchor=NW, text=REPjsk, font=('Britannic Bold', 16))
    comp4 = Pilots_Canvas.create_text(610, Pil3[10], anchor=NW, text=Pil3[4], font=('Britannic Bold', 16))
    #nompil4.destroy()

    giorno = cargarImg("giorno.gif")
    pil5img = Pilots_Canvas.create_image(30, Pil4[10], image=giorno, anchor=NW)
    flag5 = Pilots_Canvas.create_image(108, Pil4[10], image=italiano, anchor=NW)
    nompil5 = Pilots_Canvas.create_text(182, Pil4[10], anchor=NW, text=Pil4[0], font=('Britannic Bold', 16))
    edadpil5 = Pilots_Canvas.create_text(182, Pil4[10] + 25, anchor=NW, text=Pil4[1], font=('Britannic Bold', 16))
    tmppil5 = Pilots_Canvas.create_text(380, Pil4[10], anchor=NW, text=Pil4[3], font=('Britannic Bold', 16))
    rgppil5 = Pilots_Canvas.create_text(500, Pil4[10], anchor=NW, text=RGPgio, font=('Britannic Bold', 16))
    reppil5 = Pilots_Canvas.create_text(555, Pil4[10], anchor=NW, text=REPgio, font=('Britannic Bold', 16))
    comp5 = Pilots_Canvas.create_text(610, Pil4[10], anchor=NW, text=Pil4[4], font=('Britannic Bold', 16))

    dio = cargarImg('dio.gif')
    pil6img = Pilots_Canvas.create_image(30, Pil5[10], image=dio, anchor=NW)
    flag6 = Pilots_Canvas.create_image(108, Pil5[10], image=britanico, anchor=NW)
    nompil6 = Pilots_Canvas.create_text(182, Pil5[10], anchor=NW, text=Pil5[0], font=('Britannic Bold', 16))
    edadpil6 = Pilots_Canvas.create_text(182, Pil5[10] + 25, anchor=NW, text=Pil5[1], font=('Britannic Bold', 16))
    tmppil6 = Pilots_Canvas.create_text(380, Pil5[10], anchor=NW, text=Pil5[3], font=('Britannic Bold', 16))
    rgppil6 = Pilots_Canvas.create_text(500, Pil5[10], anchor=NW, text=RGPdio, font=('Britannic Bold', 16))
    reppil6 = Pilots_Canvas.create_text(555, Pil5[10], anchor=NW, text=REPdio, font=('Britannic Bold', 16))
    comp6 = Pilots_Canvas.create_text(610, Pil5[10], anchor=NW, text=Pil5[4], font=('Britannic Bold', 16))

    kira = cargarImg('kira.gif')
    pil7img = Pilots_Canvas.create_image(30, Pil6[10], image=kira, anchor=NW)
    flag7 = Pilots_Canvas.create_image(108, Pil6[10], image=japones, anchor=NW)
    nompil7 = Pilots_Canvas.create_text(182, Pil6[10], anchor=NW, text=Pil6[0], font=('Britannic Bold', 16))
    edadpil7 = Pilots_Canvas.create_text(182, Pil6[10]+ 25, anchor=NW, text=Pil6[1], font=('Britannic Bold', 16))
    tmppil7 = Pilots_Canvas.create_text(380, Pil6[10], anchor=NW, text=Pil6[3], font=('Britannic Bold', 16))
    rgppil7 = Pilots_Canvas.create_text(500, Pil6[10], anchor=NW, text=RGPkra, font=('Britannic Bold', 16))
    reppil7 = Pilots_Canvas.create_text(555, Pil6[10], anchor=NW, text=REPkra, font=('Britannic Bold', 16))
    comp7 = Pilots_Canvas.create_text(610, Pil6[10], anchor=NW, text=Pil6[4], font=('Britannic Bold', 16))

    bruno = cargarImg('bruno.gif')
    pil8img = Pilots_Canvas.create_image(30, Pil7[10], image=bruno, anchor=NW)
    flag8 = Pilots_Canvas.create_image(108, Pil7[10], image=italiano, anchor=NW)
    nompil8 = Pilots_Canvas.create_text(182, Pil7[10], anchor=NW, text=Pil7[0], font=('Britannic Bold', 16))
    edadpil8 = Pilots_Canvas.create_text(182, Pil7[10] + 25, anchor=NW, text=Pil7[1], font=('Britannic Bold', 16))
    tmppil8 = Pilots_Canvas.create_text(380, Pil7[10], anchor=NW, text=Pil7[3], font=('Britannic Bold', 16))
    rgppil8 = Pilots_Canvas.create_text(500, Pil7[10], anchor=NW, text=RGPbrn, font=('Britannic Bold', 16))
    reppil8 = Pilots_Canvas.create_text(555, Pil7[10], anchor=NW, text=REPbrn, font=('Britannic Bold', 16))
    comp8 = Pilots_Canvas.create_text(610, Pil7[10], anchor=NW, text=Pil7[4], font=('Britannic Bold', 16))

    polnareff = cargarImg('polnareff.gif')
    pil9img = Pilots_Canvas.create_image(30, Pil8[10], image=polnareff, anchor=NW)
    flag9 = Pilots_Canvas.create_image(108, Pil8[10], image=frances, anchor=NW)
    nompil9 = Pilots_Canvas.create_text(182, Pil8[10], anchor=NW, text=Pil8[0], font=('Britannic Bold', 16))
    edadpil9 = Pilots_Canvas.create_text(182, Pil8[10] + 25, anchor=NW, text=Pil8[1], font=('Britannic Bold', 16))
    tmppil9 = Pilots_Canvas.create_text(380, Pil8[10], anchor=NW, text=Pil8[3], font=('Britannic Bold', 16))
    rgppil9 = Pilots_Canvas.create_text(500, Pil8[10], anchor=NW, text=RGPpol, font=('Britannic Bold', 16))
    reppil9 = Pilots_Canvas.create_text(555, Pil8[10], anchor=NW, text=REPpol, font=('Britannic Bold', 16))
    comp9 = Pilots_Canvas.create_text(610, Pil8[10], anchor=NW, text=Pil8[4], font=('Britannic Bold', 16))

    caesar = cargarImg('caesar.gif')
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
    Test.minsize(1000, 562)
    Test.resizable(width=NO, height=NO)
    # __Se crea un canvas
    Test_Canvas = Canvas(Test, width=1000, height=562, bg='black')
    Test_Canvas.place(x=0, y=0)
    # __Se carga una imagen de fondo
    BackupTD = cargarImg('BackupTD.png')
    Test_Canvas.create_image(0, 0, image=BackupTD, anchor=NW)

    # _Luces carrito
    # Luz front
    Luz_Front = cargarImg('luz_blanca.png')
    Test_Canvas.create_image(-5, 30, image=Luz_Front, anchor=NW, tags=("L_f", "LF"), state=HIDDEN)
    Test_Canvas.create_image(50, 30, image=Luz_Front, anchor=NW, tags=("L_f2", "LF"), state=HIDDEN)
    # Luz direccion
    Luz_Direccion = cargarImg('luz_amarilla.png')
    Test_Canvas.create_image(-125, 110, image=Luz_Direccion, anchor=NW, tags=("L_left", "L_dir"), state=HIDDEN)
    Luz_Direccion2 = cargarImg('luz_amarilla2.png')
    Test_Canvas.create_image(-40, 110, image=Luz_Direccion2, anchor=NW, tags=("L_right", "L_dir2"), state=HIDDEN)
    # Luz stop
    Luz_Stop = cargarImg('luz_roja.png')
    Test_Canvas.create_image(-42, 215, image=Luz_Stop, anchor=NW, tags=("L_s", "LS"), state=NORMAL)
    Test_Canvas.create_image(9, 215, image=Luz_Stop, anchor=NW, tags=("L_s2", "LS"), state=NORMAL)
    # __Se carga una imagen del estado del vehiculo
    CarNone = cargarImg('none.png')
    CarLeft = cargarImg('left.png')
    CarRight = cargarImg('right.png')
    Test_Canvas.create_image(20, 60, image=CarNone, anchor=NW, tags=("none", "car"), state=NORMAL)
    Test_Canvas.create_image(20, 60, image=CarLeft, anchor=NW, tags=("left", "car"), state=HIDDEN)
    Test_Canvas.create_image(20, 60, image=CarRight, anchor=NW, tags=("right", "car"), state=HIDDEN)

    # _Boton de reversa
    Reverse_off = cargarImg('reverse-off.png')
    Reverse_on = cargarImg('reverse-on.png')
    Test_Canvas.create_image(110, 90, image=Reverse_off, anchor=NW, tags=("R-off", "reverse"), state=NORMAL)
    Test_Canvas.create_image(110, 90, image=Reverse_on, anchor=NW, tags=("R-on", "reverse"), state=HIDDEN)

    # __Funcionalidades principales del test drive

    # Control key press
    def Car_Control(event):
        key = event.char

        # Globales
        global left, right, NumGas, NumGas_Re, reverseON, L_rightON, L_leftON, L_frontON, L_LRON, GasON

        # Control de direccion izquierda
        if (key == "a") and not left:
            left = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("left", state=NORMAL)
            send("dir:-1;")

        # Control de direccion derecha
        elif (key == "d") and not right:
            right = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("right", state=NORMAL)
            send("dir:1;")

        # Control de aceleracion

        # #Limite Reversa
        elif NumGas_Re == -1000:
            return
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")

            # Limite hacia adelante
        elif NumGas == 1000:
            return
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")

            # Reversa
        elif (key == "w") and reverseON:
            GasON = True
            time.sleep(1)
            NumGas_Re -= 100
            Test_Canvas.itemconfig("L_s2", state=HIDDEN)
            Test_Canvas.itemconfig("L_s", state=HIDDEN)
            progress_up(NumGas)
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")

            # Hacia adelante
        elif (key == "w"):
            GasON = True
            time.sleep(1)
            NumGas += 100
            Test_Canvas.itemconfig("L_s2", state=HIDDEN)
            Test_Canvas.itemconfig("L_s", state=HIDDEN)
            progress_up(NumGas)
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")


        # Control boton de stop

        # Limite 0
        elif NumGas_Re == 0:
            return
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")

            # Limite 0
        elif NumGas == 0:
            return
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")


        # Disminucion de velocidad
        # Reversa down
        elif (key == "s") and reverseON and not GasON:
            time.sleep(1)
            NumGas_Re += 100
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")

        elif (key == "s") and not GasON:
            time.sleep(1)
            NumGas -= 100
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")


        # Control del boton de reversa
        # Activar reversa
        elif (key == "r") and not reverseON:
            reverseON = True
            Test_Canvas.itemconfig("reverse", state=HIDDEN)
            Test_Canvas.itemconfig("R-on", state=NORMAL)
            # Desactivar reversa
        elif (key == "r") and reverseON:
            reverseON = False
            Test_Canvas.itemconfig("reverse", state=HIDDEN)
            Test_Canvas.itemconfig("R-off", state=NORMAL)

        # Control de luces direccionales
        # Izquierda
        elif (key == "z") and not L_leftON:
            L_leftON = True
            Test_Canvas.itemconfig("L_dir", state=HIDDEN)
            Test_Canvas.itemconfig("L_left", state=NORMAL)
            while L_leftON:
                ##send("ll:1;")
                print("ll:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                print("ll:0;")

        elif (key == "z") and L_leftON:
            L_leftON = False
            Test_Canvas.itemconfig("L_dir", state=NORMAL)
            Test_Canvas.itemconfig("L_left", state=HIDDEN)
            if not L_leftON:
                ##send("ll:0;")
                print("ll:0;")

            # Derecha
        elif (key == "c") and not L_rightON:
            L_rightON = True
            Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
            Test_Canvas.itemconfig("L_right", state=NORMAL)
            while L_rightON:
                ##send("ll:1;")
                print("lr:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                print("lr:0;")

        elif (key == "c") and L_rightON:
            L_rightON = False
            Test_Canvas.itemconfig("L_dir2", state=NORMAL)
            Test_Canvas.itemconfig("L_right", state=HIDDEN)
            if not L_rightON:
                ##send("ll:0;")
                print("lr:0;")

            # Ambas
        elif (key == "x") and not L_LRON:
            L_LRON = True
            Test_Canvas.itemconfig("L_dir", state=HIDDEN)
            Test_Canvas.itemconfig("L_left", state=NORMAL)
            Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
            Test_Canvas.itemconfig("L_right", state=NORMAL)
            if L_LRON:
                ##send("ll:1;")
                ##send("lr:1;")
                print("ll:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                ##send("lr:0;")
                print("ll:0;")

        elif (key == "x") and L_LRON:
            L_LRON = False
            Test_Canvas.itemconfig("L_dir", state=NORMAL)
            Test_Canvas.itemconfig("L_left", state=HIDDEN)
            Test_Canvas.itemconfig("L_dir2", state=NORMAL)
            Test_Canvas.itemconfig("L_right", state=HIDDEN)
            if not L_LRON:
                ##send("ll:0;")
                ##send("lr:0;")
                print("ll:0;")

            # Frontales
        elif (key == "f") and not L_frontON:
            L_frontON = True
            Test_Canvas.itemconfig("L_F", state=HIDDEN)
            Test_Canvas.itemconfig("L_F", state=HIDDEN)
            Test_Canvas.itemconfig("L_f", state=NORMAL)
            Test_Canvas.itemconfig("L_f2", state=NORMAL)
            ##send("lf:1;")
            print("lf:1;")
        elif (key == "f") and L_frontON:
            L_frontON = False
            Test_Canvas.itemconfig("L_F", state=NORMAL)
            Test_Canvas.itemconfig("L_F", state=NORMAL)
            Test_Canvas.itemconfig("L_f", state=HIDDEN)
            Test_Canvas.itemconfig("L_f2", state=HIDDEN)
            ##send("lf:0;")
            print("lf:0;")
        elif (key == "d") and not right:
            right = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("right", state=NORMAL)
            send("dir:1;")
        elif NumGas_Re == -1000:
            return
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")
        elif NumGas == 1000:
            return
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")
        elif (key == "w") and reverseON:
            GasON = True
            time.sleep(1)
            NumGas_Re -= 100
            Test_Canvas.itemconfig("L_s2", state=HIDDEN)
            Test_Canvas.itemconfig("L_s", state=HIDDEN)
            progress_up(NumGas)
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")
        elif (key == "w"):
            GasON = True
            time.sleep(1)
            NumGas += 100
            Test_Canvas.itemconfig("L_s2", state=HIDDEN)
            Test_Canvas.itemconfig("L_s", state=HIDDEN)
            progress_up(NumGas)
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")
        elif NumGas_Re == 0:
            return
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")
        elif NumGas == 0:
            return
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")
        elif (key == "s") and reverseON and not GasON:
            time.sleep(1)
            NumGas_Re += 100
            ##send("pwm:"+str(NumGas_Re)+";")
            print("pwm:" + str(NumGas_Re) + ";")
        elif (key == "s") and not GasON:
            time.sleep(1)
            NumGas -= 100
            ##send("pwm:"+str(NumGas)+";")
            print("pwm:" + str(NumGas) + ";")
        elif (key == "r") and not reverseON:
            reverseON = True
            Test_Canvas.itemconfig("reverse", state=HIDDEN)
            Test_Canvas.itemconfig("R-on", state=NORMAL)
        elif (key == "r") and reverseON:
            reverseON = False
            Test_Canvas.itemconfig("reverse", state=HIDDEN)
            Test_Canvas.itemconfig("R-off", state=NORMAL)
        elif (key == "z") and not L_leftON:
            L_leftON = True
            Test_Canvas.itemconfig("L_dir", state=HIDDEN)
            Test_Canvas.itemconfig("L_left", state=NORMAL)
            while L_leftON:
                ##send("ll:1;")
                print("ll:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                print("ll:0;")
        elif (key == "z") and L_leftON:
            L_leftON = False
            Test_Canvas.itemconfig("L_dir", state=NORMAL)
            Test_Canvas.itemconfig("L_left", state=HIDDEN)
            if not L_leftON:
                ##send("ll:0;")
                print("ll:0;")
        elif (key == "c") and not L_rightON:
            L_rightON = True
            Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
            Test_Canvas.itemconfig("L_right", state=NORMAL)
            while L_rightON:
                ##send("ll:1;")
                print("lr:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                print("lr:0;")
        elif (key == "c") and L_rightON:
            L_rightON = False
            Test_Canvas.itemconfig("L_dir2", state=NORMAL)
            Test_Canvas.itemconfig("L_right", state=HIDDEN)
            if not L_rightON:
                ##send("ll:0;")
                print("lr:0;")
        elif (key == "x") and not L_LRON:
            L_LRON = True
            Test_Canvas.itemconfig("L_dir", state=HIDDEN)
            Test_Canvas.itemconfig("L_left", state=NORMAL)
            Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
            Test_Canvas.itemconfig("L_right", state=NORMAL)
            if L_LRON:
                ##send("ll:1;")
                ##send("lr:1;")
                print("ll:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                ##send("lr:0;")
                print("ll:0;")
        elif (key == "x") and L_LRON:
            L_LRON = False
            Test_Canvas.itemconfig("L_dir", state=NORMAL)
            Test_Canvas.itemconfig("L_left", state=HIDDEN)
            Test_Canvas.itemconfig("L_dir2", state=NORMAL)
            Test_Canvas.itemconfig("L_right", state=HIDDEN)
            if not L_LRON:
                ##send("ll:0;")
                ##send("lr:0;")
                print("ll:0;")
        elif (key == "f") and not L_frontON:
            L_frontON = True
            Test_Canvas.itemconfig("L_F", state=HIDDEN)
            Test_Canvas.itemconfig("L_F", state=HIDDEN)
            Test_Canvas.itemconfig("L_f", state=NORMAL)
            Test_Canvas.itemconfig("L_f2", state=NORMAL)
            ##send("lf:1;")
            print("lf:1;")
        elif (key == "f") and L_frontON:
            L_frontON = False
            Test_Canvas.itemconfig("L_F", state=NORMAL)
            Test_Canvas.itemconfig("L_F", state=NORMAL)
            Test_Canvas.itemconfig("L_f", state=HIDDEN)
            Test_Canvas.itemconfig("L_f2", state=HIDDEN)
            ##send("lf:0;")
            print("lf:0;")

    Test.bind("<KeyPress>", Car_Control)

    # Control key release
    def release_Control(event):
        key = event.char
        global right, left, GasON

        # Control de direccion
        if (key == "a") or (key == "d") and left or right:
            left = False
            right = False
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("none", state=NORMAL)
            send("dir:0;")

    Test.bind("<KeyRelease>", release_Control)

    # __Se crean labels con los datos inportantes
    Test_Canvas.create_text(485, 15, text="Batery Level", font=('Britannic Bold', 14), fill="red")

    Test_Canvas.create_text(45, 330, text="Pwm\nVelocity", font=('Britannic Bold', 14), fill="red")

    # Se crea una funcion para crear una barra de progreso, para cuando se esta acelerando
    style = ttk.Style()
    style.theme_use('default')
    style.configure("darkblue.Vertical.TProgressbar", background='darkblue')
    progressbar1 = Progressbar(Test, length=200, style='darkblue.Vertical.TProgressbar', orient=tk.VERTICAL,
                               maximum=1000)
    progressbar1['value'] = NumGas
    progressbar1.place(x=30, y=350)

    def progress_up(Progress):
        Num_Bar = Progress
        progressbar1['value'] = Num_Bar
        if Num_Bar == 1000:
            return
        else:
            Num_Bar += 100

    def progress_down(Progress):
        Num_Bar = Progress
        progressbar1['value'] = Num_Bar
        if Num_Bar == 0:
            return
        else:
            Num_Bar -= 100

    # Se crea una funcion para crear una barra de progreso, para el nivel de la bateria
    style = ttk.Style()
    style.theme_use('default')
    style.configure("green.Horizontal.TProgressbar", background='green')
    progressbar2 = Progressbar(Test, length=200, style='green.Horizontal.TProgressbar', maximum=1023)
    progressbar2['value'] = 500
    progressbar2.place(x=390, y=30)

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
