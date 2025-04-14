# Create a new data frame where customer_id works as an index.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
new_df = df.set_index('Customer_ID')
print(new_df)


"""Output:
             Transaction_ID                 Name                     Email  \
Customer_ID                                                                  
37249               8691788  Michelle Harrington         Ebony39@gmail.com   
69749               2174773          Kelsey Hill          Mark36@gmail.com   
30192               6679610         Scott Jensen         Shane85@gmail.com   
62101               7232460        Joseph Miller          Mary34@gmail.com   
27901               4983775        Debra Coleman       Charles30@gmail.com   
...                     ...                  ...                       ...   
12104               4246475         Meagan Ellis      Courtney60@gmail.com   
69772               1197603          Mathew Beck      Jennifer71@gmail.com   
28449               7743242           Daniel Lee  Christopher100@gmail.com   
45477               9301950       Patrick Wilson       Rebecca65@gmail.com   
53626               2882826       Dustin Merritt       William14@gmail.com   

                  Phone                       Address        City  \
Customer_ID                                                         
37249        1414786801             3959 Amanda Burgs    Dortmund   
69749        6852899987            82072 Dawn Centers  Nottingham   
30192        8362160449             4133 Young Canyon     Geelong   
62101        2776751724   8148 Thomas Creek Suite 100    Edmonton   
27901        9098267635     5813 Lori Ports Suite 269     Bristol   
...                 ...                           ...         ...   
12104        7466353743        389 Todd Path Apt. 159  Townsville   
69772        5754304957             52809 Mark Forges     Hanover   
28449        9382530370  407 Aaron Crossing Suite 495    Brighton   
45477        9373222023               3204 Baird Port     Halifax   
53626        9518926645           143 Amanda Crescent      Tucson   

                       State  Zipcode    Country  Age  Gender  Income  \
Customer_ID                                                             
37249                 Berlin    77985    Germany   21    Male     Low   
69749                England    99071         UK   19  Female     Low   
30192        New South Wales    75929  Australia   48    Male     Low   
62101                Ontario    88420     Canada   56    Male    High   
27901                England    48704         UK   22    Male     Low   
...                      ...      ...        ...  ...     ...     ...   
12104        New South Wales     4567  Australia   31    Male  Medium   
69772                 Berlin    16852    Germany   35  Female     Low   
28449                England    88038         UK   41    Male     Low   
45477                Ontario    67608     Canada   41    Male  Medium   
53626          West Virginia    25242        USA   28  Female     Low   

            Customer_Segment        Date  Year      Month      Time  \
Customer_ID                                                           
37249                Regular   9/18/2023  2023  September  22:03:55   
69749                Premium  12/31/2023  2023   December  08:42:04   
30192                Regular   4/26/2023  2023      April  04:06:29   
62101                Premium  05-08-2023  2023        May  14:55:17   
27901                Premium  01-10-2024  2024    January  16:54:07   
...                      ...         ...   ...        ...       ...   
12104                Regular   1/20/2024  2024    January  23:40:29   
69772                    New  12/28/2023  2023   December  02:55:45   
28449                Premium   2/27/2024  2024   February  02:43:49   
45477                    New  09-03-2023  2023  September  11:20:31   
53626                Premium  01-08-2024  2024    January  11:44:36   

             Total_Purchases      Amount  Total_Amount Product_Category  \
Customer_ID                                                               
37249                      3  108.028757    324.086270         Clothing   
69749                      2  403.353907    806.707815      Electronics   
30192                      3  354.477600   1063.432799            Books   
62101                      7  352.407717   2466.854021       Home Decor   
27901                      2  124.276524    248.553049          Grocery   
...                      ...         ...           ...              ...   
12104                      5  194.792597    973.962984            Books   
69772                      1  285.137301    285.137301      Electronics   
28449                      3   60.701761    182.105285         Clothing   
45477                      1  120.834784    120.834784       Home Decor   
53626                      7  340.319059   2382.233417       Home Decor   

             Product_Brand Product_Type   Feedback Shipping_Method  \
Customer_ID                                                          
37249                 Nike       Shorts  Excellent        Same-Day   
69749              Samsung       Tablet  Excellent        Standard   
30192        Penguin Books   Children's    Average        Same-Day   
62101           Home Depot        Tools  Excellent        Standard   
27901               Nestle    Chocolate        Bad        Standard   
...                    ...          ...        ...             ...   
12104        Penguin Books      Fiction        Bad        Same-Day   
69772                Apple       Laptop  Excellent        Same-Day   
28449               Adidas       Jacket    Average         Express   
45477                 IKEA    Furniture       Good        Standard   
53626           Home Depot  Decorations    Average        Same-Day   

            Payment_Method Order_Status  Ratings            products  
Customer_ID                                                           
37249           Debit Card      Shipped        5      Cycling shorts  
69749          Credit Card   Processing        4          Lenovo Tab  
30192          Credit Card   Processing        2    Sports equipment  
62101               PayPal   Processing        4       Utility knife  
27901                 Cash      Shipped        1   Chocolate cookies  
...                    ...          ...      ...                 ...  
12104                 Cash   Processing        1  Historical fiction  
69772                 Cash   Processing        5             LG Gram  
28449                 Cash      Shipped        2               Parka  
45477                 Cash      Shipped        4            TV stand  
53626                 Cash      Shipped        2              Clocks  

[293911 rows x 29 columns]
"""