import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def check_company_contribution(df):
    df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])

    # Group by date and sum all contributions
    daily_totals = df.groupby(df['CreatedDate'].dt.date).agg(
        total_contribution=('Contribution', 'sum')
    ).reset_index().rename(columns={'CreatedDate': 'date'})

    # Feature engineering
    daily_totals['day_of_week'] = pd.to_datetime(daily_totals['date']).dt.dayofweek  # Monday=0
    daily_totals['month'] = pd.to_datetime(daily_totals['date']).dt.month

    # Prepare model
    X = daily_totals[['day_of_week', 'month']]
    y = daily_totals['total_contribution']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Let's predict max possible future day (e.g., most active day)
    sample_input = pd.DataFrame({
        'day_of_week': [daily_totals['day_of_week'].mode()[0]],
        'month': [daily_totals['month'].mode()[0]],
    })

    predicted_total = model.predict(sample_input)[0]
    historical_max = y.max()

    logging.info(f"Predicted Total: {predicted_total}, Historical Max: {historical_max}")

    return predicted_total, historical_max
