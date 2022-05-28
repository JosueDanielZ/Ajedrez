import pygame as py

py.init()
#comit prueba 
WHITE=[255,255,255]
ancho = 480
altura = 480
ventana = py.display.set_mode((ancho,altura))
posiciones= [[0,0],[0,60],[0,120],[0,180],[0,240],[0,300],[0,360],[0,420],
             [60,0],[60,60],[60,120],[60,180],[60,240],[60,300],[60,360],[60,420],
             [120,0],[120,60],[120,120],[120,180],[120,240],[120,300],[120,360],[120,420],
             [180,0],[180,60],[180,120],[180,180],[180,240],[180,300],[180,360],[180,420],
             [240,0],[240,60],[240,120],[240,180],[240,240],[240,300],[240,360],[240,420],
             [300,0],[300,60],[300,120],[300,180],[300,240],[300,300],[300,360],[300,420],
             [360,0],[360,60],[360,120],[360,180],[360,240],[360,300],[360,360],[360,420],
             [420,0],[420,60],[420,120],[420,180],[420,240],[420,300],[420,360],[420,420]]


tablero = py.image.load("tablero.png").convert()
peon = py.image.load("peon.png").convert_alpha()


bandera = True
while bandera:
    for event in py.event.get():
        if event.type == py.QUIT:
            bandera = False

    pos_m = py.mouse.get_pos()
    x = pos_m[0]
    y = pos_m[1]

    ventana.blit(tablero,[0,0])
    ventana.blit(peon,[120,60])

    py.display.flip(
py.quit()
