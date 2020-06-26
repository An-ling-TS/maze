#tile.py
#瓦片类
import pygame
from py_.GLOBAL import *
class Tile(pygame.sprite.Sprite):
    def __init__(self,img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(img,(40,40))
        self.pos=pos
        self.size=TILED_SIZE
        self.rect=(pos[0],pos[1],40,40)
