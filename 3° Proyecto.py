# __________/BIBLIOTECAS
import tkinter as tk  # Se importa tkinter
from tkinter import *  # Tk(), Label, Canvas, Photo
from threading import Thread  # p.start()
import os  # ruta = os.path.join('')
import time  # time.sleep(x)
from tkinter import messagebox  # AskYesNo ()
from WiFiClient import NodeMCU  # Biblioteca para conectar con el carro
from pygame import mixer

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
# ______________________________________________
# Control del carrito por NodeMCU
Carrito = NodeMCU()
Carrito.start()
mixer.init()

# ______________________________________________
# Global
# global left, right, NumGas, NumGas_Re, reverseON, L_rightON, L_leftON, L_backON, GasON, L_DirON, pressTecla, \
#    L_frontON, front_press, left_press, right_press, Dir_press, reverse_press, pressS, num_bar
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
ListaPilotos = []
ListaCarros = []


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
root.minsize(1000, 626)
root.resizable(width=NO, height=NO)

# __________/Se crea un lienzo para objetos
Principal_Canvas = Canvas(root, width=1000, height=626, bg='#2e2e2e')
Principal_Canvas.place(x=0, y=0)

# __________/Cargar una imagen
InicioBackup = cargarImg("backup.png")
Principal_Canvas.create_image(0, 0, image=InicioBackup, anchor=NW)

# _________/Se crea la funcion que ejecuta la cancion de fondo
Play = Thread(target=Song1, args=())
Play.start()


# Funcion para salir de la aplicacion
def quitApp():
    mixer.music.stop()
    root.destroy()


# Imagen para los botones de Atras de todas las ventanas
Btn_AtrasImg = cargarImg('Btn_Atras.png')

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
    about.minsize(1000, 626)
    about.resizable(width=NO, height=NO)
    # __Se crea un canvas
    About_Canvas = Canvas(about, width=1000, height=626, bg='#2d2d2e')
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
    Label_about = Label(About_Canvas, text=InfoPer, font=('Britannic Bold', 16), fg='white', bg='#2d2d2e')
    Label_about.place(x=500, y=10)

    # __Se crea una funcion para volver a la pantalla principal
    def atras_about():
        global pausa
        pausa = True
        about.destroy()
        root.deiconify()

    Btn_Atras_about = Button(About_Canvas, image=Btn_AtrasImg, command=atras_about, bg='#2d2d2e')
    Btn_Atras_about.place(x=10, y=570)

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
    Pilots_Canvas = Canvas(Pilots, width=900, height=700, bg='#2d2d2e')
    scroll_y = Scrollbar(Pilots, orient='vertical', command=Pilots_Canvas.yview)
    Pilots_frame = Frame(Pilots_Canvas)

    BackupCars = cargarImg('backup_about.png')
    Pilots_Canvas.create_image(0, 0, image=BackupCars, anchor=NW)

    BackupCarsInverso = cargarImg('backupInverso.png')
    Pilots_Canvas.create_image(0, 626, image=BackupCarsInverso, anchor=NW)

    listaframes = []
    for i in range(0, 10):  # Se hace 10 frames para colocar cada boton en un frame diferente
        listaframes.append(Frame(Pilots_Canvas))

    # Se cargan las imagenes
    listapng = ["jonathan.png", "joseph.png", "jotaro.png", "josuke.png", "giorno.png", "dio.png", "kira.png",
                "bruno.png", "polnareff.png", "caesar.png"]
    listaimg = []
    for nombre in listapng:  # Se cargan las imagenes a una lista llamada listaimg
        listaimg.append(cargarImg(nombre))
    global ListaPilotos  # Se crea una lista la cual contendra todos los datos de los pilotos para poder ser manejada despues
    ListaY = [40, 145, 250, 355, 460, 565, 670, 775, 880, 985]
    arch1 = open('Pilotos.txt', 'r+')
    for i in range(0, 10):  # Se abre el archivo con los datos de lo pilotos y se meten dentro de la ListaPilotos
        ListaPilotos.append(arch1.readline().split('@'))
    # Se calculan los RGP de los pilotos y se agregan a la lista de cada piloto
    for i in range(0, 10):
        ListaPilotos[i].append(int(((int(ListaPilotos[i][5]) + int(ListaPilotos[i][6])) /(int(ListaPilotos[i][4]) - int(ListaPilotos[i][7])) * 100)))
    for i in range(0, 10):
        ListaPilotos[i].append(int(((int(ListaPilotos[i][5])) / (int(ListaPilotos[i][4]) -int(ListaPilotos[i][7])) * 100)))
    #Se añade a la lista la posiciones en Y a la que estara cada piloto
    for i in range(0, 10):
        ListaPilotos[i].append(ListaY[i])
    #Se revisa el ultimo dato de cada lista de pilotos para ver a que lista se añadira la imagen de cada piloto
    for i in range(0, 10):
        if ListaPilotos[i][9] == '0\n':
            ListaPilotos[i].append(listaimg[0])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '1\n':
            ListaPilotos[i].append(listaimg[1])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '2\n':
            ListaPilotos[i].append(listaimg[2])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '3\n':
            ListaPilotos[i].append(listaimg[3])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '4\n':
            ListaPilotos[i].append(listaimg[4])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '5\n':
            ListaPilotos[i].append(listaimg[5])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '6\n':
            ListaPilotos[i].append(listaimg[6])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '7\n':
            ListaPilotos[i].append(listaimg[7])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '8\n':
            ListaPilotos[i].append(listaimg[8])
    for i in range(0, 10):
        if ListaPilotos[i][9] == '9\n':
            ListaPilotos[i].append(listaimg[9])
    # Se crean listas vacias para tener control sobre todos los objetos creados en pantalla
    listatext = []
    listanom = []
    listaedad = []
    listatmp = []
    listargp = []
    listarep = []
    listacomp = []
    listanacion = []
    #Se crean las posiciones de los pilotos
    for i in range(0, 10):
        listatext.append(Pilots_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))
    #Se crean los nombres de las caracteristicas a mostrar en el canvas
    Nombre = Pilots_Canvas.create_text(182, 2, anchor=NW, text='Nombre/Edad', font=('Britannic Bold', 16),fill="#fdf2b4")
    Temp = Pilots_Canvas.create_text(380, 2, anchor=NW, text='Temporada', font=('Britannic Bold', 16),fill="#fdf2b4")
    RGP = Pilots_Canvas.create_text(500, 2, anchor=NW, text='RGP', font=('Britannic Bold', 16),fill="#fdf2b4")
    REP = Pilots_Canvas.create_text(555, 2, anchor=NW, text='REP', font=('Britannic Bold', 16),fill="#fdf2b4")
    Comp = Pilots_Canvas.create_text(610, 2, anchor=NW, text='Competencias', font=('Britannic Bold', 16),fill="#fdf2b4")

    def pilotos():
        '''
        Entradas : Ninguna
        Salidas: Crea en el canvas textos con la informacion de cada piloto y lo añade a una lista
        Restricciones: Ninguna
        '''
        for i in range(0, 10): #Ciclo que coloca el nombre del piloto en la pantalla y lo mete a una lista
            listanom.append(Pilots_Canvas.create_text(182, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][0],
                                                      font=('Britannic Bold', 16),fill='white'))
        for i in range(0, 10): #Ciclo que coloca la nacionalidad del piloto en la pantalla y lo mete a una lista
            listanacion.append(
                Pilots_Canvas.create_text(182, ListaPilotos[i][12] + 50, anchor=NW, text=ListaPilotos[i][2],
                                          font=('Britannic Bold', 16),fill='white'))
        for i in range(0, 10): #Ciclo que coloca la edad del piloto en la pantalla y lo mete a una lista
            listaedad.append(
                Pilots_Canvas.create_text(182, ListaPilotos[i][12] + 25, anchor=NW, text=ListaPilotos[i][1],
                                          font=('Britannic Bold', 16),fill='white'))
        for i in range(0, 10): #Ciclo que coloca la temporada del piloto en la pantalla y lo mete a una lista
            listatmp.append(Pilots_Canvas.create_text(380, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][3],
                                                      font=('Britannic Bold', 16),fill='white'))
        for i in range(0, 10): #Ciclo que coloca el RGP del piloto en la pantalla y lo mete a una lista
            listargp.append(Pilots_Canvas.create_text(500, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][10],
                                                      font=('Britannic Bold', 16),fill='white'))
        for i in range(0, 10): #Ciclo que coloca el REP del piloto en la pantalla y lo mete a una lista
            listarep.append(Pilots_Canvas.create_text(555, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][11],
                                                      font=('Britannic Bold', 16),fill='white'))
        for i in range(0, 10): #Ciclo que coloca la cantidad de competencias del piloto en la pantalla y lo mete a una lista
            listacomp.append(Pilots_Canvas.create_text(610, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][4],
                                                       font=('Britannic Bold', 16),fill='white'))

    def nuevoRGP(): #Funcion que vuelve a calcular el RGP y REP y lo reemplaza en la lista de pilotos
        for i in range(0, 10):
            ListaPilotos[i][10] = (int(((int(ListaPilotos[i][5]) + int(ListaPilotos[i][6])) / (
                    int(ListaPilotos[i][4]) - int(ListaPilotos[i][7])) * 100)))
        for i in range(0, 10):
            ListaPilotos[i][11] = (
                int(((int(ListaPilotos[i][5])) / (int(ListaPilotos[i][4]) - int(ListaPilotos[i][7])) * 100)))

    def borrar(k):
        '''
        Entrada: k, si es True, borra las posiciones, si es False, no
        Salidas: Borra todos los datos que se mostraban en la pantalla
        Restricciones: k debe ser booleano
        '''
        if k:
            for texts in listatext:# Ciclo que borra las posiciones
                Pilots_Canvas.delete(texts)
        for nacion in listanacion:# Ciclo que borra la nacionalidad mostradas
            Pilots_Canvas.delete(nacion)# Se borran del canvas los elementos dentro de la lista nacion
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
        print(listabotones2)
        for btn2 in listabotones2:
            btn2.destroy()
    def mayor_RGP():
        '''
        Descripcion: Ordena a los pilotos por de mayor a menor RGP
        Entradas: No tiene
        Salidas: llama a la funcion que borra las datos mostrados, compara los RGP y los ordena de mayor a menor,
        luego llama a las funciones que vuelven a mostrar los datos
        Restricciones: No tiene
        '''
        global ListaPilotos
        borrar(True)
        ListaRGP = burbuja(ListaPilotos, 10) #Se llama a la funcion burbuja para que ordene las listas
        ListaPilotos = ListaRGP[::-1]
        for i in range(0, 10): #Ciclo que asigna la nueva altura a la que se pondran los datos de los pilotos
            ListaPilotos[i][12] = ListaY[i] #Lista de alturas
            ListaPilotos[i][8] = str(i) #Se actualiza el numero que dice el orden en el que esta cada piloto
        for i in range(0, 10): #Ciclo que coloca las posiciones
            listatext.append(
                Pilots_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))
        pilotos()
        botones()

    def menor_RGP():
        '''
        Descripcion: Ordena a los pilotos por de mayor a menor RGP
        Entradas: No tiene
        Salidas: llama a la funcion que borra las datos mostrados, compara los RGP y los ordena de menor a mayor,
        luego llama a las funciones que vuelven a mostrar los datos
        Restricciones: No tiene
        '''
        global ListaPilotos
        borrar(True)
        ListaRGP = burbuja(ListaPilotos, 10)
        ListaPilotos = ListaRGP
        listatemporal = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(0, 10):
            ListaPilotos[i][12] = ListaY[i]
            ListaPilotos[i][8] = str(i)
        for i in range(0, 10):
            listatext.append(
                Pilots_Canvas.create_text(5, ListaY[i], anchor=NW, text=listatemporal[i], font=('Britannic Bold', 16)))
        pilotos()
        botones()

    def mayor_REP():
        '''
        Descripcion: Ordena a los pilotos por de mayor a mayor REP
        Entradas: No tiene
        Salidas: llama a la funcion que borra las datos mostrados, compara los REP y los ordena de mayor a menor,
        luego llama a las funciones que vuelven a mostrar los datos
        Restricciones: No tiene
        '''
        global ListaPilotos
        borrar(True)
        ListaREP = burbuja(ListaPilotos, 11)
        ListaPilotos = ListaREP[::-1]
        for i in range(0, 10):
            ListaPilotos[i][12] = ListaY[i]
            ListaPilotos[i][8] = str(i)
        for i in range(0, 10):
            listatext.append(
                Pilots_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))
        pilotos()
        botones()

    def menor_REP():
        '''
        Descripcion: Ordena a los pilotos por de maenor a mayor REP
        Entradas: No tiene
        Salidas: llama a la funcion que borra las datos mostrados, compara los RGP y los ordena de menor a mayor,
        luego llama a las funciones que vuelven a mostrar los datos
        Restricciones: No tiene
        '''
        global ListaPilotos
        borrar(True)
        ListaREP = burbuja(ListaPilotos, 11)
        ListaPilotos = ListaREP
        listatemporal = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(0, 10):
            ListaPilotos[i][12] = ListaY[i]
            ListaPilotos[i][8] = str(i)
        for i in range(0, 10):
            listatext.append(
                Pilots_Canvas.create_text(5, ListaY[i], anchor=NW, text=listatemporal[i], font=('Britannic Bold', 16)))
        pilotos()
        botones()

    def mod_strs(nuevo, cons, modo):
        '''
        Entradas: nuevo: Es el nuevo dato que sera reemplazado
                  cons: El numero que es constante en cada piloto
                  modo: string que indica que dato sera reemplazado
        Salidas: Se reemplaza en la lista de pilotos el dato
                 que pertenece a 'modo' con el nuevo
        Restricciones: nuevo debe ser un string, cons debe ser un numero
                     entero del 0 al 9
        '''
        global ListaPilotos
        if modo == 'Nombre': # Se revisa cual es la caracteristica que se va a modificar
            for i in range(0, 10):# Se encicla hasta encontrar el piloto que debe modificar
                if int(ListaPilotos[i][8]) == cons:
                    ListaPilotos[i][0] = nuevo # Modifica el dato que al piloto
                    messagebox.showinfo("Nombre", "Se cambio el nombre del\npiloto correctamente") # Informa que un
                    # dato ha sido editado
                    break
        if modo == 'Edad':
            for i in range(0, 10):
                if int(ListaPilotos[i][8]) == cons:
                    ListaPilotos[i][1] = nuevo
                    messagebox.showinfo("Edad", "Se cambio la edad \ndel piloto correctamente")
                    break
        if modo == 'Nacionalidad':
            for i in range(0, 10):
                if int(ListaPilotos[i][8]) == cons:
                    ListaPilotos[i][2] = nuevo
                    messagebox.showinfo("Nacionalidad", "Se cambio la nacionalidad\ndel piloto correctamente")
                    break
        if modo == 'Temporada':
            for i in range(0, 10):
                if int(ListaPilotos[i][8]) == cons:
                    ListaPilotos[i][3] = nuevo
                    messagebox.showinfo("Temporada", "Se cambio la temporada\ndel piloto correctamente")
                    break

    def mod_nums(nuevo, cons, arch):
        '''
        Entradas: nuevo: Es el nuevo dato que sera reemplazado
                  cons: El numero que es constante en cada piloto
                  arch: string que indica que dato sera reemplazado
        Salidas: Se reemplaza en la lista de pilotos el dato
                 que pertenece a 'arch' con el nuevo
        Restricciones: nuevo y cons deben ser un numeros
        '''
        try:
            global ListaPilotos
            nuevo = int(nuevo) # Se convierte en entero la variable ingresada por el usuario, si da error, se
            #muestra un mensaje diciendo que nuevo debe ser entero
            if isinstance(nuevo, int):
                if arch == 'Competencias':# Se modifica la caracteristica de competencias del piloto
                    for i in range(0, 10):# Se encicla hasta encontrar el piloto que debe modificar
                        if int(ListaPilotos[i][8]) == cons:
                            ListaPilotos[i][4] = str(nuevo)#Convierte el nuevo numero a un string y lo mete de nuevo
                            # a la lista
                            messagebox.showinfo("Competencias","Se cambiaron las competencias\ndel piloto correctamente")
                            #muestra una caja de mensaje informando que se cambio correctamente
                            break
                if arch == 'Victorias':
                    for i in range(0, 10):
                        if int(ListaPilotos[i][8]) == cons:
                            ListaPilotos[i][5] = str(nuevo)
                            messagebox.showinfo("Victorias",
                                                "Se cambiaron las competencias\ndel piloto correctamente")
                            break
                if arch == 'Podio':
                    for i in range(0, 10):
                        if int(ListaPilotos[i][8]) == cons:
                            ListaPilotos[i][6] = str(nuevo)
                            messagebox.showinfo("Podio",
                                                "Se cambiaron los segundos y terceros\nlugar del piloto correctamente")
                            break
                if arch == 'Abandonos':
                    for i in range(0, 10):
                        if int(ListaPilotos[i][8]) == cons:
                            ListaPilotos[i][7] = str(nuevo)
                            messagebox.showinfo("Abandonos",
                                                "Se cambiaron los abandonos\ndel piloto correctamente")
                            break
        except:
            messagebox.showerror("Error", "Se debe ingresar un numero")

    #Se crean funciones para ser asignadas a cada boton
    def mod_jon():
        mod_pil(0, str(ListaPilotos[0][9])) #Se llama a la funcion con el numero fijo de cada piloto

    def mod_jsp():
        mod_pil(1, str(ListaPilotos[1][9]))

    def mod_jot():
        mod_pil(2, str(ListaPilotos[2][9]))

    def mod_jsk():
        mod_pil(3, str(ListaPilotos[3][9]))

    def mod_gio():
        mod_pil(4, str(ListaPilotos[4][9]))

    def mod_dio():
        mod_pil(5, str(ListaPilotos[5][9]))

    def mod_kra():
        mod_pil(6, str(ListaPilotos[6][9]))

    def mod_brn():
        mod_pil(7, str(ListaPilotos[7][9]))

    def mod_pol():
        mod_pil(8, str(ListaPilotos[8][9]))

    def mod_czs():
        mod_pil(9, str(ListaPilotos[9][9]))

    def mod_pil(num, arch):
        '''
        Descripcion: Ventana en la cual se editan se pueden editar los datos de los pilotos
        Entradas: num = el numero donde estan acomodados los botones
                  arch = el numero fijo de cada piloto
        Salidas: Crea una ventana con botones para editar los pilotos
        Restricciones: num y arch deben ser enteros
        '''
        Pilots.withdraw()
        EditGiorno = Toplevel()
        EditGiorno.title('Pilot')
        EditGiorno.minsize(900, 400)
        EditGiorno.resizable(width=NO, height=NO)
        Canvas_secundario = Canvas(EditGiorno, width=600, height=400, bg='blue')
        Canvas_secundario.place(x=0, y=0)
        Canvas_derecha = Canvas(EditGiorno, width=300, height=400, bg='pink')
        Canvas_derecha.place(x=600, y=0)
        listapng2 = ['jonathan2.png', 'joseph2.png', 'jotaro2.png', 'josuke2.png', 'giorno2.png', 'dio2.png',
                     'kira2.png','bruno2.png', 'polnareff2.png', 'caesar2.png'] #se crea una lista con el nombre de los png
        listaimg2 = []
        for png in listapng2:# Se carga iterativamente las imagenes a una lista
            listaimg2.append(cargarImg(png))
        print(num)
        global ListaPilotos
        #Se compara el string arch para ver que piloto se esta modificando
        #Cuando se encuentra el piloto que es, se crea una imagen del piloto en la pantalla
        if arch == '0\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[0])
        if arch == '1\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[1])
        if arch == '2\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[2])
        if arch == '3\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[3])
        if arch == '4\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[4])
        if arch == '5\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[5])
        if arch == '6\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[6])
        if arch == '7\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[7])
        if arch == '8\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[8])
        if arch == '9\n':
            Canvas_derecha.create_image(0, 0, anchor=NW, image=listaimg2[9])

        def volver():
            Pilots.deiconify()
            EditGiorno.destroy()
            borrar(False)
            nuevoRGP()
            pilotos()
            botones()
        #Se crean entrys para que el usuario pueda modificar
        E_nombre = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_nombre.place(x=25, y=80)
        E_edad = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_edad.place(x=200, y=80)
        E_nacion = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_nacion.place(x=375, y=80)
        E_temp = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_temp.place(x=25, y=170)
        E_comp = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_comp.place(x=200, y=170)
        E_vic = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_vic.place(x=375, y=170)
        E_sec = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_sec.place(x=25, y=260)
        E_aban = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_aban.place(x=200, y=260)
        #Se crean botones para modificar cada caracteristica
        Button(Canvas_secundario, text='Atras', font=('Britannic Bold', 14), command=volver, bg='black',
               fg='white').place(x=25, y=0)
        Button(Canvas_secundario, text='Nombre', font=('Britannic Bold', 14),
               command=lambda: mod_strs(str(E_nombre.get()), num, 'Nombre'), bg='black', fg='white').place(x=25, y=40)
        Button(Canvas_secundario, text='Edad', font=('Britannic Bold', 14),
               command=lambda: mod_strs(E_edad.get(), num, 'Edad'), bg='black', fg='white').place(x=200, y=40)
        Button(Canvas_secundario, text='Nacionalidad', font=('Britannic Bold', 14),
               command=lambda: mod_strs(E_nacion.get(), num, 'Nacionalidad'), bg='black', fg='white').place(x=375, y=40)
        Button(Canvas_secundario, text='Temporada', font=('Britannic Bold', 14),
               command=lambda: mod_strs(E_temp.get(), num, 'Temporada'), bg='black', fg='white').place(x=25, y=130)
        Button(Canvas_secundario, text='Competencia', font=('Britannic Bold', 14),
               command=lambda: mod_nums(E_comp.get(), num, 'Competencia'), bg='black', fg='white').place(x=200, y=130)
        Button(Canvas_secundario, text='Victorias', font=('Britannic Bold', 14),
               command=lambda: mod_nums(E_vic.get(), num, 'Victorias'), bg='black', fg='white').place(x=375, y=130)
        Button(Canvas_secundario, text='Podio', font=('Britannic Bold', 14),
               command=lambda: mod_nums(E_sec.get(), num, 'Podio'), bg='black', fg='white').place(x=25, y=220)
        Button(Canvas_secundario, text='Abandonos', font=('Britannic Bold', 14),
               command=lambda: mod_nums(E_aban.get(), num, 'Abandonos'), bg='black', fg='white').place(x=200, y=220)
        EditGiorno.mainloop()

    def burbuja(Lista, k):
        '''
        Descripcion: Funcion que acomoda una lista de listas por un elemento
                     sub k dentro de cada lista
        Entradas: Lista = una lista de listas, k = un numero
        Salidas: Devuelve la Lista de mayor a menor por el elemento k
        Restricciones: Lista debe ser una lista de listas
        '''
        return burbuja_aux(Lista, 0, 0, len(Lista), False, k)

    def burbuja_aux(Lista, i, j, n, Swap, k):
        if i == n: # Condicion de terminacion
            return Lista
        if j == n - i - 1:
            if Swap:
                return burbuja_aux(Lista, i + 1, 0, n, False, k)
            else:
                return Lista
        if Lista[j][k] > Lista[j + 1][k]: # Se comparan los elementos de la lista [j][k]
        #con [j+1][k], y entre ambos, se coloca la lista que contiene al menor k de primero
            Tmp = Lista[j]
            Lista[j] = Lista[j + 1]
            Lista[j + 1] = Tmp
            return burbuja_aux(Lista, i, j + 1, n, True, k)
        else:
            return burbuja_aux(Lista, i, j + 1, n, Swap, k)

    def atras_Pilots():
        '''
        Entradas: No tiene
        Salidas: guarda de nuevo los datos de los pilotos en el .txt y luego
                 vuelve al menu principal
        Restricciones: No tiene
        '''
        with open("Pilotos.txt", "w") as f:
            # Se abre el archivo .txt para editarlo
            listita = []
            print(len(ListaPilotos[1][9]))
            for i in range(0, 10): # Se hace una lista con los primeros 9 datos de todos los pilotos unidos por @
                listita.append('@'.join(ListaPilotos[i][0:10]))
            print(listita)
            for strs in listita:# Luego se escribe por linea del txt la informacion de un piloto hasta acabarse los pilotos
                f.write(strs)
        global pausa
        pausa = True
        Pilots.destroy()
        root.deiconify()
    listabotones2 = [0, 1, 2, 3,4]
    listatext2 = ['Atras', 'Mayor RGP', 'Menor RGP', 'Mayor REP', 'Menor REP']
    listacomandos = [atras_Pilots, mayor_RGP, menor_RGP, mayor_REP, menor_REP]
    listabtn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    listacomandos2 = [mod_jon, mod_jsp, mod_jot, mod_jsk, mod_gio, mod_dio, mod_kra, mod_brn, mod_pol, mod_czs]

    def botones():
        '''
        Descripcion: Crea los botones de los pilotos en un frame distino por boton, y carga la
        imagen del boton desde la lista de los pilotos. Tambien se crean los botones de ordenamiento
        Entradas: No tiene
        Salidas: Crea botones, los muestra en pantalla y los agrega a una lista
        Restricciones: No tiene
        '''
        for i in range(0, 10):# Crea los botones de los pilotos con su imagen en un frame distinto por ciclo
            listabtn[i] = (Button(listaframes[i], command=listacomandos2[i], image=ListaPilotos[i][13]))
            listabtn[i].pack()
        for i in range(0, 5):
            listabotones2[i] = (
                Button(Pilots_frame, text=listatext2[i], font=('Britannic Bold', 14), command=listacomandos[i]
                       ,bg='#2d2d2e', fg="#fdf2b4"))
            listabotones2[i].pack()

    for i in range(0, 10):# Crea una ventana por piloto en el canvas
        Pilots_Canvas.create_window(75, ListaPilotos[i][12], anchor=NW, window=listaframes[i])

    Pilots_Canvas.create_window(780, 30, anchor=NW, window=Pilots_frame) #Se crea una ventana con los botones de ordenamiento
    Pilots_Canvas.update_idletasks()# Se hace update al canvas para que cargue las nuevas windows creadas
    Pilots_Canvas.configure(scrollregion=(0, 0, 500, 1100), yscrollcommand=scroll_y.set)# Se asigna una region de scroll
    #para el canvas y se da como comando de scroll al scrollbar scroll_y.set
    Pilots_Canvas.pack(fill=BOTH, expand=True, side=LEFT)
    scroll_y.pack(fill=Y, side=RIGHT)
    pilotos()
    botones()
    Pilots.mainloop()

#______________/Ventana para escoger piloto
def ventana_esc_pil():
    root.withdraw()
    EscPil = Toplevel()
    EscPil.title('Piloto')
    EscPil.minsize(700,250)
    EscPil.resizable(width=NO, height=NO)
    pil_Canvas = Canvas(EscPil, width=1000, height=626, bg='#2d2d2e')
    pil_Canvas.place(x=0,y=0)
    global ListaPilotos
    global ListaCarros
    listabtn = [0,1,2,3,4,5,6,7,8,9]
    listaframes = []
    for i in range(0,10):
        listaframes.append(Frame(EscPil))
    print(ListaPilotos)
    def atras():
        EscPil.destroy()
    def pil0():
        ventana_esc_carro(ListaPilotos[0][9])
    def pil1():
        ventana_esc_carro(ListaPilotos[1][9])
    def pil2():
        ventana_esc_carro(ListaPilotos[2][9])
    def pil3():
        ventana_esc_carro(ListaPilotos[3][9])
    def pil4():
        ventana_esc_carro(ListaPilotos[4][9])
    def pil5():
        ventana_esc_carro(ListaPilotos[5][9])
    def pil6():
        ventana_esc_carro(ListaPilotos[6][9])
    def pil7():
        ventana_esc_carro(ListaPilotos[7][9])
    def pil8():
        ventana_esc_carro(ListaPilotos[8][9])
    def pil9():
        ventana_esc_carro(ListaPilotos[9][9])
    listaX = [64,182,300,418,536]
    listacomandos = [pil0,pil1,pil2,pil3,pil4,pil5,pil6,pil7,pil8,pil9]
    for i in range(0, 10):  # Crea los botones de los pilotos con su imagen en un frame distinto por ciclo
        listabtn[i] = (Button(listaframes[i], command = listacomandos[i],image=ListaPilotos[i][13]))
        listabtn[i].pack()
    for i in range(0, 5):# Crea una ventana por piloto en el canvas
        pil_Canvas.create_window(listaX[i], 20, anchor=NW, window=listaframes[i])
    for i in range(0, 5):# Crea una ventana por piloto en el canvas
        pil_Canvas.create_window(listaX[i], 120, anchor=NW, window=listaframes[i+5])
    messagebox.showinfo("Seleccionar Piloto",
                        "Seleccione el piloto con\nel que se realizará el test drive")


    def ventana_esc_carro(piloto):
        EscCar = Toplevel()
        EscCar.title('Carros')
        EscCar.minsize(700, 250)
        EscCar.resizable(width=NO, height=NO)
        pil2_Canvas = Canvas(EscCar, width=700, height=250, bg='#2d2d2e')
        pil2_Canvas.place(x=0, y=0)
        atras()
        listabtn2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        listaframes2 = []
        print(ListaCarros)
        for i in range(0, 10):
            listaframes2.append(Frame(EscCar))

        def car0():
            if ListaCarros[0][8] == 'Descargado' or ListaCarros[0][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[0][14],piloto)
        def car1():
            if ListaCarros[1][8] == 'Descargado' or ListaCarros[1][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[1][14],piloto)
        def car2():
            if ListaCarros[2][8] == 'Descargado' or ListaCarros[2][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[2][14],piloto)
        def car3():
            if ListaCarros[3][8] == 'Descargado' or ListaCarros[3][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[3][14],piloto)
        def car4():
            if ListaCarros[4][8] == 'Descargado' or ListaCarros[4][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[4][14],piloto)
        def car5():
            if ListaCarros[5][8] == 'Descargado' or ListaCarros[5][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[5][14],piloto)
        def car6():
            if ListaCarros[6][8] == 'Descargado' or ListaCarros[6][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[6][14],piloto)
        def car7():
            if ListaCarros[7][8] == 'Descargado' or ListaCarros[7][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[7][14],piloto)
        def car8():
            if ListaCarros[8][8] == 'Descargado' or ListaCarros[8][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[8][14],piloto)
        def car9():
            if ListaCarros[9][8] == 'Descargado' or ListaCarros[9][8] == 'Reparacion':
                messagebox.showerror("Auto Descargado",
                                     "El auto seleccionado se\nencuentra descargado en el momento")
            else:
                ventana_TestDrive(ListaCarros[9][14],piloto)

        listaX = [64, 182, 300, 418, 536]
        listacomandos2 = [car0, car1,car2, car3, car4, car5, car6,car7, car8, car9]
        for i in range(0, 10):  # Crea los botones de los pilotos con su imagen en un frame distinto por ciclo
            listabtn2[i] = (Button(listaframes2[i], command=listacomandos2[i], image=ListaCarros[i][16]))
            listabtn2[i].pack()
        for i in range(0, 5):  # Crea una ventana por piloto en el canvas
            pil2_Canvas.create_window(listaX[i], 20, anchor=NW, window=listaframes2[i])
        for i in range(0, 5):  # Crea una ventana por piloto en el canvas
            pil2_Canvas.create_window(listaX[i], 120, anchor=NW, window=listaframes2[i + 5])
        messagebox.showinfo("Seleccionar Piloto",
                            "Seleccione el piloto con\nel que se realizará el test drive")
        EscCar.mainloop()

    pil_Canvas.update_idletasks()
    EscPil.mainloop()

# _____________/Ventana Carros
def ventana_Carros():
    # Esconder la pantalla principal sin destruirla
    root.withdraw()
    # Pantalla Carros
    Carros = Toplevel()
    Carros.title('Vehiculos')
    Carros.minsize(1000, 626)
    Carros.resizable(width=NO, height=NO)
    # __Se crea un canvas
    Carros_Canvas = Canvas(Carros, width=1000, height=626, bg='#2d2d2e')
    # __Se carga una imagen de fondo
    BackupCars = cargarImg('backup_about.png')
    Carros_Canvas.create_image(0, 0, image=BackupCars, anchor=NW)

    BackupCarsInverso = cargarImg('backupInverso.png')
    Carros_Canvas.create_image(0, 626, image=BackupCarsInverso, anchor=NW)

    # __Se crea un canvas y un scrollbar
    scrolly = Scrollbar(Carros, orient='vertical', command=Carros_Canvas.yview)
    Cars_frame = Frame(Carros_Canvas)
    listaframes = []
    for i in range(0, 10):
        listaframes.append(Frame(Carros_Canvas))

    listacarrospng = ["car0.png", "car1.png", "car2.png", "car3.png", "car4.png", "car5.png", "car6.png",
                      "car7.png", "car8.png", "car9.png"]
    listacarrosImg = []

    for carImg in listacarrospng:
        listacarrosImg.append(cargarImg(carImg))

    global ListaCarros
    ListaY = [60, 175, 290, 405, 520, 635, 750, 865, 980, 1095]

    # __Se abre el archivo de texto con la info. de los carros
    archCars = open('Carros.txt', 'r+')
    for i in range(0, 10):
        ListaCarros.append(archCars.readline().split('@'))

    # Se cargan los datos juntos a su carro
    for i in range(0, 10):
        ListaCarros[i].append(ListaY[i])

    for i in range(0, 10):
        ListaCarros[i].append(listacarrosImg[i])

    listatext = []
    listacar = []
    listapais = []
    listamarca = []
    listamodelo = []
    listatemp = []
    listabaterias = []
    listabaterias2 = []
    listapilas = []
    listapilas2 = []
    listaestado = []
    listacarac = []
    listacarac2 = []
    listacarac3 = []
    listaeficiencia = []
    for i in range(0, 10):
        listatext.append(Carros_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))

    CarImg = Carros_Canvas.create_text(182, 2, anchor=NW, text='Marca\nModelo', font=('Britannic Bold', 16),fill="#fdf2b4")
    TempYPais = Carros_Canvas.create_text(300, 2, anchor=NW, text='Temporada\nPais', font=('Britannic Bold', 16),fill="#fdf2b4")
    Baterias = Carros_Canvas.create_text(450, 2, anchor=NW, text='Baterias\nPilas', font=('Britannic Bold', 16),fill="#fdf2b4")
    Caracteristicas = Carros_Canvas.create_text(565, 2, anchor=NW, text='Pw Motores\nSensores,  Peso', font=('Britannic Bold', 16),fill="#fdf2b4")
    Estado = Carros_Canvas.create_text(745, 2, anchor=NW, text='Estado', font=('Britannic Bold', 16),fill="#fdf2b4")
    Eficiencia = Carros_Canvas.create_text(880, 2, anchor=NW, text='Eficiencia', font=('Britannic Bold', 16),fill="#fdf2b4")
    def F_Carros():
        print(ListaCarros)
        for i in range(0, 10):
            listacar.append(Carros_Canvas.create_image(10, ListaCarros[i][15], image=ListaCarros[i][16], anchor=NW))
        for i in range(0, 10):
            listamarca.append(Carros_Canvas.create_text(182, ListaCarros[i][15], anchor=NW, text=ListaCarros[i][0],font=('Britannic Bold', 16), fill="white"))
        for i in range(0, 10):
            listamodelo.append(Carros_Canvas.create_text(182, ListaCarros[i][15] + 25, anchor=NW, text=ListaCarros[i][1],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listapais.append(Carros_Canvas.create_text(300, ListaCarros[i][15] + 25, anchor=NW, text=ListaCarros[i][2],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listatemp.append(Carros_Canvas.create_text(300, ListaCarros[i][15], anchor=NW, text=ListaCarros[i][3],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listabaterias.append(Carros_Canvas.create_text(450, ListaCarros[i][15], anchor=NW, text=ListaCarros[i][4],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listabaterias2.append(Carros_Canvas.create_text(450, ListaCarros[i][15] + 25, anchor=NW, text=ListaCarros[i][5],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listapilas.append(Carros_Canvas.create_text(500, ListaCarros[i][15], anchor=NW, text=ListaCarros[i][6],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listapilas2.append(Carros_Canvas.create_text(500, ListaCarros[i][15] + 25, anchor=NW, text=ListaCarros[i][7],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listaestado.append(Carros_Canvas.create_text(745, ListaCarros[i][15], anchor=NW, text=ListaCarros[i][8],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listacarac.append(Carros_Canvas.create_text(565, ListaCarros[i][15], anchor=NW, text=ListaCarros[i][9],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listacarac2.append(Carros_Canvas.create_text(565, ListaCarros[i][15] + 25, anchor=NW, text=ListaCarros[i][10],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listacarac3.append(Carros_Canvas.create_text(565, ListaCarros[i][15] + 50, anchor=NW, text=ListaCarros[i][11],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listaeficiencia.append(Carros_Canvas.create_text(880, ListaCarros[i][15], anchor=NW, text=ListaCarros[i][12],font=('Britannic Bold', 16),fill="white"))

    def borrarCars(Fa_Tr):
        if Fa_Tr:
            for texts in listatext:
                Carros_Canvas.delete(texts)
        for cars in listacar:
            Carros_Canvas.delete(cars)
        for marca in listamarca:
            Carros_Canvas.delete(marca)
        for model in listamodelo:
            Carros_Canvas.delete(model)
        for pais in listapais:
            Carros_Canvas.delete(pais)
        for temp in listatemp:
            Carros_Canvas.delete(temp)
        for bat in listabaterias:
            Carros_Canvas.delete(bat)
        for bat2 in listabaterias2:
            Carros_Canvas.delete(bat2)
        for pil in listapilas:
            Carros_Canvas.delete(pil)
        for pil2 in listapilas2:
            Carros_Canvas.delete(pil2)
        for stat in listaestado:
            Carros_Canvas.delete(stat)
        for carac in listacarac:
            Carros_Canvas.delete(carac)
        for carac2 in listacarac2:
            Carros_Canvas.delete(carac2)
        for carac3 in listacarac3:
            Carros_Canvas.delete(carac3)
        for efi in listaeficiencia:
            Carros_Canvas.delete(efi)
        for btn in listaedit:
            btn.destroy()


    def mayor_Efi():
        global ListaCarros
        borrarCars(True)
        ListaEfi = burbujaCars(ListaCarros,12)
        ListaCarros = ListaEfi[::-1]
        print(ListaCarros[0])
        for i in range(0,10):
            ListaCarros[i][15] = ListaY[i]
            ListaCarros[i][13] = str(i)
        for i in range(0, 10):
            listatext.append(Carros_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))
        F_Carros()
        botonesCar()

    def menor_Efi():
        global ListaCarros
        borrarCars(True)
        print (ListaCarros)
        ListaEfi = burbujaCars(ListaCarros,12)
        ListaCarros = ListaEfi
        listatemporal = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(0, 10):
            ListaCarros[i][15] = ListaY[i]
            ListaCarros[i][13] = str(i)
        for i in range(0, 10):
            listatext.append(Carros_Canvas.create_text(5, ListaY[i], anchor=NW, text=listatemporal[i], font=('Britannic Bold', 16)))
        F_Carros()
        botonesCar()

    def burbujaCars(Lista, cord):
        return burbuja_auxCars(Lista, 0, 0, len(Lista), False, cord)

    def burbuja_auxCars(Lista, i, j, n, Swap, cord):
        if i == n:
            return Lista
        if j == n - i - 1:
            if Swap:
                return burbuja_auxCars(Lista, i + 1, 0, n, False, cord)
            else:
                return Lista
        if int(Lista[j][cord]) > int(Lista[j + 1][cord]):
            Tmp = Lista[j]
            Lista[j] = Lista[j + 1]
            Lista[j + 1] = Tmp
            return burbuja_auxCars(Lista, i, j + 1, n, True, cord)
        else:
            return burbuja_auxCars(Lista, i, j + 1, n, Swap, cord)

    def mod_strsCars(nuevo,cons,modo):
        global ListaCarros
        if modo == 'marca':
            for i in range(0,10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][0] = nuevo
                    break
        if modo == 'modelo':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][1] = nuevo
                    break
        if modo == 'temp':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][3] = nuevo
                    break
        if modo == 'pais':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][2] = nuevo
                    break
        if modo == 'baterias':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][4] = nuevo
                    break
        if modo == 'baterias2':
            for i in range(0,10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][5] = nuevo
                    break
        if modo == 'pilas':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][6] = nuevo
                    break
        if modo == 'pilas2':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][7] = nuevo
                    break
        if modo == 'consumo motores':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][9] = nuevo
                    break
        if modo == 'sensores':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][10] = nuevo
                    break
        if modo == 'peso':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][11] = nuevo
                    break
        if modo == 'estado':
            for i in range(0, 10):
                if int(ListaCarros[i][13]) == cons:
                    ListaCarros[i][8] = nuevo
                    break

    def mod_numsCars(nuevo,cons,arch):
        try:
            global ListaCarros
            nuevo = int(nuevo)
            if isinstance(nuevo,int):
                if arch == 'efi':
                    for i in range(0, 10):
                        if int(ListaCarros[i][13]) == cons:
                            ListaCarros[i][12] = str(nuevo)
                            break
        except:
            messagebox.showerror("Error", "Se debe ingresar un numero")

    def mod_car0():
        mod_car(0, str(ListaCarros[0][13]))

    def mod_car1():
        mod_car(1, str(ListaCarros[1][13]))

    def mod_car2():
        mod_car(2, str(ListaCarros[2][13]))

    def mod_car3():
        mod_car(3, str(ListaCarros[3][13]))

    def mod_car4():
        mod_car(4, str(ListaCarros[4][13]))

    def mod_car5():
        mod_car(5, str(ListaCarros[5][13]))

    def mod_car6():
        mod_car(6, str(ListaCarros[6][13]))

    def mod_car7():
        mod_car(7, str(ListaCarros[7][13]))

    def mod_car8():
        mod_car(8, str(ListaCarros[8][13]))

    def mod_car9():
        mod_car(9, str(ListaCarros[9][13]))

    def mod_car(num, arch):
        Carros.withdraw()
        EditCars = Toplevel()
        EditCars.title('Edit Cars')
        EditCars.minsize(800, 400)
        EditCars.resizable(width=NO, height=NO)
        Canvas_secundario = Canvas(EditCars, width=800, height=400, bg='#2d2d2e')
        Canvas_secundario.place(x=0, y=0)

        def volver():
            Carros.deiconify()
            EditCars.destroy()
            borrarCars(False)
            F_Carros()
            botonesCar()

        E_Marca = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_Marca.place(x=25, y=80)
        E_Modelo = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_Modelo.place(x=200, y=80)
        E_temp = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_temp.place(x=375, y=80)
        E_pais = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_pais.place(x=550, y=80)
        E_bat = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_bat.place(x=25, y=170)
        E_bat2 = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_bat2.place(x=200, y=170)
        E_pil = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_pil.place(x=375, y=170)
        E_pil2 = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_pil2.place(x=550, y=170)
        E_stat = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_stat.place(x=25, y=260)
        E_carac = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_carac.place(x=200, y=260)
        E_carac2 = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_carac2.place(x=375, y=260)
        E_carac3 = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_carac3.place(x=550, y=260)
        E_efi = Entry(Canvas_secundario, width=13, font=('Britannic Bold', 14))
        E_efi.place(x=25, y=350)
        Button(Canvas_secundario, text='Atras', font=('Britannic Bold', 14), command=volver, bg='black', fg='white').place(x=25, y=0)
        Button(Canvas_secundario, text='Marca', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_Marca.get()), num, 'marca'), bg='black', fg='white').place(x=25, y=40)
        Button(Canvas_secundario, text='Modelo', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_Modelo.get()), num, 'modelo'), bg='black', fg='white').place(x=200, y=40)
        Button(Canvas_secundario, text='Temporada', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_temp.get()), num, 'temp'), bg='black', fg='white').place(x=375, y=40)
        Button(Canvas_secundario, text='Pais', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_pais.get()), num, 'pais'), bg='black', fg='white').place(x=550, y=40)
        Button(Canvas_secundario, text='Bateria', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_bat.get()), num, 'baterias'), bg='black', fg='white').place(x=25, y=130)
        Button(Canvas_secundario, text='Bateria 2', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_bat2.get()), num, 'baterias2'), bg='black', fg='white').place(x=200, y=130)
        Button(Canvas_secundario, text='Pilas', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_pil.get()), num, 'pilas'), bg='black', fg='white').place(x=375, y=130)
        Button(Canvas_secundario, text='Pilas 2', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_pil2.get()), num, 'pilas2'), bg='black', fg='white').place(x=550, y=130)
        Button(Canvas_secundario, text='Estado', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_stat.get()), num, 'estado'), bg='black', fg='white').place(x=25, y=220)
        Button(Canvas_secundario, text='Consumo Motores', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_carac.get()), num, 'consumo motores'), bg='black', fg='white').place(x=200, y=220)
        Button(Canvas_secundario, text='Sensores', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_carac2.get()), num, 'sensores'), bg='black', fg='white').place(x=375, y=220)
        Button(Canvas_secundario, text='Peso', font=('Britannic Bold', 14),
               command=lambda: mod_strsCars(str(E_carac3.get()), num, 'peso'), bg='black', fg='white').place(x=550, y=220)
        Button(Canvas_secundario, text='Eficiencia', font=('Britannic Bold', 14),
               command=lambda: mod_numsCars(E_efi.get(), num, 'efi'), bg='black', fg='white').place(x=25, y=310)
        EditCars.mainloop()


    # __Se crea una funcion para volver a la pantalla principal
    def atras_Carros():
        #Lista Carros
        with open("Carros.txt", "w") as f:
            #   for line in lines:
            #      f.write(line)()
            listita2 = []
            print(len(ListaCarros[1][14]))
            for i in range(0,10):
                if len(ListaCarros[i][14]) ==1:
                    ListaCarros[i][14] += '\n'
            for i in range(0, 10):
                listita2.append('@'.join(ListaCarros[i][0:15]))
            print(listita2)
            for strs in listita2:
                f.write(strs)
        global pausa
        pausa = True
        Carros.destroy()
        root.deiconify()

    # Botones de edit
    listaedit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    listcomandedit = [mod_car0, mod_car1, mod_car2, mod_car3, mod_car4, mod_car5, mod_car6, mod_car7, mod_car8,
                      mod_car9]
    btnedit = cargarImg('editbutton.png')

    def botonesCar():
        btn_up = Button(Carros_Canvas, image=flechup, command=mayor_Efi, bg='#2d2d2e')
        btn_dowm = Button(Carros_Canvas, image=flechdowm, command=menor_Efi, bg='#2d2d2e')
        btn_up.place(x=101, y=5)
        btn_dowm.place(x=139, y=5)
        for i in range(0, 10):
            listaedit[i] = (Button(listaframes[i], command=listcomandedit[i], image=btnedit, bg='#2d2d2e'))
            listaedit[i].pack()

    flechup = cargarImg('flechup.png')
    flechdowm = cargarImg('flechdowm.png')

    for i in range(0, 10):
        Carros_Canvas.create_window(960, ListaCarros[i][15], anchor=NW, window=listaframes[i])

    Btn_Atras_cars = Button(Carros_Canvas, image=Btn_AtrasImg, command=atras_Carros, bg='#2d2d2e')
    Btn_Atras_cars.place(x=5, y=5)
    Carros_Canvas.create_window(780, 30, anchor=NW, window=Cars_frame)
    Carros_Canvas.update_idletasks()
    Carros_Canvas.configure(scrollregion=(0, 0, 500, 1200), yscrollcommand=scrolly.set)
    Carros_Canvas.pack(fill=BOTH, expand=True, side=LEFT)
    scrolly.pack(fill=Y, side=RIGHT)

    F_Carros()
    botonesCar()
    Carros.mainloop()


# ___________/Funcion de send, para enviar mensajes al Carrito

def send(mensaje):
    if len(mensaje) > 0 and mensaje[-1] == ";":
        Carrito.send(mensaje)
    else:
        messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    # __________ /Funcion para ventana de TestDrive


def ventana_TestDrive(piloto,carro):
    # Esconder la pantalla principal sin destruirla
    root.withdraw()
    # Pantalla Test_drive
    Test = Toplevel()
    Test.title('Test Drive')
    Test.minsize(1000, 720)
    Test.resizable(width=NO, height=NO)
    # __Se crea un canvas
    Test_Canvas = Canvas(Test, width=1000, height=720, bg='black')
    Test_Canvas.place(x=0, y=0)
    # __Se carga una imagen de fondo

    BackupVel = cargarImg('BackupVel.png')
    Test_Canvas.create_image(0, 300, image=BackupVel, anchor=NW)

    BackupTD = cargarImg('BackupTD.png')
    Test_Canvas.create_image(0, 0, image=BackupTD, anchor=NW)

    # __Se crea el control de vel
    velocimetroImg = cargarImg('velocity.png')
    Test_Canvas.create_image(200, 400, image=velocimetroImg, anchor=NW)

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

    # __Se cargan flechas para el velocimetro
    listapng = ['10vel.png', '20vel.png', '30vel.png', '40vel.png', '50vel.png', '55vel.png', '60vel.png', '65vel.png',
                '70vel.png',
                '75vel.png', '80vel.png', '85vel.png', '90vel.png', '95vel.png', '100vel.png']
    listavel = []
    listaX = [263, 248, 253, 286, 320, 320, 318, 318, 316, 316, 316, 316, 319, 315, 319]
    listaY = [553, 552, 526, 495, 480, 480, 490, 510, 530, 548, 550, 550, 551, 551, 553]
    for png in listapng:
        listavel.append(cargarImg(png))
    listatags = ['vel10', 'vel20', 'vel30', 'vel40', 'vel50', 'vel55', 'vel60', 'vel65', 'vel70', 'vel75', 'vel80',
                 'vel85', 'vel90', 'vel95', 'vel100']
    for i in range(0, 15):
        Test_Canvas.create_image(listaX[i], listaY[i], image=listavel[i], anchor=NW, tags=(listatags[i], 'vel'),
                                 state=HIDDEN)
    vel0 = cargarImg('0vel.png')
    Test_Canvas.create_image(283, 553, image=vel0, anchor=NW, tags=('vel0', 'vel'), state=NORMAL)

    middlecircle = cargarImg('center.png')
    Test_Canvas.create_image(317, 550, image=middlecircle, anchor=NW, state=NORMAL)

    # Se cargan las img para el estado de la bateria
    listapng2 = ['lvl0.png', 'lvl1.png', 'lvl2.png', 'lvl3.png', 'lvl4.png']
    listatext = ['lvl0', 'lvl1', 'lvl2', 'lvl3', 'lvl4']
    listalvl = []
    listaX2 = [460, 477, 495, 513, 532]
    listaY2 = [541, 535, 529, 523, 517]
    for png in listapng2:
        listalvl.append(cargarImg(png))
    for i in range(0, 5):
        Test_Canvas.create_image(listaX2[i], listaY2[i], image=listalvl[i], anchor=NW, tags=(listatext[i], 'lvlbat'),
                                 state=NORMAL)

    # __Se carga el texto de la velocidad
    Test_Canvas.create_text(308, 602, anchor=NW, text="Km/h", font=('Britannic Bold', 12), fill="white")
    Test_Canvas.create_text(297, 617, anchor=NW, text="o", tags="velocidad", font=('Britannic Bold', 18), fill="white")

    # _Boton de reversa
    Reverse_off = cargarImg('reverse-off.png')
    Reverse_on = cargarImg('reverse-on.png')
    Test_Canvas.create_image(570, 450, image=Reverse_off, anchor=NW, tags=("R-off", "reverse"), state=NORMAL)
    Test_Canvas.create_image(570, 450, image=Reverse_on, anchor=NW, tags=("R-on", "reverse"), state=HIDDEN)

    # __Sol
    sol_off = cargarImg('sol_off.png')
    sol_on = cargarImg('sol.png')
    Test_Canvas.create_image(517, 480, image=sol_off, anchor=NW, tags=('s-off', 'sol'), state=NORMAL)
    Test_Canvas.create_image(517, 480, image=sol_on, anchor=NW, tags=('s-on', 'sol'), state=HIDDEN)

    # __Luna
    luna_off = cargarImg('luna_off.png')
    luna_on = cargarImg('luna.png')
    Test_Canvas.create_image(458, 480, image=luna_off, anchor=NW, tags=('l-off', 'luna'), state=NORMAL)
    Test_Canvas.create_image(458, 480, image=luna_on, anchor=NW, tags=('l-on', 'luna'), state=HIDDEN)

    # __Funcionalidades principales del test drive

    # Funcion para obtener el nivel de bateria y la iluminacion de ambiente
    def GetSense():
        global Carrito
        # Obtencion de la bateria
        SenseGet = Carrito.send("sense;")
        time.sleep(3)
        BatlvlGet = Carrito.readById(SenseGet)
        BatLvlObtenido = int(BatlvlGet[0][-2:])
        BatLvl = BatLvlObtenido - 60
        BatLvlFinal = int((BatLvl * 100) / 12)
        # BatImage(BatLvlFinal)
        Test_Canvas.itemconfig("FinalBatLvl", text=str(BatLvlFinal) + "%")
        # Obtencion de la Luz
        LuzGet = Carrito.readById(SenseGet)
        LuzObtenida = int(LuzGet[1][-1])
        iluminacion_actual(LuzObtenida)
        time.sleep(15)
        return GetSense()

    def GetSenseThread():
        T_GetSense = Thread(target=GetSense)
        T_GetSense.start()

    # GetSenseThread()

    # Control de la iluminacion del ambiente
    def iluminacion_actual(luz):
        if luz == 1:
            Test_Canvas.itemconfig('l-on', state=HIDDEN)
            Test_Canvas.itemconfig('sol', state=HIDDEN)
            Test_Canvas.itemconfig('s-on', state=NORMAL)
            Test_Canvas.itemconfig('l-off', state=NORMAL)
        elif luz == 0:
            Test_Canvas.itemconfig('s-on', state=HIDDEN)
            Test_Canvas.itemconfig('luna', state=HIDDEN)
            Test_Canvas.itemconfig('l-on', state=NORMAL)
            Test_Canvas.itemconfig('s-off', state=NORMAL)

    # Nivel de bateria, presente en el test drive
    # def BatImage(BatLevel):
    # if BatLevel == 100:
    # BatLevel = 0

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
            send("dir:-1;")
            print("dir:-1;")

        # Control de direccion derecha
        elif (key == "d") and not right:
            right = True
            Test_Canvas.itemconfig("car", state=HIDDEN)
            Test_Canvas.itemconfig("right", state=NORMAL)
            send("dir:1;")
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
                T_pwm_dowm_Re = Thread(target=reverse_desaceleracion)
                T_pwm_dowm_Re.start()
            else:
                return

        # Hacia adelante
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
                    send("pwm:0;")
                    print("pwm:0;")
                    Test_Canvas.itemconfig("velocidad", text="0")
                    Test_Canvas.itemconfig("reverse", state=HIDDEN)
                    Test_Canvas.itemconfig("R-on", state=NORMAL)


        # Control de luces

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
                    send("lf:0;")
                    print("lf:0;")
                else:
                    Test_Canvas.itemconfig("L_f", state=NORMAL)
                    Test_Canvas.itemconfig("L_f2", state=NORMAL)
                    L_frontON = True
                    send("lf:1;")
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
                else:
                    Test_Canvas.itemconfig("L_dir2", state=NORMAL)
                    L_rightON = True
                    T_blinking(1, "lr")

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
            T_Blink_stop = Thread(target=direccionalesON, args=[n, command])
            T_Blink_stop.start()

    def T_blinking(n, command):
        global L_DirON, L_rightON, L_leftON
        if L_DirON or L_leftON or L_rightON:
            T_Blink = Thread(target=direccionalesON, args=[n, command])
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
                    send(command + ":1;")
                    print(command + ":1;")
                    time.sleep(0.5)
                    return direccionalesON(n + 1, command)
                else:
                    send(command + ":0;")
                    print(command + ":0;")
                    time.sleep(0.5)
                    return direccionalesON(n + 1, command)

    def aceleracion():
        global NumGas, pressTecla
        Test_Canvas.itemconfig("L_s2", state=HIDDEN)
        Test_Canvas.itemconfig("L_s", state=HIDDEN)
        if 500 <= NumGas <= 950 and pressTecla:
            if pressTecla:
                NumGas += 50
                send("pwm:" + str(NumGas) + ";")
                print("pwm:" + str(NumGas) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
                velocimetro()
                aceleracion()
            else:
                return

        elif 400 >= NumGas and pressTecla:
            if pressTecla:
                NumGas += 100
                send("pwm:" + str(NumGas) + ";")
                print("pwm:" + str(NumGas) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
                velocimetro()
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
                send("pwm:" + str(NumGas_Re) + ";")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
                velocimetro()
                reverse_aceleration()
            else:
                return

        elif -400 <= NumGas_Re and pressTecla:
            if pressTecla:
                NumGas_Re -= 100
                send("pwm:" + str(NumGas_Re) + ";")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
                velocimetro()
                reverse_aceleration()
            else:
                return

    def desaceleracion():
        global NumGas, pressS
        Test_Canvas.itemconfig("L_s2", state=HIDDEN)
        Test_Canvas.itemconfig("L_s", state=HIDDEN)
        if NumGas <= 450:
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            Test_Canvas.itemconfig("L_s", state=NORMAL)
            NumGas = 0
            send("pwm:" + str(NumGas) + ";")
            print("pwm:" + str(NumGas) + ";")
            time.sleep(1)
            Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
            velocimetro()
        elif NumGas <= 1000 and pressS:
            if pressS:
                NumGas -= 100
                send("pwm:" + str(NumGas) + ";")
                print("pwm:" + str(NumGas) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas / 10)))
                velocimetro()
                desaceleracion()
            else:
                return

    def reverse_desaceleracion():
        global NumGas_Re, Reverse_on, pressS
        Test_Canvas.itemconfig("L_s2", state=NORMAL)
        Test_Canvas.itemconfig("L_s", state=NORMAL)
        if NumGas_Re >= -450:
            Test_Canvas.itemconfig("L_s2", state=NORMAL)
            Test_Canvas.itemconfig("L_s", state=NORMAL)
            NumGas_Re = 0
            send("pwm:" + str(NumGas_Re) + ";")
            print("pwm:" + str(NumGas_Re) + ";")
            time.sleep(1)
            Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
            velocimetro()
        elif NumGas_Re >= -1000 and pressS:
            if pressS:
                NumGas_Re += 100
                send("pwm:" + str(NumGas_Re) + ";")
                print("pwm:" + str(NumGas_Re) + ";")
                time.sleep(1)
                Test_Canvas.itemconfig("velocidad", text=str(int(NumGas_Re / 10)))
                velocimetro()
                reverse_desaceleracion()
            else:
                return

    def velocimetro():
        global NumGas_Re, NumGas, pressTecla, pressS
        if NumGas_Re == -100 or NumGas == 100:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel10', state=NORMAL)
        elif NumGas_Re == -200 or NumGas == 200:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel20', state=NORMAL)
        elif NumGas_Re == -300 or NumGas == 300:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel30', state=NORMAL)
        elif NumGas_Re == -400 or NumGas == 400:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel40', state=NORMAL)
        elif NumGas_Re == -500 or NumGas == 500:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel50', state=NORMAL)
        elif NumGas_Re == -550 or NumGas == 550:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel55', state=NORMAL)
        elif NumGas_Re == -600 or NumGas == 600:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel60', state=NORMAL)
        elif NumGas_Re == -650 or NumGas == 650:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel65', state=NORMAL)
        elif NumGas_Re == -700 or NumGas == 700:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel70', state=NORMAL)
        elif NumGas_Re == -750 or NumGas == 750:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel75', state=NORMAL)
        elif NumGas_Re == -800 or NumGas == 800:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel80', state=NORMAL)
        elif NumGas_Re == -850 or NumGas == 850:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel85', state=NORMAL)
        elif NumGas_Re == -900 or NumGas == 900:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel90', state=NORMAL)
        elif NumGas_Re == -950 or NumGas == 950:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel95', state=NORMAL)
        elif NumGas_Re == -1000 or NumGas == 1000:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel100', state=NORMAL)
        elif NumGas_Re == 0 or NumGas == 0:
            Test_Canvas.itemconfig('vel', state=HIDDEN)
            Test_Canvas.itemconfig('vel0', state=NORMAL)
            time.sleep(0.5)

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
            print("dir:0;")

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

Btn_Test = cargarImg("Btn_Test.png")
Btn_Test_Driver = Button(Principal_Canvas, image=Btn_Test, command=ventana_esc_pil, bg='#2d2d2e')
Btn_Test_Driver.place(x=10, y=60)

Btn_PilotsImg = cargarImg("Btn_Pilots.png")
Btn_Pilots = Button(Principal_Canvas, image=Btn_PilotsImg, command=ventana_Pilots, bg='#2d2d2e')
Btn_Pilots.place(x=10, y=126)

Btn_CarrosImg = cargarImg('Btn_Cars.png')
Btn_Carros = Button(Principal_Canvas, image=Btn_CarrosImg, command=ventana_Carros, bg='#2d2d2e')
Btn_Carros.place(x=10, y=192)

Btn_Credits = cargarImg("Btn_Credits.png")
Btn_About = Button(Principal_Canvas, image=Btn_Credits, command=ventana_about, bg='#2d2d2e')
Btn_About.place(x=10, y=258)

Btn_QuitImg = cargarImg("Btn_Quit.png")
Btn_Quit = Button(Principal_Canvas, image=Btn_QuitImg, command=quitApp, bg='#2d2d2e')
Btn_Quit.place(x=10, y=324)

Btn_play = cargarImg("Btn_play.png")
Btn_PlayMusic = Button(Principal_Canvas, image=Btn_play, command=play, bg='#2d2d2e')
Btn_PlayMusic.place(x=10, y=586)

Btn_pause = cargarImg("Btn_pause.png")
Btn_mute = Button(Principal_Canvas, image=Btn_pause, command=pause, bg='#2d2d2e')
Btn_mute.place(x=50, y=586)

root.mainloop()
