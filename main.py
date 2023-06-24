import math
import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
running = True
board = pygame.image.load("img/board.png")
cross = pygame.image.load("img/cross.png")
circle = pygame.image.load("img/circle.png")
turn = True
board_array = [None,None,None,
               None,None,None,
               None,None,None,]

win = [(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]

def get_pos(pos):
    return(math.floor(pos[0] / 100),math.floor(pos[1] / 100))

def draw_form(cross,i):
    screen.blit(cross,((i % 3) * 100, math.floor(i/3)*100))

def finish(winner):
    global board_array
    global turn
    if winner is None:
        t = "Match Nul !"
    elif winner is True:
        t = "Les Croix on gagné !"
    else:
        t = "Les cercle on gagné !"
    font = pygame.font.Font(None, 25)
    text = font.render(t, True, (255,0,0))
    text_rect = text.get_rect(center=(300/2, 300/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    board_array = [None,None,None,
               None,None,None,
               None,None,None,]
    turn = not winner


while running:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()


    screen.blit(board,(0,0))
    if pos is not None:
        p = get_pos(pos)
        if board_array[p[0] + p[1] * 3] is None:
            board_array[p[0] + p[1] * 3] = turn
            turn = not turn
            print(board_array)

    for i, type in enumerate(board_array):
        if type == True:
            draw_form(cross,i)
        elif type == False:
            draw_form(circle,i)

    for i in win:
        if board_array[i[0]] == board_array[i[1]] == board_array[i[2]] and board_array[i[0]] is not None and board_array[i[1]] is not None and board_array[i[2]] is not None:
            finish(board_array[i[0]])
            

    if None not in board_array:
        finish(None)
    pygame.display.flip()
    clock.tick(60)



pygame.quit()
