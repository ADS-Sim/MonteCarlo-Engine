import numpy as np


class Pintle:
    def __init__(self):
        self.nb_holes = 112
        self.hole_diameter = 0.0007  # 0.7mm
        self.hole_diameter_std_dev = 0.00005  # 0.05mm
        self.hole_margin_array = np.random.normal(loc=self.hole_diameter,
                                                  scale=self.hole_diameter_std_dev,
                                                  size=self.nb_holes)
