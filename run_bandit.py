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
        for i in xrange(self.count):
            selected_arm = self.method.select()
            reward = self.bandit.select(selected_arm)
            self.total_reward += reward
            self.method.reflect(selected_arm, reward)
        self.count += count


    def average(self):
        '''
        得られた報酬の平均
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

