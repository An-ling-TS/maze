#迷宫生成脚本
#Maze_generation.py
#Prime迷宫生成算法
import random
import pygame
from py_.GLOBAL import *
class Maze:
    LEN=0#迷宫长度--- 行
    WID=0#迷宫宽度| 列
    def __init__(self,length,wid):
        self.LEN=length
        self.WID=wid
        #self.wall_01=pygame.image.load(r'G:\python_pro\maze\resource\picture\wall\wall_01.png')
        self.wall_01=pygame.image.load(r''+path.path+'\\resource\\picture\\wall\\wall_01.png')
    def create_maze(self):
        maze=[[0]*self.WID for i in range(self.LEN)]
        for i in range(self.LEN):
            maze[i][0]=1
            maze[0][i]=1
            maze[self.LEN-1][i]=1
            maze[i][self.LEN-1]=1
        X=list()
        Y=list()
        X.append(2)
        Y.append(2)
        while len(X)>0:
            r=random.randint(0,len(X))%len(X)
            x=X[r]
            y=Y[r]
            count=0
            for i in range(x-1,x+2):
                for k in range(y-1,y+2):
                    if abs(x-i)+abs(y-k)==1 and maze[i][k]>0:
                        count+=1 
            if count<=1:
                maze[x][y]=1
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if abs(x-i)+abs(y-j)==1 and maze[i][j]==0:
                            X.append(i)
                            Y.append(j)                 
            del X[r]
            del Y[r]       
        maze[2][1]=1
        for i in range(self.LEN-3,-1,-1):
            if maze[i][self.LEN-3]==1:
                maze[i][self.LEN-2]=1
                break

        return maze
    
        #print(map_)
if __name__=='__main__':
    ma=Maze(30,30)
    #ma.create_map()
