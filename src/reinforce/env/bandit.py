from typing import Iterable

import numpy as np

from reinforce.agent.base import Agent


class KArmBandit:
    def __init__(self, k: int, r: Iterable, uncertainty=0):
        """k-摇臂赌博机

        Parameters
        ----------
        k : int
            摇臂数
        r : Iterable
            每个摇臂的基础奖励
        uncertainty : float
            不确定性。游戏时会根据不确定性对摇臂的奖励做一个修正。0表示不修正，1表示偏差最多100%
        """
        self.k = k
        self.uncertainty = uncertainty
        assert 0 <= uncertainty <= 1
        self.reward = list(r)

    def get_actions(self):
        """k个摇臂就有k个action，对应0~k-1"""
        return list(range(self.k))

    def step(self, action: int, agent: Agent):
        """当agent采用action策略时，得到的奖励。（标准强化学习还应该返回转移的状态）"""
        base = self.reward[action]
        low, high = (1 - self.uncertainty) * base, (self.uncertainty + 1) * base
        reward = np.random.uniform(low, high)
        agent.update(action, reward, None)
        return reward
