import pygame
import sys
import os

pygame.init()
size_screen = (800,300)
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Animation's Frog")
clock = pygame.time.Clock()
game_active = True
running = True
root_project = '/home/alvarog/Desktop/PygameDevelopment/AnimationsPygame/animationsinpygame'

class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        frame_1 = pygame.image.load(os.path.join(root_project,'assets/images/attack_1.png')).convert_alpha()
        frame_2 = pygame.image.load(os.path.join(root_project,'assets/images/attack_2.png')).convert_alpha()
        frame_3 = pygame.image.load(os.path.join(root_project,'assets/images/attack_3.png')).convert_alpha()
        frame_4 = pygame.image.load(os.path.join(root_project,'assets/images/attack_4.png')).convert_alpha()
        frame_5 = pygame.image.load(os.path.join(root_project,'assets/images/attack_5.png')).convert_alpha()
        frame_6 = pygame.image.load(os.path.join(root_project,'assets/images/attack_6.png')).convert_alpha()
        frame_7 = pygame.image.load(os.path.join(root_project,'assets/images/attack_7.png')).convert_alpha()
        frame_8 = pygame.image.load(os.path.join(root_project,'assets/images/attack_8.png')).convert_alpha()
        frame_9 = pygame.image.load(os.path.join(root_project,'assets/images/attack_9.png')).convert_alpha()
        frame_10 = pygame.image.load(os.path.join(root_project,'assets/images/attack_10.png')).convert_alpha()
        self.frame_list = [frame_1,frame_2,frame_3,frame_4,frame_5,frame_6,frame_7,frame_8,frame_9,frame_10]
        self.frame_index = 0
        
        self.image = self.frame_list[self.frame_index]
        self.rect = self.image.get_rect(bottomleft=(10,250))
        
        
    def animate_sprite(self):
        '''Increment the index for display different images.'''
        self.frame_index += 0.1
        if self.frame_index >=len(self.frame_list):
            self.frame_index = 0
        
        #cast to integer the frame index
        self.image = self.frame_list[int(self.frame_index)]
                
    def update(self):
        self.animate_sprite()

frog = Frog()
sprite_group = pygame.sprite.GroupSingle()
sprite_group.add(frog)
                

while running:
    #event pool
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
            
    screen.fill('white')
    sprite_group.draw(screen)
    sprite_group.update()    
    pygame.display.update()
    clock.tick(60)