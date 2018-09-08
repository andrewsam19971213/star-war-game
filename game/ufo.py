import pygame
class Ufo(pygame.sprite.Sprite):
    def __init__(self,scene,image,position):
        pygame.sprite.Sprite.__init__(self)
        self.scene=scene
        self.image=pygame.image.load(image).convert_alpha()
        self.image1=[pygame.image.load("D:/python practice/ufo"+str(v)+".png").convert_alpha() for v in range(1,6)]
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.goright=True
        self.goleft=False
        self.appeared=False
        self.active=True
        self.bombhappen=False
        self.gameover=False
        self.ub_visible=False
        self.start=False
        self.ub_visible_index=0
        self.index=0
        self.interval=12
        self.interval_index=0
        self.health=10000
    def reset(self,position):
        self.rect.left,self.rect.top=position
    def action(self):
        self.interval_index+=1
        if self.interval_index < self.interval:
            return
        self.interval_index=0
        self.index+=1
        if self.index >= len(self.image1):
            self.index=0
            self.bombhappen=False
            self.gameover=True
    def draw(self,position):
        self.scene.blit(self.image1[self.index],position)
    def ub_revisible(self):
        self.ub_visible_index+=1
        if self.ub_visible_index==200:
            self.ub_visible=False
            self.ub_visible_index=0
            self.start=False