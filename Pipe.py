class Pipe:
    def __init__(self, input_system, output_system, diameter=1, diameter_margin=0.001, length=1, length_margin=0.001):
        self.diameter = diameter
        self.diameter_margin = diameter_margin
        self.length = length
        self.length_margin = length_margin

        self.input_pressure_table = []
        self.output_pressure_table = []

        self.input_system = input_system
        self.output_system = output_system

    def run_through(self, input_pressure):
        self.input_pressure_table.append(input_pressure)
        output_pressure = 0
        # Bernoulli Equation

        self.output_pressure_table.append(output_pressure)
        return output_pressure
