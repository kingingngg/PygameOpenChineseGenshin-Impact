import pygame
import math
from settings import *

clock = pygame.time.Clock()

class Home:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.background_color = WHITE
		
		self.images = []

		# 加载所有图片
		for file_name in home_images + [queren_image] + jiazai_images:
			image = pygame.image.load(r'../images/home/' + file_name)
			self.images.append(image)

		self.img = None  # 当前渲染的图片
		self.music_pos = music_kaishi_time  # 当前音乐播放进度

		self.home_jiazai = True  # 是否加载首页加载动画（包括动画与可交互事件）
		self.tiaoguoRun = False  # 是否显示跳过按钮

		self.alpha = 0
		self.jianru = True  # 渐入
		self.chixu = False  # 持续
		self.kaishi_time = 0  # 部分开始时间记录

		self.ua_tongyi = False  # 用户协议同意状态
		self.ua = False  # 用户协议显示状态
		self.jiazai = False  # 加载完成状态
		self.music = False  # 是否进入播放器界面

		self.changpian_xuanzhuan_pos = 0  # 唱片当前旋转位置

		self.play_img = pygame.image.load(r'../images/player/' + play_filename).convert_alpha()
		self.stop_img = pygame.image.load(r'../images/player/' + stop_filename).convert_alpha()
		self.chongbo_img = pygame.image.load(r'../images/player/' + chongbo_filename).convert_alpha()
		self.hongxin_img = pygame.image.load(r'../images/player/' + hongxin_filename).convert_alpha()
		self.guanyu_text_img = guanyu_font.render(guanyu_text, True, guanyu_color)
		self.guanyu_yemian_text_img = guanyu_font.render(guanyu_yemian_text, True, guanyu_color)

		self.zanting = False  # 是否暂停
		self.tuodong = False  # 是否拖动进度条
		self.tuodong_suo = False  # 拖动锁
		self.guanyu = False  # 是否启动关于界面
		self.tiaoguo_rect = pygame.Rect(*tiaoguo_pos, tiaoguo_width, tiaoguo_height)
		self.jindu_rect = pygame.Rect(0, 0, jindu_size * 2, jindu_size * 2)  # 进度控件矩形
		self.jindutiao_rect = pygame.Rect(jindutiao_pos[0][0], jindutiao_pos[0][1] - kongjian_kuan / 2, jindutiao_width, kongjian_kuan)
		self.guanyu_rect = pygame.Rect(*guanyu_pos, guanyu_width, guanyu_height)
		self.guanyu_text_rect = self.guanyu_text_img.get_rect(center = guanyu_text_pos)
		self.guanyu_yemian_text_rect = self.guanyu_yemian_text_img.get_rect(center = guanyu_yemian_pos)
		self.guanyu_yemian_rect = pygame.Rect(0, 0, guanyu_yemian_width, guanyu_yemian_height)
		self.guanyu_yemian_rect.center = guanyu_yemian_pos

		self.home_music()

	def home_music(self):
		pygame.mixer.music.load(r'../music/' + music_name)
		pygame.mixer.music.play(-1, music_kaishi_time)

	def draw_tiaoguo(self):
		"""绘制跳过按钮"""
		pygame.draw.rect(self.display_surface, tiaoguo_background_color, self.tiaoguo_rect, 0, tiaoguo_yuan)
		tiaoguo_text_img = tiaoguo_font.render(tiaoguo_text, True, tiaoguo_color)
		tiaoguo_text_rect = tiaoguo_text_img.get_rect(center = self.tiaoguo_rect.center)
		self.display_surface.blit(tiaoguo_text_img, tiaoguo_text_rect)

	def draw_home_img(self,dt):

		# 处理透明度
		if not self.chixu:
			if self.jianru:
				self.alpha = ((dt - self.kaishi_time) % guodutime) / guodutime * 255
			else:
				self.alpha = 255 - ((dt - self.kaishi_time) % guodutime) / guodutime * 255

		# 处理淡入或淡出切换以及持续状态的判断
		if dt >= 0 and dt <= oneendtime:
			pos = dt % homeweek
			if pos <= guodutime:
				self.chixu = False
				self.jianru = True
			elif homeweek - chixutime >= pos >= guodutime + chixutime:
				self.chixu = False
				self.jianru = False
			else:
				self.chixu = True
				self.kaishi_time = None
				
			# 处理持续时的透明度
			if self.chixu:
				if guodutime <= pos <= guodutime + chixutime:
					self.alpha = 255
				else:
					self.alpha = 0

		# 对透明度增减开始时间的重置
		if self.kaishi_time == None and not self.chixu:
			self.kaishi_time = math.floor(dt)

		# 处理图片的切换
		pos1 = dt // homeweek
		pos2 = dt % homeweek
		pos = pos1 + 1 if pos2 else pos1
		self.img = self.images[math.floor(pos-1)]

		# 处理对应背景色
		self.background_color = guodu_color[math.floor(pos-1)]

		# 缩放处理
		rect = self.img.get_rect()
		if rect.height > WINDOW_HEIGHT:
			suofang = WINDOW_HEIGHT / rect.height
			if rect.width * suofang > WINDOW_WIDTH:
				suofang = WINDOW_WIDTH / rect.width				
		elif rect.width > WINDOW_WIDTH:
			suofang = WINDOW_WIDTH / rect.width
		else:
			suofang = 1.0

		self.img = pygame.transform.smoothscale(self.img, (rect.width * suofang, rect.height * suofang))

	def draw_user_agreement(self):
		self.img = self.images[len(home_images)]
		self.background_color = ua_color

	def draw_jiazai_img(self,dt):
		# 重置开始时间
		if self.kaishi_time == None:
			self.kaishi_time = dt

		# 图片的切换
		pos = (dt - self.kaishi_time) // jiazaitime
		if pos < len(jiazai_images):
			self.img = self.images[int(pos) + (len(home_images) + 1)]
		else:
			self.jiazai = True
			self.kaishi_time = None

		# 背景色
		self.background_color = jiazai_color

	def player(self):
		"""播放器"""
		self.background_color = player_color
		if not self.zanting:
			self.changpian_xuanzhuan_pos += changpian_xuanzhuan

		if self.changpian_xuanzhuan_pos <= -360 or self.changpian_xuanzhuan_pos >= 360:
			self.changpian_xuanzhuan_pos = 0

		# 唱片
		changpian = pygame.image.load(r'../images/player/' + changpian_filename).convert_alpha()
		changpian_rect = changpian.get_rect()
		changpian = pygame.transform.rotozoom(changpian, self.changpian_xuanzhuan_pos, changpian_size)
		changpian_rect = changpian.get_rect(center = changpian_pos)
		self.display_surface.blit(changpian, changpian_rect)

		# 进度条
		pygame.draw.line(self.display_surface, kongjian_color, jindutiao_pos[0], jindutiao_pos[1], kongjian_kuan)
		try:
			pygame.draw.line(self.display_surface, jindu_color, jindutiao_pos[0], self.jindu_pos, kongjian_kuan)
		except:
			pygame.draw.line(self.display_surface, jindu_color, jindutiao_pos[0], (jindutiao_width / music_width * music_kaishi_time + jindutiao_pos[0][0], jindutiao_pos[1][1]), kongjian_kuan)

		# 进度调节器（小圆点）
		if not self.tuodong:
			if self.tuodong_suo:
				tuodong_pos = self.tuodong_jindu_pos[0] - self.jindu_rect.center[0]
				self.music_pos_gengxin(music_width / jindutiao_width * tuodong_pos)
				pygame.mixer.music.play(-1, self.music_pos)
				self.tuodong_suo = False
				self.zanting = False
			jindu =  jindutiao_width / music_width * self.music_pos
			self.jindu_pos = (jindutiao_pos[0][0] + jindu, jindutiao_pos[0][1])
			self.jindu_rect.center = self.jindu_pos
			pygame.draw.circle(self.display_surface, jindu_color, self.jindu_pos, jindu_size)
		else:
			self.jindu_pos = [pygame.mouse.get_pos()[0], jindutiao_pos[0][1]]
			if self.jindu_pos[0] > jindutiao_pos[1][0]:
				self.jindu_pos[0] = jindutiao_pos[1][0]
			elif self.jindu_pos[0] < jindutiao_pos[0][0]:
				self.jindu_pos[0] = jindutiao_pos[0][0]
			self.tuodong_jindu_pos = self.jindu_pos
			pygame.draw.circle(self.display_surface, jindu_color, self.jindu_pos, jindu_size)

		# 播放暂停键
		if self.zanting:
			self.play_stop_rect = self.play_img.get_rect(center = jichukongjian_pos)
			self.display_surface.blit(self.play_img, self.play_stop_rect)
		else:
			self.play_stop_rect = self.stop_img.get_rect(center = jichukongjian_pos)
			self.display_surface.blit(self.stop_img, self.play_stop_rect)

		# 重播键
		self.chongbo_rect = self.chongbo_img.get_rect(center = (self.play_stop_rect.centerx + kongjian_jiange, self.play_stop_rect.centery))
		self.display_surface.blit(self.chongbo_img, self.chongbo_rect)

		# 红心
		self.hongxin_rect = self.hongxin_img.get_rect(center = (self.play_stop_rect.centerx - kongjian_jiange, self.play_stop_rect.centery))
		self.display_surface.blit(self.hongxin_img, self.hongxin_rect)

	def music_pos_gengxin(self,dt):
		"""音乐当前位置的更新"""
		self.music_pos += dt
		if self.music_pos > music_width:
			self.music_pos = 0
		elif self.music_pos < 0:
			self.music_pos = music_width

	def draw_guanyu(self):
		"""绘制关于页面"""
		pygame.draw.rect(self.display_surface, guanyu_background_color, self.guanyu_rect, 0, guanyu_yuan)
		self.display_surface.blit(self.guanyu_text_img, self.guanyu_text_rect)

		if self.guanyu:
			pygame.draw.rect(self.display_surface, guanyu_background_color, self.guanyu_yemian_rect, 0, guanyu_yemian_yuan)
			self.display_surface.blit(self.guanyu_yemian_text_img, self.guanyu_yemian_text_rect)

	def update(self,dt):
		if self.home_jiazai:
			if dt <= oneendtime:
				self.draw_home_img(dt)
				self.img.set_alpha(self.alpha)
			elif not self.ua_tongyi:
				if not self.ua:
					self.ua = True
				self.draw_user_agreement()
			elif not self.jiazai:
				self.draw_jiazai_img(dt)
			else:
				self.home_jiazai = False
				self.music = True
			self.display_surface.blit(self.img, self.img.get_rect(center = img_pos))
			if self.tiaoguoRun:
				self.draw_tiaoguo()
		elif self.music:
			self.player()
			self.draw_guanyu()
		if not self.zanting:
			self.music_pos_gengxin(clock.tick() / 1000)