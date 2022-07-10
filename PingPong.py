from pygame import *
import random 

win = display.set_mode((1600,900),FULLSCREEN)
display.set_caption('PingPong ultra 3000 for two players')
background = transform.scale(
    image.load('resourse/background.jpg'),(1600,900)
)

class Sprite(sprite.Sprite):
    def __init__(self,x,y,width,height,speed,file_name):
        super().__init__()
        self.image = transform.scale(
            image.load(file_name),(width,height)
        )
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def PAintObjekt(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(Sprite):
    def DvigRight (self):
        keysDown = key.get_pressed()
        if keysDown [K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keysDown [K_DOWN] and self.rect.y < 750:
            self.rect.y += self.speed 
    def DvigLeft (self):
        keysDown = key.get_pressed()
        if keysDown [K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keysDown [K_s] and self.rect.y < 750:
            self.rect.y += self.speed

class Ball(Sprite):
    def __init__(self,x,y,width,height,speed,file_name):
        super().__init__(x,y,width,height,speed,file_name)
        self.nap_x = random.choice((-1,1))
        self.nap_y = random.choice((-1,1))
        self.score_left = 0
        self.score_right = 0
    def AvtoMove(self):
        global LeftSchet
        global RightSchet
        self.rect.y += self.speed * self.nap_y
        self.rect.x += self.speed * self.nap_x
        if self.rect.y < 0 or self.rect.y > 850:
            self.nap_y = self.nap_y * (-1)
        if self.rect.x < 0:
            self.rect.x = 800
            self.rect.y = 450
            self.score_right += 1
            RightSchet = shrift.render(str(self.score_right),True,(235, 1, 1))
            self.nap_x = random.choice((-1,1))
            self.nap_y = random.choice((-1,1))
        elif self.rect.x > 1550:
            self.rect.x = 800
            self.rect.y = 450
            self.score_left += 1
            LeftSchet = shrift.render(str(self.score_left),True,(235, 1, 1))
            self.nap_x = random.choice((-1,1))
            self.nap_y = random.choice((-1,1))

PlayerRight = Player(1430,200,150,250,8,'resourse/ra.png')
PlayerLeft = Player(20,200,150,250,8,'resourse/ra.png')
ball = Ball(800,450,50,50,6,'resourse/mya.png')

font.init()
shrift = font.Font('resourse/OLDENGL.TTF',50)
DveTochki = shrift.render(str(':'),True,(235, 1, 1))
LeftSchet = shrift.render(str(ball.score_left),True,(235, 1, 1))
RightSchet = shrift.render(str(ball.score_right),True,(235, 1, 1))
            
game = True
clock = time.Clock()
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
                exit()
    win.blit(background,(0,0))
    PlayerRight.PAintObjekt()
    PlayerRight.DvigRight()
    PlayerLeft.PAintObjekt()
    PlayerLeft.DvigLeft()
    ball.PAintObjekt()
    ball.AvtoMove()
    win.blit(DveTochki,(800,3))
    win.blit(LeftSchet,(730,4))
    win.blit(RightSchet,(860,4))
    if sprite.collide_rect(PlayerRight,ball) or sprite.collide_rect(PlayerLeft,ball):
       ball.nap_x = ball.nap_x * (-1)
       ball.nap_y = random.uniform(-1,1)
    display.update()                
    clock.tick(144)