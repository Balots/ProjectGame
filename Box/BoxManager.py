from Box import DamageBlock
import pygame


class HitBoxManager:
    def __init__(self, screen):
        self.__db = DamageBlock.DamageBlock
        self.__surface = pygame.Surface((1, 1), pygame.SRCALPHA).convert_alpha()
        self.__damage_boxes = {}
        self.__hit_boxes = {}
        self.__coordination = []
        self.__all_sprites = pygame.sprite.Group()
        self.__screen = screen

    def _create_boxes(self, btype, coordination, move):
        c_x, c_y = int(coordination[0]) - 13, int(coordination[1])
        for y in range(c_y, c_y - 100, -5):
                self.__hit_boxes[(c_x, y)] = self.__db(self.__surface, self.__screen, btype)
        if btype == 'damage_box':
            for y in range(c_y, c_y - 100, -5):
                self.__damage_boxes[(c_x + move, y)] = self.__db(self.__surface, self.__screen, btype)

    def _set_boxes(self, btype):
        for cor, box in self.__hit_boxes.items():
            box.set_box(cor)
        if btype == 'damage_box':
            for cor, box in self.__damage_boxes.items():
                box.set_box(cor)

    def _load_boxes(self):
        for box in ([self.__hit_boxes.values()] + [self.__damage_boxes.values()]):
            self.__all_sprites.add(box)

    def _get_cor(self):
        return list(self.__hit_boxes.keys()) + list(self.__damage_boxes.keys())

    def _wt_sit_bx(self, cor):
        try:
            return self.__hit_boxes[cor].btype
        except KeyError:
            return self.__damage_boxes[cor].btype

    def _get_boxes(self):
        return list(self.__damage_boxes.keys()) + list(self.__hit_boxes.keys())


    def _uptime_data_fleshing(self):
        self.__hit_boxes = {}
        self.__damage_boxes = {}









