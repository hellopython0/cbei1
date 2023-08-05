import pygame
import os
#스크린 크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320
#색 정의
LAND = (160,120,40)
#초기화
pygame.init()
#창 이름
pygame.display.set_caption("Image")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

#그림 불러오기
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path,'assets')
background_image = pygame.image.load(os.path.join(assets_path,'terrain.png'))
mushroom_image1 = pygame.image.load(os.path.join(assets_path,'mushroom1.png'))
mushroom_image2 = pygame.image.load(os.path.join(assets_path,'mushroom2.png'))
mushroom_image3 = pygame.image.load(os.path.join(assets_path,'mushroom3.png'))

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(LAND)

    screen.blit(background_image,background_image.get_rect())
    screen.blit(mushroom_image1,[100,50])
    screen.blit(mushroom_image2,[250,130])
    screen.blit(mushroom_image3,[350,130])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()