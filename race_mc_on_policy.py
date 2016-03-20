# encoding: utf-8
'''
方策ONモンテカルロ法(カーレース)
'''

from race import START
from race import COURSE1
from race import MAX_SPEED
from race import OUT
from race import IN
from race import GOAL

from course import Course
from race_action import RaceActionValue
from race_policy import RacePolicy

class MCONPRace:
    def __init__(self, course, value, policy, epsilon=0.1):
        self.course = course
        self.value = value
        self.policy = policy
        self.epsilon = epsilon



        
