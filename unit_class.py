import pygame

class Goomba:

    def __init__(self,starting_coords):

        self.sprite_num = 8 
        self.name = "goomba"
        self.dimensions = (50,50)
        self.jumping = False
        self.jump_vel = 20

#starting coordinates
        self.x=starting_coords[0]
        self.y=starting_coords[1]

#preparing sprite lists - loading sprites
        self.left_walking_sprites = []
        self.right_walking_sprites = []
        self.load_sprites()

#sprite- and position-related variables
        self.count = 0
        self.velocity = 0
        self.determine_sprite()

#use if there are pivoting sprites
        #self.reverse_lr = 0
        #self.reverse_rl = 0

    def determine_sprite(self):

        if self.count>=self.sprite_num*2:
            self.count = 0

        i = int(self.count/2)

        if self.velocity <0:
            self.current_sprite = self.left_walking_sprites[i]
        else: 
            self.current_sprite = self.right_walking_sprites[i]
        self.count+=1


    def load_sprites(self):
        for i in range(self.sprite_num):
            file_name = "Assets/"+self.name+"_"+str(i+1)+".png"
            self.left_walking_sprites.append(pygame.transform.scale(pygame.image.load(file_name),self.dimensions))
            self.right_walking_sprites.append(pygame.transform.flip(self.left_walking_sprites[i],True,False))
     
        self.current_sprite = self.left_walking_sprites[0]
        self.about_face = pygame.transform.scale(pygame.image.load("Assets/goomba_about_face.png"),self.dimensions)
        
#PIVOTING 
        #pivot from left to right
        #self.pivot_lr = pygame.transform.scale(pygame.image.load("Assets/goomba_pivot.png"),(60,60))
        #pivot from right to left
        #self.pivot_rl = pygame.transform.flip(self.pivot_lr,True,False)
        #about face
        #self.pivot_af = pygame.transform.scale(pygame.image.load("Assets/goomba_about_face.png"),(60,60))

    def patrol(self,left_bound,right_bound):
        
        if self.x <=left_bound:
            self.velocity = -self.velocity
#pivoting
            #self.reverse_lr = 3
        if self.x >=right_bound:
            self.velocity = -self.velocity
#pivoting
            #self.reverse_rl = 3

        self.determine_sprite()

        self.x += self.velocity

    def standby(self):
        self.velocity = 0
        self.current_sprite = self.about_face

    def move_left(self):
        self.velocity = -3
        self.determine_sprite()

    def move_right(self):
        self.velocity = 3
        self.determine_sprite()

    def update(self):
        self.x += self.velocity
        if self.jumping:
            self.y -= self.jump_vel
            self.jump_vel -=1

    def get_sprite(self):
        return self.current_sprite
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def fall(self,grav):
        self.y += grav

    def jump(self):
        self.jumping = True
        self.y -= self.jump_vel

    def hit_ground(self,val):
        self.jumping = False
        self.jump_vel = 20
        self.y=val-45

    def get_jump(self):
        return self.jumping
