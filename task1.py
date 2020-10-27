import pygame,unit_class

#declare window variables
bg_color = (67, 148, 171)
win_width,win_height = (1000,1000)
caption = "PyGame Platformer Tutorial"

#pygame initialization code
pygame.init()
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption(caption)

player = unit_class.Goomba((100,100))

while True:

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        player.move_left()
    elif keys[pygame.K_d]:
        player.move_right()
    else:
        player.standby()

    #update block
    player.update()



    #draw block
    win.fill(bg_color)

    win.blit(player.get_sprite(),(player.get_x(),player.get_y()))

    #refresh pygame
    pygame.display.update()
    pygame.time.delay(25)
