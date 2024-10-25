import Chamber
import Content
import InjectionPlate
import Nozzle
import Pintle
import Pipe
import RegCol
import System
import Tank


class Simulation:
    def __init__(self):
        self.sim_time = 5  # seconds
        self.sim_steps = 10  # steps in one second

        # INPUT PARAMETERS
        self.peroxide_tank_pressure = 45  # Bars
        self.peroxide_tank_pressure_margin = 0.001  # ratio
        self.peroxide_concentration = 0.90  # ratio

        self.propane_tank_pressure = 45  # Bars
        self.propane_tank_pressure_margin = 0.001  # ratio

        # System
        self.system = System.System()

        # Output Data
        self.hole_diameter_table = None

    def run(self):
        # Implements all the
        self.assemble_system()

        # Running the loop of the simulation
        for simu_steps in range(self.sim_steps * self.sim_time):
            print(f"\n Simu Step : {simu_steps}")
            # Processing each Line
            for index, line in enumerate(self.system.line_list):
                self.system.tank_list[index].run_through()
                # print(self.system.tank_list[index].pressure)
                self.system.pipe_list[index].run_through(self.system.tank_list[index].content,
                                                         self.system.tank_list[index].output_pressure)
                # print(self.system.pipe_list[index].pressure)
                print(
                    f"Tank {self.system.tank_list[index].content.name} massflow : {self.system.tank_list[index].massflow}")
                print(
                    f"Pipe {self.system.tank_list[index].content.name} massflow : {self.system.pipe_list[index].massflow}")

                # Retroactive Loop
                self.system.tank_list[index].update_output_pressure()
                print(
                    f"Pressure of {self.system.tank_list[index].content.name} : {self.system.tank_list[index].output_pressure}")

    def assemble_system(self):
        # Add Tanks
        self.system.tank_list.append(Tank.Tank(Content.Content('Peroxide', 1400, 283), 18, self.peroxide_tank_pressure))
        self.system.tank_list.append(Tank.Tank(Content.Content('Propane', 500, 263), 6, self.propane_tank_pressure))
        # Add Pipes
        self.system.pipe_list.append(
            Pipe.Pipe('Peroxide_Tank', 'Injector_Plate', 1.6, 1400))  # Add Peroxide Pipe
        self.system.pipe_list.append(Pipe.Pipe('Propane_Tank', 'Chamber', 0.32, 500))  # Add Propane Pipe
        # Add Regenerative cooling
        self.system.regenerative_cooling = RegCol.RegCol()
        # Add Injection Plate
        self.system.injector = InjectionPlate.InjectionPlate()
        # Add Pintle
        self.system.pintle = Pintle.Pintle()
        # Add Chamber
        self.system.chamber = Chamber.Chamber()
        # Add Nozzle
        self.system.nozzle = Nozzle.Nozzle()
