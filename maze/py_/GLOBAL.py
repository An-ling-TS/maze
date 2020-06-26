#全局常量脚本
#GLOBAL.py
from enum import Enum
################
#图片相关
################
#玩家人物角色图片
ROLE_SIZE=[40,40]#像素
#地图瓦片图片
TILED_SIZE=[40,40]#像素
#####路径####
class Path():
    def __init__(self,path_):
        self.path=path_
path=Path('')
####事件####
#精灵类型
class Elves(Enum):
    VICTORY=0
    DOOR=2#哆啦A梦的任意门
    TELESCOPE=3#哆啦A梦的望远镜
#文本内容
bg_msg=[]
bg_msg.append('在某个平行时空中，胖虎┗|*｀0′*|┛得到了')
bg_msg.append('一股邪恶势力的帮助，体魄异变。为了打败胖虎，')
bg_msg.append('救出静香,大雄不得不穿越神秘迷宫，去往迷宫')
bg_msg.append('尽头寻求哆啦A梦的帮助...')

help_msg=[]
help_msg.append('胖虎尾随着你来到了神秘迷宫的入口，他将')
help_msg.append('在10秒后进入迷宫，对你发起追杀。当你出')
help_msg.append('现在他视野之内，你将即刻死亡。注意：胖虎')
help_msg.append('并不怎么在意你这只蝼蚁，他的目标是多啦A梦')
help_msg.append(',当他寻找到出口时，这意味着你的失败。')
help_msg.append('(w,a,s,d控制角色移动)')

any_click_msg=[]
any_click_msg.append('点击鼠标继续......')
filed_msg=[]
filed_msg.append('绝对的力量最终还是战胜了一切。')
filed_msg.append('静香最终还是和胖虎生活在了一起')
filed_msg.append('至于大雄，没有人会记得一个失败')
filed_msg.append('者。')
filed_msg.append('......')
filed_msg.append('六个月后，静香生了个儿子，但奇')
filed_msg.append('怪的是，这个男婴天生长得跟狐狸')
filed_msg.append('似的，还有一张有点熟悉的尖尖的')
filed_msg.append('嘴。')
victory_msg=[]
victory_msg.append('终究唯有智慧才是永恒的，尽管')
victory_msg.append('你可能靠的是运气。但不管怎么')
victory_msg.append('说，静香最终还是被你救了出来，')
victory_msg.append('虽然她看上去不怎么情愿，但她')
victory_msg.append('终究是嫁给了大雄。')
victory_msg.append('......')
victory_msg.append('六个月后，静香生了个女儿，胖')
victory_msg.append('胖的，天生就好吃，还有着莫名')
victory_msg.append('奇妙的怪力。当她上五年级的时')
victory_msg.append('候，壮的和胖虎当年有的一比。')

door_msg=[]
door_msg.append('这是......哆啦A梦的任意门。')
door_msg.append('太好了！但是它怎么会在这里，')
door_msg.append('好奇怪。它会通往哪里呢？')

tele_msg=[]
tele_msg.append('咦，是哆啦A梦的望远镜，太')
tele_msg.append('好了！有了这个望远镜，我就')
tele_msg.append('可以看的更远了。')


