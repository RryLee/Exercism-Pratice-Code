import string
import random

class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        random.seed()
        alphas = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        digits = ''.join(random.choice(string.digits) for _ in range(3))

        self.name = alphas + digits
