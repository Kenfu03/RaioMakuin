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
reverseON = False
L_rightON = False
L_leftON = False
L_frontON = False
L_LRON = False
NumGas=0
NumGas_Re=0

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

#_Luces carrito
    #Luz front
    Luz_Front= cargarImg('luz_blanca.png')
    Test_Canvas.create_image(-5,30, image=Luz_Front, anchor = NW, tags = ("L_f","LF"), state =HIDDEN)
    Test_Canvas.create_image(50,30, image=Luz_Front, anchor = NW, tags = ("L_f2","LF"), state = HIDDEN)
    #Luz direccion
    Luz_Direccion= cargarImg('luz_amarilla.png')
    Test_Canvas.create_image(-125,110, image=Luz_Direccion, anchor = NW, tags = ("L_left","L_dir"), state =HIDDEN)
    Luz_Direccion2= cargarImg('luz_amarilla2.png')
    Test_Canvas.create_image(-40,110, image=Luz_Direccion2, anchor = NW, tags = ("L_right","L_dir2"), state = HIDDEN)
    #Luz stop
    Luz_Stop =cargarImg('luz_roja.png')
    Test_Canvas.create_image(-42,215, image=Luz_Stop, anchor = NW, tags = ("L_s","LS"), state =NORMAL)
    Test_Canvas.create_image(9,215, image=Luz_Stop, anchor = NW, tags = ("L_s2","LS"), state = NORMAL)
#__Se carga una imagen del estado del vehiculo
    CarNone=cargarImg('none.png')
    CarLeft =cargarImg('left.png')
    CarRight= cargarImg('right.png')
    Test_Canvas.create_image(20,60, image=CarNone, anchor = NW, tags = ("none","car"), state =NORMAL)
    Test_Canvas.create_image(20,60, image=CarLeft, anchor = NW, tags = ("left", "car"), state = HIDDEN)
    Test_Canvas.create_image(20,60, image=CarRight, anchor = NW, tags = ("right", "car"), state = HIDDEN)

#_Boton de reversa
    Reverse_off =cargarImg('reverse-off.png')
    Reverse_on= cargarImg('reverse-on.png')
    Test_Canvas.create_image(110,90, image=Reverse_off, anchor = NW, tags = ("R-off","reverse"), state =NORMAL)
    Test_Canvas.create_image(110,90, image=Reverse_on, anchor = NW, tags = ("R-on","reverse"), state = HIDDEN)

    def Car_Control(event):
        key = event.char
        global left, right, gas, NumGas,NumGas_Re, reverseON, L_rightON, L_leftON, L_frontON, L_LRON #Globales
        #Control de direccion izquierda
        if (key == "a") and not left:
            left = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("left", state=NORMAL)
            send("dir:-1;")
        #Control de direccion derecha
        elif(key=="d") and not right:
            right = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("right", state=NORMAL)
            send("dir:1;")
        #Control de aceleracion
            #Limite Reversa
        elif NumGas_Re ==-1000:
            return
            ##send("pwm:"+str(NumGas_Re)+";")
            print ("pwm:"+str(NumGas_Re)+";")
            #Limite hacia adelante
        elif NumGas ==1000:
            return
            ##send("pwm:"+str(NumGas)+";")
            print ("pwm:"+str(NumGas)+";")
            #Reversa
        elif (key == "w") and gas and reverseON:
            gas = True
            time.sleep(1)
            NumGas_Re -= 100
            Test_Canvas.itemconfig("L_s2", state=HIDDEN)
            Test_Canvas.itemconfig("L_s", state=HIDDEN)
            ##send("pwm:"+str(NumGas_Re)+";")
            print ("pwm:"+str(NumGas_Re)+";")
            #Hacia adelante
        elif (key == "w") and gas:
            gas = True
            time.sleep(1)
            NumGas += 100
            Test_Canvas.itemconfig("L_s2", state=HIDDEN)
            Test_Canvas.itemconfig("L_s", state=HIDDEN)
            ##send("pwm:"+str(NumGas)+";")
            print ("pwm:"+str(NumGas)+";")
        #Control del boton de reversa
            #Activar reversa
        elif (key == "r") and not reverseON:
            reverseON = True
            Test_Canvas.itemconfig("reverse", state=HIDDEN)
            Test_Canvas.itemconfig("R-on", state=NORMAL)
            #Desactivar reversa
        elif (key == "r") and reverseON:
            reverseON = False
            Test_Canvas.itemconfig("reverse", state=HIDDEN)
            Test_Canvas.itemconfig("R-off", state=NORMAL)
    #Control de luces direccionales
        #Izquierda
        elif (key=="z") and not L_leftON:
            L_leftON = True
            Test_Canvas.itemconfig("L_dir", state=HIDDEN)
            Test_Canvas.itemconfig("L_left", state=NORMAL)
            if L_leftON:
                ##send("ll:1;")
                print ("ll:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                print ("ll:0;")
        elif (key=="z") and L_leftON:
            L_leftON = False
            Test_Canvas.itemconfig("L_dir", state=NORMAL)
            Test_Canvas.itemconfig("L_left", state=HIDDEN)
            if not L_leftON:
                ##send("ll:0;")
                print ("ll:0;")
        #Derecha
        elif (key=="c") and not L_rightON:
            L_rightON = True
            Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
            Test_Canvas.itemconfig("L_right", state=NORMAL)
            if L_rightON:
                ##send("ll:1;")
                print ("lr:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                print ("lr:0;")
        elif (key=="c") and L_rightON:
            L_rightON = False
            Test_Canvas.itemconfig("L_dir2", state=NORMAL)
            Test_Canvas.itemconfig("L_right", state=HIDDEN)
            if not L_rightON:
                ##send("ll:0;")
                print ("lr:0;")
        #Ambas
        elif (key=="x") and not L_LRON:
            L_LRON = True
            Test_Canvas.itemconfig("L_dir", state=HIDDEN)
            Test_Canvas.itemconfig("L_left", state=NORMAL)
            Test_Canvas.itemconfig("L_dir2", state=HIDDEN)
            Test_Canvas.itemconfig("L_right", state=NORMAL)
            if  L_LRON:
                ##send("ll:1;")
                ##send("lr:1;")
                print ("ll:1;")
                time.sleep(0.5)
                ##send("ll:0;")
                ##send("lr:0;")
                print ("ll:0;")
        elif (key=="x") and L_LRON:
            L_LRON = False
            Test_Canvas.itemconfig("L_dir", state=NORMAL)
            Test_Canvas.itemconfig("L_left", state=HIDDEN)
            Test_Canvas.itemconfig("L_dir2", state=NORMAL)
            Test_Canvas.itemconfig("L_right", state=HIDDEN)
            if not L_LRON:
                ##send("ll:0;")
                ##send("lr:0;")
                print ("ll:0;")
            #Frontales
        elif (key=="f") and not L_frontON:
            L_frontON = True
            Test_Canvas.itemconfig("L_F", state=HIDDEN)
            Test_Canvas.itemconfig("L_F", state=HIDDEN)
            Test_Canvas.itemconfig("L_f", state=NORMAL)
            Test_Canvas.itemconfig("L_f2", state=NORMAL)
            ##send("lf:1;")
            print ("lf:1;")
        elif (key=="f") and L_frontON:
            L_frontON = False
            Test_Canvas.itemconfig("L_F", state=NORMAL)
            Test_Canvas.itemconfig("L_F", state=NORMAL)
            Test_Canvas.itemconfig("L_f", state=HIDDEN)
            Test_Canvas.itemconfig("L_f2", state=HIDDEN)
            ##send("lf:0;")
            print ("lf:0;")

        
    Test.bind("<KeyPress>", Car_Control)

    def release_Control(event):
        key = event.char
        global right, left, gas, NumGas,NumGas_Re, reverseON
        #Control de direccion
        if (key == "a") or (key == "d") and left or right:
            left = False
            right = False
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("none", state=NORMAL)
            send("dir:0;")
        #Control de Reversa
        elif (key == "w") and gas and reverseON:
            gas = True
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            Test_Canvas.itemconfig("L_s", state=NORMAL)
            while NumGas_Re != 0:
                time.sleep(1)
                NumGas_Re += 100
                ##send("pwm:"+str(NumGas_Re)+";")
                print ("pwm:"+str(NumGas_Re)+";")
                
        #Control Hacia adelante
        elif (key == "w") and gas:
            gas = True
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            Test_Canvas.itemconfig("L_s", state=NORMAL)
            while NumGas != 0:
                time.sleep(1)
                NumGas -= 100
                ##send("pwm:"+str(NumGas)+";")
                print ("pwm:"+str(NumGas)+";")

    Test.bind("<KeyRelease>", release_Control)
            
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
