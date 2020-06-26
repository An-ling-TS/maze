#button.py
#按钮脚本
import pygame.font
import pygame
class Button():
    def __init__(self,screen,name,msg,position,size):
        self.screen = screen
        #用于识别按钮
        self.name=name
        self.screen_rect = screen.get_rect()#/引入整个大屏幕的参数
        self.width = size[0]
        self.height = size[1]
        self.button_color = (255,86,12)
        self.text_size=48
        self.text_color = (255,255,255)#设置参数，在下面会调用，都是简单的数据类型而已。
        self.font = pygame.font.SysFont('SimHei', self.text_size)
        #self.font = pygame.font.SysFont(None , 48)#None是字体类型，48是字体大小
        self.pos=position
        self.rect = pygame.Rect(self.pos[0],self.pos[1] , self.width , self.height)#设置矩形大小
        #self.rect.center = self.screen_rect.center#将矩形放到屏幕中间
        #按钮所带字体信息
        self.msg=msg
        self.load_msg()
    
    def load_msg(self):
        self.msg_image = self.font.render(self.msg, True , self.text_color,self.button_color)#要打印的字符串，是否抗锯齿，字体颜色，矩形颜色
        self.msg_image_rect = self.msg_image.get_rect()#不解释
        self.msg_image_rect.center = self.rect.center#将该矩形放到中间去
    
    def draw_button(self):#绘制的时候调用该函数
        self.load_msg()
        self.screen.fill(self.button_color , self.rect)#绘制出一个矩形作为背景
        self.screen.blit(self.msg_image,self.msg_image_rect)#在一个矩形中绘制出文本信息
    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. pos
        w, h = 200,50   
        in_x = x < point_x < x + w
        in_y = y  < point_y < y + h
        return in_x and in_y
