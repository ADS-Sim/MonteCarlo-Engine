# IMPORTS
import math as m


class Chamber:
    def __init__(self):
        self.geometrical = None
        self.geometrical_margin = 0.0001  # 0.1mm
        self.combustion_efficiency = 0.95  # ratio

        self.input_diameter = None
        self.input_diameter_margin = None
        self.output_diameter = 0.0408  # meters  throat diameter
        self.output_diameter_margin = 0.0001  # meters

        self.output_diameter = \
        np.random.normal(loc=self.output_diameter + self.output_diameter_margin / 2, scale=self.output_diameter_margin,
                         size=1)[0]

        self.massflow = 0
        self.characteristic_velocity = 1600
        self.pressure = 20

    def run_through(self):
        self.massflow_calculation()

    def massflow_calculation(self):
        # Area calculation
        area = m.pi * pow(self.output_diameter, 2) / 4
        self.massflow = self.pressure * pow(10, 5) * area / self.characteristic_velocity

    def update_characterstic_velocity(self, c_star):
        self.characteristic_velocity = c_star * self.combustion_efficiency
