import pygame
import random
import os

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (20,60,120)
ORANGE = (250,170,70)
RED = (255,0,0)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 900

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path,"assets")

class Ball():
    def __init__(self,bounce_sound):
        self.rect = pygame.Rect(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,12,12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 5
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0:
            self.dx *= -1.01
            self.rect.left = 0
            self.bounce_sound.play()
        elif self.rect.right > SCREEN_WIDTH:
            self.dx *= -1.01
            self.rect.right = SCREEN_WIDTH
            self.bounce_sound.play()
    def reset(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.dx = random.randint(-3,3)
        self.dy = 5
    def draw(self,screen):
        pygame.draw.rect(screen,ORANGE,self.rect,0)

class Player():
    def __init__(self,ping_sound):
        self.rect = pygame.Rect(SCREEN_WIDTH//2,SCREEN_HEIGHT-40,500000,150)
        self.ping_sound = ping_sound
        self.dx = 0
    def update(self,ball):
        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        elif self.rect.right >= SCREEN_WIDTH and self.dx > 0:
            self.dx = 0
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5,5)
            ball.dy *= -1.01
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()
        self.rect.x += self.dx
    def draw(self,screen):
        pygame.draw.rect(screen,RED,self.rect)

class Enemy():
    def __init__(self,pong_sound):
        self.rect = pygame.Rect(SCREEN_WIDTH//2,0,500000,40)
        self.pong_sound = pong_sound
    def update(self,ball):
        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            if diff > 4:
                self.rect.x -= 4
            else:
                self.rect.centerx = ball.rect.centerx
        elif self.rect.centerx < ball.rect.centerx:
            diff =  ball.rect.centerx - self.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x += 4
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5,5)
            ball.dy *= -1.01
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()
    def draw(self,screen):
        pygame.draw.rect(screen,BLACK,self.rect)

class Game():
    def __init__(self):
        bounce_sound = pygame.mixer.Sound(os.path.join(assets_path,"bounce.wav"))
        ping_sound = pygame.mixer.Sound(os.path.join(assets_path,"ping.wav"))
        pong_sound = pygame.mixer.Sound(os.path.join(assets_path,"pong.wav"))
        self.font = pygame.font.SysFont("malgungothic",50,False,False)
        self.ball = Ball(bounce_sound)
        self.player = Player(ping_sound)
        self.enemy = Enemy(pong_sound)
        self.player_score = 0
        self.enemy_score = 0
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx = -10
                elif event.key == pygame.K_RIGHT:
                    self.player.dx = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0
        return True
    def run_logic(self):
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)
        if self.ball.rect.top < 0:
            self.player_score += 1
            self.ball.reset(self.player.rect.centerx,self.player.rect.centery)
        elif self.ball.rect.bottom > SCREEN_HEIGHT:
            self.enemy_score += 1
            self.ball.reset(self.enemy.rect.centerx,self.enemy.rect.centery)
    def display_message(self,screen,message,color):
        label = self.font.render(message,True,color)
        width = label.get_width()
        height = label.get_height()
        pos_x = SCREEN_WIDTH//2 - (width / 2)
        pos_y = SCREEN_HEIGHT // 2 - (height / 2)
        screen.blit(label,(pos_x,pos_y))
        pygame.display.update()
    def display_frame(self,screen):
        screen.fill(BLUE)
        if self.player_score == 10:
            self.display_message(screen,"승리",WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        elif self.enemy_score == 10:
            self.display_message(screen,"패배",WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        else:
            self.ball.draw(screen)
            self.player.draw(screen)
            self.enemy.draw(screen)

            for x in range(0,SCREEN_WIDTH,24):
                pygame.draw.rect(screen,WHITE,[x,SCREEN_HEIGHT//2,10,10])
            enemy_score_label = self.font.render("적 "+str(self.enemy_score),True,WHITE)
            screen.blit(enemy_score_label,(10,260))
            player_score_label = self.font.render("나 "+str(self.player_score),True,WHITE)
            screen.blit(player_score_label,(10,340))

def main():
    pygame.init()
    pygame.display.set_caption("핑퐁게임")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()
    running = True
    while running:
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()
main()