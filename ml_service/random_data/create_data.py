import csv
import random
from datetime import datetime, timedelta

# Generate 10 unique names
names = [f'Person{i + 1}' for i in range(10)]

# Create data rows
data = []
for _ in range(1000):
    name = random.choice(names)

    # Random date within a month (January 2023)
    day = random.randint(1, 31)
    try:
        created_date = datetime(2023, 1, day).strftime('%Y-%m-%d')
    except ValueError:
        created_date = datetime(2023, 1, 31).strftime('%Y-%m-%d')

    contribution = random.randint(0, 100)

    data.append([name, created_date, contribution])

# Write to CSV
with open('contributions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'CreatedDate', 'Contribution'])
    writer.writerows(data)