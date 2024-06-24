import pygame


class DamageBlock(pygame.sprite.Sprite):
    def __init__(self, psurf, screen, btype):
        pygame.sprite.Sprite.__init__(self)
        self.__image = psurf
        self.__rect = self.__image.get_rect()
        self.__is_stunning = False
        self.__duration = 1
        self.__damaged = False
        self.__screen = screen
        self.btype = btype

    def return_collision_status(self):
        return self.__damaged

    def set_box(self, coordination: tuple):
        self.__rect.center = coordination
        self.__screen.blit(self.__image, self.__rect)

