#角色动画类
import pygame
from py_.GLOBAL import *
class Role_Animation:
    rd=[]
    ru=[]
    rr=[]
    rl=[]
    def __init__(self):
        '''
        self.ru0=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_02.png')
        self.ru1=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_01.png')
        self.ru2=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_03.png')
        self.rl0=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_05.png')
        self.rl1=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_04.png')
        self.rl2=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_06.png')
        self.rr0=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_08.png')
        self.rr1=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_07.png')
        self.rr2=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_09.png')
        self.rd0=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_11.png')
        self.rd1=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_10.png')
        self.rd2=pygame.image.load(r'G:\python_pro\maze\resource\role\picture\role_12.png')
        '''
        self.ru0=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_02.png')
        self.ru1=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_01.png')
        self.ru2=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_03.png')
        self.rl0=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_05.png')
        self.rl1=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_04.png')
        self.rl2=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_06.png')
        self.rr0=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_08.png')
        self.rr1=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_07.png')
        self.rr2=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_09.png')
        self.rd0=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_11.png')
        self.rd1=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_10.png')
        self.rd2=pygame.image.load(r''+path.path+'\\resource\\role\\picture\\role_12.png')
        self.rd=[self.rd0,self.rd1,self.rd2]
        self.ru=[self.ru0,self.ru1,self.ru2]
        self.rl=[self.rl0,self.rl1,self.rl2]
        self.rr=[self.rr0,self.rr1,self.rr2]
