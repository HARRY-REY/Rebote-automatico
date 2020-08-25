# !/usr/bin/env-python
# -*- coding: utf-8 -*-

import pygame,sys

# -COLORES
negro    = ( 0   , 0   , 0   )
blanco   = ( 255 , 255 , 255 )
rojo     = ( 200 , 0   , 0   )
verde    = ( 0   , 200 , 00  )
azul     = ( 0   , 0   , 200 )
amarillo = ( 255 , 255 , 0   )

# -VENTANA
tamaño    = ancho,alto = 300,500            # Tamaño de la pantalla
pantalla  = pygame.display.set_mode(tamaño) # Se cre una pantall con pygame con el tamaño prediseñado
pygame.display.set_caption("Gravedad")      # Se le pone un nombre al borde de la pantalla

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
movimiento_AB = 0 # Movimiento de arriba - abajo
movimiento_ID = 0 # Movimiento de izquierda - derecha


# -OBJETOS
balon = Pelota ( 150 , 20 , 20 , rojo)

# -BUCLÉ 
while True:

    """
    El efecto se efectua simpre que se presione la tecla,
    cuando deja de ser presionada el movimiento es 0 
    """
    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()

        # Si alguna tecla es presionada 
        elif accion.type == pygame.KEYDOWN:

            if accion.key == pygame.K_DOWN:
                movimiento_AB = 10
                print("Tecla ABAJO presionada")
                # Movimiento en el eje Y
                balon.y += movimiento_AB
            
            elif accion.key == pygame.K_UP:
                movimiento_AB = -10
                print("Tecla ARRIBA presionada")
                # Movimiento en el eje Y
                balon.y += movimiento_AB

            elif accion.key == pygame.K_LEFT:
                movimiento_ID = -10
                print("Tecla IZQUIERDA presionada")
                # Movimiento en el eje Y
                balon.x += movimiento_ID

            elif accion.key == pygame.K_RIGHT:
                movimiento_ID = 10
                print("Tecla DERECHA presionada")
                # Movimiento en el eje Y
                balon.x += movimiento_ID
        """
        # Si alguna tecla se deja de presionar
        elif accion.type == pygame.KEYUP:
            if accion.key == pygame.K_DOWN:
                movimiento_AB = 0
            if accion.key == pygame.K_UP:
                movimiento_AB = 0
            if accion.key == pygame.K_LEFT:
                movimiento_ID = 0
            if accion.key == pygame.K_RIGHT:
                movimiento_ID = 0
        """
    # Muestra la pantalla con fondo de color
    pantalla.fill(blanco)

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
