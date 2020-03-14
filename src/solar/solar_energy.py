import pandas as pd
import json

"""
    Clase que gestiona toda la informacion destinada y alamacena toda la informacion detallada de la energia solar
    Datos extraidos de la web de la eu
"""

class Solar_energy:
    def __init__(self, configurator, type_data):
        self.config = configurator
        self.type_data = type_data 

    def extract_json_to_dataframe(self):
        # Limpiamos los datos
        with open(self.config.get_where(input_type = self.type_data)) as json_file:
            self.data = json.load(json_file)
            return pd.DataFrame(self.data["outputs"][self.type_data])

    def get_data(self):
        return self.data

    def number_panels_compare_consume(self, df_sensor_month):
        """Metodo que compara con un dataset del mismo tipo y saca el numero placas para superar el consumo
        
        Arguments:
            df_sensor_month {[type]} -- [description]
        """
        print(df_sensor_month)
        #return self.data.where(self.data.values==self.df_sensor_month.values)
        
