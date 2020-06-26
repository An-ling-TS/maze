#robot.py
#机器人脚本
#机器人将在玩家出发一定时间后出现在起点
#机器人具有自动寻路到终点的功能
#玩家被机器人发现后游戏失败
#采用DFS算法寻路
#
from py_.GLOBAL import *
import pygame
class Robot(pygame.sprite.Sprite):
    def __init__(self,map_):
        pygame.sprite.Sprite.__init__(self)
        self.pos=[80,80]
        view = [41,41]
        self.picnum=0
        self.dfs_map=map_
        self.stack = []
        for i in range(len(self.dfs_map)):
            self.dfs_map[i][0]=0
            self.dfs_map[0][i]=0
            self.dfs_map[len(self.dfs_map)-1][i]=0
            self.dfs_map[i][len(self.dfs_map)-1]=0
        self.speed=10
        self.stack.append(self.pos)
        self.rect=pygame.Rect(80,80,view[0],view[1])
        self.ru0=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_13.png')
        self.ru1=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_14.png')
        self.ru2=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_16.png')
        self.rl0=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_05.png')
        self.rl1=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_06.png')
        self.rl2=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_08.png')
        self.rr0=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_09.png')
        self.rr1=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_10.png')
        self.rr2=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_12.png')
        self.rd0=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_01.png')
        self.rd1=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_02.png')
        self.rd2=pygame.image.load(r''+path.path+'\\resource\\picture\\robot\\images\\1_04.png')
        self.rd=[self.rd0,self.rd1,self.rd2]
        self.ru=[self.ru0,self.ru1,self.ru2]
        self.rl=[self.rl0,self.rl1,self.rl2]
        self.rr=[self.rr0,self.rr1,self.rr2]
        self.pic=self.ru[0]
        self.run=False
    #x,y是要前往的map_基坐标
    def move(self,x,y):
        print('move('+str(x)+','+str(y)+')  pos('+str(self.pos[0])+','+str(self.pos[1])+')')
        if (x*40)==self.pos[0] and (y*40)==self.pos[1]:
            self.run=False
        else:
            self.picnum+=1
            self.picnum=self.picnum%3
            
            if x*40<self.pos[0]:
                self.pos[0]-=self.speed
                self.pic=self.rl[self.picnum]
            elif x*40>self.pos[0]:
                self.pos[0]+=self.speed
                self.pic=self.rr[self.picnum]
            elif y*40>self.pos[1]:
                self.pos[1]+=self.speed
                self.pic=self.rd[self.picnum]
            elif y*40<self.pos[1]:
                self.pos[1]-=self.speed
                self.pic=self.ru[self.picnum]
        self.rect.x=self.pos[0]
        self.rect.y=self.pos[1]
    def DFS(self):
        #DFS在更新循环中被调用，所以省去循环
        #当机器人走遍某一分支后可能需要返回起点（根）而去往下一分支
        if len(self.stack)==0:
            self.stack.append([80,80])
        x=int(self.stack[len(self.stack)-1][0]/40)
        y=int(self.stack[len(self.stack)-1][1]/40)
        
        self.dfs_map[x][y]=0
        
        if x==len(self.dfs_map)-2 or y==len(self.dfs_map)-2:
            #print('robot')
            return ''
        #每次向栈顶单元移动
        if self.run==True:
            self.move(x,y)
            return 'Move'

        self.run=True
        #是路时则
        if y+1<=len(self.dfs_map)-1 and self.dfs_map[x][y+1]>0:
            self.stack.append([x*40,(y+1)*40])
            return 'D'
        if x+1<=len(self.dfs_map)-1 and self.dfs_map[x+1][y]>0:
            self.stack.append([(x+1)*40,y*40])
            return 'S'
        if x-1>=0 and self.dfs_map[x-1][y]>0:
            self.stack.append([(x-1)*40,y*40])
            return 'A'
        if y-1>=0 and self.dfs_map[x][y-1]>0:
            self.stack.append([x*40,(y-1)*40])
            return 'W'
        self.stack.pop()
