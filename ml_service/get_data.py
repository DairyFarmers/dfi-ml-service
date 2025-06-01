import pandas as pd
from config.database_connection import db_conn

# Getting the supply details of a specific item
def read_data(item_id):

    connection = db_conn()

    read_query = f'''SELECT * FROM "SuppliersContribution" WHERE "ItemId" = {item_id}'''
    past_data_df = pd.read_sql(read_query, connection)


    return past_data_df