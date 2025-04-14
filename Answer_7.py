# Make products column as index in the same dataframe and arrange them in descending order.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

df.set_index('products', inplace=True)
df.sort_index(ascending=False, inplace=True)
print(df)


"""Output:
          Transaction_ID  Customer_ID            Name                 Email  \
products                                                                      
iPhone           9709387        57737     Sarah Avila     April33@gmail.com   
iPhone           5092653        45865    Linda Garcia    Charles4@gmail.com   
iPhone           6118132        11415  Kathleen Eaton    Andrew32@gmail.com   
iPhone           4915821        96525  Nicholas Brown  Victoria40@gmail.com   
iPhone           2487756        95336      Dale Drake    Donald72@gmail.com   
...                  ...          ...             ...                   ...   
4K TV            9201039        20485  Kimberly Smith     Tyler24@gmail.com   
4K TV            8085476        47826  Derrick Barber    Steven28@gmail.com   
4K TV            5213974        66019   Gabriel Ramos     Yvonne4@gmail.com   
4K TV            8617170        77884      Lisa Brown      Cody48@gmail.com   
4K TV            8417828        50993     Tracy Munoz    Leslie90@gmail.com   

               Phone                         Address         City  \
products                                                            
iPhone    1242148962                 721 Daniel Lake   Portsmouth   
iPhone    2945019961               0216 Curtis Inlet    Newcastle   
iPhone    7058946000  61338 Fischer Bypass Suite 473     New York   
iPhone    7353268071   96032 Payne Springs Suite 200       Boston   
iPhone    5778370397       7900 Diaz Tunnel Apt. 148  New Orleans   
...              ...                             ...          ...   
4K TV     3501601003    06159 Sarah Street Suite 100       Boston   
4K TV     8650339735                8504 Patty Mount       Boston   
4K TV     5494389129                296 Price Greens         Hull   
4K TV     3426473388     9919 Huynh Rapids Suite 075     Winnipeg   
4K TV     8220404075              54111 Joshua Shore  Quebec City   

                    State  Zipcode    Country  Age  Gender  Income  \
products                                                             
iPhone            England     2804         UK   19    Male  Medium   
iPhone    New South Wales    24376  Australia   20    Male    High   
iPhone            Arizona    86035        USA   22    Male  Medium   
iPhone            Georgia    30783        USA   23  Female    High   
iPhone         Washington    99220        USA   37    Male    High   
...                   ...      ...        ...  ...     ...     ...   
4K TV             Georgia    16713        USA   23  Female    High   
4K TV             Georgia    70191        USA   23  Female    High   
4K TV             England     3672         UK   18    Male     Low   
4K TV             Ontario    73489     Canada   46    Male    High   
4K TV             Ontario    51527     Canada   45  Female    High   

         Customer_Segment        Date  Year      Month      Time  \
products                                                           
iPhone            Regular   6/23/2023  2023       June  14:53:48   
iPhone            Regular   6/26/2023  2023       June  18:56:08   
iPhone            Regular   6/22/2023  2023       June  13:32:18   
iPhone            Regular  10/22/2023  2023    October  10:34:01   
iPhone            Regular   8/21/2023  2023       July  00:45:09   
...                   ...         ...   ...        ...       ...   
4K TV             Regular  11-12-2023  2023   November  19:26:53   
4K TV             Regular  08-06-2023  2023     August  01:28:58   
4K TV                 New  03-10-2023  2023      March  07:37:09   
4K TV                 New  09-10-2023  2023  September  22:33:18   
4K TV                 New  01-11-2024  2024     August  13:15:44   

          Total_Purchases      Amount  Total_Amount Product_Category  \
products                                                               
iPhone                  5  285.091529   1425.457643      Electronics   
iPhone                  6  307.289355   1843.736127      Electronics   
iPhone                  9  460.028723   4140.258506      Electronics   
iPhone                  8  151.542026   1212.336205      Electronics   
iPhone                  9   44.919011    404.271098      Electronics   
...                   ...         ...           ...              ...   
4K TV                   6  436.560198   2619.361190      Electronics   
4K TV                   6  420.197943   2521.187659      Electronics   
4K TV                   2  437.891935    875.783870      Electronics   
4K TV                   9  167.268450   1505.416052      Electronics   
4K TV                   2  191.122564    382.245127      Electronics   

         Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
products                                                                        
iPhone         Samsung   Smartphone    Average        Same-Day           Cash   
iPhone           Apple   Smartphone  Excellent        Same-Day           Cash   
iPhone         Samsung   Smartphone    Average        Same-Day         PayPal   
iPhone            Sony   Smartphone       Good        Standard           Cash   
iPhone            Sony   Smartphone        Bad         Express    Credit Card   
...                ...          ...        ...             ...            ...   
4K TV          Samsung   Television    Average        Standard    Credit Card   
4K TV             Sony   Television  Excellent         Express           Cash   
4K TV             Sony   Television        Bad        Standard     Debit Card   
4K TV             Sony   Television  Excellent        Same-Day         PayPal   
4K TV          Samsung   Television  Excellent        Standard     Debit Card   

         Order_Status  Ratings  
products                        
iPhone     Processing        2  
iPhone      Delivered        5  
iPhone      Delivered        2  
iPhone      Delivered        3  
iPhone      Delivered        1  
...               ...      ...  
4K TV         Shipped        2  
4K TV         Pending        4  
4K TV       Delivered        1  
4K TV      Processing        5  
4K TV         Shipped        5  

[293911 rows x 29 columns]
"""