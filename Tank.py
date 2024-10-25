# IMPORTS
import math as m


class Tank:
    def __init__(self, content, volume, pressure):
        self.content = content  # Object Content()
        self.volume = volume  # Liter
        self.pressure = pressure  # Bar
        self.outlet_diameter = 0.021  # meters
        self.discharge_coefficient = 2  # Cd = 2

        self.output_pressure = 15  # Bar
        self.massflow = None  # kg/s

    def run_through(self):
        self.massflow_calculation()
        self.update_output_pressure()

    def massflow_calculation(self):
        try:
            pressure_diff = (self.pressure - self.output_pressure) * pow(10, 5)
            self.massflow = self.discharge_coefficient * m.pi * pow(self.outlet_diameter, 2) / 4 * m.sqrt(
                2 * self.content.density * pressure_diff)
        except Exception as e:
            print(f"In Tank : massflow_calculation : {e}")

    def update_output_pressure(self):
        for _ in range(100):
            self.output_pressure = self.pressure - pow((self.massflow / (self.discharge_coefficient * self.outlet_diameter)), 2)
            self.massflow_calculation()
            print(f"Updated Pressure : {self.pressure} - {self.output_pressure}")

