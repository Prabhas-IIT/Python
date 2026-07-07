import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [color for color, num in kwargs.items() for _ in range(num)]

    def draw(self, draw_num):
        if draw_num >= len(self.contents):
            removed = self.contents
            self.contents = []
            return removed
        removed = random.sample(self.contents, draw_num)
        for element in removed:
            self.contents.remove(element)
        return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        trial_hat = copy.deepcopy(hat)
        removed = trial_hat.draw(num_balls_drawn)
        removed_dict = {}
        for elem in removed:
            removed_dict[elem] = removed_dict.get(elem, 0) + 1
        if all(removed_dict.get(exp_col, 0) >= exp_num for exp_col, exp_num in expected_balls.items()):
            success += 1
    return success/num_experiments
