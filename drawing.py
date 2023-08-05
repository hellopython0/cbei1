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
    #font = pygame.font.SysFont('FixeSys',50,False,True)
    #text = font.render("made by Lucas",False,BLACK)
    pygame.draw.circle(screen,RED,[400,300],50,0)
    pygame.draw.circle(screen,RED,[300,400],50,0)
    pygame.draw.circle(screen,RED,[200,300],50,0)
    pygame.draw.circle(screen,RED,[300,200],50,0)
    pygame.draw.line(screen,BLUE,[300,200],[300,400],4)
    pygame.draw.line(screen,BLUE,[200,300],[400,300],4)
    pygame.draw.line(screen,GREEN,[200,300],[300,200],4)
    pygame.draw.line(screen,GREEN,[300,200],[400,300],4)
    pygame.draw.line(screen,GREEN,[400,300],[300,400],4)
    pygame.draw.line(screen,GREEN,[300,400],[200,300],4)
    pygame.draw.line(screen,RED,[200,200],[400,400],4)
    pygame.draw.line(screen,RED,[200,400],[400,200],4)
    pygame.draw.rect(screen,RED,[200,200,200,200],6)
    pygame.draw.circle(screen,GREEN,[300,300],100,4)
    pygame.draw.polygon(screen,BLACK,[[300,200],[200,400],[400,400]],4)
    pygame.draw.polygon(screen,BLACK,[[200,300],[400,200],[400,400]],4)
    pygame.draw.polygon(screen,BLACK,[[300,400],[200,200],[400,200]],4)
    pygame.draw.polygon(screen,BLACK,[[400,300],[200,200],[200,400]],4)
    pygame.draw.ellipse(screen,BLUE,[250,200,100,200],4)
    pygame.draw.ellipse(screen,BLUE,[200,250,200,100],4)
    #screen.blit(text,[400,400])
    #화면 업데이트
    pygame.display.flip()
    #초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()