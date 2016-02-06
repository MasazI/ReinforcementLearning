# encoding: utf-8
'''
レンタカー状態価値
'''

import rental_car_util as util
import numpy as np

class StatusValue():
    '''
    状態価値
    '''
    def __init__(self):
        '''
        コンストラクタ
        状態価値の初期化
        第1営業所と第2営業所に何台づつレンタカーがあるかの組み合わせの状態がある 20x20
        '''
        rcu = util.RentalCarUtil()

        self.value = np.zeros([rcu.MAX_NUM_RENTAL_CAR, rcu.MAX_NUM_RENTAL_CAR], dtype=np.float)
        print("value shape: ")
        print(self.value.shape)
   
    def get(self, x, y):
        '''
        arguments:
            x: 第1営業所の台数
            y: 第2営業所の台数
        '''
        return self.value[x][y]

    def set(self, x, y, new_value):
        '''
        arguments:
            x: 第1営業所の台数
            y: 第2営業所の台数
            new_value: 新しい状態価値
        '''
        self.value[x][y] = new_value

 
if __name__ == '__main__':
    sv = StatusValue()
    print("a value: ")
    print(sv.get(1, 2))

    print("new value: ")
    sv.set(1,2,3.0)
    print(sv.get(1,2))
