import pygame
import sys
import random


# declarar constantes

ancho = 800
alto = 600
color_verde = (0, 200, 0)
color_negro = (0, 0, 0)
color_azul = (0, 0, 200)

# JUGADOR
player_size = 50
player_pos = [ancho / 2, alto - (player_size * 2)]


# Enemigo(s)
enemy_size = 50
enemy_pos = [random.randint(0, ancho - enemy_size), 0]


# ventana
ventana = pygame.display.set_mode((ancho, alto))

clock = pygame.time.Clock()
game_over = False

# Funciones


def detectar_colision(player_pos, enemy_pos):
    px = player_pos[0]
    py = player_pos[1]
    ex = enemy_pos[0]
    ey = enemy_pos[1]

    if (ex >= px and ex < (px + player_size)) or (px >= ex and px < (ex + enemy_size)):
        if (ey >= py and ey < (py + player_size)) or (
            py >= ey and py < (ey + enemy_size)
        ):
            return True
    return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]

            if event.key == pygame.K_LEFT:
                x -= player_size
            if event.key == pygame.K_RIGHT:
                x += player_size
            player_pos[0] = x
    ventana.fill(color_negro)

    if enemy_pos[1] >= 0 and enemy_pos[1] < alto:
        enemy_pos[1] += 20
    else:
        enemy_pos[0] = random.randint(0, ancho - enemy_size)
        enemy_pos[1] = 0

    # Colisiones
    if detectar_colision(player_pos, enemy_pos):
        game_over = True
    # Dibujar enemigo
    pygame.draw.rect(
        ventana, color_azul, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    )
    # Dibujar jugador
    pygame.draw.rect(
        ventana, color_verde, (player_pos[0], player_pos[1], player_size, player_size)
    )

    clock.tick(30)
    pygame.display.update()
