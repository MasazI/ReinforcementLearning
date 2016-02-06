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
        self.rcu = util.RentalCarUtil()

        self.value = np.zeros([self.rcu.MAX_NUM_RENTAL_CAR, self.rcu.MAX_NUM_RENTAL_CAR], dtype=np.float)
        print("value shape: ")
        print(self.value.shape)

        self.print_bar = "----" + ("-------" * self.rcu.MAX_NUM_RENTAL_CAR)
        self.print_header = "   |"
        for i in range(self.rcu.MAX_NUM_RENTAL_CAR):
            self.print_header += "    %02d " % (i+1)

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

    def output(self):
        '''
        状態価値の出力
        '''
        print self.print_bar
        print self.print_header
        print self.print_bar
        for j in range(self.rcu.MAX_NUM_RENTAL_CAR):
            print_format = "%02d |" % (j+1)
            for i in range(self.rcu.MAX_NUM_RENTAL_CAR):
                print_format += " %5.1f " % self.value[i][j]
            print print_format

    def value_of_move(self, x, y, move):
        '''
        行動(車の移動)のとき状態価値の計算
        arguments:
            x: 第1営業所
            y: 第2営業所
            move: 状態(x, y) から moveだけ車を移動する行動
                  moveは第1営業所から第2営業所に移動する数
                  -であれば逆になる
        return:
            value: 状態価値
        '''
        # 初期化
        value = .0 
        
        # 次の朝に第1営業所にある車の数
        next_x_start = x - move
        # 次の朝に第2営業所にある車の数
        next_y_start = y + move

        # validation
        if (next_x_start < 0) or (next_x_start > self.rcu.MAX_NUM_REANTAL_CAR) or (next_y_start < 0) or (next_y_start > self.rcu.MAX_NUM_REANTAL_CAR):
            raise Exception("move is invalid.")

        # 第1営業所で貸し出せるのは 0 ~ next_x_start、第2営業所で貸し出せるのは 0 ~ next_y_start
        

        

 
def test():
    sv = StatusValue()
    print("a value: ")
    print(sv.get(1, 2))

    print("new value: ")
    sv.set(1,2,3.0)
    print(sv.get(1,2))

    sv.output()


if __name__ == '__main__':
    test()
