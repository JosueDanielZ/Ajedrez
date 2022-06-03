#Importando la libreria de pygame
from cmath import rect
from numpy import rec
import pygame
import sys

#Iniciador de la libreria
pygame.init()

#Color blanco en RGB

WHITE=[255,255,255]

#Medidas de la ventan del juego
ancho = 480
altura = 480

#Creando la ventana
ventana = pygame.display.set_mode((ancho,altura))

#Posiciones de cada bloque (cada bloque es de 60x60 pixeles)
posiciones= [[0,0],[0,60],[0,120],[0,180],[0,240],[0,300],[0,360],[0,420],
             [60,0],[60,60],[60,120],[60,180],[60,240],[60,300],[60,360],[60,420],
             [120,0],[120,60],[120,120],[120,180],[120,240],[120,300],[120,360],[120,420],
             [180,0],[180,60],[180,120],[180,180],[180,240],[180,300],[180,360],[180,420],
             [240,0],[240,60],[240,120],[240,180],[240,240],[240,300],[240,360],[240,420],
             [300,0],[300,60],[300,120],[300,180],[300,240],[300,300],[300,360],[300,420],
             [360,0],[360,60],[360,120],[360,180],[360,240],[360,300],[360,360],[360,420],
             [420,0],[420,60],[420,120],[420,180],[420,240],[420,300],[420,360],[420,420]]

#Cargando imagenes
tablero = pygame.image.load("tablero.png").convert()
peon = pygame.image.load("peon.png").convert_alpha()

class Cursor(pygame.Rect):
    def __init__(self):
        super().__init__(0,0,1,1)

    def update(self):
        self.left,self.top=pygame.mouse.get_pos()


class Caballo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("caballo.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = posiciones[15][0]
        self.rect.y = posiciones[15][1]
        if cursor1.colliderect(self.rect):
            print("true")


    def posicion1(self):
        verde_s = Verde(self.rect.x - 60 ,self.rect.y - 120)
        posiciones_piezas.add(verde_s)

    def posicion2(self):
        verde_s = Verde(self.rect.x + 60 ,self.rect.y - 120)
        posiciones_piezas.add(verde_s)

    def posicion3(self):
        verde_s = Verde(self.rect.x + 120 ,self.rect.y - 60)
        posiciones_piezas.add(verde_s)

    def posicion4(self):
        verde_s = Verde(self.rect.x + 120 ,self.rect.y + 60)
        posiciones_piezas.add(verde_s)

    def posicion5(self):
        verde_s = Verde(self.rect.x + 60 ,self.rect.y + 120)
        posiciones_piezas.add(verde_s)

    def posicion6(self):
        verde_s = Verde(self.rect.x - 60 ,self.rect.y + 120)
        posiciones_piezas.add(verde_s)
        

    def posicion7(self):
        verde_s = Verde(self.rect.x - 120 ,self.rect.y - 60)
        posiciones_piezas.add(verde_s)

    def posicion8(self):
        verde_s = Verde(self.rect.x - 120 ,self.rect.y + 60)
        posiciones_piezas.add(verde_s)

class Verde(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("verde.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def update(self):
        if cursor1.colliderect(self.rect):
            print("verde")
    

caballito = Caballo()

verdesito = Verde(-60,-60)
piezas = pygame.sprite.Group()
piezas.add(caballito)

cursor1 = Cursor()

posiciones_piezas = pygame.sprite.Group()

#Motor de pygame
bandera = True
while bandera:
    # Eventos de pygame
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(caballito.rect):
                caballito.posicion1()
                caballito.posicion2()
                caballito.posicion3()
                caballito.posicion4()
                caballito.posicion5()
                caballito.posicion6()
                caballito.posicion7()
                caballito.posicion8()
                if cursor1.colliderect(verdesito.rect):
                    pass

        if event.type == pygame.QUIT:
            bandera = False

    #Todo Codigo que se coloque en esta INDENTACION se ejecutara en la ventana del juego

    #mostrando las imagenes en pantalla
    ventana.blit(tablero,[0,0])
    ventana.blit(peon,[120,60])


    piezas.update()
    piezas.draw(ventana)
    cursor1.update()
    posiciones_piezas.update()
    posiciones_piezas.draw(ventana)


    #Funcion para que se actualice la ventana
    pygame.display.flip()

#Funcion para hacer que el juego se cierre complentamente
pygame.quit()
