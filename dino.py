# first make the classic dinosaur game
# make it in classes
# have an activate bot function? let it play unlimited on its own
# extend it to equip swords that can cut down cactus.
# bigger swords can cut bigger cactuses

# gonna need a:
'''
Classes:
cloud class -> done!
small cactus
large cactus 
bird
Background - Functions

'''

import pygame
import time
import random
import math
pygame.init()
# variables
winWidth = 800
winHeight = 500
SCREEN = pygame.display.set_mode((winWidth, winHeight))
# loading all the images duh :
RUNNING = [pygame.image.load("Assets/Dino/DinoRun1.png"),
        pygame.image.load("Assets/Dino/DinoRun2.png")]

DUCKING = [pygame.image.load("Assets/Dino/DinoDuck1.png"),
        pygame.image.load("Assets/Dino/DinoDuck2.png")]

JUMPING = pygame.image.load("Assets/Dino/DinoJump.png")

SMALLCACTUS = [pygame.image.load("Assets/Cactus/SmallCactus1.png"),
            pygame.image.load("Assets/Cactus/SmallCactus2.png"),
            pygame.image.load("Assets/Cactus/SmallCactus3.png")]

LARGECACTUS = [pygame.image.load("Assets/Cactus/LargeCactus1.png"),
            pygame.image.load("Assets/Cactus/LargeCactus2.png"),
            pygame.image.load("Assets/Cactus/LargeCactus3.png")]

BIRD = [pygame.image.load("Assets/Bird/Bird1.png"),
        pygame.image.load("Assets/Bird/Bird2.png")]

CLOUD = pygame.image.load("Assets/Other/Cloud.png")

BG = pygame.image.load("Assets/Other/Track.png")


class Dino:  # creating a class named dino
    X_POS = 100  # x running pos maybe?
    Y_POS = 300
    Y_POS_DUCK = 500
    # THIS IS THE VARIABLE THATS ALWAYS GONNA BE CONSTANT, WHEREAS THE jump_vel (lowercase) variable will be the one that will be changed all the time
    JUMP_VEL = 4.0
    JUMP_VAL = 12

    def __init__(self):
        self.duck_img = DUCKING  # these are the ducking images
        self.jump_img = JUMPING
        self.run_img = RUNNING

        self.dino_duck = False  # by default dino is not ducking
        self.dino_jump = False
        self.dino_run = True

        self.step_index = 0  # probably
        self.jump_vel = self.JUMP_VEL  # you can change the jump velocities of this
        # this could alternate between 0 and 1 so that it looks like the dino is running
        self.image = self.run_img[0]
        # allows to get pos of the dinosaur in any given time
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS  # x pos of the dino
        self.dino_rect.y = self.Y_POS  # y pos of the dino

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_jump = True
            self.dino_run = False

        if userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False

        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

    def duck(self):
        # this will give only 2 options becuase step_index is only from 0-9, so when floor division happens then we only get 0 or 1 which is what we want from our images list
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()  # coordinates of the rect image
        self.dino_rect.x = self.X_POS  # those have to be at X_POS that was defined earlier
        self.dino_rect.y = self.Y_POS_DUCK  # same as above
        self.step_index += 1  # step index increases by one

    def run(self):
        self.image = self.run_img[self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        self.dino_rect = self.image.get_rect()
        if self.dino_jump:  # go up
            self.Y_POS -= self.JUMP_VAL*1.8
            self.JUMP_VAL -= 1
            # eventually the jump_vel will become a negative value so it would start going down
        if self.JUMP_VAL < -12:  # it means its down
            self.JUMP_VAL = 12  # back to its normal constant value
            self.dino_jump = False
            self.dino_run = True

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.X_POS, self.Y_POS))


class Cloud:
    def __init__(self):  # init, update, draw
        self.image = CLOUD
        self.cloud_width = self.image.get_width()
        # 0+self.cloud_width, winWidth - self.cloud_width
        self.x = random.randint(800, 1000)
        self.y = random.randint(50, 100)
        
    def update(self):
        self.x -= gameSpeed
        if self.x < -self.cloud_width:
            self.x = random.randint(2000, 2300)
            self.y = random.randint(50,100)

    def draw(self,SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type): #3 parameters becase image and type can be changed so this class will be inherited for the cactus later on
        self.image = image #this image will be used to input the cactus later
        self.type = type  #this image will be used to input the type(for the array)
        self.rect = self.image[self.type].get_rect()
        self.rect.x= winWidth
    def update(self):
        self.rect.x -= gameSpeed
        if self.rect.x < -self.rect.width:
            obstacles.pop() #this will have an array later probably will have to go make this after writing all the cactus classes. What this does is simply delete the particular obstacle 
    def draw(self,SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
    
class SmallCactus(Obstacle): #inheriting from the obstacle class over here
    def __init__(self,image):
        self.type = random.randint(0,2)#in order to choose which image to use
        super().__init__(image,self.type)
        self.rect.y = 300
class LargeCactus(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 290

class Bird(Obstacle):
    def __init__(self,image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.x -= (gameSpeed)
        self.rect.y = 230
        self.index = 0
    def draw(self, SCREEN):
        if self.index>=9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5],self.rect)
        self.index +=1


global points

def main():
    global gameSpeed, obstacles, bg_x_pos,bg_y_pos
    run = True
    player = Dino()
    clock = pygame.time.Clock()
    gameSpeed = 10
    bgCloud = Cloud()
    obstacles = []
    deathCount = 0
    points = 0
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    def score():
        global gameSpeed
        points = points + 1
        if points % 100 == 0:
            gameSpeed +=1
        text = font.render("Points: "+ str(points),True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (500,40)
        SCREEN.blit(text,  textRect.center)

    def background():
        bg_x_pos = 0
        bg_y_pos = 380
        image_width = BG.get_width()
        SCREEN.blit(BG, (bg_x_pos, bg_y_pos))
        SCREEN.blit(BG, (image_width+bg_x_pos, bg_y_pos))
        if bg_x_pos <= -image_width:
            SCREEN.blit(BG, (image_width+bg_x_pos, bg_y_pos))
            bg_x_pos = 0
        bg_x_pos -= gameSpeed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles)==0:
            if random.randint(0,2)==0:
                obstacles.append(SmallCactus(SMALLCACTUS))
            if random.randint(0,2) ==1:
                obstacles.append(LargeCactus(LARGECACTUS))
            if random.randint(0,2) == 2:
                obstacles.append(Bird(BIRD))
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):#collision is very easy! maybe don't need any collision function
                pygame.time.delay(2000)
                deathCount += 1
                menu(deathCount)
        
        bgCloud.draw(SCREEN)
        bgCloud.update()
        background()
        score()
        clock.tick(30)
        pygame.display.update()
def menu(deathCount):
    global points
    run = True
    while run:
        SCREEN.fill((255,255,255))
        font = pygame.font.Font("freesansbold.ttf", 30)
        if deathCount == 0:
            text = font.render("Press any key to start", True, (0,0,0))
        elif deathCount>0:
            text = font.render("Press any key to restart", True, (0,0,0))
            score = font.render("Your score" + str(points), True, (0,0,0))
            scoreRect = (score.get_rect())
            scoreRect.center = (winWidth//2, winHeight//2+50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (winWidth//2,winHeight//2 + 20)
        SCREEN.blit(text,textRect)
        SCREEN.blit(RUNNING[0], (winWidth // 2 -
                    20, winHeight // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(deathCount=0)
pygame.quit()
