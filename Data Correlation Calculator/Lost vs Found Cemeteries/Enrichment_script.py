import pandas as pd
import scipy.stats as stats

# # Create a DataFrame
#
existent_df = pd.read_csv('Existing Cemeteries.csv')
lost_df = pd.read_csv('Lost Cemeteries.csv')

# print(df)
#
# # Calculate the correlation matrix
# correlation_matrix = df_numeric.corr()
#
# # Display the correlation matrix
# print(correlation_matrix)
#
# # Create a heatmap
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Matrix')
# plt.show()

# Sample data
column_variables = ["Population Density",
                    "Total Population",
                    "Median Age",
                    "% Seniors",
                    "% w/ Children",
                    "Median Home Value",
                    "Per Capita Income",
                    "% White",
                    "% Black",
                    "% Amerindian",
                    "% Asian",
                    "% Pacific Islander",
                    "% Other Race",
                    "% 2+ Races",
                    "Diversity Index",
                    "Total Housing Units",
                    "% w/ Disability",
                    "% Below Poverty",
                    "Median Household Income"
                    ]
existing_as_lists = []
lost_as_lists = []
for var in column_variables:
    existing_as_lists.append(existent_df[var].tolist())
    lost_as_lists.append(lost_df[var].tolist())

# Mann-Whitney U Test
lines_of_output = []

for i in range(len(existing_as_lists)):
    u_stat, p_value = stats.mannwhitneyu(existing_as_lists[i], lost_as_lists[i], alternative='two-sided')
    lines_of_output.append((column_variables[i], float(u_stat), float(p_value)))

final_csv = open('results.csv', 'w')
final_csv.write('Variable,U-Statistic,P-Value\n')

for var in lines_of_output:
    final_csv.write(f'{var[0]},{var[1]},{var[2]}'+'\n')

final_csv.close()
