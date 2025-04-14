# Display the data of ratings greater than 3 and excellent feedback.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['Ratings'] > 3) & (df['Feedback'] == 'Excellent')].iloc[:, -8:])


"""Output:
       Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
0               Nike       Shorts  Excellent        Same-Day     Debit Card   
1            Samsung       Tablet  Excellent        Standard    Credit Card   
3         Home Depot        Tools  Excellent        Standard         PayPal   
9         Home Depot  Decorations  Excellent        Standard           Cash   
13            Nestle       Snacks  Excellent         Express         PayPal   
...              ...          ...        ...             ...            ...   
293897        Adidas      T-shirt  Excellent        Standard           Cash   
293900       Samsung       Tablet  Excellent        Same-Day           Cash   
293903    Home Depot        Tools  Excellent         Express           Cash   
293905          Nike       Shorts  Excellent        Standard           Cash   
293907         Apple       Laptop  Excellent        Same-Day           Cash   

       Order_Status  Ratings        products  
0           Shipped        5  Cycling shorts  
1        Processing        4      Lenovo Tab  
3        Processing        4   Utility knife  
9         Delivered        4         Candles  
13        Delivered        4    Fruit snacks  
...             ...      ...             ...  
293897   Processing        4  Scoop neck tee  
293900      Shipped        5            iPad  
293903      Pending        5           Level  
293905    Delivered        4    Chino shorts  
293907   Processing        5         LG Gram  

[98016 rows x 8 columns]
"""