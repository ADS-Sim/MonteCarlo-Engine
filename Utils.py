import pandas as pd
import math as m


class Utils:
    def __init__(self):
        # Oxidizer Fuel Ratio
        self.file_path_of_ratio = 'rocket_cea_data_h2o2_c3h8.xlsx'
        self.sheet_name_of_ratio = 'CEA analysis'
        self.of_ratio_dataframe = None

        self.data_importer()

    def data_importer(self):
        self.of_ratio_dataframe = pd.read_excel(self.file_path_of_ratio, sheet_name=self.sheet_name_of_ratio)

    def get_of_ratio_data(self, of_ratio, pressure):
        col_name_of = "O/F"
        col_name_pressure = "P_c [bar]"
        result_row = self.of_ratio_dataframe[(self.of_ratio_dataframe[col_name_of] == of_ratio) & (
                    self.of_ratio_dataframe[col_name_pressure] == pressure)]
        return result_row

    def gamma_defintion(self, gamma):
        gamma_m = m.sqrt(gamma) * pow(2 / (gamma + 1), (gamma + 1) / (2 * (gamma - 1)))
        return gamma_m

    def characteristic_velocity_calculation(self, temperature, gamma_m, gaz_constant, molar_mass):
        c_star = m.sqrt(gaz_constant * temperature) / gamma_m
        return c_star
