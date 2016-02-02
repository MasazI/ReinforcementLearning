#encoding: utf-8

import math
import random

class Greedy:
    '''
    greedy法クラス
    '''
    def __init__(self, size=10, epsilon=0.0, stepsize=None):
        '''
        arguments:
            size: n本腕
            epsilon: epsilonグリーディのランダムに選択する確率epsilon
            stepsize: 繰り返し回数
        '''
        self.size = size
        self.epsilon = epsilon
        self.stepsize = stepsize

        self.times = [0]*size # 行動の試行回数
        self.values = [0.0]*size # 行動に対する価値


    def select(self):
        '''
        greedyに腕を選択(選択した腕のインデックスを返す)
        '''
        if random.random() < self.epsilon:
            # epsilonより小さい場合はランダムに腕を選択
            return random.randint(0, self.size-1)
        else:
            # 前回までの試行でもっとも価値の高い腕を選択
            return self.values.index(max(self.values))
    

    def reflect(self, selected, value):
        '''
        学習=得られた報酬の反映
        arguments:
            selected: 選んだ腕のindex
            value: 得られた報酬(selectedの選択で得た報酬)
        '''
        # 試行回数をインクリメント
        self.times[selected] += 1

        if self.stepsize is not None:
            # stepsizeの指定があれば使用
            stepsize = self.stepsize
        else:
            # stepsizeの指定がなければ、1/試行回数k
            stepsize = 1.0/self.times[selected]

        # 報酬の更新
        self.values[selected] += stepsize * (value - self.values[selected])

    

def test():
    greedy = Greedy(epsilon=0.3)
    greedy.reflect(greedy.select(), 3)    
    greedy.reflect(greedy.select(), 3)
    greedy.reflect(greedy.select(), 4)
    print greedy.values

if __name__ == '__main__':
    test()
