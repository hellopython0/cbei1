import pygame

# 게임 스크린 크기
SCREEN_WIDTH = 800 # 가로 길이
SCREEN_HEIGHT = 800 # 세로 길이

# 색 정의
BLACK = (0,0,0) # 검은색
WHITE = (255,255,255) # 하얀색
RED = (255,0,0) # 빨간색
GREEN = (0,255,0) # 초록색
BLUE = (0,0,255) # 파란색

# 초기화
pygame.init()
# 창 이름
pygame.display.set_caption("그림그리기")
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
    #화면 삭제 구간
    #스크린 채우기
    screen.fill(WHITE)
    #화면 그리기 구간
    #화면 업데이트
    pygame.display.flip()
    #초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()