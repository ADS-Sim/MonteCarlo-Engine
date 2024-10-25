import numpy as np
import math as m


class InjectionPlate:
    def __init__(self):
        self.nb_holes = 112
        self.hole_diameter = 0.0007  # 0.7mm
        self.hole_diameter_std_dev = 0.00005  # 0.05mm
        self.hole_margin_array = np.random.normal(loc=self.hole_diameter,
                                                  scale=self.hole_diameter_std_dev,
                                                  size=self.nb_holes)
        self.discharge_coefficient = 0.6  # Cd = 0.6
        self.area = 0


    def run_through(self, input_massflow, fluid_density):
        output_pressure = 0
        # Calculate the area of all the holes
        self.calculate_area()

        flowrate = self.discharge_coefficient * self.area * m.sqrt(2 * fluid_density * 0)

        # Convert input pressure in flow rate

        #
        return output_pressure

    def calculate_area(self):
        for hole in self.hole_margin_array:
            self.area += m.pi * hole*hole / 4

    def calculate_pressure_drop(self, input_pressure):
        for hole in self.hole_margin_array:
            pass