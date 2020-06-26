#dialogue.py
#对话框脚本 打印剧情线 道具说明等
#也可在以后的应用中作为外部模块或基类重新利用
#偷懒 没有参数检查
import pygame
from py_.GLOBAL import *
class Dialogue():
    def __init__(self,screen,pos,name,msg):
        #####基础属性######
        self.screen=screen
        #绘制位置
        
        self.pos=pos
        #标识名 相当于ID 或者 tag
        self.name=name
        #承载信息
        self.msg=[]
        self.msg=msg
        self.texts=[]
        self.msg_rects=[]
        #默认大小
        self.size=[400,50]
        #默认背景
        self.color=(0,0,0)
        self.show_bg=False
        self.bg=pygame.image.load(r''+path.path+'\\resource\\picture\\1.jpg')

        #self.bg=pygame.image.load(r'G:\python_pro\maze\resource\picture\1.jpg')
        #默认背景图片大小
        self.bg_size=[400,50]
        self.pic=pygame.transform.scale(self.bg,self.bg_size)
        self.rect=pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        #####信息属性######
        #默认字体大小
        self.text_size=24
        #字体
        self.font=pygame.font.SysFont('SimHei', self.text_size)
        #默认字体颜色
        self.text_color=(255,255,255)
        #文本布局
        self.x_offset=self.size[0]/2
        self.y_offset=self.size[1]/2

        self.load_msg(self.msg)
    def load_msg(self,msg):
        for each in self.msg:
            #要打印的字符串，是否抗锯齿，字体颜色，矩形颜色
            msg_image = self.font.render(each, True , self.text_color,self.pic)
            self.texts.append(msg_image)
        lines=len(self.msg)/2-1
        for each in self.texts:
            offset=self.text_size*lines
            msg_image_rect = each.get_rect()
            msg_image_rect.center = self.rect.center
            msg_image_rect.y=msg_image_rect.y-offset+self.y_offset
            lines-=1
            self.msg_rects.append(msg_image_rect)

    def update_msg(self,msg):
        lines=len(self.msg)/2-1
        for each in self.msg_rects:
            offset=self.text_size*lines
            #msg_image_rect.center = self.rect.center
            each.center = self.rect.center
            each.y=self.pos[1]-offset+self.y_offset
            lines-=1
            each.x=self.pos[0]+self.x_offset
        #self.msg_image_rect = self.msg_image.get_rect()
        #self.msg_image_rect.center = self.rect.center#将该矩形放到中间去
    def draw(self):
        self.rect=pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.update_msg(self.msg)
        if self.show_bg:
            self.pic=pygame.transform.scale(self.bg,self.bg_size)
            self.screen.blit(self.pic , self.rect)#绘制出一个矩形作为背景
        else:
            self.screen.fill(self.color,self.rect)
        for i in range(len(self.texts)):
            self.screen.blit(self.texts[i],self.msg_rects[i])
        #self.screen.blit(self.msg_image,self.msg_image_rect)#在一个矩形中绘制出文本信息
