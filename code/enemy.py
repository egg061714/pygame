from pathlib import Path
from typing import Union
import pygame
from pygame.surface import Surface, SurfaceType
from gobject import GameObject
import random
import math

class Enemy(GameObject):
    def __init__(self, playground,xy=None,sensitivity = 1):
        GameObject.__init__(self,playground)
        self._moveScale=0.1*sensitivity
        _parent_path=Path(__file__).parents[1]
        self._player_path = _parent_path/'resource'/'enemy.png'
        self._image = pygame.image.load(self._player_path)
        self._center = self._x+self._image.get_rect().w/2,self._y+self._image.get_rect().h/2
        self._radius = 0.3 *math.hypot(self._image.get_rect().w,self._image.get_rect().h)

        if xy is None:
            self._x = random.randint(10, playground[0]-103)
            self._y = -113
        else:
            self._x = xy[0]
            self._y = xy[1]
        
        self._objectBound = (10, self._playground[0] - 103,-113, self._playground[1])

           # 控制敵人的左右移動
        if random.random() > 0.5:
            self._slope = 0.5
        else:
            self._slope = -0.5
        self._moveScaleX = math.sin(self._slope * math.pi/2) * self._moveScale
        self._moveScaleY = math.cos(self._slope * math.pi/2) * self._moveScale

        self.to_the_bottom()

    def to_the_bottom(self):
        self._changeY = self._moveScaleY
        self._changeX = self._moveScaleX

    def update(self):
        self._x += self._changeX
        self._y += self._changeY

        if random.random() < 0.001:
            self._slope = -self._slope
            self._changeX = math.sin(self._slope * math.pi/2) * self._moveScale
        if self._x > self._objectBound[1]:
            self._x = self._objectBound[1]
            self._slope = -self._slope
            self._changeX = math.sin(self._slope * math.pi / 2) * self._moveScale
        if self._x < self._objectBound[0]:
            self._x = self._objectBound[0]
            self._slope = -self._slope
            self._changeX = math.sin(self._slope * math.pi / 2) * self._moveScale
        if self._y > self._objectBound[3]:
            self._y = self._objectBound[3]
            self.available = False
        if self._y < self._objectBound[2]:
            self._y = self._objectBound[2]

        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2