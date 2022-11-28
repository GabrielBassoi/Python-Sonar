from time import sleep
import numpy as np


class Tests:
    def __init__(self):
        self.angg = 0
        self.x = False
        self.indx = 0
        self.y = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
                  40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
                  60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
                  60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
                  70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
                  70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
                  70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
                  70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
                  90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
                  90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
                  90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
                  90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
                  90, 90, 90, 90, 90, 90, 90, 90, 90, 90
                  ]

    def get_data_test(self):
        angle = int(input("Angle: "))
        dist = int(input("Distance: "))
        return angle, dist

    def get_data_auto_test(self):
        sleep(0.01)
        if self.angg == 180:
            self.x = True
        if self.angg == 0:
            self.x = False
        if not self.x:
            self.angg += 1
        if self.x:
            self.angg -= 1
        return self.angg, np.random.randint(0, 100)

    def get_data_defined_test(self):
        self.indx += 1
        if self.indx == 179:
            self.indx = 0
        return self.indx, self.y[self.indx]
