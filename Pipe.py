# IMPORTS
import math as m


class Pipe:
    def __init__(self, input_system, output_system, flow_factor, specific_gravity):
        self.pressure = 1
        self.output_pressure = 1
        self.massflow = 0

        self.discharge_coefficient = 0.76  # Cd = 0.76
        self.flow_factor = flow_factor  # Kv = 0
        self.specific_gravity = specific_gravity

    def run_through(self, content, input_pressure):
        self.update_pressure(input_pressure)
        self.massflow_calculation(content)

    def massflow_calculation(self, content):
        try:
            pressure_diff = (self.pressure - self.output_pressure) * pow(10, 5)
            volume_flow = self.flow_factor * m.sqrt(self.specific_gravity / pressure_diff)
            self.massflow = content.density * volume_flow
        except Exception as e:
            print(f"In Pipe : massflow_calculation : {e}")

    def update_pressure(self, input_pressure):
        self.pressure = input_pressure
