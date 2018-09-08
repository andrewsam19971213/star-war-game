import pygame
import random
class Supplies(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=random.randint(0,750),-65
        self.supply_speed=1
        self.index=0
        self.visible=True
    def reset(self):
        self.rect.left,self.rect.top=random.randint(0,750),-65
    def reset1(self):
        if self.visible==False:
            self.index+=1
            if self.index==750:
                self.visible=True
                self.index=0    