import pygame

playerSpeed = 300
playerSize = 20


def Init_player(screen):
    global player_pos
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    

def Draw_Player(screen):
    pygame.draw.circle(screen, "blue", player_pos, playerSize)


def Input_Player(dt):
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= playerSpeed * dt
    if keys[pygame.K_s]:
        player_pos.y += playerSpeed * dt
    if keys[pygame.K_a]:
        player_pos.x -= playerSpeed * dt
    if keys[pygame.K_d]:
        player_pos.x += playerSpeed * dt