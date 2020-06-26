#角色类
import py_.role_animation
import sys
import pygame
from py_.GLOBAL import *
from pygame.locals import *
class Player(pygame.sprite.Sprite):
    speed=5
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.head_pic=pygame.transform.scale(pygame.image.load(r'G:\python_pro\maze\resource\picture\tips\1.png'),[300,400])
        self.head_pic=pygame.transform.scale(pygame.image.load(r''+path.path+'\\resource\\picture\\tips\\1.png'),[300,400])
        self.view=950#迷雾中视距
        self.animation=py_.role_animation.Role_Animation()#绑定动画
        self.pic=self.animation.ru[0]#静止图
        self.picnum=0#轮播坐标
        self.pos=[80,80]#初始位置
        self.rect=pygame.Rect(80,80,30,30)#碰撞器位置及大小
    def move(self,keyup,map_,tile_group,item_group):
        kp=pygame.key.get_pressed()
        #此处仅使用elif无法避免同时按键导致的bug 所以禁止同时按下多个方向键
        if kp[K_a] and not kp[K_d] and not kp[K_w] and not kp[K_s]:
            self.picnum+=1
            self.picnum=self.picnum%3#轮播移动图片
            #flag 碰撞检测
            if not pygame.sprite.spritecollide(self,tile_group,False):
                self.pos[0]=self.pos[0]-self.speed
            else:
                self.pos[0]+=self.speed
            self.pic=self.animation.rl[self.picnum]
        elif kp[K_d] and not kp[K_a] and not kp[K_w] and not kp[K_s]:
            self.picnum+=1
            self.picnum=self.picnum%3
            if not pygame.sprite.spritecollide(self,tile_group,False):
                self.pos[0]=self.pos[0]+self.speed
            else:
                self.pos[0]-=self.speed
            self.pic=self.animation.rr[self.picnum]
        elif kp[K_s] and not kp[K_d] and not kp[K_w] and not kp[K_a]:
            self.picnum+=1
            self.picnum=self.picnum%3
            if not pygame.sprite.spritecollide(self,tile_group,False):
                self.pos[1]=self.pos[1]+self.speed
            else:
                self.pos[1]-=self.speed
            self.pic=self.animation.ru[self.picnum]
        elif kp[K_w] and not kp[K_d] and not kp[K_a] and not kp[K_s]:
            self.picnum+=1
            self.picnum=self.picnum%3
            if not pygame.sprite.spritecollide(self,tile_group,False):
                self.pos[1]=self.pos[1]-self.speed
            else:
                self.pos[1]+=self.speed
            self.pic=self.animation.rd[self.picnum]
        if keyup:
            '''
            #人物左上角
            posx=self.pos[0]
            posy=self.pos[1]
            
            if pygame.sprite.spritecollide(self,tile_group,False):
                if map_[int(posx/40)][int(posy/40)]==0 and map_[int(posx/40)][int((posy+30)/40)]==0:
                    self.pos[0]=self.pos[0]+self.speed
                if map_[int((posx+30)/40)][int(posy/40)]==0 and map_[int((posx+30)/40)][int((posy+30)/40)]==0:
                    self.pos[0]=self.pos[0]-self.speed
                if map_[int(posx/40)][int(posy/40)]==0 and map_[int((posx+30)/40)][int(posy/40)]==0:
                    self.pos[1]=self.pos[1]+self.speed
                if map_[int(posx/40)][int((posy+30)/40)]==0 and map_[int((posx+30)/40)][int((posy+30)/40)]==0:
                    self.pos[1]=self.pos[1]-self.speed
            '''
            if keyup==K_a and keyup!=K_d and keyup!=K_s and keyup!=K_w:
                self.picnum=0
                self.pic=self.animation.rl[0]
                #立定检测 防止陷入连续碰撞检测中而使人物无法移动
                if pygame.sprite.spritecollide(self,tile_group,False):
                    self.pos[0]=self.pos[0]+self.speed
            if keyup==K_d and keyup!=K_a and keyup!=K_s and keyup!=K_w:
                self.picnum=0
                self.pic=self.animation.rr[0]
                if pygame.sprite.spritecollide(self,tile_group,False):
                    self.pos[0]=self.pos[0]-self.speed
            if keyup==K_w and keyup!=K_d and keyup!=K_s and keyup!=K_a:
                self.picnum=0
                self.pic=self.animation.rd[0]
                if pygame.sprite.spritecollide(self,tile_group,False):
                    self.pos[1]=self.pos[1]+self.speed
            if keyup==K_s and keyup!=K_d and keyup!=K_a and keyup!=K_w:
                self.picnum=0
                self.pic=self.animation.ru[0]
                if pygame.sprite.spritecollide(self,tile_group,False):
                    self.pos[1]=self.pos[1]-self.speed

        #刷新位置
        self.rect.x=self.pos[0]
        self.rect.y=self.pos[1]

