import pandas as pd


class Extracts:
    def __init__(self, data_source) -> None:
        self.data_source = data_source

    def read_csv(self):
        df = pd.read_csv(filepath_or_buffer=self.data_source)
        return df
