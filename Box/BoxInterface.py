from Box import BoxManager


class Interface(BoxManager.HitBoxManager):
    def create_boxes(self, btype, coordination, move):
        self._create_boxes(btype, coordination, move)

    def set_boxes(self, btype):
        self._set_boxes(btype)

    def load_boxes(self):
        self._load_boxes()

    def get_cor(self):
        return self._get_cor()

    def get_boxes(self):
        return self._get_boxes()

    def uptime_freshening(self):
        self._uptime_data_fleshing()





