import pygame
import time
import sys
from pygame.locals import *
import math
import random

'''
#movements

w = up arrow = up
s = down arrow = down
d = right arrow = right
a = left arrow = left
1 = anticlockwise(A-C)
2 = clockwise(C)
note: if you want sound effects then searcg mixer in code and incomment it
'''




pygame.init() # function

t0=time.time()

width=500
height=500

disp=pygame.display.set_mode((width,height)) # making display (width,height)


white=(245,245,245) # defining colors (R,G,B)
white1=(255,255,255)
watermark1=(200,200,200)
watermark=(230,230,230)
black=(0,0,0)
red=(255,0,0)
red1=(255,50,50)
blue=(0,0,255)

pygame.display.set_caption("snakegame") # making caption

apple = pygame.image.load('apple.jpg')
apple_SIZE=(30,30)
apple = pygame.transform.scale(apple, apple_SIZE)

x=250
y=250
vx=0.000000001 # to avoid gleech of 'Game over' at starting
vy=0 
v=5
snake_size=9
fps=90
n=0
score=0
positions=[]
position=[x,y]
positions.append(position)
position=[]

aim_x=random.randint(23,500)
aim_y=random.randint(23,500)

apple_POSITION=(aim_x,aim_y)
disp.blit(apple,apple_POSITION)

clock=pygame.time.Clock()


game_exit=False # becomes True when player wants to exit
game_over=False # becomes True when player looses game


def refresh():
	
	disp.fill(white)
	global right 
	right = pygame.draw.rect(disp,watermark,[400,420,90,70])
	global left 
	left = pygame.draw.rect(disp,watermark,[20,420,90,70])
	global exit 
	exit = pygame.draw.rect(disp,red1,[420,10,70,50])	
		
	myfont = pygame.font.SysFont("",30)
	label = myfont.render("A-C", 1,watermark1)
	disp.blit(label, (45,450))
		
	myfont = pygame.font.SysFont("",30)
	label = myfont.render("C", 1,watermark1)
	disp.blit(label, (445,450))
		
	myfont = pygame.font.SysFont("",30)
	label = myfont.render("exit(q)",1,white1)
	disp.blit(label, (425,25))
	
	myfont = pygame.font.SysFont("",50)
	label = myfont.render("score= "+str(score), 1,watermark1)
	disp.blit(label, (25,18))
	
	global positions
	
	myfont = pygame.font.SysFont("",50)
	label = myfont.render(str(positions),1,watermark1)
	disp.blit(label, (1000,50))

	#positions=[]
	
	

while not game_exit: # creating game loop till game_exit==False
	
	x=250
	y=250
	vx=0.000000001 # to avoid gleech of 'Game over' at starting
	vy=0
	score=0
	refresh() 
	regame=False
	stop_game=False
	positions=[]
	
	while not regame and not game_exit:

		for event in pygame.event.get():
			print(event)
			if event.type==pygame.QUIT:
				game_exit = True
	
	        
			if event.type == pygame.MOUSEBUTTONDOWN: # runs when we touch screen
				if right.collidepoint(event.pos) and stop_game==False:
					vx=v*int(math.sin(1.5707963268*n))
					vy=-v*int(math.cos(1.5707963268*n))
					n+=1
				
				elif left.collidepoint(event.pos) and stop_game==False:
					vx=-v*int(math.sin(1.5707963268*n))
					vy=v*int(math.cos(1.5707963268*n))
					n-=1
					
				elif exit.collidepoint(event.pos):
					game_exit=True
					
					
			if event.type == pygame.KEYDOWN: # runs when we touch screen
		
				if event.key == pygame.K_2 :
					vx=v*(math.sin(1.5707963268*n))
					vy=-v*math.cos(1.5707963268*n)
					n+=1
					print('key pressed')
					
				if event.key == pygame.K_1 :
					vx=-v*(math.sin(1.5707963268*n))
					vy=v*math.cos(1.5707963268*n)
					n-=1
					print("key pressed")
					
				if event.key == pygame.K_q:
					game_exit = True
						
			if event.type == pygame.KEYDOWN: # runs when we type button
			
				if event.key == pygame.K_RIGHT and vx!=-v and stop_game==False :
					vx=v	
					vy=0
					
					print('key pressed')
					
				if event.key == pygame.K_LEFT and vx!=v and stop_game==False :
					vx=-v
					vy=0
	
					print("key pressed")
					
				if event.key == pygame.K_UP and vy!=v and stop_game==False :
					vx=0
					vy=-v
					
				if event.key == pygame.K_DOWN and vy!=-v and stop_game==False :
					vx=0
					vy=v
					
					print("key pressed")
####			
													
				if event.key == pygame.K_d and vx!=-v and stop_game==False :
					vx=v	
					vy=0
					
					print('key pressed')
					
				if event.key == pygame.K_a and vx!=v and stop_game==False :
					vx=-v
					vy=0
	
					print("key pressed")
					
				if event.key == pygame.K_w and vy!=v and stop_game==False :
					vx=0
					vy=-v
					
				if event.key == pygame.K_s and vy!=-v and stop_game==False :
					vx=0
					vy=v
					
					print("key pressed")
					
				if event.key == pygame.K_q:
					game_exit = True

				if event.key == pygame.K_r:
					regame = True
					
		x+=vx
		y+=vy
		
		if x<=12:
			vx=0
			vy=0
			myfont = pygame.font.SysFont("Arial",30)
			label = myfont.render("GAME OVER (r to restart)", 1,red)
			disp.blit(label, (80,220))
			'''if stop_game==False:
				pygame.mixer.Sound('game_over.mp3').play()
			stop_game=True'''
			
			if event.type == pygame.KEYDOWN: # runs when we type button		
				if event.key == pygame.K_r :
					regame=True												
	#		x=2080
	
		if y<=12:
			vx=0
			vy=0
			myfont = pygame.font.SysFont("Arial",30)
			label = myfont.render("GAME OVER (r to restart)", 1,red)
			disp.blit(label, (80,220))
			'''if stop_game==False:
				pygame.mixer.Sound('game_over.mp3').play()	
			stop_game=True'''
			
			if event.type == pygame.KEYDOWN: # runs when we type button		
				if event.key == pygame.K_r : # not working
					regame=True						
	#		y=1205
	
		if x>=485:
			vx=0
			vy=0
			myfont = pygame.font.SysFont("Arial",30)
			label = myfont.render("GAME OVER (r to restart)", 1,red)
			disp.blit(label, (80,220))
			'''if stop_game==False:
				pygame.mixer.Sound('game_over.mp3').play()
			stop_game=True'''
			
			if event.type == pygame.KEYDOWN: # runs when we type button		
				if event.key == pygame.K_r :# not working
					regame=True		
	#		x=0
	
		if y>=485:
			vx=0
			vy=0
			myfont = pygame.font.SysFont("Arial",30)
			label = myfont.render("GAME OVER (r to restart)", 1,red)
			disp.blit(label, (80,220))
			'''if stop_game==False:
				pygame.mixer.Sound('game_over.mp3').play()		
			stop_game=True'''
			
			if event.type == pygame.KEYDOWN: # runs when we type button		
				if event.key == pygame.K_r :# not working
					regame=True
	#		y=0
	
		if abs(x-aim_x)<=25 and abs(y-aim_y)<=25:
			score+=10
			aim_x=random.randint(30,470)
			aim_y=random.randint(30,470)
			
			apple_POSITION=(aim_x,aim_y)

			'''pygame.mixer.Sound('food.mp3').play()'''
			#refresh()
			
			#game_exit=True
		
		
		#aim=pygame.draw.rect(disp,blue,[aim_x,aim_y,snake_size,snake_size])
		disp.blit(apple,apple_POSITION)
#		snake=pygame.draw.rect(disp,black,[x,y,snake_size,snake_size])
		
		for a,b in positions:
	
			snake=pygame.draw.circle(disp,black,[a,b],snake_size,0)
								
										
		boundry=pygame.draw.rect(disp, (0, 100, 255), (0, 0, 500, 500), 8)  # width = 8
		
		position=[x,y]
		if positions.count(position)==0:
			positions.append(position)
			if len(positions)>score+1:
				del positions[0]
			
		elif positions.count(position)!=0:
			vx=0
			vy=0

			myfont = pygame.font.SysFont("Arial",30)
			label = myfont.render("GAME OVER (r to restart)", 1,red)
			disp.blit(label, (80,220))
			'''if stop_game==False:
				pygame.mixer.Sound('game_over.mp3').play()
			stop_game=True'''
			
			if event.type == pygame.KEYDOWN: # runs when we type button		
				if event.key == pygame.K_r :
					regame=True
	#		
	#	position=[]
	 
	#	pygame.display.flip(),	
		clock.tick(fps)
		pygame.display.update()
		refresh()
		
					
					
pygame.quit() # quit game after game_exit==True
quit()
