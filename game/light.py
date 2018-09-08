import pygame
class Light(pygame.sprite.Sprite):
    def __init__(self,image,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.visible=True
        self.light_goright=True
        self.light_goleft=False
    def reset(self,position):
        self.rect.left,self.rect.top=position