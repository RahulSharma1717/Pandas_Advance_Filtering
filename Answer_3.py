# Arrange the above data frame in ascending order.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.sort_values(by='Transaction_ID'))  # Sorted by Transaction_ID as the index was already sorted in ascending order