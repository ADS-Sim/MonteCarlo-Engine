import numpy as np


class InjectionPlate:
    def __init__(self):
        self.nb_holes = 100
        self.hole_diameter = 0.002  # mm
        self.hole_diameter_std_dev = 0.0005  # mm
        self.hole_margin_array = np.random.normal(loc=self.hole_diameter,
                                                  scale=self.hole_diameter_std_dev,
                                                  size=self.nb_holes)

