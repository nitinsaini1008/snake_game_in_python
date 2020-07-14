import pygame
import random

def draw_snake(color,snk,snake_len):
	for i in snk:
		pygame.draw.rect(gamewindow,color,[i[0],i[1],snake_len,snake_len])
white=(200,200,200)
x=pygame.init()
gamewindow=pygame.display.set_mode((800,600))
pygame.display.set_caption("Nitin's Game")
def game_start():
	s=0

	font = pygame.font.Font('freesansbold.ttf', 32) 
	text=font.render("Score"+str(s),True,(0,200,0),(0,0,200))
	react_text=text.get_rect()
	react_text.center=(10,10)

	#---------------------
	snake_x=400
	snake_y=300
	snane_size=10
	snane_lenght=10
	snake_color=(10,10,10)
	game_over=False

	factor=0.5
	snake_l=False
	snake_r=False
	snake_u=False
	snake_d=False
	snk_arr=[]
	#---------------------

	fruit_x=100
	fruit_y=100
	fruit_size=10
	fruit_color=(100,10,10)

	exit_game=False
	while not exit_game:
		if game_over==True:
			gamewindow.fill(white)
			over=font.render("GAME OVER \n Score"+str(s)+"\n Press Enter to play again",True,(0,200,0),(0,0,200))
			react_over=text.get_rect()
			react_over.center=(200,200)
			gamewindow.blit(over,react_over)
			for i in pygame.event.get():
				if i.type==pygame.QUIT:
					exit_game=True
				if i.type==pygame.KEYDOWN:
					if i.key==pygame.K_RETURN:
						print("restart")
						game_start()
				

		else:
			for i in pygame.event.get():
				if i.type==pygame.QUIT:
					exit_game=True
			
				if i.type==pygame.KEYDOWN:
					if i.key==pygame.K_UP:
						snake_u=True
						snake_l=False
						snake_r=False
						snake_d=False
					if i.key==pygame.K_DOWN:
						snake_u=False
						snake_l=False
						snake_r=False
						snake_d=True
					if i.key==pygame.K_LEFT:
						snake_u=False
						snake_l=True
						snake_r=False
						snake_d=False
					if i.key==pygame.K_RIGHT:
						snake_u=False
						snake_l=False
						snake_r=True
						snake_d=False
			
			if snake_u==True:
				snake_y-=factor
			if snake_d==True:
				snake_y+=factor
			if snake_l==True:
				snake_x-=factor
			if snake_r==True:
				snake_x+=factor
			snk_arr.append([snake_x,snake_y])
			if len(snk_arr)>=snane_lenght:
				snk_arr.pop(0)
			if s>=1:
				for e in range(2,len(snk_arr)):
					if (snk_arr[e][0]==snk_arr[0][0]) and (snk_arr[e][1]==snk_arr[0][1]):
						game_over=True

			if (snk_arr[0][0]==800 or snk_arr[0][0]==0) or (snk_arr[0][1]==0 or snk_arr[0][1]==600):
				game_over=True
				print("over\n\n\n")
			if (snake_x-10<fruit_x and snake_x+10>fruit_x) and (snake_y-10<fruit_y and snake_y+10>fruit_y):
				fruit_x=random.randint(10,500)
				fruit_y=random.randint(10,500)
				s+=1
				snane_lenght+=10
			text=font.render("Score"+str(s),True,(0,200,0),(0,0,200))
			react_text=text.get_rect()
			react_text.center=(100,10)
			gamewindow.fill(white)
			gamewindow.blit(text,react_text)
			draw_snake(snake_color,snk_arr,snane_size)
			#pygame.draw.rect(gamewindow,snake_color,[snake_x,snake_y,snane_lenght,snane_size])
			pygame.draw.rect(gamewindow,fruit_color,[fruit_x,fruit_y,fruit_size,fruit_size])
		pygame.display.update()
game_start()
pygame.quit()
quit()
