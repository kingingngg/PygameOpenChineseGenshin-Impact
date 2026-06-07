import pygame
pygame.font.init()

# Font
font_url = r'C:\Windows\Fonts\msyh.ttc'  # 微软雅黑

# Window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# 跳过按钮
tiaoguo_width = 100
tiaoguo_height = 50
tiaoguo_yuan = 10  # 圆角弧度
tiaoguo_text = '跳过'
tiaoguo_color = (255,255,255)
tiaoguo_background_color = (150,150,150)
tiaoguo_font = pygame.font.Font(font_url, 30)
tiaoguo_pos = (WINDOW_WIDTH - (tiaoguo_width + 30), 20)

# Color
WHITE = (255,255,255)

# 用户初始数据样本
date_mode = {"yunxutiaoguo":False,  # 是否允许跳过加载动画
}


# 过渡动画全部图片列表
home_images = [
	'01-mihoyo标.jpg',
	'02-原神标.jpg',
	'03-警告.jpg'	
]
# 确认页面
queren_image = '04-用户条款同意.jpg'
# 加载页面
jiazai_images = [
	'05-加载1.jpg',
	'06-加载2.jpg',
	'07-加载3.jpg',
	'08-加载4.jpg',
	'09-加载5.jpg',
	'10-加载6.jpg'
]
# DNA小曲
music_name = 'shed a light.mp3'
# 用户配置文件
user_data_filename = 'user.json'

# 控件图片
play_filename = '播放.png'
stop_filename = '暂停.png'
chongbo_filename = '重播.png'
hongxin_filename = '红心.png'

# 唱片
changpian_filename = '唱片.png'
changpian_pos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4 + 50)
changpian_size = 0.7
changpian_xuanzhuan = -0.5  # 唱片单次旋转速度

# 播放器控件
kongjian_color = WHITE
kongjian_pos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 150)  # 基础位置
kongjian_width = WINDOW_WIDTH - 80
kongjian_height = WINDOW_HEIGHT / 4
kongjian_kuan = 5
jindutiao_jiange = 100  # 进度条左右两边与基本播放器控件的间隔
jindutiao_pos = ((kongjian_pos[0] - kongjian_width / 2 + jindutiao_jiange, kongjian_pos[1] - kongjian_height / 4), (kongjian_pos[0] + kongjian_width / 2 - jindutiao_jiange, kongjian_pos[1] - kongjian_height / 4))
jindutiao_width = jindutiao_pos[1][0] - jindutiao_pos[0][0]  # 进度条长度
jindu_color = (00,125,172)  # 调节进度的进度控件主题颜色
jindu_size = 15  # 半径
kongjian_jiange = 50  # 各控件间的间隔
jichukongjian_pos = (kongjian_pos[0], kongjian_pos[1] + kongjian_height / 4)  # 基础控件的基础位置

# 关于
guanyu_width = 30
guanyu_height = 30
guanyu_pos = (WINDOW_WIDTH - guanyu_width - 30, 30)
guanyu_yuan = 5  # 弧度
guanyu_text = 'i'
guanyu_text_size = 25
guanyu_text_pos = (guanyu_pos[0] + guanyu_width / 2, guanyu_pos[1] + guanyu_height / 2)
guanyu_color = WHITE
guanyu_background_color = (150,150,150)
guanyu_font = pygame.font.Font(font_url, guanyu_text_size)
guanyu_yemian_pos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
guanyu_yemian_width = 500
guanyu_yemian_height = 100
guanyu_yemian_yuan = 5  # 弧度
guanyu_yemian_pos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
guanyu_yemian_text = "king  E-mail:1437167327@qq.com"


# 过渡动画过渡时间
guodutime = 2
# 过渡动画持续时间
chixutime = 1
# 过渡动画一个周期
homeweek = guodutime * 2 + chixutime * 2
# 过渡动画结束时间
oneendtime = homeweek * len(home_images)


# 大多数图片的居中位置
img_pos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)


# 背景色
guodu_color = [  # 过渡动画
	(254,254,254),
	(252,252,252),
	(253,253,253)
]
ua_color = (76,76,76)  # 用户协议页面
jiazai_color = (255,255,255)  # 加载页面
player_color = (0,125,114)  # 播放器界面


# 加载页面间隔时间
jiazaitime = 0.5

# 音乐首次播放时的开始时间
music_kaishi_time = 49.637 - (homeweek + guodutime)
# 时长
music_width = 193.0