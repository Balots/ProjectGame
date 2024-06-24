import pygame


class AnimationMethod:
    def __init__(self, screen, timer, counts, objects, load_objects):
        self._screen = screen
        self._objects = objects
        self._load_objects = load_objects
        self._rects = {}
        self._rects_cor = {}
        self._screen_rect = screen.get_rect()
        self._timer = timer
        self._counts = counts

    def _get_load_rect(self):
        for name, obj in self._load_objects.items():
            self._rects[name] = obj.get_rect()

    def _output(self):
        for name, obj in self._objects.items():
            m_status = self._objects['Hector'].m_status
            self._load_objects[name] = [pygame.image.load(x) for x in obj.output()]
            self._rects[name].centerx = self._objects[name].coordination[0]
            self._rects[name].bottom = self._objects[name].coordination[1]
            self._rects_cor[name] = [self._objects[name].coordination[0], self._objects[name].coordination[1]]
            load_object = self._load_objects[name][self._counts[m_status]]
            self._screen.blit(load_object, self._rects[name])


if __name__ == '__main__':
    print('This is not library. Use main file to connect animation.')