# encoding: utf-8
'''
カーレース学習クラス
'''

import race
from course import Course
from race_action_value import RaceActionValue
from race_policy import RacePolicy

from race_mc_off_policy import MCOFFPRace

def do(course_info):
    '''
    指定したコースについて学習する
    arguments:
        course_info: コース情報(文字列)
    '''
    course = Course(course_info)
    value = RaceActionValue()
    policy = RacePolicy(course)
    mcon_policy_race = MCOFFPRace(course, value, policy, 0.3)

    epochs = 30
    iterations = 10000

    for i in xrange(epochs):
        print("*"*20)
        print("epocs.%d" %(i))
        for j in xrange(iterations):
            mcon_policy_race.simulate(training=True, verbose=False)

        print("="*20)
        print("iteration.%d done" %(i*iterations))
        for start in course.starts:
            print("-"*25)
            print("start: %s" % (start))
            mcon_policy_race.simulate(start, training=False, verbose=True)


if __name__ == '__main__':
    do(race.COURSE1)
