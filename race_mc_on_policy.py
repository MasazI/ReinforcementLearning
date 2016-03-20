# encoding: utf-8
'''
方策ONモンテカルロ法(カーレース)
'''

from race import START
from race import COURSE1
from race import MAX_SPEED
from race import OUT
from race import IN
from race import GOAL

from course import Course
from race_action_value import RaceActionValue
from race_policy import RacePolicy

import random

from collections import deque

class MCONPRace:
    def __init__(self, course, value, policy, epsilon=0.1):
        self.course = course
        self.value = value
        self.policy = policy
        self.epsilon = epsilon

    def simulate(self, start=None, learning=True, verbose=False):
        '''
        シュミレーション(方策ONモンテカルロ学習)
        arguments:
            開始地点(Noneの場合はランダムで選択)
            学習フラグ(Trueの場合は学習する)
            デバッグフラグ(Trueの場合はデバッグ実行)
        '''
        if start is None:
            starts = self.course.starts
            start = random.choice(starts)
            print start

        # 状態行動列キュー
        states = deque()
        actions = deque()
        rewards = deque()

        # 初期の状態文字列
        state = start
        # 状態リストに追加
        states.append(state)

        # シュミレーション開始
        while(True):
            valid_actions = self.course.get_valid_actions(state)
            select_action = self.policy.get_action(state)

            # 学習の場合はソフト方式で行動を選択
            if learning:
                select = random.random()
                for i, action in enumerate(valid_actions):
                    if select < ((self.epsilon / len(valid_actions)) * (i+1)):
                        select_action = action
                        break
            # 選択したアクションを状態行動列に追加
            actions.append(select_action)

            # 状態-行動による次の状態と報酬の取得
            next_state, reward = self.course.step(state, select_action)

            states.append(next_state)
            rewards.append(reward)

            state_list = state.split(",")
            action_list = action.split(",")

            if verbose:
                print("position: (%2s, %2s), speed: (%2s, %2s), action: (%2s, %2s), raward: %2d" % (state_list[0], state_list[1], state_list[2], state_list[3], action_list[0], action_list[1], reward))


            if self.course.is_goal(next_state):
                if verbose:
                    print("total rewards: %f" % (sum(rewards)))
                break
            else:
                state = next_state

        if learning:
            # 行動価値を更新
            updated = deque()
            # 終端を切り捨て
            states.pop()
            for i, [state, action] in enumerate(zip(states, actions)):
                # 初回のみ更新:
                if not [state, action] in updated:
                    rewards_list = list(rewards)
                    reward_sum = sum(rewards_list[i:len(rewards)-i])
                    self.value.update(state, action, reward_sum)
                    updated.append([state, action])

            # 方策を更新
            for state, action in updated:
                max_action = self.value.get_max_action(state)
                self.policy.set_action(state, max_action)

def test():
    course = Course(COURSE1)
    value = RaceActionValue()
    policy = RacePolicy(course)
    mcon_policy_race = MCONPRace(course, value, policy, 0.3)

    epochs = 30
    iterations = 10000

    for i in xrange(epochs):
        for j in xrange(iterations):
            mcon_policy_race.simulate(verbose=True)


if __name__ == '__main__':
    test()
