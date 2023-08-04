import pygame
from pygame.locals import *

pygame.init()


screen_height = 400
screen_width = 400
s_height_d = screen_height // 3
s_width_d = screen_width // 3

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

#define variables
line_width = int((s_height_d // (50/3)))
markers = []
clicked = False
pos = []
player = 1
game_over = False


#define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#define font
font = pygame.font.SysFont(None, 40)

#create play again rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2 + 10, 160, 50)


def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range (1,3):
        pygame.draw.line(screen, grid, (0, x * s_height_d), (screen_width, x * s_height_d), line_width)
        pygame.draw.line(screen, grid, (x * s_width_d, 0), (x * s_width_d, screen_height), line_width)


for x in range(3):
    row = [0] * 3
    markers.append(row)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                #                               (x_pos * 100       +        15          , y_pos *   100      +          15)         , (x_pos *     100   +      85             , y_pos *    100     +           85) 
                pygame.draw.line(screen, green, (x_pos * s_width_d + (s_width_d//(20/3)), y_pos * s_height_d + (s_height_d//(20/3))), (x_pos * s_width_d + (s_width_d//(20/17)), y_pos * s_height_d + (s_height_d//(20/17))), line_width) 
                #                               (x_pos * 100       +        15          , y_pos *   100      +          85)          , (x_pos *     100   +         85          , y_pos *   100      +           15)
                pygame.draw.line(screen, green, (x_pos * s_width_d + (s_width_d//(20/3)), y_pos * s_height_d + (s_height_d//(20/17))), (x_pos * s_width_d + (s_width_d//(20/17)), y_pos * s_height_d + (s_height_d//(20/3))), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * s_width_d + (s_width_d//2), y_pos * s_height_d + (s_height_d//2)), s_height_d//(50/19), line_width)
            y_pos += 1
        x_pos += 1



def check_winner():

    global winner
    global game_over

    y_pos = 0
    for x in markers:
        #check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        #check rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        
    #check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True



def draw_winner(winner):
    win_text = f'Player {str(winner)} wins!'
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = 'Play Again?'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 20))


run = True
while run:

    draw_grid()
    draw_markers()

    # add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // s_width_d][cell_y // s_height_d] == 0:
                # if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // s_width_d][cell_y // s_height_d] = player
                    player *= -1
                    check_winner()
        
    if game_over == True:
        draw_winner(winner)
        #check for mouseclick to see if user has clicked on Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variables
                markers = []
                pos = []
                player = 1
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    markers.append(row)


    pygame.display.update()

pygame.quit()