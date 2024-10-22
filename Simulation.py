import Content
import InjectionPlate
import Pipe
import System
import Tank


class Simulation:
    def __init__(self):
        self.sim_time = 17  # seconds
        self.sim_steps = 1000  # steps in one second

        # INPUT PARAMETERS
        self.peroxide_tank_pressure = 40  # Bars
        self.peroxide_tank_pressure_margin = 0.001  # ratio
        self.peroxide_concentration = 0.90  # ratio

        self.propane_tank_pressure = 50  # Bars
        self.propane_tank_pressure_margin = 0.001  # ratio

        # System
        self.system = System.System()

        # Output Data
        self.hole_diameter_table = None

    def run(self):
        self.assemble_system()
        self.hole_diameter_table = self.system.injector.hole_margin_array

    def assemble_system(self):
        # Add Tanks
        self.system.tank_list.append(Tank.Tank(Content.Content('Peroxide'), 35))
        self.system.tank_list.append(Tank.Tank(Content.Content('Propane'), 35))
        # Add Pipes
        self.system.pipe_list.append(
            Pipe.Pipe('Peroxide_Tank', 'Injector_Plate', 20, 0.0001, 600, 0.001))  # Add Peroxide Pipe
        self.system.pipe_list.append(Pipe.Pipe('Propane_Tank', 'Chamber', 20, 0.0001, 650, 0.001))  # Add Propane Pipe
        # Add Injection Plate
        self.system.injector = InjectionPlate.InjectionPlate()
