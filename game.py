import sys, pygame, time,os

## VARIABLES:


screenSize = width, height = 500, 400
characterSize = width, height = 100, 50
BLACK = (0, 0, 0)
fps = 60
location = 2
posX = 200
posY = 350
menuSelection = True
gameStart = False
isGaming = True
pygame.init()
screen = pygame.display.set_mode(screenSize)

## CLASSES AND FUNCTIONS:
class Player(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.images = []
      img = pygame.transform.scale(pygame.image.load(r"C:\Users\bianc\Desktop\Jogo\PythonGame\Sprites\character.png").convert(), characterSize)
      self.images.append(img)
      self.image = self.images[0]
      self.rect = self.image.get_rect()



#Loading images
menu = pygame.transform.scale(pygame.image.load(r'C:\Users\bianc\Desktop\Jogo\PythonGame\Sprites\menu.png').convert(), screenSize)
menuPlay = pygame.transform.scale(pygame.image.load(r'C:\Users\bianc\Desktop\Jogo\PythonGame\Sprites\menuPlay.png').convert(), screenSize)
menuCredits = pygame.transform.scale(pygame.image.load(r'C:\Users\bianc\Desktop\Jogo\PythonGame\Sprites\menuCredits.png').convert(), screenSize)
menuExit = pygame.transform.scale(pygame.image.load(r'C:\Users\bianc\Desktop\Jogo\PythonGame\Sprites\menuExit.png').convert(), screenSize)
testeCreditos = pygame.transform.scale(pygame.image.load(r'C:\Users\bianc\Desktop\Jogo\PythonGame\Sprites\creditosTeste.png').convert(), screenSize)
telaPreta = pygame.transform.scale(pygame.image.load(r'C:\Users\bianc\Desktop\Jogo\PythonGame\Sprites\blackScreen.png').convert(), screenSize)

## INITS:
clock = pygame.time.Clock()
screen.blit(menu, (0, 0)) 
worldBox =  screen.get_rect()

#Player init
player = Player() 
player_list = pygame.sprite.Group()
player_list.add(player) 
player.rect.y = posY 


## THE GAME:
while isGaming:
   # CONTROLS:
   for event in pygame.event.get():
      if event.type == pygame.QUIT: #QUIT GAME
         isGaming = False
         sys.exit() 
      
      # MENU:
      if menuSelection:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: #MENU SELECTION
               location += 1
               if location > 2: location = 0
            
            if event.key == pygame.K_DOWN: #MENU SELECTION
               location -= 1
               if location < 0: location = 2
                     
            if event.key == pygame.K_RETURN: #PLAYER PRESSED ENTER
               if location == 2: #Starts game
                  gameStart = True 
                  menuSelection = False  
               elif location == 1: screen.blit(testeCreditos, (0, 0)) #Game credits
               elif location == 0: 
                  isGaming = False
                  sys.exit() #Exit game
               else: screen.fill(BLACK) #ERROR          
         
         if location == 2:
            screen.blit(menuPlay, (0, 0)) #"Play" selection image 
         elif location == 1:   
            screen.blit(menuCredits, (0, 0)) #"Credits" selection image
         else:
            screen.blit(menuExit, (0, 0)) #"Exit" selection image
   
   # GAME:
   if gameStart:
      if pygame.key.get_pressed()[pygame.K_RIGHT]: #CHARACTER GOES RIGHT
         if posX + characterSize[0] < screenSize[0]:
            posX += 5
      if pygame.key.get_pressed()[pygame.K_LEFT]: #CHARACTER GOES RIGHT
         if posX > 0:
            posX -= 5   
      player.rect.x = posX 
      screen.blit(telaPreta, worldBox)
      player_list.draw(screen)
      pygame.display.flip()
   
   clock.tick(fps) 
   pygame.display.update()
    
