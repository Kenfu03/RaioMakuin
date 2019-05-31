InfoPer="""
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
#Global
left = False
right = False
gas = True
reverseON = False
L_rightON = False
L_leftON = False
L_frontON = False
L_LRON = False
stopON = False
NumGas=0
NumGas_Re=0
num_bar = 0

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
InicioBackup=cargarImg("backup.png")
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
#__Se crea un fondo
    Backup_aboutImg =cargarImg('backup_about.png')
    Backup_about=Label(About_Canvas, image=Backup_aboutImg)
    Backup_about.photo=Backup_aboutImg
    Backup_about.place(x=0,y=0)
#__Se carga una imagen
    PersonalImg =cargarImg('Personalimg.gif')
    Personal=Label(About_Canvas, image=PersonalImg,bg='white')
    Personal.photo=PersonalImg
    Personal.place(x=10,y=60)
    ImgCris = cargarImg('fotoCris.gif')
    Personal1 = Label(About_Canvas, image=ImgCris, bg='white')
    Personal1.photo = ImgCris
    Personal1.place(x=230, y=60)
#__Se crea un label con informacion crucial
    Label_about=Label(About_Canvas, text=InfoPer ,font= ('Britannic Bold',16), fg='white', bg='#040521')
    Label_about.place(x=500,y=10)
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
        #Globales
        global left, right, gas, NumGas,NumGas_Re, reverseON, L_rightON, L_leftON, L_frontON, L_LRON, stopON
        

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
            progress_up(NumGas)
            ##send("pwm:"+str(NumGas_Re)+";")
            print ("pwm:"+str(NumGas_Re)+";")

            Thread_gasdown_reverse.stop()
            
            #Hacia adelante
        elif (key == "w") and gas:
            gas = True
            time.sleep(1)
            NumGas += 100
            Test_Canvas.itemconfig("L_s2", state=HIDDEN)
            Test_Canvas.itemconfig("L_s", state=HIDDEN)
            progress_up(NumGas)
            ##send("pwm:"+str(NumGas)+";")
            print ("pwm:"+str(NumGas)+";")

            Thread_gasdown.stop()

        #Control boton de stop
        elif (key == "s") and not stopON:
            stopON = True
            ##send("pwm:0;")
            print ("pwm:0;")
            
            #Desactivar reversa
        elif (key == "s") and stopON:
            stopON = False
            
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
            def gasdown_reverse():
                while NumGas_Re != 0:
                    pressingW = False
                    time.sleep(1)
                    NumGas_Re += 100
                    ##send("pwm:"+str(NumGas_Re)+";")
                    print ("pwm:"+str(NumGas_Re)+";")
                    progress_down(NumGas)

                    Thread_gasdown_reverse = threading.Thread(target=wait)
                    Thread_gasdown_reverse.start()
                    
                
        #Control Hacia adelante
        elif (key == "w") and gas:
            gas = True
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            Test_Canvas.itemconfig("L_s", state=NORMAL)
            def gasdown():
                while NumGas != 0 and not pressingW:
                    pressingW = False
                    time.sleep(1)
                    NumGas -= 100
                    ##send("pwm:"+str(NumGas)+";")
                    print ("pwm:"+str(NumGas)+";")
                    
                    Thread_gasdown = threading.Thread(target=gasdown)
                    Thread_gasdown.start()

    Test.bind("<KeyRelease>", release_Control)
            
#__Se crean labels con los datos inportantes
    Test_Canvas.create_text(485, 15, text="Batery Level" ,font= ('Britannic Bold',14), fill="red")
  
    Test_Canvas.create_text(45, 330, text="Pwm\nVelocity" ,font= ('Britannic Bold',14), fill = "red")

#Se crea una funcion para crear una barra de progreso, para cuando se esta acelerando
    style = ttk.Style()
    style.theme_use('default')
    style.configure("darkblue.Vertical.TProgressbar", background='darkblue') 
    progressbar1 = Progressbar(Test, length=200, style='darkblue.Vertical.TProgressbar', orient= tk.VERTICAL, maximum=1000) 
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

Btn_mute=Button(Principal_Canvas,text='Mute',font= ('Britannic Bold',12),command=off,bg='#040521',fg='#8c9fc5')
Btn_mute.place(x=483,y=490)

Btn_QuitImg= cargarImg("Btn_Quit.png")
Btn_Quit=Button(Principal_Canvas, image=Btn_QuitImg, command=root.destroy, bg='#040521')
Btn_Quit.place(x=10,y=480)

Btn_PlayMusic=Button(Principal_Canvas, text='Music',font= ('Britannic Bold',12), command=play1,bg='#040521', fg='#8c9fc5')
Btn_PlayMusic.place(x=480,y=530)

Btn_Credits= cargarImg("Btn_Credits.png")
Btn_About = Button(Principal_Canvas,image=Btn_Credits,command=ventana_about,bg='#040521')
Btn_About.place(x=850,y=480)

Btn_Pilots= cargarImg("Btn_Pilots.png")
Btn_Puntajes = Button(Principal_Canvas,image=Btn_Pilots,command=ventana_Pilots,bg='#040521')
Btn_Puntajes.place(x=10,y=10)

Btn_Test= cargarImg("Btn_Test.png")
Btn_Test_Driver = Button(Principal_Canvas,image=Btn_Test,command=ventana_TestDrive,bg='#040521')
Btn_Test_Driver.place(x=850,y=10)

root.mainloop()
