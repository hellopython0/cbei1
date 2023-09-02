import pygame
import os
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
SKYBLUE = (100,100,255)

pygame.init()
pygame.display.set_caption("복습")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path,'assets')
fish_img = pygame.image.load(os.path.join(assets_path,'fish.png'))
running = True
dx = 0
dy = 0
x = 0
y = 0
width = fish_img.get_rect().width
height = fish_img.get_rect().height
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                dy = 5
            elif event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_LEFT:
                dx = -5
            elif event.key == pygame.K_RIGHT:
                dx = 5
        elif event.type == pygame.KEYUP:
            dx = 0
            dy = 0
    x += dx
    y += dy
    screen.fill(WHITE)
    pygame.draw.line(screen,RED,[50,50],[300,300],50)
    pygame.draw.line(screen,RED,[300,50],[50,300],50)
    pygame.draw.rect(screen,GREEN,[200,200,50,50],0)
    pygame.draw.circle(screen,BLACK,[300,300],15,3)
    font = pygame.font.SysFont("malgungothic",30,False,False)
    font1 = pygame.font.SysFont("malgungothic",10,False,False)
    text = font.render("안녕 파이게임",True,BLACK)
    text1 = font1.render("9월 2일 토요일",True,BLACK)
    screen.blit(text,[10,10])
    screen.blit(text1,[10,50])
    screen.blit(fish_img,[x,y])
    if x >= SCREEN_WIDTH - width:
        dx = 0
    if x <= 0:
        dx = 0
    if y >= SCREEN_HEIGHT - height:
        dy = 0
    if y <= 0:
        dy = 0
    pygame.display.flip()
    clock.tick(60)
pygame.quit()