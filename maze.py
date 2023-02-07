from pygame import*

mixer.init()

mixer.music.load('jungles.ogg')
mixer.music.play(-1)
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

font.init()
font = font.Font(None,100)
win = font.render('YOU WIN!',True,(255,215,0))
lose = font.render('YOU LOSE!',True,(180,0,0))

fps = 60
w = 1200
h = 800
mw = display.set_mode((w,h))
display.set_caption('Maze')
back = transform.scale(image.load('background.jpg'),(w,h))

class GameSprite(sprite.Sprite):
    def __init__(self,picture, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (60,60)).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self,col_1,col_2,col_3,x,y,w,h):
        super().__init__()
        self.col_1 = col_1
        self.col_2 = col_2
        self.col_3 = col_3
        self.w = w
        self.h = h
        self.image = Surface((self.w,self.h))
        self.image.fill((col_1,col_2,col_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

clock = time.Clock()

hero = GameSprite('hero.png',4,0,h-100)
cyborg = GameSprite('cyborg.png',2,w-225,h-350)
treasure = GameSprite('treasure.png',0,w-185,h-150)
wall_1 = Wall(13,160,0,100,100,10,600)
wall_2 = Wall(13,160,0,100,100,100,10)
wall_3 = Wall(13,160,0,200,0,10,110)
wall_4 = Wall(13,160,0,300,0,10,110)
wall_5 = Wall(13,160,0,300,100,100,10)
wall_6 = Wall(13,160,0,100,200,100,10)
wall_7 = Wall(13,160,0,100,400,200,10)
wall_8 = Wall(13,160,0,300,400,10,200)
wall_9 = Wall(13,160,0,200,600,110,10)
wall_10 = Wall(13,160,0,200,700,10,100)
wall_11 = Wall(13,160,0,200,700,100,10)
wall_12 = Wall(13,160,0,400,600,10,200)
wall_13 = Wall(13,160,0,400,600,100,10)
wall_14 = Wall(13,160,0,500,600,10,100)
wall_15 = Wall(13,160,0,200,300,300,10)
wall_16 = Wall(13,160,0,300,200,10,100)
wall_18 = Wall(13,160,0,300,200,100,10)
wall_19 = Wall(13,160,0,500,0,10,200)
wall_20 = Wall(13,160,0,500,200,100,10)
wall_21 = Wall(13,160,0,600,200,10,100)
wall_22 = Wall(13,160,0,200,500,10,100)
wall_23 = Wall(13,160,0,400,300,10,100)
wall_24 = Wall(13,160,0,400,400,500,10)
wall_25 = Wall(13,160,0,600,400,10,200)
wall_26 = Wall(13,160,0,600,300,100,10)
wall_27 = Wall(13,160,0,700,100,10,210)
wall_28 = Wall(13,160,0,600,100,100,10)
wall_29 = Wall(13,160,0,800,0,10,100)
wall_30 = Wall(13,160,0,800,100,100,10)
wall_31 = Wall(13,160,0,700,600,10,200)
wall_32 = Wall(13,160,0,700,700,100,10)
wall_33 = Wall(13,160,0,500,500,100,10)
wall_34 = Wall(13,160,0,900,200,10,500)
wall_35 = Wall(13,160,0,900,200,200,10)
wall_36 = Wall(13,160,0,900,0,10,110)
wall_37 = Wall(13,160,0,1000,100,10,100)
wall_38 = Wall(13,160,0,1000,100,100,10)
wall_39 = Wall(13,160,0,1100,100,10,110)
wall_40 = Wall(13,160,0,800,400,10,200)
wall_41 = Wall(13,160,0,900,700,10,100)

game = True
end = False

direction = 'left'

while game:
    
    mw.blit(back,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if end != True:
        keys = key.get_pressed()
        if keys[K_a] and hero.rect.x > 0:
            hero.rect.x -= hero.speed
        if keys[K_d] and hero.rect.x <= w-55:
            hero.rect.x += hero.speed
        if keys[K_s] and hero.rect.y <= h-55:
            hero.rect.y += hero.speed
        if keys[K_w] and hero.rect.y > 0:
            hero.rect.y -= hero.speed

        if cyborg.rect.x <= 925:
            direction = 'right'
        if cyborg.rect.x >= w - 105:
            direction = 'left'

        if direction == 'left':
            cyborg.rect.x -= cyborg.speed
        else:
            cyborg.rect.x += cyborg.speed

        hero.reset()
        cyborg.reset()
        treasure.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
        wall_11.draw_wall()
        wall_12.draw_wall()
        wall_13.draw_wall()
        wall_14.draw_wall()
        wall_15.draw_wall()
        wall_16.draw_wall()
        wall_18.draw_wall()
        wall_19.draw_wall()
        wall_20.draw_wall()
        wall_21.draw_wall()
        wall_22.draw_wall()
        wall_23.draw_wall()
        wall_24.draw_wall()
        wall_25.draw_wall()
        wall_26.draw_wall()
        wall_27.draw_wall()
        wall_28.draw_wall()
        wall_29.draw_wall()
        wall_30.draw_wall()
        wall_31.draw_wall()
        wall_32.draw_wall()
        wall_33.draw_wall()
        wall_34.draw_wall()
        wall_35.draw_wall()
        wall_36.draw_wall()
        wall_37.draw_wall()
        wall_38.draw_wall()
        wall_39.draw_wall()
        wall_40.draw_wall()
        wall_41.draw_wall()

        if sprite.collide_rect(hero,cyborg) or sprite.collide_rect(hero,wall_1) or sprite.collide_rect(hero,wall_2) or sprite.collide_rect(hero,wall_3) or sprite.collide_rect(hero,wall_4) or sprite.collide_rect(hero,wall_5) or sprite.collide_rect(hero,wall_6) or sprite.collide_rect(hero,wall_7) or sprite.collide_rect(hero,wall_8) or sprite.collide_rect(hero,wall_9) or sprite.collide_rect(hero,wall_10) or sprite.collide_rect(hero,wall_11) or sprite.collide_rect(hero,wall_12) or sprite.collide_rect(hero,wall_13) or sprite.collide_rect(hero,wall_14) or sprite.collide_rect(hero,wall_15) or sprite.collide_rect(hero,wall_16) or sprite.collide_rect(hero,wall_18) or sprite.collide_rect(hero,wall_19) or sprite.collide_rect(hero,wall_20) or sprite.collide_rect(hero,wall_21) or sprite.collide_rect(hero,wall_22) or sprite.collide_rect(hero,wall_23) or sprite.collide_rect(hero,wall_24) or sprite.collide_rect(hero,wall_25) or sprite.collide_rect(hero,wall_26) or sprite.collide_rect(hero,wall_27) or sprite.collide_rect(hero,wall_28) or sprite.collide_rect(hero,wall_29) or sprite.collide_rect(hero,wall_30) or sprite.collide_rect(hero,wall_31) or sprite.collide_rect(hero,wall_32) or sprite.collide_rect(hero,wall_33) or sprite.collide_rect(hero,wall_34) or sprite.collide_rect(hero,wall_35) or sprite.collide_rect(hero,wall_36) or sprite.collide_rect(hero,wall_37) or sprite.collide_rect(hero,wall_38) or sprite.collide_rect(hero,wall_39) or sprite.collide_rect(hero,wall_40):
            end = True
            mw.blit(lose,(450,200))
            kick.play()

        if sprite.collide_rect(hero,treasure):
            end = True
            mw.blit(win,(450,200))
            money.play()
    
    if sprite.collide_rect(hero,cyborg) or sprite.collide_rect(hero,wall_1) or sprite.collide_rect(hero,wall_2) or sprite.collide_rect(hero,wall_3) or sprite.collide_rect(hero,wall_4) or sprite.collide_rect(hero,wall_5) or sprite.collide_rect(hero,wall_6) or sprite.collide_rect(hero,wall_7) or sprite.collide_rect(hero,wall_8) or sprite.collide_rect(hero,wall_9) or sprite.collide_rect(hero,wall_10) or sprite.collide_rect(hero,wall_11) or sprite.collide_rect(hero,wall_12) or sprite.collide_rect(hero,wall_13) or sprite.collide_rect(hero,wall_14) or sprite.collide_rect(hero,wall_15) or sprite.collide_rect(hero,wall_16) or sprite.collide_rect(hero,wall_18) or sprite.collide_rect(hero,wall_19) or sprite.collide_rect(hero,wall_20) or sprite.collide_rect(hero,wall_21) or sprite.collide_rect(hero,wall_22) or sprite.collide_rect(hero,wall_23) or sprite.collide_rect(hero,wall_24) or sprite.collide_rect(hero,wall_25) or sprite.collide_rect(hero,wall_26) or sprite.collide_rect(hero,wall_27) or sprite.collide_rect(hero,wall_28) or sprite.collide_rect(hero,wall_29) or sprite.collide_rect(hero,wall_30) or sprite.collide_rect(hero,wall_31) or sprite.collide_rect(hero,wall_32) or sprite.collide_rect(hero,wall_33) or sprite.collide_rect(hero,wall_34) or sprite.collide_rect(hero,wall_35) or sprite.collide_rect(hero,wall_36) or sprite.collide_rect(hero,wall_37) or sprite.collide_rect(hero,wall_38) or sprite.collide_rect(hero,wall_39) or sprite.collide_rect(hero,wall_40):
        mw.blit(lose,(450,200))

    if sprite.collide_rect(hero,treasure):
        mw.blit(win,(450,200))

    clock.tick(fps)

    display.update()