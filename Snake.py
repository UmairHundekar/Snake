
#You have to install pygame using pip in the terminal for the program to work
import pygame
pygame.init()

#Which way snake is moving
movingLeft = False
movingDown = False
movingUp = False
movingRight = False

import random

objectiveExists = False

objectiveX = 900
objectiveY = 900

addPiece = False

gameover = False

#Each block in the sanke
class PlayerPiece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, 50, 50))







(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))

playermovementCounter = 5

#A list of all the snakes blocks
snake = [PlayerPiece(400, 400)]

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Player movmeent
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                movingLeft = True
                movingDown = False
                movingUp = False
                movingRight = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                movingLeft = False
                movingDown = False
                movingUp = False
                movingRight = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                movingLeft = False
                movingDown = False
                movingUp = True
                movingRight = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                movingLeft = False
                movingDown = True
                movingUp = False
                movingRight = False
            if event.key == pygame.K_e:
                addPiece = True

    #Actaully moving the snake and seeing if it hit an objective and seeing if it lost.
    #Its moves it by adding a block of the snake to the front and removing one from the back of the list unless they get the objective
    playermovementCounter -= 1
    if playermovementCounter == 0:
        playermovementCounter = 5
        if movingDown:
            snake.append(PlayerPiece(snake[-1].x, snake[-1].y+50))
            if snake[-1].x == objectiveX * 50 and snake[-1].y == objectiveY * 50:
                addPiece = True
                objectiveExists = False
            if addPiece == False:
                snake.pop(0)
            else:
                addPiece = False
        if movingLeft:
            snake.append(PlayerPiece(snake[-1].x - 50, snake[-1].y))
            if snake[-1].x == objectiveX * 50 and snake[-1].y == objectiveY * 50:
                addPiece = True
                objectiveExists = False
            if addPiece == False:
                snake.pop(0)
            else:
                addPiece = False
        if movingUp:
            snake.append(PlayerPiece(snake[-1].x, snake[-1].y - 50))
            if snake[-1].x == objectiveX * 50 and snake[-1].y == objectiveY * 50:
                addPiece = True
                objectiveExists = False
            if addPiece == False:
                snake.pop(0)
            else:
                addPiece = False
        if movingRight:
            snake.append(PlayerPiece(snake[-1].x + 50, snake[-1].y))
            if snake[-1].x == objectiveX * 50 and snake[-1].y == objectiveY * 50:
                objectiveExists = False
                addPiece = True
            if addPiece == False:
                snake.pop(0)
            else:
                addPiece = False
    if len(snake) > 1:
        for block in snake[0:-2]:
            if snake[-1].x == block.x and snake[-1].y == block.y:
                gameover = True
    
    if -1 > snake[-1].x or snake[-1].x > 801:
        gameover = True
    
    if -1 > snake[-1].y or snake[-1].y > 801:
        gameover = True


    #Creates background grid
    for i in range(0, 16):

        for l in range(0, 16):
            
            if not i % 2:
                if l % 2:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i * 50, l * 50, 50, 50))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i * 50, l * 50, 50, 50))
            else:
                if l % 2:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i * 50, l * 50, 50, 50))
                else:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i * 50, l * 50, 50, 50))
    

    #The snake objective
    if objectiveExists:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(objectiveX * 50, objectiveY * 50, 50, 50))
    else:
        noSelected = True
        
        while noSelected:
            listNoSelected = False
            objectiveX = random.randint(0, 15)
            objectiveY = random.randint(0, 15)
            for block in snake:
                if objectiveX * 50 == block.x and objectiveY * 50 == block.y:
                    listNoSelected = True
            
            if listNoSelected == False:
                objectiveExists = True
                noSelected = False


    if gameover:
        running = False

    for block in snake:
        block.draw()

    pygame.display.update()