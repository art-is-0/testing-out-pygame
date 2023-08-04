import pygame

pygame.init()

SCREEN_WIDGH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDGH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:
    
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        if player.centerx <= 0:
            pass
        else:
            player.move_ip(-1, 0)
    
    elif key[pygame.K_d] == True:
        if player.centerx >= SCREEN_WIDGH:
            pass
        else:
            player.move_ip(1, 0)

    elif key[pygame.K_w] == True:
        if player.centery <= 0:
            pass
        else:
            player.move_ip(0, -1)

    elif key[pygame.K_s] == True:
        if player.centery >= SCREEN_HEIGHT:
            pass
        else:
            player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit