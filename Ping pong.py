from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed,player_speedn2):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (50, 50))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.speed2 =player_speedn2

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite2(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (20, 120))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
       
class Player(GameSprite2):

   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < 370: #and self.rect.x < win_width - 80
           self.rect.y += self.speed
   def fire(self):
       bullet = Bullet('bullet.png', self.rect.x, self.rect.top, 10)
       bullets.add(bullet)


class Player2(GameSprite2):

   def update(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < 370:#and self.rect.x < win_width - 80
           self.rect.y += self.speed
   def fire(self):
       bullet = Bullet('bullet.png', self.rect.x, self.rect.top, 10)
       bullets.add(bullet)





#lost=0
#ball=0


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed2
        self.rect.x -= self.speed

        if self.rect.y >450 or self.rect.y < 0:
            self.speed2*=-1

            


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


player1 = Player('rocket.png', 665,  200, 4)
player2 = Player2('rocket.png', 10,  200, 4)
bullet=Bullet('bullet.png', 300,  410, 4,3)

665,  410
game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 35)
font = font.Font(None, 70)
win = font.render('Player 1 lose!', True, (240, 0, 0))
lose = font.render('Player 2 lose!', True, (240, 0, 0))



while game:
    '''text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
    text_ball = font1.render("Счёт: " + str(ball), 1, (255, 255, 255))'''
    for e in event.get():
        if e.type == QUIT:
           game = False
        

  
    if finish != True:
        window.blit(background,(0, 0))
        player1.update()
        player2.update()
        bullet.update()
        
        
        player1.reset()
        player2.reset()
        bullet.reset()
        #bullet.draw(window)
        #window.blit(text_lose, (5, 35))
        #window.blit(text_ball, (5, 5))

           
    '''if lost>=3:
        finish = True
        window.blit(lose, (210, 210))
    if ball>=10:
        finish = True
        window.blit(win, (210, 210))   '''
        
        
    '''if pygame.sprite.spritecollide(player1, bullet, True, True):
        ball+=1'''
    if bullet.rect.colliderect(player1):
        bullet.speed*=-1
    if bullet.rect.colliderect(player2):
        bullet.speed*=-1
    if bullet.rect.x >730:
       window.blit(lose, (210, 210)) 
    if bullet.rect.x <-40:
       window.blit(win, (210, 210))


    display.update()
    clock.tick(FPS)
