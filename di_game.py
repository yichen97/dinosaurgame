import pygame,sys
import obstacle
from settings import Settings
from dino import Dino
from counter import Scoreboard
from obstacle import Bird
from map import MyMap
import time
from hitfind import hit_find
from tips import prtips

def run_game():
    #初始化循环并创建一个对象
    prtips()
    pygame.init()
    #设置背景音效
    pygame.mixer_music.load('Lullatone - outside sandwiches.mp3')
    pygame.mixer_music.play(10, 0)
    #加载动作音效
    di_settings = Settings()
    screen = pygame.display.set_mode(
        (di_settings.screen_width, di_settings.screen_height))
    pygame.display.set_caption('dinosaur run!')
    #生成对象图片列表
    image_d = ['images/long1.png', 'images/long2.png', 'images/long3.png']
    image_c = ['images/cactus01.png', 'images/cactus02.png', 'images/cactus03.png']
    image_b = ['images/bird1.png', 'images/bird2.png', 'images/bird3.png']
    #初始化障碍物-鸟
    bird = Bird(800, 150, screen)
    dino = Dino(screen)
    dino.load('images/long1_2.png', 40, 43, 2)
    group = pygame.sprite.Group()
    group.add(dino)
    #初始化地图
    aa = 0
    cc = 0
    dd = 0
    bg1 = MyMap(0, 0, screen)
    bg2 = MyMap(734, 0, screen)
    ca1 = obstacle.Cactus(800, 205, screen)
    ca2 = obstacle.Cactus(1200, 205, screen)
    ca3 = obstacle.Cactus(800, 205, screen)
    #设置一些标志变量
    player_jump = 0
    jump_vel = -4.95
    flag_bird = False
    flag_cactus1 = -1
    flag_cactus2 = -1
    flag_cactus3 = -1
    a_rate = 10000
    rate = 2
    #载入结束图像
    image_over = pygame.image.load('images/game_over.png').convert_alpha()
    image_overd = pygame.image.load('images/over.png').convert_alpha()

    tick = pygame.time.Clock()
    #开始游戏主循环
    while True:
        tick.tick(100)
        ticks = pygame.time.get_ticks()
        #计数器
        dd += 1
        scoreboard = Scoreboard(di_settings, screen, dd/10)
        cc += 1
        if int(cc/10) == 3:
            cc  = 0
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_jump = 1
                elif event.key == pygame.K_p:
                    while not event.key == 27:
                        for event in pygame.event.get():
                            print()
                elif event.key == 27:
                    sys.exit()
                else:
                    prtips()

        if dd == 1050:
            a_rate = 2100


        #绘制背景
        bg1.map_update()
        bg2.map_update()
        bg1.map_rolling(rate*(1 + dd/a_rate))
        bg2.map_rolling(rate*(1 + dd/a_rate))
        #是否生成仙人掌
        flag_cactus1 = ca1.randcactus(flag_cactus1)
        flag_cactus2 = ca2.randcactus(flag_cactus2)
        if (not flag_cactus1 == -1) and dd > 1300:
            # 绘制仙人掌
            ca1.blitme(image_c[flag_cactus1])
            flag_cactus1 = ca1.cactus_rolling(flag_cactus1,  rate*(1 + dd/a_rate))
        if (not flag_cactus2 == -1) and dd > 1300:
            ca2.blitme(image_c[flag_cactus2])
            flag_cactus2 = ca2.cactus_rolling(flag_cactus2, rate*(1 + dd/a_rate))
        if dd <= 1000:
            flag_cactus3 = 2
        if flag_cactus3 == 2:
            ca3.blitme(image_c[flag_cactus3])
            flag_cactus3 = ca3.cactus_rolling(flag_cactus3, rate*(1 + dd/a_rate))
        #更新恐龙位置
        jump_vel, player_jump = dino.jump(player_jump, jump_vel, 1+dd/a_rate)
        if player_jump == 0:
            group.update(ticks)
            group.draw(screen)
        else:
            dino.blitme(image_d[2])
        #是否生成飞鸟
        if dd == 800:
            flag_bird = True
            # 更新飞鸟
        if flag_bird:
            flag_bird = bird.bird_rolling()
            bird.blitme(image_b[int(cc / 15)])
        #更新计分板
        scoreboard.show_score()
        # 更新画面

        pygame.display.update()
        #检测碰撞
        hit = hit_find(dino.x, ca1.x, ca2.x, bird.x, dino.y)
        if hit:
            break
    screen.blit(image_over, (270, 100))
    screen.blit(image_overd, (220, 140))
    pygame.display.update()
    time.sleep(1)

run_game()



