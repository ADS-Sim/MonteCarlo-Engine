# IMPORTS
import Display
import Simulation


def main():
    print(f"MONTE CARLO SIMULATION - ENGINE")
    sim = Simulation.Simulation()
    sim.run()
    display = Display.Display(sim)
    display.display()


if __name__ == '__main__':
    main()
