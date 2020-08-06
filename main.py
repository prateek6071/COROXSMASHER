import sys
import random as rand
import numbers
import pygame
import matplotlib.pyplot as plty
import math
import mixer
import time
from pygame import mixer
mixer.init()
pygame.init()


screen=pygame.display.set_mode((900,670))
background =pygame.image.load('battle.jpg')
pygame.display.set_caption("COROSMASHER")
pygame.display.set_icon(pygame.image.load('strong.png'))

sanimg=pygame.image.load('sanitizer.png')
sanitizerx=420
sanitizery=580
corimg=pygame.image.load('virus.png')
corimg2=pygame.image.load('virus.png')
corimg3=pygame.image.load('virus.png')
corimg4=pygame.image.load('virus.png')
corimg5=pygame.image.load('virus.png')
corx=450
corx2=450
corx3=450
corx4=450
corx5=450
cory=60
cory2=60
cory3=60
cory4=60
cory5=60
sanitizerxchange=3
sanitizerychange=0
corxchange=.1
corx2change=.1
corx3change=.1
corx4change=.1
corx5change=.1
corychange=.1
cory2change=.1
cory3change=.1
cory4change=.1
cory5change=.1
dropx=430
dropy=550
dropimg=pygame.image.load('drop.png')
dropxchange=0
dropychange=-10
totalscore=-4
myfont=pygame.font.SysFont("Verdana",24)

def dropmove(x,y):
    screen.blit(dropimg,(x,y))

def sanitizer( x, y):
    screen.blit(sanimg,(x,y))

def corona(x,y):
    screen.blit(corimg,(x,y))
def coronatwo(x, y):

    screen.blit(corimg2, (x, y))

def coronathree(x,y):
    screen.blit(corimg3,(x,y))

def coronafour(x,y):
    screen.blit(corimg4,(x,y))

def coronafive(x,y):
    screen.blit(corimg5,(x,y))

def iscollision(x1,y1,x2,y2):
    distance=math.sqrt( (   (x1-x2)*(x1-x2) ) + ( (y1-y2)*(y1-y2) )   )
    return distance

def iscollision2(x3,y3,x4,y4):
    distance2=math.sqrt( (   (x3-x4)*(x3-x4) ) + ( (y3-y4)*(y3-y4) )   )
    return distance2
def iscollision3(x5,y5,x6,y6):
    distance3=math.sqrt( (   (x5-x6)*(x5-x6) ) + ( (y5-y6)*(y5-y6) )   )
    return distance3
def iscollision4(x7,y7,x8,y8):
    distance4=math.sqrt( (   (x7-x8)*(x7-x8) ) + ( (y7-y8)*(y7-y8) )   )
    return distance4
def iscollision5(x9,y9,x10,y10):
    distance5=math.sqrt( (   (x9-x10)*(x9-x10) ) + ( (y9-y10)*(y9-y10) )   )
    return distance5



running =True
county=0

while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    mixer.music.load("bullet.mp3")
    mixer.music.play()
    totalscore1=totalscore
    label=myfont.render("Score=" + str(totalscore1),1,(0,255,0))
    screen.blit(label,(780,20))
    for event in pygame.event.get():



        if event.type == pygame.QUIT or ((  (cory>670 and cory4>670) and (cory2>670 and cory3>670)  ) and cory5>670):



            running =False

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                sanitizerxchange=-20
            if event.key==pygame.K_RIGHT:
                sanitizerxchange=20




            if event.type==pygame.KEYDOWN:

                sanitizerxchange=0
    sanitizerx=sanitizerx+sanitizerxchange
    dropx=dropx+sanitizerxchange
    dropy=dropy+dropychange
    if(dropy<50):
        dropy=550


    if sanitizerx <0:

        sanitizerx=0
        dropx=0




    if sanitizerx>800:


        sanitizerx=800
        dropx=800

    else:

        sanitizerxchange=0




    corx=corx+corxchange
    cory=cory+corychange
    if corx<0:
        corxchange=.1
        corychange=1
    if corx>750:
        corxchange=-.1
        corychange=1
    if iscollision(corx,cory,dropx,dropy) <27:
        mixer.music.load("ex.mp3")
        mixer.music.play()

        corx=rand.randint(0,700)
        cory=rand.randint(0,150)
        totalscore=totalscore+1

    corx2=corx2+corx2change
    cory2=cory2+cory2change
    if corx2 < 0:
        corx2change = .1
        cory2change = 1
    if corx2 > 750:
        corx2change = -.1
        cory2change = 1
    if iscollision2(corx2,cory2,dropx,dropy) <27 :
        mixer.music.load("ex.mp3")
        mixer.music.play()

        corx2= rand.randint(0, 700)
        cory2 = rand.randint(0, 150)
        totalscore=totalscore+1
    corx3 = corx3 + corx3change
    cory3 = cory3 + cory3change
    if corx3 < 0:
        corx3change = .1
        cory3change = 1
    if corx3 > 750:
        corx3change = -.1
        cory3change = 1
    if iscollision3(corx3,cory3,dropx,dropy) <27:
        mixer.music.load("ex.mp3")
        mixer.music.play()

        corx3 = rand.randint(0, 700)
        cory3 = rand.randint(0, 150)
        totalscore=totalscore+1
    corx4= corx4 + corx4change
    cory4 = cory4 + cory4change
    if corx4 < 0:
        corx4change = .1
        cory4change = 1
    if corx4 > 750:
        corx4change = -.1
        cory4change = 1
    if iscollision4(corx4,cory4,dropx,dropy) <27:
        mixer.music.load("ex.mp3")
        mixer.music.play()
        corx4 = rand.randint(0, 700)
        cory4 = rand.randint(0, 150)
        totalscore=totalscore+1
    corx5 = corx5 + corx5change
    cory5 = cory5 + cory5change
    if corx5 < 0:
        corx5change = .1
        cory5change = 1
    if corx5 > 750:
        corx5change = -.1
        cory5change = 1
    if iscollision5(corx5,cory5,dropx,dropy)<27:
        mixer.music.load("ex.mp3")
        mixer.music.play()

        corx5 = rand.randint(0, 700)
        cory5 = rand.randint(0, 150)
        totalscore=totalscore+1

    corx=corx+corxchange
    cory=cory+corychange

    corx2 = corx2 + corx2change
    cory2 = cory2 + cory2change

    corx3 = corx3 + corx3change
    cory3 = cory3 + cory3change

    corx4 = corx4 + corx4change
    cory4 = cory4 + cory4change
    corx5 = corx5 + corx5change
    cory5 = cory5 + cory5change

    sanitizer(sanitizerx,sanitizery)
    corona(corx,cory)
    coronatwo(corx2,cory2)
    coronathree(corx3,cory3)
    coronafour(corx4,cory4)
    coronafive(corx5,cory5)
    dropmove(dropx,dropy)
    if cory>670 and cory2>670:
        if cory3>670 and cory4>670:
            if cory5>670:
                gameoverscreen = pygame.display.set_mode((900, 670))
                Gameover = pygame.image.load('GameOver.png')
                gameoverscreen.blit(Gameover, (0, 0))

                #running=False
    pygame.display.update()

print(totalscore)
