import pygame
from RAC import *
from const import *


class LoadMethod:
    def __init__(self, screen):
        self._graphic_objects = compilerRAC.ExportModule()
        self._objects = {}
        self._load_objects = {}
        self._screen = screen

    def _load_gamer_person(self):
        coordination = [self._screen.get_rect().centerx, self._screen.get_rect().bottom]
        self._objects['Hector'] = self._graphic_objects.AG['Hector'].Hector('Hector',
                                                                            ANIMATION_STATUSES[0],
                                                                            HEALTH_POINTS,
                                                                            DAMAGE,
                                                                            coordination,
                                                                            FRAME_COUNTS,
                                                                            coordination[1],
                                                                            BODY_INERTION)

    def _load(self):
        for name, obj in self._objects.items():
            for load_object in obj.output():
                self._load_objects[name] = pygame.image.load(load_object)

    def _runtime_load(self):
        for obj in self._objects.values():
            obj.changes()

    @property
    def objects(self):
        return self._objects

    @property
    def load_objects(self):
        return self._load_objects


if __name__ == '__main__':
    print('PROTECT')
