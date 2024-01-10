import pandas as pd


class Transforms:

    def __init__(self, dataset, param_0="", param_1="", param_2=""):
        self.dataset = dataset
        self.param_0 = param_0
        self.param_1 = param_1
        self.param_2 = param_2

    def split_columns(self):
        df = self.dataset[self.param_0].str.split(self.param_1, expand=True)
        return df

    def transform_state(self):
        df = pd.merge(self.dataset, self.param_0, on=self.param_1, how='inner')
        return df
