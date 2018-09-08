import pygame
class Bossairplane(pygame.sprite.Sprite):
    def __init__(self,scene,imagename,position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene=scene
        self.image=pygame.image.load(imagename).convert_alpha()
        self.image1=[pygame.image.load("D:/python practice/bossairplane"+str(v)+".png").convert_alpha() for v in range(1,6)]
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.index=0
        self.interval=7
        self.index_interval=0
        self.bombhappen=False
        self.boss_relive=False
        self.boss_speed=speed
        self.active=True
        self.add_other_speed=False
        self.mask=pygame.mask.from_surface(self.image)
    def reset(self,position):
        self.rect.left,self.rect.top=position
        self.active=True
        self.add_other_speed=True
    def action(self):
        self.index_interval+=1
        if self.index_interval < self.interval:
            return
        self.index_interval=0
        self.index+=1
        if self.index >= len(self.image1):
            self.index=0
            self.bombhappen=False
            self.boss_relive=True
    def draw(self,position):
        self.main_scene.blit(self.image1[self.index],position)