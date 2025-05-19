from pathlib import Path
from typing import Union
import pygame
from pygame.surface import Surface, SurfaceType
from gobject import GameObject
import random
import math


class Explosion(GameObject):


    explosion_effect = []

    def __init__(self,xy=None):
        GameObject.__init__(self)
        if xy is None:
            self._y = -100
            self._x = random.randint(10,self._playground[0] -100)
        else:
            self._y = xy[1]
            self._x = xy[0]

        if Explosion.explosion_effect:
            pass
        else:

            _parent_path=Path(__file__).parents[1]
            icon_path=_parent_path /'resource'/'explosion_small.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            icon_path=_parent_path /'resource'/'explosion_medium.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            icon_path=_parent_path /'resource'/'explosion_large.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            icon_path=_parent_path /'resource'/'explosion_medium.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))


        self.__image_index = 0
        self._image = Explosion.explosion_effect[self.__image_index]
        self.__fps_count = 0
        
    def update(self):
        self.__fps_count+=1
        if self.__fps_count>30:
            self.__image_index+=1
            if self.__image_index>3:
                self._available =False
            else:
                self._image = Explosion.explosion_effect[self.__image_index]