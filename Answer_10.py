# Reset the index of the above data frame in the same variable.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

new_df = df.set_index('Zipcode').sort_index(ascending=True)

new_df.reset_index(inplace=True)
print(new_df)


"""Output:
        Zipcode  Transaction_ID  Customer_ID             Name  \
0           501         6045120        77711  Mr. David Brown   
1           501         2081428        10619      David Burns   
2           502         3525546        33693    Jacob Jackson   
3           503         3765171        46329   Stephanie Dunn   
4           504         7925436        99421     David Dillon   
...         ...             ...          ...              ...   
293906    99948         5684703        34129     Amanda Allen   
293907    99948         6509404        51257    Kevin Sanchez   
293908    99949         7100236        15232      Nancy Welch   
293909    99949         3841207        27689    Jeremiah Ryan   
293910    99949         3652401        90991     Rachel Ramos   

                          Email       Phone  \
0           Kenneth49@gmail.com  2841244874   
1          Jermaine60@gmail.com  1737652428   
2               Amy33@gmail.com  4406902408   
3              Luis64@gmail.com  1265109283   
4           Brianna57@gmail.com  4603742358   
...                         ...         ...   
293906       Ashley23@gmail.com  8450397909   
293907     Jennifer96@gmail.com  1998163286   
293908  Christopher35@gmail.com  2815554860   
293909      Matthew39@gmail.com  8669015748   
293910       Nicole26@gmail.com  6084399608   

                                  Address           City            State  \
0              5506 Smith Forks Suite 869  San Francisco            Maine   
1              583 Keith Highway Apt. 605     Birmingham          England   
2                        391 Foley Cliffs          Essen           Berlin   
3                        458 Jackson Loaf         Darwin  New South Wales   
4         55852 Erickson Prairie Apt. 535     Düsseldorf           Berlin   
...                                   ...            ...              ...   
293906       8238 Lucas Mission Suite 679        Chicago      Connecticut   
293907  914 Nicholas Trafficway Suite 073   Jacksonville           Alaska   
293908          7703 Gina Shore Suite 732           Mesa           Alaska   
293909       2822 Richard Street Apt. 374         Boston          Georgia   
293910                886 Matthew Highway  Oklahoma City           Alaska   

          Country  Age  Gender  Income Customer_Segment        Date  Year  \
0             USA   26    Male    High          Regular  12/30/2023  2023   
1              UK   53  Female    High          Regular  05-02-2023  2023   
2         Germany   26    Male     Low              New  11/23/2023  2023   
3       Australia   58    Male  Medium          Regular  05-07-2023  2023   
4         Germany   22    Male     Low          Regular   8/13/2023  2023   
...           ...  ...     ...     ...              ...         ...   ...   
293906        USA   34    Male  Medium          Regular  06-09-2023  2023   
293907        USA   68  Female     Low          Regular   3/21/2023  2023   
293908        USA   44  Female     Low          Regular  10-08-2023  2023   
293909        USA   23    Male    High          Regular   1/29/2024  2024   
293910        USA   41    Male    High          Premium   7/25/2023  2023   

           Month      Time  Total_Purchases      Amount  Total_Amount  \
0        January  14:15:49                7  277.412781   1941.889465   
1            May  13:10:32                9  381.233102   3431.097922   
2       November  16:08:42                1  312.909118    312.909118   
3           July  11:45:21                4  250.558371   1002.233484   
4         August  14:23:41                2   10.430495     20.860990   
...          ...       ...              ...         ...           ...   
293906      June  06:39:34                8  245.038144   1960.305154   
293907     March  17:55:27                2  358.700091    717.400181   
293908   October  08:31:01               10  388.574789   3885.747891   
293909   January  23:42:29                4  281.617435   1126.469740   
293910      July  15:48:27                6   15.841500     95.049001   

       Product_Category  Product_Brand Product_Type   Feedback  \
0            Home Decor           IKEA  Decorations        Bad   
1              Clothing         Adidas        Shoes       Good   
2           Electronics          Apple       Tablet       Good   
3                 Books  Penguin Books      Fiction        Bad   
4            Home Decor           IKEA  Decorations       Good   
...                 ...            ...          ...        ...   
293906          Grocery          Pepsi        Water       Good   
293907            Books  Penguin Books   Children's        Bad   
293908       Home Decor     Home Depot        Tools       Good   
293909            Books  HarperCollins     Thriller  Excellent   
293910          Grocery      Coca-Cola        Water    Average   

       Shipping_Method Payment_Method Order_Status  Ratings         products  
0             Same-Day    Credit Card    Delivered        1         Curtains  
1             Same-Day    Credit Card   Processing        3       High heels  
2             Same-Day    Credit Card    Delivered        4  Acer Iconia Tab  
3              Express     Debit Card      Shipped        1         Thriller  
4              Express           Cash    Delivered        3         Curtains  
...                ...            ...          ...      ...              ...  
293906        Same-Day         PayPal      Shipped        3   Alkaline water  
293907         Express           Cash   Processing        1         Clothing  
293908        Standard    Credit Card   Processing        3  Screwdriver set  
293909        Standard    Credit Card   Processing        5        Detective  
293910         Express           Cash      Pending        2   Artesian water  

[293911 rows x 30 columns]
"""