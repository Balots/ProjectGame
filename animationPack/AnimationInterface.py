from animationPack import animation


class AnimationMethodInterface(animation.AnimationMethod):
    def output(self):
        if len(self._rects) > 0:
            super()._output()
        else:
            super()._get_load_rect()
