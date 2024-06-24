from abc import ABC, abstractmethod


class PersonSubject(ABC):
    @abstractmethod
    def output(self):
        pass

    @abstractmethod
    def access_info(self):
        pass

    @abstractmethod
    def changes(self):
        pass

    @abstractmethod
    def _right(self):
        pass

    @abstractmethod
    def _left(self):
        pass

    @abstractmethod
    def _jump(self):
        pass

    @abstractmethod
    def _hit(self):
        pass

    @abstractmethod
    def _gravitation(self):
        pass

    @abstractmethod
    def _inertion(self):
        pass

    @abstractmethod
    def _kick(self):
        pass


if __name__ == '__main__':
    print('PROTECT')