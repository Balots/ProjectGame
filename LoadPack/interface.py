from LoadPack import Load_package


class LoadMethodInterface(Load_package.LoadMethod):
    def get_load_objects(self):
        super()._load_gamer_person()
        super()._load()
        return self.load_objects

    def get_runtime_load(self):
        super()._runtime_load()