import copy
import random

class Hat:
    def __init__(self, **kvargs):
        self.contents = []
        for key, value in kvargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, num):
        removed = []
        if num >= len(self.contents):
            removed = self.contents[:]
            self.contents = []  # Empty the hat
        else:
            for _ in range(num):
                index = random.randint(0, len(self.contents) - 1)
                removed_el = self.contents.pop(index)
                removed.append(removed_el)
        return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        ex_copy = copy.deepcopy(expected_balls)
        color_get = hat_copy.draw(num_balls_drawn)

        for color in color_get:
            if color in ex_copy:
                ex_copy[color] -= 1

        if all(value <= 0 for value in ex_copy.values()):
            count += 1
    return count / num_experiments

# Example usage
hat = Hat(red=1, green=2, blue=3)
random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000
)
print("Probability:", probability)
