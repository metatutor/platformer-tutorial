import pygame

#declare window variables
bg_color = (0,0,0)
win_width,win_height = (500,500)
caption = "My First PyGame"

#pygame initialization code
pygame.init()
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption(caption)

while True:

    #event block
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    #update block




    #draw block
    win.fill(bg_color)

    
    #pygame updates
    pygame.display.update()
    pygame.time.delay(25)
