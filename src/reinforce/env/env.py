from abc import ABCMeta


class Environment(metaclass=ABCMeta):
    def step(self):
        pass
