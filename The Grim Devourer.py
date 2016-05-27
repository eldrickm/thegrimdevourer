#The Grim Devourer.
#Code Developer: Eldrick Millares
#Artist: Wes Withrow

#Imports Needed Modules and Such.
import pygame, sys, time
from pygame.locals import *

#Inititalizes Pygame
pygame.init()

#Sets Window
screen=pygame.display.set_mode((640, 400),0,32)
pygame.display.set_caption("The Grim Devourer")
pygame.font.init

#Assigns Variables to Sprites
bground="OfficialBackground.bmp"
char="playersprite1.png"
charun1="PlayerSpriteRun1.png"
charrun2="PlayerSpriteRun2.png"
char1l="PlayerSprite1Left.png"
charrun1l="PlayerSpriteRun1Left.png"
charrun2l="PlayerSpriteRun2Left.png"
oppo="EnemySprite.png"
ground="TopCenterGrass.bmp"
lefttopground="TopLeftGrass.png"
righttopground="TopRightGrass.png"
bottomground="BottomCenterGrass.png"
leftbottomground="BottomLeftGrass.png"
rightbottomground="BottomRightGrass.png"
pup="Powerup.png"
wat="Water.png"
sco="ScoreCounter.png"
over="GameOverScr.png"
rjum="PlayerSpriteJump.png"
ljum="PlayerSpriteJumpLeft.png"
box="Invisibox.png"
wan="WaterAni.png"
ens="EnemySpriteNS.png"

#Music Function!
sound="Tune1.mp3"
pygame.mixer.music.load(sound)
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(1)

#Converting Sprites
background=pygame.image.load(bground).convert()
player=pygame.image.load(char).convert_alpha()
playerstill=pygame.image.load(char).convert_alpha()
leftplayerstill=pygame.image.load(char1l).convert_alpha()
enemy=pygame.image.load(oppo).convert_alpha()
enemystill=pygame.image.load(oppo).convert_alpha()
tcgrass=pygame.image.load(ground).convert()
tlgrass=pygame.image.load(lefttopground).convert_alpha()
trgrass=pygame.image.load(righttopground).convert_alpha()
bcgrass=pygame.image.load(bottomground).convert_alpha()
blgrass=pygame.image.load(leftbottomground).convert_alpha()
brgrass=pygame.image.load(rightbottomground).convert_alpha()
powerup=pygame.image.load(pup).convert_alpha()
water=pygame.image.load(wat).convert_alpha()
score=pygame.image.load(sco).convert_alpha()
gameover=pygame.image.load(over).convert_alpha()
playerrun1=pygame.image.load(charun1).convert_alpha()
playerrun2=pygame.image.load(charrun2).convert_alpha()
lplayerrun1=pygame.image.load(charrun1l).convert_alpha()
lplayerrun2=pygame.image.load(charrun2l).convert_alpha()
rplayerjump=pygame.image.load(rjum).convert_alpha()
lplayerjump=pygame.image.load(ljum).convert_alpha()
invisibox=pygame.image.load(box).convert_alpha()
invisiboxrestart=pygame.image.load(box).convert_alpha()
waterani=pygame.image.load(wan).convert_alpha()
waterani2=pygame.image.load(wat).convert_alpha()
nsenemy=pygame.image.load(ens).convert_alpha()

#Coordinate Positioning for Moving Sprites
x,y=320,300
g,h=10,300

moveg, moveh= 0,0
movex, movey= 0,0

t = 260
b = 301

#Correct Direction Facing and Falling
face=False
jface=False
jump=False

#Death Sense
dead=False

#Setting Main Loop
while True:
#Exit Detection
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit
#Key Press Detection	
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				movex=-.4
				if int(x%2)==0:
					player=lplayerrun1
				if int(x%2)==1:
					player=lplayerrun2
				jface=True
			elif event.key == K_RIGHT:
				movex=+.4
				if int(x%2)==0:
					player=playerrun1
				if int(x%2)==1:
					player=playerrun2
				jface=False
			elif event.key == K_SPACE:
				movey=-.3
				if jface== False:
					player=rplayerjump
				if jface == True:
					player=lplayerjump
				jump=True
						

#Key Release Detection				
		if event.type == KEYUP:
			if event.key == K_LEFT:
				movex=0
				face=True
			elif event.key == K_RIGHT:
				movex=0
				face=False
			elif event.key == K_SPACE:
				movey=0
				if y != 300:
					movey=+.1
					if y<299:
						y=300
				if face==True:
					player=playerrun2
				if face==False:
					player=lplayerrun2
				jump=False

#Clock
	milli=pygame.time.get_ticks()
	seconds=int(milli/1000)
	time=seconds
#Score System
	if dead == False:
		win= "Score: " + str(time)
		font = pygame.font.Font(None, 30)
		text = font.render(win, 1, (250, 250, 250))
#Water Animation
	if seconds%2==0:
		water=waterani
	else:
		water=waterani2
				
#Develop Enemy AI
	if x > g:
		moveg=+.3
	elif x < g:
		moveg=-.3
	if y > h:
		moveh=+.045
	elif y < h:
		moveh=-.045

#Simple Physics Code
	if y < t:
		movey=+.02
	if x<=195:
		if y > b:
			y=300
	if x>=475:
		if y > b:
			y=300
	if x <=408.6:
		if x >= 285:
			if y > b:
				y=300
	if x >= 285:
		if x <= 408.6:
			if y > b:
				y = 300
	if x <285:
		if x > 195:
			movey=+.15
	if x > 195:
		if x < 285:
			movey=+.15
	if x > 408.6:
		if x < 475:
			movey=+.15
	if x < 475:
		if x > 408.6:
			movey=+.15
	if jump==False:
		if x <285: 
			if x > 195:
				movey=+.3
		if x > 195:
			if x < 285:
				movey=+.3
		if x > 408.6:
			if x < 475:
				movey=+.3
		if x < 475:
			if x > 408.6:
				movey=+.3

#Monster Jump Code and NoShadow
	if h < t:
		moveh=+.18
	if g<=195:
		if h> b:
			h=300
	if g>=475:
		if h > b:
			h=300
	if g <=408.6:
		if g >= 285:
			if h > b:
				h=300
	if g >= 285:
		if g <= 408.6:
			if h > b:
				h = 300

	if g <285:
		if g > 195:
			moveh=-.1
			enemy=nsenemy
	if g > 195:
		if g < 285:
			moveh=-.1
			enemy=nsenemy
	if g > 408.6:
		if g < 475:
			moveh=-.1
			enemy=nsenemy
	if g < 475:
		if g > 408.6:
			moveh=-.1
			enemy=nsenemy
	if h == 300:
		enemy=enemystill
#Directional Facing
	if movex == 0:
		if face==False:
			player=playerstill
		if face==True:
			player=leftplayerstill
#Grass Wall Collision
	if y > 350:
		movex=0

#BASIC GameOver Detection. Need to have Restart Mode and Clickable Items!
	if y > 390:
		dead=True

	o=round (x)
	p=round (y)
	u=round (g)
	i=round (h)
	dx =(o - u)
	dy =(p - i)
	distance = dx+dy

	if distance > -.3:
		if distance < .3:
			distance=0
	if distance < .3:
		if distance > -.3:
			distance = 0
	if distance == 0:
		dead=True
	if dead == True:
		invisibox = gameover
		(k,l) = pygame.mouse.get_pos()
		pygame.event.get()
		if event.type== MOUSEBUTTONDOWN:
			if k > 30 and k < 155:
				if l > 274 and l < 315:
					dead=False
					invisibox=invisiboxrestart
					x,y=320,300
					g,h=10,300
#Movement Code
	x+=movex
	y+=movey
	g+=moveg
	h+=moveh

#Wall Coding
	if x >= 620:
		movex=0
	if x <= 0:
		movex=0
#Blitting all Sprites
	screen.blit(background, (0,0))
	screen.blit(player, (x,y))
	screen.blit(enemy, (g,h))
	screen.blit(tlgrass, (300,325))
	screen.blit(tcgrass, (323,325))
	screen.blit(tcgrass, (345,325))
	screen.blit(trgrass, (368,325))
	screen.blit(blgrass, (300,350))
	screen.blit(bcgrass, (323,350))
	screen.blit(bcgrass, (345,350))
	screen.blit(brgrass, (368,350))
	screen.blit(water, (0,370))
	screen.blit(water, (50,370))
	screen.blit(water, (450,370))
	screen.blit(water, (100,370))
	screen.blit(water, (150,370))
	screen.blit(water, (200,370))
	screen.blit(water, (250,370))
	screen.blit(water, (300,370))
	screen.blit(water, (350,370))
	screen.blit(water, (400,370))
	screen.blit(water, (450,370))
	screen.blit(water, (500,370))
	screen.blit(water, (550,370))
	screen.blit(water, (600,370))
	screen.blit(water, (649,370))
	screen.blit(tlgrass, (0,325))
	screen.blit(tcgrass, (50,325))
	screen.blit(tcgrass, (100,325))
	screen.blit(trgrass, (150,325))
	screen.blit(blgrass, (0,350))
	screen.blit(bcgrass, (50,350))
	screen.blit(bcgrass, (100,350))
	screen.blit(brgrass, (150,350))
	screen.blit(tlgrass, (490,325))
	screen.blit(tcgrass, (540,325))
	screen.blit(trgrass, (590,325))
	screen.blit(blgrass, (490,350))
	screen.blit(bcgrass, (540,350))
	screen.blit(brgrass, (590,350))
	screen.blit(powerup, (0,0))
	screen.blit(invisibox, (0,0))
	screen.blit(score, (400, 5))
	screen.blit(text, (419,30))
	
	
#Updating the display for smooth animation.
	pygame.display.update()
