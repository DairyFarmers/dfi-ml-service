import csv
import random
from datetime import datetime, timedelta
import pandas as pd

from config.database_connection import db_conn


def generate_random_sample_data():

    table_name ="SuppliersContribution"
    # Connect to the database
    connection = db_conn()
    # Generate 10 unique names
    names = [f'Person{i + 1}@gmail.com' for i in range(10)]

    # Create data rows
    data = []
    for _ in range(1000):

        name = random.choice(names)

        # Random ItemId
        item_id = random.randint(1, 10)

        # Random date within a month (January 2023)
        day = random.randint(1, 30)

        try:
            created_date = datetime(2025, 4, day).strftime('%Y-%m-%d')
        except ValueError:
            created_date = datetime(2025, 4, 30).strftime('%Y-%m-%d')

        contribution = random.randint(0, 100)

        data.append([name, created_date, item_id,contribution])

    df = pd.DataFrame(data, columns=['SupplierMailId', 'CreatedDate', 'ItemId','Contribution'])

    try:
        # Insert data into the database
        df.to_sql(table_name,con=connection, if_exists='replace', index=False)

    except Exception as e:
        print(f"Error inserting data into the database: {e}")
