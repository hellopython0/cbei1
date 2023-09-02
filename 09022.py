import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
pygame.init()
pygame.display.set_caption("과녁")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
x = int(SCREEN_WIDTH/2) + 10
y = int(SCREEN_HEIGHT/2)
dx = 5
dy = 5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += dx
    y += dy
    screen.fill(BLACK)
    pygame.draw.circle(screen,RED,[x,y],50,0)
    pygame.draw.circle(screen,GREEN,[x,y],25,0)
    pygame.draw.circle(screen,BLUE,[x,y],12.5,0)
    if x >= SCREEN_WIDTH - 50 or x - 50 <= 0:
        dx *= -1.001
    if y >= SCREEN_HEIGHT - 50 or y - 50 <= 0:
        dy *= -1.001
    pygame.display.flip()
    clock.tick(60)
pygame.quit()