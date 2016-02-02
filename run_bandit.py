# encoding: utf-8
import n_bandit
import greedy as gd

class RunBandit():
    '''
    N本腕バンディット問題のアルゴリズム実行
    '''
    def __init__(self, bandit, method):
        self.bandit = bandit
        self.method = method
        self.count = 0
        self.total_reward = 0


    def do(self, count):
        '''
        試行と学習(行動価値の更新)
        '''
        for i in xrange(self.count):
            # 腕を選択
            selected_arm = self.method.select()
            # 試行して報酬を取得
            reward = self.bandit.select(selected_arm)
            # 合計報酬に加算
            self.total_reward += reward
            # 行動の価値を更新
            self.method.reflect(selected_arm, reward)
        self.count += count


    def average(self):
        '''
        得られた報酬の試行回数に対する平均(報酬の期待値の最大値に近づくことを目指す)
        '''
        try:
            return (self.total_reward * 1.0) / self.count
        except Exception:
            return 0.0


    def max_exp(self):
        '''
        報酬の期待値の最大値
        '''
        return max(self.bandit.reward_exps)


    def optimality(self):
        '''
        最適度
        '''
        return self.average()/self.max_exp()
    


if __name__ == '__main__':
    bandit_num = 10

    bandit = n_bandit.N_Bandit(size=bandit_num)
    
    greedy = RunBandit(bandit, gd.Greedy(bandit_num))

    epsilon_greedy = RunBandit(bandit, gd.Greedy(bandit_num))

    for method in [greedy, epsilon_greedy]:
        print("---------------------------------")
        print("time, reward.average, optimality")
        print("---------------------------------")
        for i in range(20):
            method.do(100)
            print("%d, %f, %f" % (method.count, method.average(), method.optimality()))

