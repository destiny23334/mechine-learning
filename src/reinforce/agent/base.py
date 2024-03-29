from abc import abstractmethod


class Agent:
    def __init__(self):
        pass

    @abstractmethod
    def best_action(self):
        """基于当前状态选择策略"""
        pass

    @abstractmethod
    def update(self, action, reward, status):
        """agent基于环境的反馈更新状态"""
        pass
