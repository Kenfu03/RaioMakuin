InfoPer="""
_______________________________________________
    Insituto Tecnologico de Costa Rica         
            Computer Engineering                        

    Kenneth Fuentes Martinez      
    Carnet: 2019026305               
    Curso: Taller de Programacion
    Año: 2019                             
    Prof: Milton Villegas Lemus    
    Pais: Costa Rica                    
    Version: 1.0.0                        
_________________________________________________
Guia basica:
                      
_________________________________________________
"""
#__________/BIBLIOTECAS
import tkinter as tk #Se importa tkinter
from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading                    # 
import winsound                     # Playsound
import os                           # ruta = os.path.join('')
import time                         # time.sleep(x)
from tkinter import messagebox      # AskYesNo ()
import random                   #Biblioteca Random
from tkinter.ttk import Progressbar #Se utiliza para hacer una progressbar
from tkinter import ttk
global left, right
#______________________________________________
#Biblioteca para conectar con el carro
import WiFiClient
from WiFiClient import NodeMCU

#______________________________________________
#Control del carrito por NodeMCU
Carrito = NodeMCU()
Carrito.start()

#______________________________________________
#Globale
left = False
right = False
gas = True
NumGas=23

#__________/Función para cargar imagenes
def cargarImg(nombre):
    ruta=os.path.join('img',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

#__________/Música
def Song1():
    winsound.PlaySound('song1.wav', winsound.SND_ASYNC)

#__________/funcion para el boton mute
def off():
    winsound.PlaySound(None, winsound.SND_ASYNC)

#__________/Ventana Principal
root=tk.Tk()
root.title('Raio Makuin')
root.minsize(1000,562)
root.resizable(width=NO,height=NO)

#__________/Se crea un lienzo para objetos
Principal_Canvas=Canvas(root, width=1000,height=562, bg='black')
Principal_Canvas.place(x=0,y=0)

#__________/Cargar una imagen
InicioBackup=cargarImg("backup.gif")
Principal_Canvas.create_image(0,0, image = InicioBackup, anchor = NW)


#_________/Se crea la funcion que ejecuta la cancion de fondo
off()
Play=Thread(target=Song1,args=())
Play.start()

def play1():
    off()
    Play=Thread(target=Song1,args=())
    Play.start()

# __________ /Funcion para ventana about
def ventana_about():
    #Esconder la pantalla principal sin destruirla
    root.withdraw()
    #Pantalla About
    about = Toplevel()
    about.title('About')
    about.minsize(1000,562)
    about.resizable(width=NO,height=NO)
#__Se crea un canvas
    About_Canvas=Canvas(about, width=1000,height=562, bg='black')
    About_Canvas.place(x=0,y=0)
#__Se carga una imagen
    PersonalImg =cargarImg('Personalimg.gif')
    Personal=Label(About_Canvas, image=PersonalImg,bg='white')
    Personal.photo=PersonalImg
    Personal.place(x=10,y=60)
#__Se crea un label con informacion crucial
    Label_about=Label(About_Canvas, text=InfoPer ,font= ('Britannic Bold',16), fg='white', bg='black')
    Label_about.place(x=410,y=10)
#__Se crea una funcion para volver a la pantalla principal
    def atras_about():
        global pausa
        pausa=True
        about.destroy()
        root.deiconify()
        
    Btn_Atras = Button(About_Canvas,text='Atras', font= ('Britannic Bold',18), command=atras_about,bg='black',fg='white')
    Btn_Atras.place(x=5,y=512)

# __________ /Funcion para ventana de Pilotos
def ventana_Pilots():
    #Esconder la pantalla principal sin destruirla
    root.withdraw()
    #Pantalla About
    Pilots = Toplevel()
    Pilots.title('Pilots')
    Pilots.minsize(1000,900)
    Pilots.resizable(width=NO,height=NO)
#__Se crea un canvas
    Pilots_Canvas=Canvas(Pilots, width=1000,height=900, bg='black')
    Pilots_Canvas.place(x=0,y=0)
#__Se carga una imagen


#__Se crea un label con informacion crucial

    
#__Se crea una funcion para volver a la pantalla principal
    def atras_Pilots():
        global pausa
        pausa=True
        Pilots.destroy()
        root.deiconify()
        
    Btn_Atras = Button(Pilots_Canvas,text='Atras', font= ('Britannic Bold',18), command=atras_Pilots,bg='black',fg='white')
    Btn_Atras.place(x=5,y=640)

#___________/Funcion de send, para enviar mensajes al Carrito
    
def send (mensaje):
    if(len(mensaje)>0 and mensaje[-1] == ";"):
        Carrito.send(mensaje)
    else:
        messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')") 

# __________ /Funcion para ventana de TestDrive
def ventana_TestDrive():
    #Esconder la pantalla principal sin destruirla
    root.withdraw()
    #Pantalla About
    Test = Toplevel()
    Test.title('Test Drive')
    Test.minsize(1000,562)
    Test.resizable(width=NO,height=NO)
#__Se crea un canvas
    Test_Canvas=Canvas(Test, width=1000,height=562, bg='black')
    Test_Canvas.place(x=0,y=0)
#__Se carga una imagen de fondo
    BackupTD =cargarImg('BackupTD.png')
    Test_Canvas.create_image(0,0, image = BackupTD, anchor = NW)
#__Se carga una imagen del estado del vehiculo
    CarNone=cargarImg('none.png')
    CarLeft =cargarImg('left.png')
    CarRight= cargarImg('right.png')
    Test_Canvas.create_image(0,20, image=CarNone, anchor = NW, tags = ("none","car"), state =NORMAL)
    Test_Canvas.create_image(0,20, image=CarLeft, anchor = NW, tags = ("left", "car"), state = HIDDEN)
    Test_Canvas.create_image(0,20, image=CarRight, anchor = NW, tags = ("right", "car"), state = HIDDEN)
    
    def Tdir(event):
        key = event.char
        global left, right, gas, NumGas
        if (key == "a") and not left:
            left = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("left", state=NORMAL)
            send("dir:-1;")
        elif(key=="d") and not right:
            right = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("right", state=NORMAL)
            send("dir:1;")
        elif NumGas ==1023:
            print (NumGas)
            return NumGas
        elif (key == "w") and gas:
            gas = True
            time.sleep(1)
            NumGas += 100
            send("pwm:"+str(NumGas)+";")
            print (NumGas)
        elif (key == "s") and gas:
            gas = True
            time.sleep(1)
            NumGas += 100
            send("pwm:"+"-"+str(NumGas)+";")
            print (NumGas)
            
    Test.bind("<KeyPress>", Tdir)

    def none_dir(event):
        key = event.char
        global right, left, gas, NumGas
        if (key == "a") or (key == "d") and left or right:
            left = False
            right = False
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("none", state=NORMAL)
            send("dir:0;")
        if (key == "w") or (key=="s") and gas:
            gas = True
            while NumGas != 23:
                time.sleep(1.5)
                NumGas -= 100
                send("pwm:"+str(NumGas)+";")
                print (NumGas)

    Test.bind("<KeyRelease>", none_dir)
        
            
#__Se crean labels con los datos inportantes
    Test_Canvas.create_text(485, 15, text="Batery Level" ,font= ('Britannic Bold',14), fill="red")
  
    Test_Canvas.create_text(45, 330, text="Pwm\nVelocity" ,font= ('Britannic Bold',14), fill = "red")

#Se crea una funcion para crear una barra de progreso, para cuando se esta acelerando
    style = ttk.Style()
    style.theme_use('default')
    style.configure("darkblue.Vertical.TProgressbar", background='darkblue') 
    progressbar1 = Progressbar(Test, length=200, style='darkblue.Vertical.TProgressbar', orient= tk.VERTICAL, maximum=1023) 
    progressbar1['value'] = NumGas
    progressbar1.place(x=30, y=350)

    progressbar1.step(NumGas)

#Se crea una funcion para crear una barra de progreso, para el nivel de la bateria
    style = ttk.Style()
    style.theme_use('default')
    style.configure("green.Horizontal.TProgressbar", background='green') 
    progressbar2 = Progressbar(Test, length=200, style='green.Horizontal.TProgressbar', maximum=1023) 
    progressbar2['value'] = 500
    progressbar2.place(x=390, y=30)
    
#__Se crea un label con informacion crucial

    
#__Se crea una funcion para volver a la pantalla principal
    def atras_Test():
        global pausa
        pausa=True
        Test.destroy()
        root.deiconify()
        
    Btn_Atras = Button(Test_Canvas,text='Atras', font= ('Britannic Bold',14), command=atras_Test,bg='white',fg='black')
    Btn_Atras.place(x=5,y=5)

    Test.mainloop()

#__________/Botones de ventana principal

Btn_mute=Button(Principal_Canvas,text='Mute',font= ('Britannic Bold',12),command=off,fg='red')
Btn_mute.place(x=483,y=490)

Btn_Quit=Button(Principal_Canvas, text='Quit',font= ('Britannic Bold',20), command=root.destroy, fg='red')
Btn_Quit.place(x=10,y=490)

Btn_PlayMusic=Button(Principal_Canvas, text='Music',font= ('Britannic Bold',12), command=play1, fg='red')
Btn_PlayMusic.place(x=480,y=530)

Btn_About = Button(Principal_Canvas,text='Credits',font= ('Britannic Bold',20),command=ventana_about,fg='red')
Btn_About.place(x=890,y=485)

Btn_Puntajes = Button(Principal_Canvas,text='Pilots',font= ('Britannic Bold',20),command=ventana_Pilots,fg='red')
Btn_Puntajes.place(x=10,y=35)

Btn_Puntajes = Button(Principal_Canvas,text='Test Driver',font= ('Britannic Bold',20),command=ventana_TestDrive,fg='red')
Btn_Puntajes.place(x=840,y=35)

root.mainloop()
