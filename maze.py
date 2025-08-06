#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_size_x,player_size_y):
        super().__init__
        self.image=transform.scale(image.load(player_image),(player_size_x,player_size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>=6:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <450:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x >=0:
            self.rect.x -=self.speed
        if keys_pressed[K_d] and self.rect.x<=652:
            self.rect.x +=self.speed

class Enemy(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_size_x,player_size_y):
        super().__init__(player_image,player_x,player_y,player_speed,player_size_x,player_size_y)
        self.direction='left'
        self.direction1='w'
    def update(self):
        if self.direction=='left':
            self.rect.x+=self.speed
        if self.direction == 'right':
            self.rect.x-=self.speed
        if self.rect.x <=500:
            self.direction='left'
        if self.rect.x >625:
            self.direction='right'
    def update1(self):
        if self.direction1=='w':
            self.rect.y+=self.speed
        if self.direction1 == 's':
            self.rect.y-=self.speed
        if self.rect.y >=430:
            self.direction1='s'
        if self.rect.y <20:
            self.direction1='w'

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.width=wall_width
        self.height=wall_height
        self.image=Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

window=display.set_mode((700,500))
display.set_caption('Лабиинт')
background=transform.scale(image.load('background.jpg'),(700,500))

stena_1=Wall(11,113,215,60,0,10,410)
stena_2=Wall(11,113,215,60,480,10,310)

stena_3=Wall(11,113,215,60,480,165,10)
stena_4=Wall(11,113,215,60,400,100,10)

stena_5=Wall(11,113,215,215,10,10,100)
stena_7=Wall(11,113,215,215,280,10,200)
stena_6=Wall(11,113,215,150,180,10,230)

stena_8=Wall(11,113,215,215,280,100,10)
stena_9=Wall(11,113,215,215,200,155,10)
stena_10=Wall(11,113,215,215,350,155,10)
stena_11=Wall(11,113,215,360,200,10,150)

stena_12=Wall(11,113,215,150,10,10,200)

stena_13=Wall(11,113,215,150,10,70,10)

stena_14=Wall(11,113,215,150,10,10,200)

stena_15=Wall(11,113,215,220,100,70,10)

stena_16=Wall(11,113,215,430,100,10,100)

stena_17=Wall(11,113,215,430,200,280,10)

stena_18=Wall(11,113,215,430,280,10,200)

stena_19=Wall(11,113,215,280,420,70,10)

stena_20=Wall(11,113,215,300,430,10,60)

stena_21=Wall(11,113,215,200,480,240,10)

stena_22=Wall(11,113,215,430,270,70,10)

stena_23=Wall(11,113,215,490,280,10,20)

stena_24=Wall(11,113,215,345,100,35,10)

stena_25=Wall(11,113,215,345,50,45,50)

stena_26=Wall(11,113,215,290,10,10,100)

stena_27=Wall(11,113,215,430,50,100,10)
stena_28=Wall(11,113,215,380,50,10,60)

stena_29=Wall(11,113,205,290,0,300,10)

stena_30=Wall(11,113,205,590,0,10,200)
stena_31=Wall(11,113,205,490,130,100,10)

stena_32=Wall(11,113,205,440,480,1000,10)
stena_33=Wall(11,113,205,490,280,10,200)
stena_34=Wall(11,113,205,690,200,10,290)
hero=Player('hero.png',0,422,3,40,40)
cyborg=Enemy('cyborg.png',500,310,4,60,60)
cyborg1=Enemy('cyborg1.png',160,10,3,50,50)
cyborg2=Enemy('cyborg2.png',389,5,5,40,40)
treasure=GameSprite('treasure.png',620,390,0,60,60)
# hero=transform.scale(image.load('hero.png'),(60,60))
# cyborg=transform.scale(image.load('cyborg.png'),(60,60))
# treasure=transform.scale(image.load('treasure.png'),(60,60))


clock=time.Clock()
FPS=60
font.init()
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.71)
mixer.music.play()
money=mixer.Sound('money.ogg')
kick=mixer.Sound('kick.ogg')
font=font.Font(None,80)
win=font.render("YOU WIN!",True,(0,255,0))
lose=font.render("YOU LOSE!",True,(255,0,0))
finish=False
game=True
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
        if e.type==KEYDOWN:
            if e.key==K_r:
                hero.rect.x=0
                hero.rect.y=422
                mixer.music.play()
                finish=False




    if finish!=True:
        window.blit(background,(0,0))
        hero.reset()
        hero.update()
        cyborg.reset()
        cyborg.update()
        cyborg1.reset()
        cyborg1.update1()
        cyborg2.reset()
        cyborg2.update1()
        treasure.reset()
        stena_33.draw_wall()
        stena_34.draw_wall()
        stena_32.draw_wall()
        stena_31.draw_wall()
        stena_30.draw_wall()
        stena_29.draw_wall()
        stena_26.draw_wall()
        stena_28.draw_wall()
        stena_27.draw_wall()
        stena_25.draw_wall()
        stena_24.draw_wall()
        stena_22.draw_wall()
        stena_23.draw_wall()
        stena_1.draw_wall()
        stena_2.draw_wall()
        stena_3.draw_wall()
        stena_4.draw_wall()
        stena_5.draw_wall()
        stena_6.draw_wall()
        stena_7.draw_wall()
        stena_8.draw_wall()
        stena_9.draw_wall()
        stena_10.draw_wall()
        stena_11.draw_wall()
        stena_12.draw_wall()
        stena_13.draw_wall()
        stena_14.draw_wall()
        stena_15.draw_wall()
        stena_16.draw_wall()
        stena_17.draw_wall()
        stena_18.draw_wall()
        stena_19.draw_wall()
        stena_20.draw_wall()
        stena_21.draw_wall()
        if sprite.collide_rect(hero,treasure):
            finish=True
            money.play()
            window.blit(win,(250,250))
            mixer.music.stop()
        if sprite.collide_rect(hero,stena_1) or sprite.collide_rect(hero,stena_2) or sprite.collide_rect(hero,stena_3) or sprite.collide_rect(hero,stena_4):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_5) or sprite.collide_rect(hero,stena_6) or sprite.collide_rect(hero,stena_7) or sprite.collide_rect(hero,stena_8):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_9) or sprite.collide_rect(hero,stena_10) or sprite.collide_rect(hero,stena_11) or sprite.collide_rect(hero,stena_12):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_13) or sprite.collide_rect(hero,stena_14) or sprite.collide_rect(hero,stena_15) or sprite.collide_rect(hero,stena_16):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_17) or sprite.collide_rect(hero,stena_18) or sprite.collide_rect(hero,stena_19) or sprite.collide_rect(hero,stena_20):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_21) or sprite.collide_rect(hero,stena_22) or sprite.collide_rect(hero,stena_23) or sprite.collide_rect(hero,stena_24):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_25) or sprite.collide_rect(hero,stena_26) or sprite.collide_rect(hero,stena_27) or sprite.collide_rect(hero,stena_28):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_29) or sprite.collide_rect(hero,stena_30) or sprite.collide_rect(hero,stena_31) or sprite.collide_rect(hero,stena_32):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,stena_33) or sprite.collide_rect(hero,stena_34):
            kick.play()
            hero.rect.x=0
            hero.rect.y=422
        if sprite.collide_rect(hero,cyborg):
            finish=True
            kick.play()
            window.blit(lose,(250,250))
            mixer.music.stop()
        if sprite.collide_rect(hero,cyborg1):
            finish=True
            kick.play()
            window.blit(lose,(250,250))
            mixer.music.stop()
        if sprite.collide_rect(hero,cyborg2):
            finish=True
            kick.play()
            window.blit(lose,(250,250))
            mixer.music.stop()

            
    display.update()
    clock.tick(FPS)
    