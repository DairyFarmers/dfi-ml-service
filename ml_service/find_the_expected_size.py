import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def predict_the_contribution(df,total_expected):

    logging.info('Finding the prediction for the suppliers')

    df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])
    # df = df[df['ItemId'] == item_id] # Filtering the df only for specific item
    # Aggregate per person
    today = datetime.today()
    agg_df = df.groupby('SupplierMailId').agg(
        total_contribution=('Contribution', 'sum'),
        avg_contribution=('Contribution', 'mean'),
        max_contribution=('Contribution', 'max'),
        count=('Contribution', 'count'),
        last_contribution_date=('CreatedDate', 'max')
    ).reset_index()

    # Days since last contribution
    agg_df['days_since_last'] = (today - agg_df['last_contribution_date']).dt.days

    # We'll treat total_contribution as the label to learn contribution patterns
    X = agg_df[['avg_contribution', 'max_contribution', 'count', 'days_since_last']]
    y = agg_df['total_contribution']

    # Train a regression model
    model = RandomForestRegressor()
    model.fit(X, y)


    # Predict expected future contribution behavior (raw)
    agg_df['raw_prediction'] = model.predict(X)

    agg_df = scale_predictions(agg_df, total_expected)
    final_predictions = agg_df[['SupplierMailId', 'scaled_prediction']].sort_values(by='scaled_prediction', ascending=False)
    # Final Output
    return final_predictions


# Function: scale predictions to match total expected amount
def scale_predictions(df, total_expected):
    df['scaled_prediction'] = df['raw_prediction'] / df['raw_prediction'].sum() * total_expected
    return df
