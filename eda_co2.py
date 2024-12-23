import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
data = pd.read_csv('co2-data.csv')

#Overview of Data
print(data.head())
print(data.info())
print(data.describe())

#Missing Values
print(data.isnull().sum())

# Univariate Analysis
sns.histplot(data['co2'], kde=True)
plt.title('Distribution of CO2 Emissions')
plt.show()

# Correlation Heatmap
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Group Analysis
country_emissions = data.groupby('country')['co2_emissions'].sum().sort_values(ascending=False)
country_emissions.head(10).plot(kind='bar', figsize=(10, 6))
plt.title('Top 10 CO2 Emitting Countries')
plt.show()