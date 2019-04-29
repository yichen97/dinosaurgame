import pygame.font

class Button():

    def __init__(self,ai_settings,screen,message):
        '''初始化按钮的属性'''
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color=(255, 255, 255)
        self.font=pygame.font.SysFont(None, 48)

        self.rect=pygame.Rect(0, 0, self.width, self.height)
        self.rect.center=self.screen_rect.center


        self.prep_message(message)


    def prep_message(self, message):
        #图像渲染
        self.message_image_rect = self.font.render(message, True, self.text_color,
                                            self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
