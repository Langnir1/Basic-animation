#IDEA / ALTER model
import pygame
import random

def main():
    #I - Import and initialize
    pygame.init()
    
    #D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("move a box!")
    
    #E - Entities (just background for now)
    background = pygame.image.load("cosmos.jpg")
    background = background.convert()
    background = pygame.transform.scale(background,(640, 480))
        
        #Loading an img
    sword = pygame.image.load("fire_sword.png")
    sword = sword.convert_alpha()
    sword = pygame.transform.scale(sword, (50, 150))
    
        #Img variables
    sword_x = 0
    sword_y = 200
    
    #A - Action (broken into ALTER steps)
        #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    dx = 5
    dy = 5
    
        #L - Set up main loop
    while keepGoing:
        
        #T - Timer to set frame rate
        clock.tick(30)
        
        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
            #sword value
        #check boundaries
        if (sword_x + 50) > screen.get_width():
            dx = random.randint(-15, -2)
            
        if sword_x < 0:
            dx = random.randint(2, 15)
        
        if (sword_y + 150) > screen.get_height():
            dy = random.randint(-15, -2)
        
        if sword_y < 0:
            dy = + random.randint(2, 15)
        #print(f"{sword_x=}, {dx=}")
        sword_x += dx
        sword_y += dy

        #R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(sword, (sword_x, sword_y))
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
