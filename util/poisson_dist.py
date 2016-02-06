# encoding: utf-8

import math

class PoissonDist:
    '''
    ポアソン分布クラス
    '''
    def get_dist(self, n, expect):
        '''
        arguments:
            expect: 期待値
            n: n
        return:
            P(X=n)
        '''
        if n > 0:
            return (expect ** n) * (math.exp(-expect)) / math.factorial(n)
        else:
            return math.exp(-expect)


def test():
    poisson = PoissonDist()
    print poisson.get_dist(3, 4)


if __name__ == "__main__":
    test()
