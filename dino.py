import pygame
from pygame.sprite import Sprite
from settings import Settings
settings=Settings()

class Dino(Sprite):
    '''表示恐龙的类'''

    def __init__(self, screen,):
        '''初始化恐龙并设置其初始位置'''
        super(Dino, self).__init__()
        self.screen = screen
        #加载恐龙的图像
        self.x = 70
        self.y = 200
        self.frame = 0
        self.image = None
        self.master_image = None
        self.rect = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = self.x, self.y, width, height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=80):
      # 更新动画帧
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def blitme(self, file):
        '''在指定的位置绘制恐龙'''
        if file :
            image = pygame.image.load(file).convert_alpha()
            self.screen.blit(image, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x, self.y))

    def jump(self, player_jumping, jump_vel, rate):
        if player_jumping == 1:
            if jump_vel < 0:
                jump_vel += 0.11*(rate**2)
            elif jump_vel >= 0:
                jump_vel += 0.13*(rate**2)
            self.y += jump_vel
            '''判断龙一次起跳是否落地'''
            if self.y >= 200:
                player_jumping = 0
                self.y = 200
                jump_vel = -4.95 * rate
            return jump_vel, player_jumping
        elif self.y >= 200:
            player_jumping = 0
            self.y = 200
            jump_vel = -4.95 * rate
            return jump_vel, player_jumping
        else:
            return jump_vel, player_jumping







