import pygame
class Airplane(pygame.sprite.Sprite):
    def __init__(self,scene,filename,position,speed=10):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene=scene
        self.image=pygame.image.load(filename).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.airplane_speedx=speed
        self.airplane_speedy=speed
        self.blood_len=100
        self.mask=pygame.mask.from_surface(self.image)
        self.active=True
        self.switch_name=True
    def Upmove(self):
        self.airplane_speedy=-10
        self.Y_bolen=True
    def Downmove(self):
        self.airplane_speedy=10
        self.Y_bolen=True
    def Leftmove(self):
        self.airplane_speedx=-10
        self.X_bolen=True
    def Rightmove(self):
        self.airplane_speedx=10
        self.X_bolen=True
    def health(self,scene,color,x,y):
        pygame.draw.rect(scene,color,(x,y,self.blood_len,10))
    def reset(self,position):
        self.rect.left,self.rect.top=position
        self.active=True