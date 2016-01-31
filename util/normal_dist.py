#encoding: utf-8

import math
import random
import numpy as np

class NormalDist:
    '''
    正規分布クラス
    '''
    def __init__(self, exp=0.0, var=1.0):
        '''
        arguments:
            exp: 平均
            var: 分散
        '''
        self.exp = exp
        self.var = var
        self.randoms = np.array([], dtype=np.float)
    
    def get_random(self):
        '''
        分布に従う乱数を生成する
        '''
        if self.randoms.size == 0:
            a = 1.0 - random.random()
            b = 1.0 - random.random()

            z1 = math.sqrt(-2.0 * math.log(a)) * math.cos(2 * math.pi * b)
            z2 = math.sqrt(-2.0 * math.log(a)) * math.sin(2 * math.pi * b)

            rand1 = z1 * math.sqrt(self.var) + self.exp
            rand2 = z2 * math.sqrt(self.var) + self.exp
            self.randoms = np.append(self.randoms, [rand1, rand2])

        value = self.randoms[0]
        self.randoms = np.delete(self.randoms, [0], axis=0)

        return value


if __name__ == '__main__':
    nd = NormalDist()
    print nd.get_random()
    print nd.get_random()
