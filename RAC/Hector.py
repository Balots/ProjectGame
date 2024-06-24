from KindObjectArc import PersonSubject


class Hector(PersonSubject):
    def __init__(self, t, ANIMATION_STATUS, HEALTH_POINTS, DAMAGE,
                 coordination, FRAME_COUNTS, earth_level, INERTION):
        self.type = t
        self.status = ANIMATION_STATUS
        self.HP = HEALTH_POINTS
        self.damage = DAMAGE
        self.inertion = INERTION
        self.m_status = 'stay'
        self.coordination = coordination
        self.counts = FRAME_COUNTS
        self.earth = earth_level
        self.atype = {
            'STAY_R': ['animationPack/stay/pixil-frame-l1.png'],
            'STAY_L': ['animationPack/stay/pixil-frame-r1.png'],
            'RUN_R': ['animationPack/run_r/pixil-frame-1.png',
                      'animationPack/run_r/pixil-frame-2.png',
                      'animationPack/run_r/pixil-frame-3.png',
                      'animationPack/run_r/pixil-frame-4.png',
                      'animationPack/run_r/pixil-frame-5.png',
                      'animationPack/run_r/pixil-frame-6.png'],
            'RUN_L': ['animationPack/run_l/pixil-frame-1.png',
                      'animationPack/run_l/pixil-frame-2.png',
                      'animationPack/run_l/pixil-frame-3.png',
                      'animationPack/run_l/pixil-frame-4.png',
                      'animationPack/run_l/pixil-frame-5.png',
                      'animationPack/run_l/pixil-frame-6.png'],
            'JUMP_R': ['animationPack/jump_r/pixil-frame-0.png',
                       'animationPack/jump_r/pixil-frame-1.png',
                       'animationPack/jump_r/pixil-frame-2.png',
                       'animationPack/jump_r/pixil-frame-3.png',
                       'animationPack/jump_r/pixil-frame-4.png',
                       'animationPack/jump_r/pixil-frame-5.png'],
            'JUMP_L': ['animationPack/jump_l/pixil-frame-0.png',
                       'animationPack/jump_l/pixil-frame-1.png',
                       'animationPack/jump_l/pixil-frame-2.png',
                       'animationPack/jump_l/pixil-frame-3.png',
                       'animationPack/jump_l/pixil-frame-4.png',
                       'animationPack/jump_l/pixil-frame-5.png'],
            'HIT_R': ['animationPack/hit/right/pixil-frame-1.png',
                      'animationPack/hit/right/pixil-frame-2.png',
                      'animationPack/hit/right/pixil-frame-3.png',
                      'animationPack/hit/right/pixil-frame-4.png',
                      'animationPack/hit/right/pixil-frame-5.png',
                      'animationPack/hit/right/pixil-frame-6.png'],
            'HIT_L': ['animationPack/hit/left/pixil-frame-1.png',
                      'animationPack/hit/left/pixil-frame-2.png',
                      'animationPack/hit/left/pixil-frame-3.png',
                      'animationPack/hit/left/pixil-frame-4.png',
                      'animationPack/hit/left/pixil-frame-5.png',
                      'animationPack/hit/left/pixil-frame-6.png'],
            'HIT_JUMP_R': ['animationPack/jum_hit/r/pixil-frame-0.png',
                           'animationPack/jum_hit/r/pixil-frame-1.png',
                           'animationPack/jum_hit/r/pixil-frame-2.png',
                           'animationPack/jum_hit/r/pixil-frame-3.png',
                           'animationPack/jum_hit/r/pixil-frame-4.png',
                           'animationPack/jum_hit/r/pixil-frame-5.png'],
            'HIT_JUMP_L': ['animationPack/jum_hit/l/pixil-frame-0.png',
                           'animationPack/jum_hit/l/pixil-frame-1.png',
                           'animationPack/jum_hit/l/pixil-frame-2.png',
                           'animationPack/jum_hit/l/pixil-frame-3.png',
                           'animationPack/jum_hit/l/pixil-frame-4.png',
                           'animationPack/jum_hit/l/pixil-frame-5.png'],
            'KICK_R': ['animationPack/kick/r/pixil-frame-0.png',
                       'animationPack/kick/r/pixil-frame-1.png',
                       'animationPack/kick/r/pixil-frame-2.png',
                       'animationPack/kick/r/pixil-frame-3.png',
                       'animationPack/kick/r/pixil-frame-4.png',
                       'animationPack/kick/r/pixil-frame-5.png'],
            'KICK_L': ['animationPack/kick/l/pixil-frame-0.png',
                       'animationPack/kick/l/pixil-frame-1.png',
                       'animationPack/kick/l/pixil-frame-2.png',
                       'animationPack/kick/l/pixil-frame-3.png',
                       'animationPack/kick/l/pixil-frame-4.png',
                       'animationPack/kick/l/pixil-frame-5.png'],
            'KICK_JUMP_R': ['animationPack/jump_kick/r/pixil-frame-0.png',
                            'animationPack/jump_kick/r/pixil-frame-1.png',
                            'animationPack/jump_kick/r/pixil-frame-2.png',
                            'animationPack/jump_kick/r/pixil-frame-3.png',
                            'animationPack/jump_kick/r/pixil-frame-4.png',
                            'animationPack/jump_kick/r/pixil-frame-5.png'],
            'KICK_JUMP_L': ['animationPack/jump_kick/l/pixil-frame-0.png',
                            'animationPack/jump_kick/l/pixil-frame-1.png',
                            'animationPack/jump_kick/l/pixil-frame-2.png',
                            'animationPack/jump_kick/l/pixil-frame-3.png',
                            'animationPack/jump_kick/l/pixil-frame-4.png',
                            'animationPack/jump_kick/l/pixil-frame-5.png']
        }

    def output(self):
        return self.atype[self.status]

    def access_info(self):
        return self.status, self.m_status, self.coordination

    def changes(self):
        self._right()
        self._left()
        self._jump()
        self._hit()
        self._gravitation()
        self._inertion()
        self._kick()

    def _right(self):
        if self.status == 'RUN_R':
            self.coordination[0] += 10
            self.counts['frame_run'] += 1
            self.inertion += 1
            if self.counts['frame_run'] > 5:
                self.counts['frame_run'] = 0

    def _left(self):
        if self.status == 'RUN_L':
            self.coordination[0] -= 10
            self.counts['frame_run'] += 1
            self.inertion -= 1
            if self.counts['frame_run'] > 5:
                self.counts['frame_run'] = 0

    def _inertion(self):
        if self.status != 'RUN_L' or self.status != 'RUN_R':
            self.coordination[0] += self.inertion
            self.inertion += (-self.inertion)/6
        if self.status == 'STAY_R' or self.status == 'STAY_L':
            self.coordination[0] += self.inertion
            self.inertion = 0

    def _jump(self):
        if self.status == 'JUMP_R' or self.status == 'JUMP_L' or self.counts['frame_jump'] >= 1:
            if self.counts['frame_jump'] < 5:
                self.counts['frame_jump'] += 1
                self.coordination[1] -= 20
                self.coordination[0] += self.inertion

    def _gravitation(self):
        if self.counts['frame_jump'] >= 5:
            self.coordination[1] += 20
            self.coordination[0] += self.inertion
            if self.coordination[1] == self.earth:
                self.counts['frame_jump'] = 0
                if self.status[-1] == 'R':
                    self.status = 'STAY_R'
                    self.m_status = 'stay'
                elif self.status[-1] == 'L':
                    self.status = 'STAY_L'
                    self.m_status = 'stay'

    def _hit(self):
        if (self.status == 'HIT_R' or
                self.status == 'HIT_L' or
                self.status == 'HIT_JUMP_R' or
                self.status == 'HIT_JUMP_L'):
            self.counts['frame_hit'] += 1
        if self.counts['frame_hit'] == 5:
            self.counts['frame_hit'] = 0
            if self.status == 'HIT_R' or self.status == 'HIT_JUMP_R':
                self.status = 'STAY_R'
            else:
                self.status = 'STAY_L'

    def _kick(self):
        if (self.status == 'KICK_R' or
                self.status == 'KICK_L' or
                self.status == 'KICK_JUMP_R' or
                self.status == 'KICK_JUMP_L'):
            self.counts['frame_kick'] += 1
        if self.counts['frame_kick'] == 5:
            self.counts['frame_kick'] = 0
            if self.status == 'KICK_R' or self.status == 'KICK_JUMP_R':
                self.status = 'STAY_R'
            else:
                self.status = 'STAY_L'


if __name__ == '__main__':
    print('PROTECT')
