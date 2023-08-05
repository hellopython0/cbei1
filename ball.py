import pygame

# 게임 스크린 크기
SCREEN_WIDTH = 2000 # 가로 길이
SCREEN_HEIGHT = 900 # 세로 길이

# 색 정의
BLACK = (0,0,0) # 검은색
WHITE = (255,255,255) # 하얀색
RED = (255,0,0) # 빨간색
GREEN = (0,255,0) # 초록색
BLUE = (0,0,255) # 파란색

ball_x = SCREEN_WIDTH / 2
ball_y = SCREEN_HEIGHT / 2
ball_dx = 100
ball_dy = 500
ball_size = 90
# 초기화
pygame.init()
# 창 이름
pygame.display.set_caption("Ball")
# 창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# 게임화면 업데이트 속도
clock = pygame.time.Clock()
# 게임종료여부
done = False
# 게임 반복 구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #게임 로직 구간
    ball_x += ball_dx
    ball_y += ball_dy

    if (ball_x + ball_size) > SCREEN_WIDTH or (ball_x - ball_size) < 0:
        ball_dx *= -1
    if (ball_y + ball_size) > SCREEN_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy *= -1
    #화면 삭제 구간
    #스크린 채우기
    screen.fill(WHITE)
    #화면 그리기 구간
    pygame.draw.circle(screen,RED,[ball_x,ball_y],ball_size,0)
    pygame.draw.circle(screen,BLUE,[ball_x,ball_y],ball_size-30,0)
    pygame.draw.circle(screen,GREEN,[ball_x,ball_y],ball_size-60,0)
    #화면 업데이트
    pygame.display.flip()
    #초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()