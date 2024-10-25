# IMPORTS
import math as m


class Content:
    def __init__(self, name, density, temperature):
        self.name = name
        self.density = density  # kg/m3
        self.viscosity = None
        self.temperature = temperature  # K

    def peroxide_viscosity(self, temperature):
        self.viscosity = 1.8177 * m.exp(-0.017 * (temperature - 273.15)) * 0.001

    def peroxide_density(self, temperature):
        self.density = -1.1217 * (temperature - 273.15) + 1414.2

    def set_parameters(self):
        if self.name == 'Peroxide':
            self.peroxide_density(self.temperature)
            self.peroxide_viscosity(self.temperature)
        elif self.name == 'Propane':
            pass
        else:
            print(f"Error Content Name Issue : {self.name}")

    def update_temperature(self, temperature):
        if 0 <= temperature:
            self.temperature = temperature
