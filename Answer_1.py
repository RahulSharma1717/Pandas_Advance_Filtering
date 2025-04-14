# Display the data of the orders that are either shipped or processing only.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[df['Order_Status'].isin(['Shipped', 'Processing']), ['Date', 'Total_Amount', 'Product_Brand', 'Order_Status']])


"""Output:
              Date  Total_Amount  Product_Brand Order_Status
0        9/18/2023    324.086270           Nike      Shipped
1       12/31/2023    806.707815        Samsung   Processing
2        4/26/2023   1063.432799  Penguin Books   Processing
3       05-08-2023   2466.854021     Home Depot   Processing
4       01-10-2024    248.553049         Nestle      Shipped
...            ...           ...            ...          ...
293906   1/20/2024    973.962984  Penguin Books   Processing
293907  12/28/2023    285.137301          Apple   Processing
293908   2/27/2024    182.105285         Adidas      Shipped
293909  09-03-2023    120.834784           IKEA      Shipped
293910  01-08-2024   2382.233417     Home Depot      Shipped

[118930 rows x 4 columns]
"""