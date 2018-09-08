import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,filename1,x,y,speed=60):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename1).convert_alpha()
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.left,self.rect.top=self.x,self.y
        self.bullet_speed=speed
        self.fire_speed=-50
        self.mask=pygame.mask.from_surface(self.image)
        self.btbolen=True
        self.fire_btbolen=False
    def move(self):
        self.bullet_speed=-50
        self.btbolen=True