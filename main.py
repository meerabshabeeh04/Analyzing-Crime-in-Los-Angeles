import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Read the crimes dataset from CSV file, parsing dates and specifying data types
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
# Extract the hour of the crime occurrence by taking the first two digits of the 'TIME OCC' column
# and converting it to an integer for numerical operations.
crimes["HOUR OCC"] = crimes['TIME OCC'].str[:2].astype(int)
# Visualize the count of crimes by hour of occurrence using a count plot.
sns.countplot(data=crimes, x='HOUR OCC')
plt.show()
# Define the peak crime hour for future analysis
peak_crime_hour = 12
# Filter the dataset to include only night hours (10 PM to 3 AM) based on 'TIME OCC'.
# Use string slicing to identify these time ranges.
night_hours = crimes[crimes['TIME OCC'].str[:2].isin(['22', '23', '24', '00', '01', '02', '03'])]
# Find the area with the highest number of crimes during night hours by grouping the data by 'AREA NAME'
# and counting the occurrences, then sorting them in descending order.
peak_night_crime_location = crimes.groupby('AREA NAME')['AREA NAME'].count().sort_values(ascending=False).index[0]
# Create age bins to categorize victims into specific age groups for analysis.
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]  # Define the age ranges
labels = ['0-17', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']  # Labels for the age bins
# Assign each victim's age to a corresponding age bracket using the bins and labels defined.
crimes['Age Bracket'] = pd.cut(crimes['Vict Age'], labels=labels, bins=age_bins)
# Print the assigned age brackets to check the results.
print(crimes['Age Bracket'])
# Count the number of victims in each age bracket and print the result.
victim_ages = crimes['Age Bracket'].value_counts()
print(victim_ages)
# Display the first few rows of the updated DataFrame to inspect the new columns and data.
crimes.head()
