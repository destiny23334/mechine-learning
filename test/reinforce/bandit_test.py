from loguru import logger

from reinforce.agent.bandit import EpsilonGreedyAgent
from reinforce.env.bandit import KArmBandit

if __name__ == '__main__':
    bandit_num = 5
    bandit_reward = [8, 2, 3, 7, 5]
    epsilon = 0.1
    uncertainty = 0.1
    agent = EpsilonGreedyAgent(epsilon, bandit_num)
    env = KArmBandit(bandit_num, bandit_reward, uncertainty=uncertainty)

    for i in range(1000):  # 进行100轮游戏
        action = agent.best_action()
        reward = env.step(action, agent)
        logger.info(f"第{i + 1}轮游戏：摇动摇臂{action}，得到奖励{reward}")
    logger.info(f"最终策略为：{agent.strategy}")
    logger.info(f"摇动摇臂数量统计：{agent.action_count}")
