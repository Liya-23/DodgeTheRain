import pygame
import time
pygame.init()

white = (51, 51, 51)
black = (0, 0, 0)
blue = (0, 0, 225)
red = (255, 0, 0)

dis = pygame.display.set_mode((300, 800))
pygame.display.set_caption('Dodge That Ish')

def gameLoop():
    game_over = False
    game_close = False
    x1 = 150
    y1 = 700
    h1 = 100
    v1 = 200
    
    x1_change = 0       
    y1_change = 0
    h1_change = 0
    v1_change = 0
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! R-Restart or Q-Quit", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.key == pygame.K_r:
                    gameLoop()
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.K_ESCAPE:
                game_over = True    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    v1_change = 10
                    h1_change = 0 
        if x1 >= 290 or x1 < 10 or v1 <=0:
            game_over = True
                    
        v1 += v1_change
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, 10, 10])
        pygame.draw.rect(dis, blue, [h1, v1, 10, 10])
        pygame.draw.rect(dis, blue, [h1+40, v1+20, 10, 10])
        pygame.draw.rect(dis, blue, [h1+70, v1+40, 10, 10])
        pygame.draw.rect(dis, blue, [h1+100, v1+60, 10, 10])
        pygame.draw.rect(dis, blue, [h1+130, v1+80, 10, 10])
        pygame.display.update()
    
        clock.tick(30)

pygame.quit()
quit()