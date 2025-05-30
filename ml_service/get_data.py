import pandas as pd


# I will write a query then convert that into a DataFrame when we get a proper DB architecture
def read_data():
    past_data_df = pd.read_csv('ml_service/random_data/contributions.csv')

    return past_data_df


