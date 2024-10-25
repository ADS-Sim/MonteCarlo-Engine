import matplotlib.pyplot as plt


class Display:
    def __init__(self, simulation):
        self.holes_figure, self.holes_ax = plt.subplots()

        self.simulation = simulation

    def display_injection_holes_diameters(self, gaussian_values):
        # Display the Injection holes diameters
        self.holes_ax.hist(gaussian_values, bins=200, density=True, alpha=1, color='g')
        self.holes_ax.set_xlabel('Diameter (m)')
        self.holes_ax.set_yticklabels([])
        self.holes_ax.set_title('Gaussian Diameter Distribution')

    def display(self):
        # Display all the graphs
        self.display_injection_holes_diameters(self.simulation.hole_diameter_table)
        try:
            plt.show()
        except KeyboardInterrupt:
            pass
