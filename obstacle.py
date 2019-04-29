import pygame
import random
from pygame.sprite import Sprite
from settings import Settings


settings=Settings()

class Bird(Sprite):
    '''初始化鸟并设置其初始位置'''
    def __init__(self, x, y, screen,):
        super(Bird, self).__init__()
        self.screen = screen
        '''加载鸟的图像，并设置其rect属性'''
        self.image = pygame.image.load('images/bird1.png').convert_alpha()
        '''每只鸟都从右上角出发'''
        self.x = x
        self.y = y
        '''储存鸟的准确位置'''
        self.x = float(self.x)
        self.y = float(self.y)

    def bird_rolling(self):
        if self.x < -100:
            self.x = 800
            flag = False
            return flag
        else:
            self.x -= 5
            flag = True
            return flag

    '''在指定的位置绘制飞鸟'''
    def blitme(self, file=''):
        if file :
            image = pygame.image.load(file).convert_alpha()
            self.screen.blit(image, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x, self.y))


class Cactus(Sprite):

    #初始化仙人掌并设置其初始位置
    def __init__(self, x, y, screen):
        super(Cactus, self).__init__()
        self.screen = screen
        self.x = x
        self.y = y


        '''加载仙人掌的图像'''
        self.image = pygame.image.load('images/cactus01.png').convert_alpha()

        '''储存仙人掌的准确位置'''
        self.x = float(self.x)
        self.y = float(self.y)

    def cactus_rolling(self, flag, rate):
        if self.x < -10:
            self.x = 800+random.randint(1,1600)
            flag = -1
            return flag
        else:
            self.x -= rate
            return flag

    def randcactus(self, flag):
        if flag == -1:
            randnum = random.randint(0, 300)
            if 0 < randnum < 100:
                flag = 0
            elif 100 < randnum < 200:
                flag = 1
            elif 200 < randnum < 300:
                flag = 2
            return flag

        else:
            return flag

    '''在指定的位置绘制仙人掌'''
    def blitme(self, file=''):

        if file :
            image = pygame.image.load(file).convert_alpha()
            self.screen.blit(image, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x, self.y))