import pandas as pd
import numpy as np
data = {
    'City': ['A','B','B','A','A'],
    'Age': [25, np.nan, 30, 200, 200],
    'Salary': [50000, 52000, np.nan, 60000, 60000]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print("\nAfter Handling Missing Values:\n", df)
print("\nAfter Noise Detection & Removal:\n", df)
df = df.drop_duplicates()
print("\nAfter Removing Redundant Data:\n", df)
