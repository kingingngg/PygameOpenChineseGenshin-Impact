import pygame
import sys
from pathlib import Path
import json
from settings import *
from home import Home

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('真·原神')

move = Home()

# 检查用户数据文件
user_data_file = Path(r'../data/' + user_data_filename)
try:
	user_date = json.loads(user_data_file.read_text())
	if user_date['yunxutiaoguo']:
		move.tiaoguoRun = True
	else:
		user_date['yunxutiaoguo'] = True
		user_data_file.write_text(f"{json.dumps(user_date)}")
except:
	print('!')
	user_data_mode = date_mode
	user_data_mode['yunxutiaoguo'] = True
	user_data_file.write_text(f"{json.dumps(user_data_mode)}")

# 主循环
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				move.guanyu = False
				if move.ua:
					move.ua_tongyi = True
					move.ua = False
				if move.home_jiazai and move.tiaoguoRun and move.tiaoguo_rect.collidepoint(pygame.mouse.get_pos()):
					move.home_jiazai = False
					move.music = True
				elif (move.music and move.jindu_rect.collidepoint(pygame.mouse.get_pos())) or (move.music and move.jindutiao_rect.collidepoint(pygame.mouse.get_pos())):
					move.tuodong = True
					move.tuodong_suo = True
				elif move.music and move.play_stop_rect.collidepoint(pygame.mouse.get_pos()):
					if move.zanting:
						move.zanting = False
						pygame.mixer.music.unpause()
					else:
						move.zanting = True
						pygame.mixer.music.pause()
				elif move.music and move.chongbo_rect.collidepoint(pygame.mouse.get_pos()):
					move.music_pos = 0
					move.zanting = False
					move.changpian_xuanzhuan_pos = 0
					pygame.mixer.music.play(-1)
				elif move.music and move.guanyu_rect.collidepoint(pygame.mouse.get_pos()):
					move.guanyu = True
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				move.tuodong = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if move.music:
					if move.zanting:
						move.zanting = False
						pygame.mixer.music.unpause()
					else:
						move.zanting = True
						pygame.mixer.music.pause()
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_q]:
		sys.exit()

	screen.fill(move.background_color)

	dt = pygame.time.get_ticks() / 1000

	move.update(dt)
	pygame.display.update()
