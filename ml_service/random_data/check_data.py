import pandas as pd

df = pd.read_csv('contributions.csv')

filtered_df = df[df['Name'] == 'Person5']
filtered_df = filtered_df[filtered_df['CreatedDate'] == '2023-01-03']
if not filtered_df.empty:
    print(filtered_df['Contribution'].sum())