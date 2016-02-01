# encoding: utf-8

from util import normal_dist

class N_Bandit():
    '''
    N本バンディット問題クラス
    '''
    def __init__(self, size=10, reward_exp_avg=0.0, reward_exp_var=1.0, reward_var=1.0):
        '''
        arguments:
            size: N
            reward_exp_avg: 行動に対する報酬の期待値の平均 E
            reward_var_avg: 行動に対する報酬の期待値の分散 V
            reward_var: 行動に対する報酬の分散
        '''
        self.size = size
        self.bandits = [0]*size
        self.reward_exps = [0]*size
        random = normal_dist.NormalDist(reward_exp_avg, reward_exp_var)

        for i in xrange(size):
            # 報酬の期待値はランダムに生成
            # 行動(N本のバンディット)に対するガウシアン分布
            reward_exp = random.get_random()
            self.bandits[i] = normal_dist.NormalDist(reward_exp, reward_var)
            # 行動(N本のバンディット)に対する報酬の期待値をランダムに決定
            self.reward_exps[i] = reward_exp 

    def select(self, i):
        '''
        i番目のバンディットを選択
        '''
        return self.bandits[i].get_random()


def bandit_exec():
    bandit = N_Bandit()
    print("input 0 - %d, or 'q'" % (bandit.size - 1))
    
    while True:
        input_line = raw_input()

        if input_line == 'q':
            print('quit')
            break

        if 0 <= int(input_line) and int(input_line) <= 9:
            print(bandit.select(int(input_line)))
        else:
            print("input 0 - %d, or 'q'" % (bandit.size - 1))
   
    print("各バンディットの期待値:")
    print(bandit.reward_exps)

    

def test():
    bandit = N_Bandit()
    print bandit.select(0)

    


if __name__ == '__main__':
    #test()
    bandit_exec()
    
