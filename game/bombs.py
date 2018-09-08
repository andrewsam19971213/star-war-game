import pygame
class Bombs(pygame.sprite.Sprite):
    def __init__(self,scene,position):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene=scene
        self.image=[pygame.image.load("D:/python practice/bomb"+str(v)+".png").convert_alpha() for v in range(1,6)]
        self.index=0
        self.interval=4
        self.interval_index=0
        self.bomb_position=position
        self.visible=False
        self.otherairplane_alive=False
    def action(self):
        self.interval_index+=1
        if self.interval_index < self.interval:
            return
        self.interval_index=0
        self.index+=1
        if self.index >= len(self.image):
            self.index=0
            self.visible=False
            self.otherairplane_alive=True
    def draw(self,position):
        self.bomb_position=position
        self.main_scene.blit(self.image[self.index],self.bomb_position)