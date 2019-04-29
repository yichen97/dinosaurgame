import pygame.font


class Scoreboard():

    def __init__(self, di_settings, screen, score):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.di_settings = di_settings

        self.text_color = (30, 30, 30)
        self.bg_color = (225, 225, 225)
        self.font = pygame.font.SysFont('oldenglishtext', 25)
        self.score = score
        '''将得分渲染成图像'''
        int_score = int(self.score)
        score_str = "score:" +"  " + "{:,}".format(int_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)



