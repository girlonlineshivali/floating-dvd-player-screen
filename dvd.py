import pygame, time
# installs packages 

pygame.init()
#initiates pygame 

width, height = 800, 600
#screen size

dvdLogoSpeed = [1, 1]
#speed of logo moving around 

backgroundColor = 255, 0 , 0 

screen = pygame.display.set_mode((width, height))
#creates the screen 

dvdLogo = pygame.image.load("dvdlogo.png")
dvdLogoRect = dvdLogo.get_rect()
#uploads the image 

#forever loop
while True:
    screen.fill(backgroundColor)

    screen.blit(dvdLogo, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

    if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
        dvdLogoSpeed[0] = -dvdLogoSpeed[0]
    if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
        dvdLogoSpeed[1] = -dvdLogoSpeed[1]
    #allows the dvd to bounce off the screen, instead of the image disappearing 

    pygame.display.flip()
    #reset screen
    
    time.sleep(10 / 1000)
