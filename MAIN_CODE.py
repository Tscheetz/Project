##created by JACK MATSON '19 and TRISTAN SHEETZ '19

# code taken from F-Prime  at https://github.com/f-prime/FlappyBird
# rolling background from here https://youtu.be/US3HSusUBeI
#importing libraries
## tristan found the overall code on Github
import pygame 
from pygame.locals import *  
import sys
import random
import os
#jack and tristan both worked on trying to create a main menu but were unsuccessful and so progress was taken out of the code 
#under imput allowing the user to choose the theme of the game 
#jack make the user imput 
theme = input("Choose your theme: (space, beach, original, mario, pro) ")
#class of FlappyBird
class FlappyBird:
    def __init__(self):
        #size of playing screen 
        self.screen = pygame.display.set_mode((400, 708))
        #size of images
        self.bird = pygame.Rect(65, 50, 50, 50) 
        #if statement depending on the user imput for the theme 
        #jack made this theme 
        if theme == "space": 
            #the background in the game from the folder 'assets'
            self.background = pygame.image.load("assets/background3.png").convert()
            #the images of the bird from assets 
            # 1 is stagnant 
            # 2 is jumping 
            # dead/3 is the death image when the user hit an obstacle 
            self.birdSprites = [pygame.image.load("assets/ufo.png").convert_alpha(),
                                pygame.image.load("assets/ufo2.png").convert_alpha(),
                                pygame.image.load("assets/ufo3.png")]
            #the obstacles in the game from the folder
            #bottom wall
            self.wallUp = pygame.image.load("assets/lightsaber3.png").convert_alpha()
    ##attempt at rolling background 
    ##did not work, covered whole screen blocking out bird 
    #jack wrote out code from youtube 
            # def events():
	        #     for event in pygame.event.get():
		    #         if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			#             pygame.quit()
			#             sys.exit()
            # # define display surface			
            # #W, H = 576, 1024
            # W, H = 400, 708
            # HW, HH = W / 2, H / 2
            # AREA = W * H
            # os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"
            # # setup pygame
            # pygame.init()
            # CLOCK = pygame.time.Clock()
            # DS = pygame.display.set_mode((W, H))
            # #pygame.display.set_caption("code.Pylet - Scrolling Background Image")
            # FPS = 120
            # bkgd = pygame.image.load("assets/background1.png").convert()
            # x = 0
            # # main loop
            # while True:
	        #     events()
	        #     rel_x = x % bkgd.get_rect().width
	        #     DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
	        #     if rel_x < W:
	        #     	DS.blit(bkgd, (rel_x, 0))
	        #     x -= 1
	        #     #pygame.draw.line(DS, (255, 0, 0), (rel_x, 0), (rel_x, H), 3)
	        #     pygame.display.update()
	        #     CLOCK.tick(FPS)
            #top wall
            self.wallDown = pygame.image.load("assets/lightsaber2.png").convert_alpha()
        #jack made this theme 
        if theme == "beach": 
            self.background = pygame.image.load("assets/background4.png").convert()
            self.birdSprites = [pygame.image.load("assets/beachball.png").convert_alpha(),
                                pygame.image.load("assets/beachball.png").convert_alpha(),
                                pygame.image.load("assets/explosion.gif")]
            self.wallUp = pygame.image.load("assets/tree.png").convert_alpha()
            self.wallDown = pygame.image.load("assets/tree2.png").convert_alpha()
        #tristan made this theme 
        if theme == "original":
            self.background = pygame.image.load("assets/background2.png").convert()
            self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                                pygame.image.load("assets/2.png").convert_alpha(),
                                pygame.image.load("assets/dead.png")]
            self.wallUp = pygame.image.load("assets/OGbottom.png").convert_alpha()
            self.wallDown = pygame.image.load("assets/OGtop.png").convert_alpha()
        #tristan made this theme 
        if theme == "mario": 
            self.background = pygame.image.load("assets/background1.png").convert()
            self.birdSprites = [pygame.image.load("assets/mar1.png").convert_alpha(),
                                pygame.image.load("assets/mar1.png").convert_alpha(),
                                pygame.image.load("assets/marDead.png")]
            self.wallUp = pygame.image.load("assets/mariobottom.png").convert_alpha()
            self.wallDown = pygame.image.load("assets/OGtop.png").convert_alpha()
        #tristan made this theme 
        if theme == "pro": 
            self.background = pygame.image.load("assets/background1.png").convert()
            self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                                pygame.image.load("assets/2.png").convert_alpha(),
                                pygame.image.load("assets/dead.png")]
            self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
            self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
            
        #changes the distance between obstacles 
        # both jack and tristan edited ironed out the kinks in the code to make it smoother and more like the original game 
        #wall gape was made smaller
        self.gap = 140
        #the first wall was put further back so user and get used to game and have time for first walls 
        self.wallx = 500
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        #user = alive 
        self.dead = False
        self.sprite = 0 
        #counter begins at 0
        self.counter = 0
        self.offset = random.randint(-110, 110)
        #jack tried to get sounds to work
        #the sound file was not a '.wav' and ultimately was unable to be accessed 
        ##dead = pygame.mixer.Sound('deathsound.')
        ##dead.play()
        ##jump = pygame.mixer.Sound('sound.')
        ##jump.play()
    def updateWalls(self):
        #jack and tristan made 'if' statement with 'pro' theme 
        #jack and tristan tested out the perameters of the pro setting 
        #jack and tristan adjusted accordingly to what could be handeled in the pro setting 
        if theme == "pro":
                #walls move faster towards you 
                self.wallx -= 6
                #the gap inbetween the walls is smaller making the game more difficult 
                self.gap = 110
                # the gravity is increased making the user fall quicker and need to jump more 
                self.gravity = 8
        #this is the normal speed for the wall 
        self.wallx -= 5
        if self.wallx < -80:/
            self.wallx = 550
            #this is the addition of one point every time the user gets through a wall
            self.counter += 1
            #wall randomization 
            #this is the randomization of the reoccuring walls 
            self.offset = random.randint(-110, 110)

    def birdUpdate(self):
        if self.jump:
            #this is the speed at which the bird jumps 
            self.jumpSpeed -= 1
            #this is the location of the bird when the user jumps
            self.birdY -= self.jumpSpeed
            #this is the height of the users jump
            self.jump -= 1
        else:
            #gravity setttings for the bird
            self.birdY += self.gravity
            self.gravity += 0.3
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
        if upRect.colliderect(self.bird):
            self.dead = True
        if downRect.colliderect(self.bird):
            self.dead = True
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-110, 110)
            self.gravity = 5

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        #this is the font and size of the score 
        font = pygame.font.SysFont("Arial", 60)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #key commands for the bird to jump, uses all of the keys 
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 12
#variation of the walls 
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            if not self.dead:
                self.sprite = 0
            self.updateWalls()
            self.birdUpdate()
            pygame.display.update()

if __name__ == "__main__":
    #class of FlappyBird running 
    FlappyBird().run()
