#游戏主脚本
import random
import sys
import os
path_ = os.getcwd()
#sys.path.append(path_+'\py_')
from py_.GLOBAL import *
#初始化路径 注意路径和自定义模块的导入顺序
path.path=path_.replace('\\','\\\\')
print('path='+str(path.path))
import py_.role
import pygame
import py_.tile
import py_.Maze_generation
import py_.clock
import py_.item
from py_.robot import *
from py_.button import *
from py_.dialogue import *
keyDown=''
keyUp=''
pygame.init()
#bg=pygame.image.load(r'G:\python_pro\maze\resource\picture\1.jpg')
bg=pygame.image.load(r''+path.path+'\\resource\\picture\\1.jpg')

fps=pygame.time.Clock()
screen=pygame.display.set_mode((1240,825))
pygame.display.set_caption("maze")

#bg_music=pygame.mixer.music.load(r'G:\python_pro\maze\resource\music\bg.wav')
bg_music=pygame.mixer.music.load(r''+path.path+'\\resource\\music\\bg.wav')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

#item_music=pygame.mixer.Sound(r'G:\python_pro\maze\resource\music\item.wav')
item_music=pygame.mixer.Sound(r''+path.path+'\\resource\\music\\item.wav')
item_music.set_volume(0.3)

######
tiled_map=py_.Maze_generation.Maze(20,20)
map_=[]
clocker=py_.clock.Clock('ROBOT',10)
#创建地图精灵组
def create_collider():
    for i in range(tiled_map.LEN):
        for j in range(tiled_map.WID):
            if map_[i][j]==0:
                tile_=py_.tile.Tile(tiled_map.wall_01,(40*(i),40*(j)))
                tile_group.add(tile_)
#创建地图数组
def get_maze():
    global map_
    map_=tiled_map.create_maze()
#创建外围墙壁
def create_walls():
    global walls,exit_pos
    for i in range(tiled_map.LEN-1):
        if map_[i][1]==0:
            walls.append([i*40,40])
        if map_[tiled_map.LEN-2][i]==0:
            walls.append([(tiled_map.LEN-2)*40,i*40])    
        if map_[1][i]==0:
            walls.append([40,i*40])
        if map_[i][tiled_map.LEN-2]==0:
            walls.append([i*40,(tiled_map.LEN-2)*40])
            
        if map_[i][tiled_map.LEN-2]==1 and i>0:
            exit_pos=[i*40,(tiled_map.LEN-2)*40]

def draw_walls(): 
    for each in walls:
        screen.blit(pygame.transform.scale(tiled_map.wall_01,(40,40)),(each[0],each[1]))
#地图事件监听
product_i=0
def item_event():
    global start,game_over,win
    it=None#当前事件
    for each in item_group:
        if pygame.sprite.collide_rect(role_, each):
            item_music.play()
            if each.kind == Elves.VICTORY:
                start=False
                game_over=True
                win=True
            elif each.kind == Elves.DOOR:
                door_tip=Dialogue(screen,[0,600],'DOOR',door_msg)
                door_tip.size=[800,225]
                door_tip.x_offset=300
                door_tip.draw()
                screen.blit(role_.head_pic,(0,425))
                it=Elves.DOOR
            elif each.kind == Elves.TELESCOPE:
                tele_tip=Dialogue(screen,[0,600],'TELESCOPE',tele_msg)
                tele_tip.size=[800,225]
                tele_tip.x_offset=300
                tele_tip.draw()
                screen.blit(role_.head_pic,(0,425))
                it=Elves.TELESCOPE
            pos=(each.pos[0]/40,each.pos[1]/40)
            confirm_Btn.draw_button()
            cancel_Btn.draw_button()
    if it != None:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if confirm_Btn.isOver():
                    if it==Elves.DOOR:
                        while True:
                            index_x=random.randint(1,18)
                            index_y=random.randint(1,18)
                            if map_[index_x][index_y]==1:
                                role_.pos=[index_x*40,index_y*40]
                                it=None
                                item_group.remove(product[pos])
                                return
                    if it==Elves.TELESCOPE:
                        it=None
                        item_group.remove(product[pos])
                        role_.view-=15
                        return
                elif cancel_Btn.isOver():
                    if it==Elves.DOOR:
                        item_group.remove(product[pos])
                    elif it==Elves.TELESCOPE:
                        item_group.remove(product[pos])
                    it=None
                    return
#UI事件监听
def event_listen():
    global plot,pause,game_over,start,win,tip
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit() #防止程序卡死
        if plot:
            if event.type == pygame.MOUSEBUTTONUP:
                plot=False
                tip=True
                break
        if pause:
            if event.type == pygame.MOUSEBUTTONUP:
                #游戏继续
                if pause_Btn.isOver():
                    pause=False
                    pause_Btn.msg='暂停'
                    pause_Btn.button_color = (255,86,12)
                    break
                elif exit_Btn.isOver():
                    pygame.quit()
                    sys.exit()
                elif restart_Btn.isOver():
                    restart()
        if game_over:
            if event.type == pygame.MOUSEBUTTONUP:
                game_over=False
                pause=False
                break
        if tip:
            if event.type == pygame.MOUSEBUTTONUP:
                tip=False
                break
#鼠标悬停时改变按钮颜色
def change_btn_color():
    global pause_Btn,exit_Btn,start_Btn
    if pause_Btn.rect.collidepoint(pygame.mouse.get_pos()):
        pause_Btn.button_color=(201,48,44)
    else:
        pause_Btn.button_color=(255,86,12)
    if exit_Btn.rect.collidepoint(pygame.mouse.get_pos()):
        exit_Btn.button_color=(201,48,44)
    else:
        exit_Btn.button_color=(255,86,12)
    if start_Btn.rect.collidepoint(pygame.mouse.get_pos()):
        start_Btn.button_color=(201,48,44)
    else:
        start_Btn.button_color=(255,86,12)
    if cancel_Btn.rect.collidepoint(pygame.mouse.get_pos()):
        cancel_Btn.button_color=(201,48,44)
    else:
        cancel_Btn.button_color=(255,86,12)
    if confirm_Btn.rect.collidepoint(pygame.mouse.get_pos()):
        confirm_Btn.button_color=(201,48,44)
    else:
        confirm_Btn.button_color=(255,86,12)
    if restart_Btn.rect.collidepoint(pygame.mouse.get_pos()):
        restart_Btn.button_color=(201,48,44)
    else:
        restart_Btn.button_color=(255,86,12)
def produce_item():
    global item_group,produce,door,product
    #这里用字典存储事件，以键(一个坐标,是一个元组存放)来区分分布位置不同的事件
    #触发时可以通过精灵的坐标与其事件坐标的倍数关系来获取其事件坐标
    #表现形式是 事件组<事件坐标[x,y]，事件>     
    product=dict()
    count=0
    
    while count<6:
        index_x=random.randint(1,18)
        index_y=random.randint(1,18)
        if map_[index_x][index_y]==1:
            pos=(index_x,index_y)#用来标识相同事件不同分布
            #刷出两个任意门
            if produce[Elves.DOOR]<2:
                map_[index_x][index_y]=2
                product[pos]=py_.item.Item((index_x*40,index_y*40),Elves.DOOR,'任意门')
                produce[Elves.DOOR]+=1
            #刷出4个望远镜
            elif produce[Elves.TELESCOPE]<4:
                map_[index_x][index_y]=3
                product[pos]=py_.item.Item((index_x*40,index_y*40),Elves.TELESCOPE,'望远镜')
                produce[Elves.TELESCOPE]+=1
            item_group.add(product[pos])
            count+=1
def restart():
    global start,game_over,tile_group,item_group,produce,walls,role_,robot_,pause
    start=False
    game_over=False
    pause=False
    pause_Btn.msg='暂停'
    tile_group = pygame.sprite.Group()
    #创建迷宫数组
    get_maze()
    #为迷宫地图添加瓦片和碰撞器
    create_collider()
    #创建外墙
    walls=[]
    create_walls()
    item_group=pygame.sprite.Group() #组第一个必须是胜利精灵
    produce=dict()
    produce[Elves.DOOR]=0
    produce[Elves.TELESCOPE]=0
    victory = py_.item.Item(exit_pos,Elves.VICTORY,'胜利')
    item_group.add(victory)
    role_=py_.role.Player()
    robot_ = Robot(map_)
    produce_item()

######创建玩家#####
#创建玩家角色
role_ = py_.role.Player()
######创建地图#####
#创建地图碰撞器组
tile_group = pygame.sprite.Group()
#创建迷宫数组
get_maze()
#为迷宫地图添加瓦片和碰撞器
create_collider()
#创建外墙
walls=[]
#出口坐标
exit_pos=[0,0]
create_walls()
#####创建地图事件组####
item_group=pygame.sprite.Group() #组第一个必须是胜利精灵
produce=dict()
produce[Elves.DOOR]=0
produce[Elves.TELESCOPE]=0
#创建胜利精灵
print('1'+str(exit_pos))
victory = py_.item.Item(exit_pos,Elves.VICTORY,'胜利')
item_group.add(victory)
#创建机器人
robot_ = Robot(map_)
####初始化状态####
pause=False#暂停
plot=True#剧情播放
start=False#开始游戏
game_over=False
win=False
tip=False#叙事框
produce_item()#刷新事件组
######创建菜单#####
#创建暂停按钮
pause_Btn=Button(screen,'PAUSE','暂停',(1000,200),(200,50))
#创建开始按钮
start_Btn=Button(screen,'START','出发',(1000,100),(200,50))
#创建退出按钮
exit_Btn=Button(screen,'EXIT','退出游戏',(1000,400),(200,50))
#创建重新开始按钮
restart_Btn=Button(screen,'RESTART','重新开始',(1000,300),(200,50))
#创建确认 取消按钮
confirm_Btn=Button(screen,'CONFIRM','使用',(150,750),(200,50))
cancel_Btn=Button(screen,'CANCEL','取消',(450,750),(200,50))
#####创建剧情线#####
#创建对话框
bg_tip=Dialogue(screen,[0,0],'BG',bg_msg)
bg_tip.size=[800,800]
bg_tip.x_offset=400
vic_tip=Dialogue(screen,[0,0],'VIC',victory_msg)
vic_tip.size=[800,800]
vic_tip.x_offset=400
filed_tip=Dialogue(screen,[0,0],'FAILED',filed_msg)
filed_tip.size=[800,800]
filed_tip.x_offset=400
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit() #防止程序卡死
        if event.type == pygame.MOUSEBUTTONUP:
            if start_Btn.isOver():
                start=True
                pause=False
                pause_Btn.msg='暂停'
                clocker.start()
            elif exit_Btn.isOver():
                pygame.quit()
                sys.exit()
            elif restart_Btn.isOver():
                restart()
    #剧情循环
    while plot:
        event_listen()
        screen.fill((0,0,0),(0,0,1240,825))
        bg_tip.pos[1]+=1
        if bg_tip.pos[1]<825:
            bg_tip.draw()
        else:
            any_click=Dialogue(screen,[1240/2,825/2],'N1',any_click_msg)
            any_click.x_offset=-100
            any_click.draw()
        pygame.display.flip()
        fps.tick(60)
    #叙事框循环
        
    while tip:
        event_listen()
        tip_=Dialogue(screen,[0,600],'TIP',help_msg)
        tip_.size=[800,225]
        tip_.y_offset=100
        #tip_.bg=pygame.image.load(r'G:\python_pro\maze\resource\picture\tips\0.jpg')
        tip_.bg=pygame.image.load(r''+path.path+'\\resource\\picture\\tips\\0.jpg')
        tip_.show_bg=True
        tip_.bg_size=[800,225]
        
        screen.blit(pygame.transform.scale(bg, (1240,825)),(0,0))
        tile_group.draw(screen)
        item_group.draw(screen)
        #绘制迷雾
        pygame.draw.circle(screen,(0,0,0),(role_.pos[0]+15,role_.pos[1]+15),1000,950)
        #绘制菜单背景
        screen.blit(pygame.transform.scale(bg,(440,825)),(800,0))
        #绘制按钮
        change_btn_color()
        pause_Btn.button_color = (128,128,128)
        pause_Btn.draw_button()
        start_Btn.draw_button()
        exit_Btn.draw_button()
        restart_Btn.draw_button()
        #绘制外墙
        draw_walls()

        change_btn_color()
        tip_.draw()
        
        screen.blit(pygame.transform.scale(role_.pic,(30,30)),role_.rect)
        pygame.display.flip()
        fps.tick(60)
    #暂停循环
    while pause and start:
        #绘制迷雾
        pygame.draw.circle(screen,(0,0,0),(role_.pos[0]+15,role_.pos[1]+15),1000,950)
        event_listen()
        item_event()
    #执行循环
    while not pause and start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit() #防止程序卡死
            if event.type==pygame.KEYDOWN:
                keyDown=event.key
            else:
                keyDown=None
            if event.type==pygame.KEYUP:
                keyUp=event.key
            else:
                keyUp=None
            if event.type == pygame.MOUSEBUTTONUP:
                if pause_Btn.isOver():
                    pause=True
                    pause_Btn.msg='继续'
                elif exit_Btn.isOver():
                    pygame.quit()
                    sys.exit()
                elif restart_Btn.isOver():
                    restart()                
        
        role_.move(keyUp,map_,tile_group,item_group)

        screen.blit(pygame.transform.scale(bg, (1240,825)),(0,0))
        
        tile_group.draw(screen)
        item_group.draw(screen)
        if clocker.timing():
            #绘制胖虎
            screen.blit(pygame.transform.scale(robot_.pic,(40,40)),robot_.rect)
            robot_.DFS()
            #失败判断
            if pygame.sprite.collide_rect(role_, robot_):
                win=False
                game_over=True
                start=False
            for each in item_group:
                if pygame.sprite.collide_rect(robot_,each):
                    if each.kind==Elves.VICTORY:
                        win=False
                        game_over=True
                        start=False
        #绘制大雄
        screen.blit(pygame.transform.scale(role_.pic,(30,30)),role_.rect)
        #绘制迷雾
        pygame.draw.circle(screen,(0,0,0),(role_.pos[0]+15,role_.pos[1]+15),1000,role_.view)
        #绘制菜单背景
        screen.blit(pygame.transform.scale(bg,(440,825)),(800,0))
        #绘制按钮
        change_btn_color()
        pause_Btn.button_color = (255,86,12)
        pause_Btn.draw_button()
        start_Btn.draw_button()
        exit_Btn.draw_button()
        restart_Btn.draw_button()
        #绘制外墙
        draw_walls()
        
        item_event()
        pygame.display.flip()
        fps.tick(60)
    #结束循环
    while game_over:   
        screen.fill((0,0,0),(0,0,1240,825))
        event_listen()
        if vic_tip.pos[1]<840 and win:
            vic_tip.pos[1]+=1
            vic_tip.draw()
            
        elif filed_tip.pos[1]<840 and not win:
            filed_tip.pos[1]+=1
            filed_tip.draw()
        else:
            any_click=Dialogue(screen,[1240/2,825/2],'N1',any_click_msg)
            any_click.x_offset=-100
            any_click.draw()
        pygame.display.flip()
        fps.tick(60)
    change_btn_color()
    screen.blit(pygame.transform.scale(bg, (1240,825)),(0,0))
    tile_group.draw(screen)
    item_group.draw(screen)
    #绘制迷雾
    pygame.draw.circle(screen,(0,0,0),(role_.pos[0]+15,role_.pos[1]+15),1000,role_.view)
    #绘制菜单背景
    screen.blit(pygame.transform.scale(bg,(440,825)),(800,0))
    if not pause:
        pause_Btn.button_color = (128,128,128)
    pause_Btn.draw_button()
    restart_Btn.draw_button()
    start_Btn.draw_button()
    exit_Btn.draw_button()
    #绘制外墙
    draw_walls()
    screen.blit(pygame.transform.scale(role_.pic,(30,30)),role_.rect)
    pygame.display.flip()
    fps.tick(60)

