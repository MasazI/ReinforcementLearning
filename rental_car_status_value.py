# encoding: utf-8
'''
レンタカー状態価値
'''

import rental_car_util as util
import numpy as np

from util import poisson_dist

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

        self.value = np.zeros([self.rcu.MAX_NUM_RENTAL_CAR+1, self.rcu.MAX_NUM_RENTAL_CAR+1], dtype=np.float)
        print("value shape: ")
        print(self.value.shape)

        self.print_boundary = "====" + ("=======" * (self.rcu.MAX_NUM_RENTAL_CAR+1))
        self.print_bar = "----" + ("-------" * (self.rcu.MAX_NUM_RENTAL_CAR+1))
        self.print_header = "   |"
        for i in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
            self.print_header += "    %02d " % (i)

        # ポアソン分布
        self.pd = poisson_dist.PoissonDist()

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
        print self.print_boundary
        print self.print_header
        print self.print_bar
        for j in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
            print_format = "%02d |" % (j)
            for i in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
                print_format += " %5.1f " % self.value[i][j]
            print print_format

    def value_of_move(self, x, y, move):
        '''
        状態x,yに対する行動(車の移動)の価値の計算
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
       
        # V(s) 
        # 次の朝に第1営業所にある車の数
        next_x_start = x - move
        # 次の朝に第2営業所にある車の数
        next_y_start = y + move

        # validation
        if (next_x_start < 0) or (next_x_start > self.rcu.MAX_NUM_RENTAL_CAR) or (next_y_start < 0) or (next_y_start > self.rcu.MAX_NUM_RENTAL_CAR):
            raise Exception("move is invalid.")

        # 次の朝第1営業所で貸し出せるのは 0 ~ next_x_start
        # 次の朝第2営業所で貸し出せるのは 0 ~ next_y_start
        for x_rental in xrange(next_x_start + 1):
            for y_rental in xrange(next_y_start + 1):
                x_rest = next_x_start - x_rental
                y_rest = next_y_start - y_rental

                # 次の朝第1営業所に返却することができるのは 0 ~ MAX_NUM_RANTAL_CAR - x_rest
                # 次の朝第2営業所に返却することができるのは 0 ~ MAX_NUM_RENTAL_CAR - y_rest
                for x_return in xrange(self.rcu.MAX_NUM_RENTAL_CAR + 1 - x_rest):
                    for y_return in xrange(self.rcu.MAX_NUM_RENTAL_CAR + 1 - y_rest):
                        # 全ての行動の確率を掛け合わせる
                        probability = self.x_rental_probability(x_rental) * self.y_rental_probability(y_rental) * self.x_return_probability(x_return) * self.y_return_probability(y_return)
           
                        # 報酬(Reward)
                        # 貸し出すと10ドルの報酬、逆に借りると2ドルの減益
                        reward = (x_rental + y_rental) * 10 - abs(move) * 2
                        
                        # さらに次の状態 V(s+1) は、次の朝の台数に貸出分を引き、返却分を足す
                        next_x = next_x_start - x_rental + x_return
                        next_y = next_y_start - y_rental + y_return

                        # 価値の期待値
                        # 確率 * (報酬 + 次の[x, y]の報酬) を全ての状態について足し合わせる
                        value += probability * (reward + self.rcu.discount_rate * self.value[next_x][next_y])
                        
        return value

    def get_most_valuable_move(self, x, y, *move_list):
        '''
        最大の価値の行動
        '''
        # 状態x, yに対する行動と価値のMapを生成
        # key: move, value: value of move
        move_value_map = {}
        print move_list
        for move in move_list:
            print move
            value = self.value_of_move(x, y, move)
            move_value_map[move] = value

        # 最大の価値をとる行動
        highest_value_move = max(move_value_map)
        # 最大の価値
        highest_value = move_value_map[highest_value_move]

        return highest_value_move, highest_value

    def x_rental_probability(self, n):
        '''
        第1営業所の貸台数がnになる確率. 期待値3
        '''
        return self.pd.get_dist(n, 3)
    
    def y_rental_probability(self, n):
        '''
        第2営業所の貸台数がnになる確率. 期待値4
        '''
        return self.pd.get_dist(n, 4)
    
    def x_return_probability(self, n):
        '''
        第1営業所への返却台数がnになる確率. 期待値3
        '''
        return self.pd.get_dist(n, 3)
    
    def y_return_probability(self, n):
        '''
        第2営業所への返却台数がnになる確率. 期待値4
        '''
        return self.pd.get_dist(n, 2)

 
def test():
    sv = StatusValue()
    print("a value: ")
    print(sv.get(1, 2))

    print("new value: ")
    sv.set(1,2,3.0)
    print(sv.get(1,2))

    sv.output()
    print sv.get_most_valuable_move(5,6,1,2,3)


if __name__ == '__main__':
    test()
