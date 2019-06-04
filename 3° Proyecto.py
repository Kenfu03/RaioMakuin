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
#global left, right, NumGas, NumGas_Re, reverseON, L_rightON, L_leftON, L_backON, GasON, L_DirON, pressTecla, \
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
    listaframes = []
    for i in range(0, 10):
        listaframes.append(Frame(Pilots_Canvas))

    # Se cargan las imagenes
    listapng = ["jonathan.png", "joseph.png", "jotaro.png", "josuke.png", "giorno.png", "dio.png", "kira.png",
                "bruno.png", "polnareff.png", "caesar.png"]
    listaimg = []
    for nombre in listapng:
        listaimg.append(cargarImg(nombre))
    britanico = cargarImg("britanico.png")  # en la lista cargar la imagen
    japones = cargarImg("japones.png")
    italiano = cargarImg("italiano.png")
    frances = cargarImg("frances.png")
    americano = cargarImg("americano.png")

    global ListaPilotos
    ListaPilotos = []
    ListaY = [40, 145, 250, 355, 460, 565, 670, 775, 880, 985]
    # __Se abre el archivo de texto con la info. de los pilotos
    arch1 = open('Pilotos.txt', 'r+')
    for i in range(0, 10):
        ListaPilotos.append(arch1.readline().split('@'))

    def flag0():
        ListaPilotos[0].append(britanico)

    def flag1():
        ListaPilotos[1].append(americano)

    def flag2():
        ListaPilotos[2].append(japones)

    def flag3():
        ListaPilotos[3].append(japones)

    def flag4():
        ListaPilotos[4].append(italiano)

    def flag5():
        ListaPilotos[5].append(britanico)

    def flag6():
        ListaPilotos[6].append(japones)

    def flag7():
        ListaPilotos[7].append(italiano)

    def flag8():
        ListaPilotos[8].append(frances)

    def flag9():
        ListaPilotos[9].append(italiano)

    flag0()
    flag1()
    flag2()
    flag3()
    flag4()
    flag5()
    flag6()
    flag7()
    flag8()
    flag9()
    # Se calculan los RGP de los pilotos y se agregan a la lista de cada piloto
    for i in range(0, 10):
        ListaPilotos[i].append(int(((int(ListaPilotos[i][5]) + int(ListaPilotos[i][6])) / (int(ListaPilotos[i][4]) - int(ListaPilotos[i][7])) * 100)))

    for i in range(0, 10):
        ListaPilotos[i].append(int(((int(ListaPilotos[i][5])) / (int(ListaPilotos[i][4]) - int(ListaPilotos[i][7])) * 100)))

    for i in range(0, 10):
        ListaPilotos[i].append(ListaY[i])

    for i in range(0, 10):
        ListaPilotos[i].append(listaimg[i])

    print(ListaPilotos)
    # la lista de cada piloto

    # ListaPilotos=(Pil0,Pil1,Pil2,Pil3,Pil4,Pil5,Pil6,Pil7,Pil8,Pil9)
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
    listanacion = []
    for i in range(0, 10):
        listatext.append(Pilots_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))

    Nombre = Pilots_Canvas.create_text(182, 2, anchor=NW, text='Nombre/Edad', font=('Britannic Bold', 16))
    Temp = Pilots_Canvas.create_text(380, 2, anchor=NW, text='Temporada', font=('Britannic Bold', 16))
    RGP = Pilots_Canvas.create_text(500, 2, anchor=NW, text='RGP', font=('Britannic Bold', 16))
    REP = Pilots_Canvas.create_text(555, 2, anchor=NW, text='REP', font=('Britannic Bold', 16))
    Comp = Pilots_Canvas.create_text(610, 2, anchor=NW, text='Competencias', font=('Britannic Bold', 16))

    def pilotos():
        print(ListaPilotos)
        for i in range(0, 10):
            listaflags.append(Pilots_Canvas.create_image(108, ListaPilotos[i][12], image=ListaPilotos[i][9], anchor=NW))
        for i in range(0, 10):
            listanom.append(Pilots_Canvas.create_text(182, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][0],
                                                      font=('Britannic Bold', 16)))
        for i in range(0, 10):
            listanacion.append(
                Pilots_Canvas.create_text(182, ListaPilotos[i][12] + 50, anchor=NW, text=ListaPilotos[i][2],
                                          font=('Britannic Bold', 16)))
        for i in range(0, 10):
            listaedad.append(
                Pilots_Canvas.create_text(182, ListaPilotos[i][12] + 25, anchor=NW, text=ListaPilotos[i][1],
                                          font=('Britannic Bold', 16)))
        for i in range(0, 10):
            listatmp.append(Pilots_Canvas.create_text(380, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][3],
                                                      font=('Britannic Bold', 16)))
        for i in range(0, 10):
            listargp.append(Pilots_Canvas.create_text(500, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][10],
                                                      font=('Britannic Bold', 16)))
        for i in range(0, 10):
            listarep.append(Pilots_Canvas.create_text(555, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][11],
                                                      font=('Britannic Bold', 16)))
        for i in range(0, 10):
            listacomp.append(Pilots_Canvas.create_text(610, ListaPilotos[i][12], anchor=NW, text=ListaPilotos[i][4],
                                                       font=('Britannic Bold', 16)))

    # Pilots_Canvas.delete(nomp)
    # Boton.destroy()
    def nuevoRGP():
        for i in range(0, 10):
            ListaPilotos[i][10] = (int(((int(ListaPilotos[i][5]) + int(ListaPilotos[i][6])) / (
                    int(ListaPilotos[i][4]) - int(ListaPilotos[i][7])) * 100)))
        for i in range(0, 10):
            ListaPilotos[i][11](
                int(((int(ListaPilotos[i][5])) / (int(ListaPilotos[i][4]) - int(ListaPilotos[i][7])) * 100)))

    def borrar():
        for texts in listatext:
            Pilots_Canvas.delete(texts)
        for flags in listaflags:
            Pilots_Canvas.delete(flags)
        for nacion in listanacion:
            Pilots_Canvas.delete(nacion)
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
        for btn2 in listabotones2:
            btn2.destroy()
        # Pilots_Canvas.delete(listatext)

    def mayor_RGP():
        global ListaPilotos
        borrar()
        ListaRGP = burbuja(ListaPilotos, 10)
        ListaPilotos = ListaRGP[::-1]
        print(ListaPilotos[0])
        for i in range(0, 10):
            ListaPilotos[i][12] = ListaY[i]
            ListaPilotos[i][8] = str(i)
        for i in range(0, 10):
            listatext.append(
                Pilots_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))
        pilotos()
        botones()

    def menor_RGP():
        global ListaPilotos
        borrar()
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
        global ListaPilotos
        borrar()
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
        global ListaPilotos
        borrar()
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

    def mod_nom(nuevo, cons, arch):
        global ListaPilotos
        for i in range(0, 10):
            print(ListaPilotos[i][8])
            print(cons)
            if int(ListaPilotos[i][8]) == cons:
                ListaPilotos[i][0] = nuevo
                print(nuevo)
                print(ListaPilotos[i])
                break

    def mod_jon():
        mod_pil(0, 'jon')

    def mod_jsp():
        mod_pil(1, 'jsp')

    def mod_jot():
        mod_pil(2, 'jot')

    def mod_jsk():
        mod_pil(3, 'jsk')

    def mod_gio():
        mod_pil(4, 'gio')

    def mod_dio():
        mod_pil(5, 'dio')

    def mod_kra():
        mod_pil(6, 'kra')

    def mod_brn():
        mod_pil(7, 'brn')

    def mod_pol():
        mod_pil(8, 'pol')

    def mod_czs():
        mod_pil(9, 'czs')

    def mod_pil(num, arch):
        Pilots.withdraw()
        EditGiorno = Toplevel()
        EditGiorno.title('Pilot')
        EditGiorno.minsize(600, 400)
        EditGiorno.resizable(width=NO, height=NO)
        Canvas_secundario = Canvas(EditGiorno, width=600, height=400, bg='blue')
        Canvas_secundario.place(x=0, y=0)

        def volver():
            Pilots.deiconify()
            Pilots.update()
            EditGiorno.destroy()

        global ListaPilotos
        print(num)
        E_nombre1 = Entry(Canvas_secundario, width=15, font=('Britannic Bold', 14))
        E_nombre1.place(x=120, y=80)
        Button(Canvas_secundario, text='Atras', font=('Britannic Bold', 14), command=volver, bg='black',
               fg='white').place(x=25, y=0)
        Button(Canvas_secundario, text='Nombre', font=('Britannic Bold', 14),
               command=lambda: mod_nom(str(E_nombre1.get()), num, arch), bg='black', fg='white').place(x=100, y=40)

        EditGiorno.mainloop()

    # def mod_gio

    def burbuja(Lista, k):
        return burbuja_aux(Lista, 0, 0, len(Lista), False, k)

    def burbuja_aux(Lista, i, j, n, Swap, k):
        if i == n:
            return Lista
        if j == n - i - 1:
            if Swap:
                return burbuja_aux(Lista, i + 1, 0, n, False, k)
            else:
                return Lista
        if Lista[j][k] > Lista[j + 1][k]:
            Tmp = Lista[j]
            Lista[j] = Lista[j + 1]
            Lista[j + 1] = Tmp
            return burbuja_aux(Lista, i, j + 1, n, True, k)
        else:
            return burbuja_aux(Lista, i, j + 1, n, Swap, k)

    # __Se carga una imagen

    # __Se crea un label con informacion crucial

    # __Se crea una funcion para volver a la pantalla principal
    def atras_Pilots():
        # ListaPilotos
        with open("Pilotos.txt", "w") as f:
            #   for line in lines:
            #      f.write(line)()
            listita = []
            if len(ListaPilotos[1][8]) == 1:
                for i in range(0, 10):
                    ListaPilotos[i][8] += '\n'
            for i in range(0, 10):
                listita.append('@'.join(ListaPilotos[i][0:9]))
            for strs in listita:
                f.write(strs)
        global pausa
        pausa = True
        Pilots.destroy()
        root.deiconify()

    listabotones2 = [0, 1, 2, 3, 4]
    listatext2 = ['Atras', 'Mayor RGP', 'Menor RGP', 'Mayor REP', 'Menor REP']
    listacomandos = [atras_Pilots, mayor_RGP, menor_RGP, mayor_REP, menor_REP]
    # Botones de los pilotos
    listabtn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    listacomandos2 = [mod_jon, mod_jsp, mod_jot, mod_jsk, mod_gio, mod_dio, mod_kra, mod_brn, mod_pol, mod_czs]
    print(ListaPilotos)

    # Button(Pilots_Canvas,text = 'giorno',font=('Britannic Bold', 14), command=lambda:mod_gio('4') ,bg='black', fg='white').place(x=700,y=200)
    def botones():
        for i in range(0, 10):
            listabtn[i] = (Button(listaframes[i], command=listacomandos2[i], image=ListaPilotos[i][13]))
            listabtn[i].pack()
        for i in range(0, 5):
            listabotones2[i] = (
                Button(Pilots_frame, text=listatext2[i], font=('Britannic Bold', 14), command=listacomandos[i],
                       bg='black', fg='white'))
            listabotones2[i].pack()

    for i in range(0, 10):
        Pilots_Canvas.create_window(30, ListaPilotos[i][12], anchor=NW, window=listaframes[i])

    Pilots_Canvas.create_window(780, 30, anchor=NW, window=Pilots_frame)
    Pilots_Canvas.update_idletasks()
    Pilots_Canvas.configure(scrollregion=(0, 0, 500, 1100), yscrollcommand=scroll_y.set)
    Pilots_Canvas.pack(fill=BOTH, expand=True, side=LEFT)
    scroll_y.pack(fill=Y, side=RIGHT)
    pilotos()
    botones()
    Pilots.mainloop()


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

    # __Se crea una funcion para volver a la pantalla principal
    def atras_Carros():
        global pausa
        pausa = True
        Carros.destroy()
        root.deiconify()

    # __Se crea un canvas y un scrollbar
    scrolly = Scrollbar(Carros, orient='vertical', command=Carros_Canvas.yview)
    Cars_frame = Frame(Carros_Canvas)
    listaframes = []
    for i in range(0, 10):
        listaframes.append(Frame(Carros_Canvas))

    Btn_Atras_cars = Button(Carros_Canvas, image=Btn_AtrasImg, command=atras_Carros, bg='#2d2d2e')
    Btn_Atras_cars.place(x=5, y=5)

    listacarrospng = ["car0.png", "car1.png", "car2.png", "car3.png", "car4.png", "car5.png", "car6.png",
                      "car7.png", "car8.png", "car9.png"]
    listacarrosImg = []

    for carImg in listacarrospng:
        listacarrosImg.append(cargarImg(carImg))

    global ListaCarros
    ListaCarros = []
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
    listapilas = []
    listaestado = []
    listacarac = []
    listaeficiencia = []
    for i in range(0, 10):
        listatext.append(Carros_Canvas.create_text(5, ListaY[i], anchor=NW, text=i + 1, font=('Britannic Bold', 16)))

    CarImg = Carros_Canvas.create_text(182, 2, anchor=NW, text='Marca\nModelo', font=('Britannic Bold', 16),fill="#fdf2b4")
    TempYPais = Carros_Canvas.create_text(300, 2, anchor=NW, text='Temporada\nPais', font=('Britannic Bold', 16),fill="#fdf2b4")
    Baterias = Carros_Canvas.create_text(450, 2, anchor=NW, text='Baterias\nPilas', font=('Britannic Bold', 16),fill="#fdf2b4")
    Caracteristicas = Carros_Canvas.create_text(565, 2, anchor=NW, text='Caracteristicas', font=('Britannic Bold', 16),fill="#fdf2b4")
    Estado = Carros_Canvas.create_text(745, 2, anchor=NW, text='Estado', font=('Britannic Bold', 16),fill="#fdf2b4")
    Eficiencia = Carros_Canvas.create_text(845, 2, anchor=NW, text='Eficiencia', font=('Britannic Bold', 16),fill="#fdf2b4")

    def F_Carros():
        print (ListaCarros)
        for i in range(0, 10):
            listacar.append(Carros_Canvas.create_image(10, ListaCarros[i][5], image=ListaCarros[i][6], anchor=NW))
        for i in range(0, 10):
            listamarca.append(Carros_Canvas.create_text(182, ListaCarros[i][5], anchor=NW, text=ListaCarros[i][0],font=('Britannic Bold', 16), fill="white"))
        for i in range(0, 10):
            listamodelo.append(Carros_Canvas.create_text(182, ListaCarros[i][5] + 25, anchor=NW, text=ListaCarros[i][1],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listapais.append(Carros_Canvas.create_text(300, ListaCarros[i][5] + 25, anchor=NW, text=ListaCarros[i][2],font=('Britannic Bold', 16),fill="white"))
        for i in range(0, 10):
            listatemp.append(Carros_Canvas.create_text(300, ListaCarros[i][5], anchor=NW, text=ListaCarros[i][3],font=('Britannic Bold', 16),fill="white"))
        #for i in range(0, 10):
            #listabaterias.append(Carros_Canvas.create_text(380, ListaCarros[i][5], anchor=NW, text=ListaCarros[i][3],font=('Britannic Bold', 16)))
        #for i in range(0, 10):
            #listapilas.append(Carros_Canvas.create_text(500, ListaCarros[i][5], anchor=NW, text=ListaCarros[i][10],font=('Britannic Bold', 16)))
        #for i in range(0, 10):
            #listaestado.append(Carros_Canvas.create_text(555, ListaCarros[i][5], anchor=NW, text=ListaCarros[i][11],font=('Britannic Bold', 16)))
        #for i in range(0, 10):
            #listacarac.append(Carros_Canvas.create_text(610, ListaCarros[i][5], anchor=NW, text=ListaCarros[i][4],font=('Britannic Bold', 16)))
        for i in range(0, 10):
            listaeficiencia.append(Carros_Canvas.create_text(845, ListaCarros[i][5], anchor=NW, text=ListaCarros[i][4],font=('Britannic Bold', 16),fill="white"))

    Carros_Canvas.create_window(780, 30, anchor=NW, window=Cars_frame)
    Carros_Canvas.update_idletasks()
    Carros_Canvas.configure(scrollregion=(0, 0, 500, 1200), yscrollcommand=scrolly.set)
    Carros_Canvas.pack(fill=BOTH, expand=True, side=LEFT)
    scrolly.pack(fill=Y, side=RIGHT)

    F_Carros()
    Carros.mainloop()


# ___________/Funcion de send, para enviar mensajes al Carrito

def send(mensaje):
    if len(mensaje) > 0 and mensaje[-1] == ";":
        Carrito.send(mensaje)
    else:
        messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    # __________ /Funcion para ventana de TestDrive


def ventana_TestDrive():
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
        #BatImage(BatLvlFinal)
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
    #def BatImage(BatLevel):
        #if BatLevel == 100:
            #BatLevel = 0

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
Btn_Test_Driver = Button(Principal_Canvas, image=Btn_Test, command=ventana_TestDrive, bg='#2d2d2e')
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
