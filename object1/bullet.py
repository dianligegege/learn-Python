'''子弹类'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船发射子弹'''

    def __init__(self, ai_seetings, screen, ship):
        '''在飞船所处位置创建一个子弹对象'''
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_seetings.bullet_width, ai_seetings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.ytop = float(self.rect.y)
        self.color = ai_seetings.bullet_color
        self.speed_factor = ai_seetings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.ytop -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.ytop

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
