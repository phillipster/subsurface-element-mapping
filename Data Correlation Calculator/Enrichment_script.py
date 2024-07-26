import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame

df = pd.read_csv('Cemeteries in NYC - Enriched Cemetery Data.csv')
df = df.replace({'Yes': True, 'No': False})
df_numeric = df.select_dtypes(include=[int, float])

print(df)

# Calculate the correlation matrix
correlation_matrix = df_numeric.corr()

# Display the correlation matrix
print(correlation_matrix)

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
