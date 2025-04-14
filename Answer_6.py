# Reset the index of the above data frame and remove the older index.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.set_index(['Customer_ID', 'Name']).iloc[:, :2])
print("------------------------------------------------------------------------------------")
new_df = df.reset_index(drop=True).iloc[:, :4]
print(new_df)


"""Output:
                                 Transaction_ID                     Email
Customer_ID Name                                                         
37249       Michelle Harrington         8691788         Ebony39@gmail.com
69749       Kelsey Hill                 2174773          Mark36@gmail.com
30192       Scott Jensen                6679610         Shane85@gmail.com
62101       Joseph Miller               7232460          Mary34@gmail.com
27901       Debra Coleman               4983775       Charles30@gmail.com
...                                         ...                       ...
12104       Meagan Ellis                4246475      Courtney60@gmail.com
69772       Mathew Beck                 1197603      Jennifer71@gmail.com
28449       Daniel Lee                  7743242  Christopher100@gmail.com
45477       Patrick Wilson              9301950       Rebecca65@gmail.com
53626       Dustin Merritt              2882826       William14@gmail.com

[293911 rows x 2 columns]
------------------------------------------------------------------------------------
        Transaction_ID  Customer_ID                 Name  \
0              8691788        37249  Michelle Harrington   
1              2174773        69749          Kelsey Hill   
2              6679610        30192         Scott Jensen   
3              7232460        62101        Joseph Miller   
4              4983775        27901        Debra Coleman   
...                ...          ...                  ...   
293906         4246475        12104         Meagan Ellis   
293907         1197603        69772          Mathew Beck   
293908         7743242        28449           Daniel Lee   
293909         9301950        45477       Patrick Wilson   
293910         2882826        53626       Dustin Merritt   

                           Email  
0              Ebony39@gmail.com  
1               Mark36@gmail.com  
2              Shane85@gmail.com  
3               Mary34@gmail.com  
4            Charles30@gmail.com  
...                          ...  
293906      Courtney60@gmail.com  
293907      Jennifer71@gmail.com  
293908  Christopher100@gmail.com  
293909       Rebecca65@gmail.com  
293910       William14@gmail.com  

[293911 rows x 4 columns]
"""



