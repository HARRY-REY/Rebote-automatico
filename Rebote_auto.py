# !/usr/bin/env-python
# -*- coding: utf-8 -*-

from random import random,randint
import pygame,sys

pygame.init()

# -COLORES
negro    = ( 0   , 0   , 0   )
blanco   = ( 255 , 255 , 255 )
rojo     = ( 200 , 0   , 0   )
verde    = ( 0   , 200 , 00  )
azul     = ( 0   , 0   , 200 )
amarillo = ( 255 , 255 , 0   )

# -VENTANA
tamaño    = ancho,alto = 300,500                # Tamaño de la pantalla
pantalla  = pygame.display.set_mode(tamaño)     # Se cre una pantall con pygame con el tamaño prediseñado
pygame.display.set_caption("Rebote automatico") # Se le pone un nombre al borde de la pantalla

# -CLASES
class Pelota:

    def __init__(self, x , y , radio , color):
        self.x      = x
        self.y      = y
        self.radio  = radio
        self.color  = color
        self.grosor = 0 

    def mostrar(self):
        pygame.draw.circle ( pantalla , self.color , (  self.x , self.y ) , self.radio , self.grosor )

# -DATOS
movimiento_AB         = 0                          # Movimiento de arriba - abajo
movimiento_ID         = 0                          # Movimiento de izquierda - derecha
fuente_predeterminada = pygame.font.Font(None, 30) # Fuente, tamaño de la fuente
texto_inicio          = fuente_predeterminada.render("Presiona 'ESPACIO'",0,negro)
texto_inicio_1        = fuente_predeterminada.render("para comenzar",0,negro)
texto_inicio_2        = fuente_predeterminada.render("'c' para detener",0,negro)
mostar_texto          = False                      # Condición para mostrar el texto

# -OBJETOS
balon = Pelota ( 150 , 20 , 20 , rojo)

# -BUCLÉ 
while True:

    # Varibale aleatoria para el movimiento del objeto
    movimiento    = randint(0,3)


    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()

        # Si alguna tecla es presionada 
        elif accion.type == pygame.KEYDOWN:
            # Si se presiona "ESPACIO" comenzara a moverse
            if accion.key == pygame.K_SPACE:
                # Movimientos de manera aleatoria

                # ABAJO - DERECHA
                if movimiento == 0:
                    movimiento_AB = 10
                    movimiento_ID = 10

                # ABAJO - IZQUIERDA
                if movimiento == 1:
                    movimiento_AB = 10
                    movimiento_ID =-10

                # ARRIBA - DERECHA
                if movimiento == 2:
                    movimiento_AB =-10
                    movimiento_ID = 10

                # ARRIBA - IZQUIERDA
                if movimiento == 3:
                    movimiento_AB =-10
                    movimiento_ID =-10

            # si se presiona "c" se detiene
            if accion.key == pygame.K_c:
                movimiento_AB = 0
                movimiento_ID = 0
    
    # Muestra la pantalla con fondo de color
    pantalla.fill(blanco)
    pantalla.blit(texto_inicio  ,(20,150))
    pantalla.blit(texto_inicio_1,(20,200))
    pantalla.blit(texto_inicio_2,(20,250))

    # Movimiento en el eje Y
    balon.y += movimiento_AB
    
    # Movimiento en el eje X
    balon.x += movimiento_ID

    # Muestra la pelota
    balon.mostrar()

    # Condición para no rebasar el suelo
    if balon.y >= alto:
        movimiento_AB *= -1
    # Condición para no rebasar el techo
    if balon.y <= 0:
        movimiento_AB *= -1

    # Condición para no rebasar el lado izquierdo 
    if balon.x <= 0:
        movimiento_ID *= -1

    # Condición para no rebasar el lado derecho 
    if balon.x >= ancho:
        movimiento_ID *= -1

    # Manejo de la pantalla
    pygame.display.update()

    # Actualización de la pantalla
    pygame.time.delay(30)
