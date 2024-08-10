import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
column_variables = ['Latitude', 'Longitude', 'Lifespan']
data = {}
df = pd.read_csv('Cemeteries in NYC - Enriched Cemetery Data.csv')
for var in column_variables:
    data[var] = df[var].tolist()


# Plotting
plt.figure(figsize=(10, 6))
sc = plt.scatter(df['Longitude'], df['Latitude'], c=df['Lifespan'], cmap='viridis', s=100)
plt.colorbar(sc, label='Duration')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Location Plot with Duration as Color Indicator')
plt.show()
