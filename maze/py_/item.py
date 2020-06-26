#item.py
#事件精灵
#用于创建胜利精灵,对话精灵等
from py_.GLOBAL import *
import pygame
class Item(pygame.sprite.Sprite):
    def __init__(self,pos,kind,name):
        pygame.sprite.Sprite.__init__(self)
        #精灵位置
        self.pos=pos
        #精灵种类
        self.kind=kind
        #精灵名
        self.name=name
        self.rect=pygame.Rect(pos[0],pos[1],40,40)
        if kind==Elves.VICTORY:
            self.image=pygame.transform.scale(pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\dlam_01.png'),(40,40))
            #self.image=pygame.transform.scale(pygame.image.load(r'G:\python_pro\maze\resource\picture\robot\images\dlam_01.png'),(40,40))
        elif kind==Elves.DOOR:
            self.image=pygame.transform.scale(pygame.image.load(r''+path.path+'\\resource\\picture\\item\\door.png'),(40,40))
            #self.image=pygame.transform.scale(pygame.image.load(r'G:\python_pro\maze\resource\picture\item\door.png'),(40,40))
        elif kind==Elves.TELESCOPE:
            self.image=pygame.transform.scale(pygame.image.load(r''+path.path+'\\resource\\picture\\item\\telescope.png'),(40,40))
            #self.image=pygame.transform.scale(pygame.image.load(r'G:\python_pro\maze\resource\picture\item\telescope.png'),(40,40))
