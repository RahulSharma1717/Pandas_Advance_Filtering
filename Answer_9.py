# Make zipcode as a new index, sort it in ascending order and store it in a new variable.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

new_df = df.set_index('Zipcode').sort_index(ascending=True)
print(new_df)


"""Output:
         Transaction_ID  Customer_ID             Name  \
Zipcode                                                 
501             6045120        77711  Mr. David Brown   
501             2081428        10619      David Burns   
502             3525546        33693    Jacob Jackson   
503             3765171        46329   Stephanie Dunn   
504             7925436        99421     David Dillon   
...                 ...          ...              ...   
99948           5684703        34129     Amanda Allen   
99948           6509404        51257    Kevin Sanchez   
99949           7100236        15232      Nancy Welch   
99949           3841207        27689    Jeremiah Ryan   
99949           3652401        90991     Rachel Ramos   

                           Email       Phone  \
Zipcode                                        
501          Kenneth49@gmail.com  2841244874   
501         Jermaine60@gmail.com  1737652428   
502              Amy33@gmail.com  4406902408   
503             Luis64@gmail.com  1265109283   
504          Brianna57@gmail.com  4603742358   
...                          ...         ...   
99948         Ashley23@gmail.com  8450397909   
99948       Jennifer96@gmail.com  1998163286   
99949    Christopher35@gmail.com  2815554860   
99949        Matthew39@gmail.com  8669015748   
99949         Nicole26@gmail.com  6084399608   

                                   Address           City            State  \
Zipcode                                                                      
501             5506 Smith Forks Suite 869  San Francisco            Maine   
501             583 Keith Highway Apt. 605     Birmingham          England   
502                       391 Foley Cliffs          Essen           Berlin   
503                       458 Jackson Loaf         Darwin  New South Wales   
504        55852 Erickson Prairie Apt. 535     Düsseldorf           Berlin   
...                                    ...            ...              ...   
99948         8238 Lucas Mission Suite 679        Chicago      Connecticut   
99948    914 Nicholas Trafficway Suite 073   Jacksonville           Alaska   
99949            7703 Gina Shore Suite 732           Mesa           Alaska   
99949         2822 Richard Street Apt. 374         Boston          Georgia   
99949                  886 Matthew Highway  Oklahoma City           Alaska   

           Country  Age  Gender  Income Customer_Segment        Date  Year  \
Zipcode                                                                      
501            USA   26    Male    High          Regular  12/30/2023  2023   
501             UK   53  Female    High          Regular  05-02-2023  2023   
502        Germany   26    Male     Low              New  11/23/2023  2023   
503      Australia   58    Male  Medium          Regular  05-07-2023  2023   
504        Germany   22    Male     Low          Regular   8/13/2023  2023   
...            ...  ...     ...     ...              ...         ...   ...   
99948          USA   34    Male  Medium          Regular  06-09-2023  2023   
99948          USA   68  Female     Low          Regular   3/21/2023  2023   
99949          USA   44  Female     Low          Regular  10-08-2023  2023   
99949          USA   23    Male    High          Regular   1/29/2024  2024   
99949          USA   41    Male    High          Premium   7/25/2023  2023   

            Month      Time  Total_Purchases      Amount  Total_Amount  \
Zipcode                                                                  
501       January  14:15:49                7  277.412781   1941.889465   
501           May  13:10:32                9  381.233102   3431.097922   
502      November  16:08:42                1  312.909118    312.909118   
503          July  11:45:21                4  250.558371   1002.233484   
504        August  14:23:41                2   10.430495     20.860990   
...           ...       ...              ...         ...           ...   
99948        June  06:39:34                8  245.038144   1960.305154   
99948       March  17:55:27                2  358.700091    717.400181   
99949     October  08:31:01               10  388.574789   3885.747891   
99949     January  23:42:29                4  281.617435   1126.469740   
99949        July  15:48:27                6   15.841500     95.049001   

        Product_Category  Product_Brand Product_Type   Feedback  \
Zipcode                                                           
501           Home Decor           IKEA  Decorations        Bad   
501             Clothing         Adidas        Shoes       Good   
502          Electronics          Apple       Tablet       Good   
503                Books  Penguin Books      Fiction        Bad   
504           Home Decor           IKEA  Decorations       Good   
...                  ...            ...          ...        ...   
99948            Grocery          Pepsi        Water       Good   
99948              Books  Penguin Books   Children's        Bad   
99949         Home Decor     Home Depot        Tools       Good   
99949              Books  HarperCollins     Thriller  Excellent   
99949            Grocery      Coca-Cola        Water    Average   

        Shipping_Method Payment_Method Order_Status  Ratings         products  
Zipcode                                                                        
501            Same-Day    Credit Card    Delivered        1         Curtains  
501            Same-Day    Credit Card   Processing        3       High heels  
502            Same-Day    Credit Card    Delivered        4  Acer Iconia Tab  
503             Express     Debit Card      Shipped        1         Thriller  
504             Express           Cash    Delivered        3         Curtains  
...                 ...            ...          ...      ...              ...  
99948          Same-Day         PayPal      Shipped        3   Alkaline water  
99948           Express           Cash   Processing        1         Clothing  
99949          Standard    Credit Card   Processing        3  Screwdriver set  
99949          Standard    Credit Card   Processing        5        Detective  
99949           Express           Cash      Pending        2   Artesian water  

[293911 rows x 29 columns]
"""
