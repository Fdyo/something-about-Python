__author__ = 'Fdyo'
#coding: utf-8
from random import choice

class Free_walk():
    def __init__(self, steps=5000):
        self.x_label = [0]
        self.y_label = [0]
        self.steps = steps
    def start_walk(self):
        while len(self.x_label) <= self.steps:
            next_x = self.step_point()
            next_y = self.step_point()
            if next_x == next_y == 0:
                continue
            next_xlabel = self.x_label[-1] + next_x
            next_ylabel = self.y_label[-1] + next_y
            self.x_label.append(next_xlabel)
            self.y_label.append(next_ylabel)

    def step_point(self):
        step_direction = choice([-1, 1])
        step_distance = choice([0, 1, 2, 3, 4, 5])
        step_label = step_direction*step_distance
        return step_label