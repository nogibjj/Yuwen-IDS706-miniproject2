import pandas as pd

def load_data(datapath):
    return pd.read_csv(datapath)

def get_data_descriptive_stats(dataframe):
    statistics = {
        'Mean': dataframe.mean(),
        'Median': dataframe.median(),
        'StdDev': dataframe.std(),
        'Min': dataframe.min(),
        'Max': dataframe.max()
    }
    return pd.Series(statistics)