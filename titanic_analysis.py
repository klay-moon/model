import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
data = pd.read_csv('titanic.csv')

# Ensure it's a fresh copy of the DataFrame
data = data.copy()

# Fill missing values for 'Age' column
data['Age'] = data['Age'].fillna(data['Age'].median())

# Drop 'Cabin' column if it exists
if 'Cabin' in data.columns:
    data = data.drop(columns=['Cabin'])

# Plot survival by sex
sns.countplot(data=data, x='Survived', hue='Sex')
plt.show()
