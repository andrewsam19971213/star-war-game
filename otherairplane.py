import pygame
class Otherairplane(pygame.sprite.Sprite):
    def __init__(self,imagename,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imagename).convert_alpha()
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.left,self.rect.top=self.x,self.y
        self.o_speed=speed
        self.active=True
        self.mask=pygame.mask.from_surface(self.image)
    def reset(self,x,y):
        self.x=x
        self.y=y
        self.rect.left,self.rect.top=self.x,self.y
        self.active=True