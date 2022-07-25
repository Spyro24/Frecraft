import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

H = 480
W = 640

window = pygame.display.set_mode([W, H])

def start_screen():
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont(None, 48)
    (C) = font.render('(c) Spyro24', True, WHITE)
    window.blit((C), (int(W - 190), int(H - 48)))
    pl = font.render("Play", True, WHITE)
    window.blit(pl, (int(W / 2 - 48), int(H / 2 - H / 8)))
    mp = font.render("MultiPlayer", True, WHITE)
    window.blit(mp, (int(W / 2 - 90), int(H / 2 - H / 20)))
    cd = font.render("Credits", True, WHITE)
    window.blit(cd, (int(W / 2 - 65), int(H / 2 + H / 20)))
    pygame.display.update()
    
start_screen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN.K_0:
            running = False

pygame.quit()