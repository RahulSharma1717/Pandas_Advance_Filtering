# Change the index of the data frame to city, state, country in the same variable.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

df.set_index(['City', 'State', 'Country'], inplace=True)
print(df)


"""Output:
                                      Transaction_ID  Customer_ID  \
City       State           Country                                  
Dortmund   Berlin          Germany           8691788        37249   
Nottingham England         UK                2174773        69749   
Geelong    New South Wales Australia         6679610        30192   
Edmonton   Ontario         Canada            7232460        62101   
Bristol    England         UK                4983775        27901   
...                                              ...          ...   
Townsville New South Wales Australia         4246475        12104   
Hanover    Berlin          Germany           1197603        69772   
Brighton   England         UK                7743242        28449   
Halifax    Ontario         Canada            9301950        45477   
Tucson     West Virginia   USA               2882826        53626   

                                                     Name  \
City       State           Country                          
Dortmund   Berlin          Germany    Michelle Harrington   
Nottingham England         UK                 Kelsey Hill   
Geelong    New South Wales Australia         Scott Jensen   
Edmonton   Ontario         Canada           Joseph Miller   
Bristol    England         UK               Debra Coleman   
...                                                   ...   
Townsville New South Wales Australia         Meagan Ellis   
Hanover    Berlin          Germany            Mathew Beck   
Brighton   England         UK                  Daniel Lee   
Halifax    Ontario         Canada          Patrick Wilson   
Tucson     West Virginia   USA             Dustin Merritt   

                                                         Email       Phone  \
City       State           Country                                           
Dortmund   Berlin          Germany           Ebony39@gmail.com  1414786801   
Nottingham England         UK                 Mark36@gmail.com  6852899987   
Geelong    New South Wales Australia         Shane85@gmail.com  8362160449   
Edmonton   Ontario         Canada             Mary34@gmail.com  2776751724   
Bristol    England         UK              Charles30@gmail.com  9098267635   
...                                                        ...         ...   
Townsville New South Wales Australia      Courtney60@gmail.com  7466353743   
Hanover    Berlin          Germany        Jennifer71@gmail.com  5754304957   
Brighton   England         UK         Christopher100@gmail.com  9382530370   
Halifax    Ontario         Canada          Rebecca65@gmail.com  9373222023   
Tucson     West Virginia   USA             William14@gmail.com  9518926645   

                                                           Address  Zipcode  \
City       State           Country                                            
Dortmund   Berlin          Germany               3959 Amanda Burgs    77985   
Nottingham England         UK                   82072 Dawn Centers    99071   
Geelong    New South Wales Australia             4133 Young Canyon    75929   
Edmonton   Ontario         Canada      8148 Thomas Creek Suite 100    88420   
Bristol    England         UK            5813 Lori Ports Suite 269    48704   
...                                                            ...      ...   
Townsville New South Wales Australia        389 Todd Path Apt. 159     4567   
Hanover    Berlin          Germany               52809 Mark Forges    16852   
Brighton   England         UK         407 Aaron Crossing Suite 495    88038   
Halifax    Ontario         Canada                  3204 Baird Port    67608   
Tucson     West Virginia   USA                 143 Amanda Crescent    25242   

                                      Age  Gender  Income Customer_Segment  \
City       State           Country                                           
Dortmund   Berlin          Germany     21    Male     Low          Regular   
Nottingham England         UK          19  Female     Low          Premium   
Geelong    New South Wales Australia   48    Male     Low          Regular   
Edmonton   Ontario         Canada      56    Male    High          Premium   
Bristol    England         UK          22    Male     Low          Premium   
...                                   ...     ...     ...              ...   
Townsville New South Wales Australia   31    Male  Medium          Regular   
Hanover    Berlin          Germany     35  Female     Low              New   
Brighton   England         UK          41    Male     Low          Premium   
Halifax    Ontario         Canada      41    Male  Medium              New   
Tucson     West Virginia   USA         28  Female     Low          Premium   

                                            Date  Year      Month      Time  \
City       State           Country                                            
Dortmund   Berlin          Germany     9/18/2023  2023  September  22:03:55   
Nottingham England         UK         12/31/2023  2023   December  08:42:04   
Geelong    New South Wales Australia   4/26/2023  2023      April  04:06:29   
Edmonton   Ontario         Canada     05-08-2023  2023        May  14:55:17   
Bristol    England         UK         01-10-2024  2024    January  16:54:07   
...                                          ...   ...        ...       ...   
Townsville New South Wales Australia   1/20/2024  2024    January  23:40:29   
Hanover    Berlin          Germany    12/28/2023  2023   December  02:55:45   
Brighton   England         UK          2/27/2024  2024   February  02:43:49   
Halifax    Ontario         Canada     09-03-2023  2023  September  11:20:31   
Tucson     West Virginia   USA        01-08-2024  2024    January  11:44:36   

                                      Total_Purchases      Amount  \
City       State           Country                                  
Dortmund   Berlin          Germany                  3  108.028757   
Nottingham England         UK                       2  403.353907   
Geelong    New South Wales Australia                3  354.477600   
Edmonton   Ontario         Canada                   7  352.407717   
Bristol    England         UK                       2  124.276524   
...                                               ...         ...   
Townsville New South Wales Australia                5  194.792597   
Hanover    Berlin          Germany                  1  285.137301   
Brighton   England         UK                       3   60.701761   
Halifax    Ontario         Canada                   1  120.834784   
Tucson     West Virginia   USA                      7  340.319059   

                                      Total_Amount Product_Category  \
City       State           Country                                    
Dortmund   Berlin          Germany      324.086270         Clothing   
Nottingham England         UK           806.707815      Electronics   
Geelong    New South Wales Australia   1063.432799            Books   
Edmonton   Ontario         Canada      2466.854021       Home Decor   
Bristol    England         UK           248.553049          Grocery   
...                                            ...              ...   
Townsville New South Wales Australia    973.962984            Books   
Hanover    Berlin          Germany      285.137301      Electronics   
Brighton   England         UK           182.105285         Clothing   
Halifax    Ontario         Canada       120.834784       Home Decor   
Tucson     West Virginia   USA         2382.233417       Home Decor   

                                      Product_Brand Product_Type   Feedback  \
City       State           Country                                            
Dortmund   Berlin          Germany             Nike       Shorts  Excellent   
Nottingham England         UK               Samsung       Tablet  Excellent   
Geelong    New South Wales Australia  Penguin Books   Children's    Average   
Edmonton   Ontario         Canada        Home Depot        Tools  Excellent   
Bristol    England         UK                Nestle    Chocolate        Bad   
...                                             ...          ...        ...   
Townsville New South Wales Australia  Penguin Books      Fiction        Bad   
Hanover    Berlin          Germany            Apple       Laptop  Excellent   
Brighton   England         UK                Adidas       Jacket    Average   
Halifax    Ontario         Canada              IKEA    Furniture       Good   
Tucson     West Virginia   USA           Home Depot  Decorations    Average   

                                     Shipping_Method Payment_Method  \
City       State           Country                                    
Dortmund   Berlin          Germany          Same-Day     Debit Card   
Nottingham England         UK               Standard    Credit Card   
Geelong    New South Wales Australia        Same-Day    Credit Card   
Edmonton   Ontario         Canada           Standard         PayPal   
Bristol    England         UK               Standard           Cash   
...                                              ...            ...   
Townsville New South Wales Australia        Same-Day           Cash   
Hanover    Berlin          Germany          Same-Day           Cash   
Brighton   England         UK                Express           Cash   
Halifax    Ontario         Canada           Standard           Cash   
Tucson     West Virginia   USA              Same-Day           Cash   

                                     Order_Status  Ratings            products  
City       State           Country                                              
Dortmund   Berlin          Germany        Shipped        5      Cycling shorts  
Nottingham England         UK          Processing        4          Lenovo Tab  
Geelong    New South Wales Australia   Processing        2    Sports equipment  
Edmonton   Ontario         Canada      Processing        4       Utility knife  
Bristol    England         UK             Shipped        1   Chocolate cookies  
...                                           ...      ...                 ...  
Townsville New South Wales Australia   Processing        1  Historical fiction  
Hanover    Berlin          Germany     Processing        5             LG Gram  
Brighton   England         UK             Shipped        2               Parka  
Halifax    Ontario         Canada         Shipped        4            TV stand  
Tucson     West Virginia   USA            Shipped        2              Clocks  

[293911 rows x 27 columns]
"""

