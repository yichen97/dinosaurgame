import pygame

class MyMap(pygame.sprite.Sprite):
    '''一个滚动地图类'''
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.bg = pygame.image.load("images/map2.png").convert_alpha()
        self.screen = screen

    def map_rolling(self, rate):
        if self.x < -735:
            self.x = 733
        else:
            self.x -= rate

    def map_update(self):
        self.screen.blit(self.bg, (self.x, self.y))
