from typing import List


class KArmBandit:
    def __init__(self, k: int, reward: List[int]):
        """

        Args:
            k: 摇臂的个数
            reward: 每个摇臂的奖励
        """
        self.reward = reward

    def conduct(self, idx: int) -> int:
        """
        执行一次摇臂

        Args:
            idx: 要执行的摇臂编号，从0开始

        Returns:
            reward：奖励
        """
        return self.reward[idx]


class Agent:
    pass


class SoftmaxAgent(Agent):
    pass


class EGreedyAgent(Agent):
    pass


if __name__ == '__main__':
    game = KArmBandit(8, [1, 2, 3, 4, 5, 6, 7, 8])

