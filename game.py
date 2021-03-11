import sys, pygame, time,os


pygame.init()

screenSize = width, height = 500, 400

screen = pygame.display.set_mode(screenSize)
menu = pygame.transform.scale(pygame.image.load(r'C:\Users\bianc\Desktop\Jogo\Sprites\menu.jpg').convert(), screenSize)
#menu = pygame.transform.scale(menu, (500, 400))
#time.sleep(3)

while 1:
    screen.blit(menu, (0, 0)) 

    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()
    
