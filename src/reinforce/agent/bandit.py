import numpy as np

from reinforce.agent.base import Agent


class EpsilonGreedyAgent(Agent):

    def __init__(self, epsilon: float, k: int):
        """
        Parameters
        ----------
        epsilon : float
            阈值
        k : int
            摇臂数
        """
        super().__init__()
        self.epsilon = epsilon
        self.k = k
        self.strategy = np.zeros(k)
        self.action_count = np.zeros(k, dtype=int)

    def best_action(self) -> int:
        """当随机数大于阈值的时候就选择当前平均奖励最高的那个摇臂，否则随机选一个摇臂"""
        r = np.random.random()
        if r < self.epsilon:  # 随机取
            return np.random.randint(0, self.k)
        # 否则取最大
        action = np.random.choice(np.where(self.strategy == np.max(self.strategy))[0])
        return action

    def update(self, action, reward, status):
        """k摇臂赌博只需要reward就可以更新"""
        self.action_count[action] += 1
        self.strategy[action] = (self.strategy[action] + reward) / (self.action_count[action])
