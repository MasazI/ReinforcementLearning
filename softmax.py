# encoding: utf-8

import math
import random

class SoftMaxMethod:
    '''
    softmax法クラス
    '''
    def __init__(self, size=10, tau=0.1, stepsize=None):
        self.size = size
        self.tau = tau
        self.stepsize = stepsize
   
        self.times = [0]*size
        self.values = [0.0]*size
        self.weights = [1.0]*size

    def select(self):
        '''
        腕の選択
        '''
        weight_total = sum(self.weights)
        rand = random.random() * weight_total
        selected = 0
        for i in range(10):
            # 重みが大きいほど選択されやすい
            if rand <= self.weights[i]:
                selected = i
                break
            else:
                rand -= self.weights[i]
        return selected   

    def reflect(self, selected, value):
        '''
        選択した腕の報酬を推定行動価値に反映
        '''
        self.times[selected] += 1
        if self.stepsize is not None:
            stepsize = self.stepsize
        else:
            # stepsizeの指定がなければ、1/各腕の試行回数
            stepsize = 1.0/self.times[selected] 
        # 前回の行動価値に対して今回の行動を反映
        self.values[selected] += stepsize * (value - self.values[selected])
        self.weights[selected] = math.exp(self.values[selected]/self.tau)
