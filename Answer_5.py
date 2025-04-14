# Create a new data frame that has customer id and name as index.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.set_index(['Customer_ID', 'Name']).iloc[:, :4])


"""Output:
                                 Transaction_ID                     Email  \
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

                                      Phone                       Address  
Customer_ID Name                                                           
37249       Michelle Harrington  1414786801             3959 Amanda Burgs  
69749       Kelsey Hill          6852899987            82072 Dawn Centers  
30192       Scott Jensen         8362160449             4133 Young Canyon  
62101       Joseph Miller        2776751724   8148 Thomas Creek Suite 100  
27901       Debra Coleman        9098267635     5813 Lori Ports Suite 269  
...                                     ...                           ...  
12104       Meagan Ellis         7466353743        389 Todd Path Apt. 159  
69772       Mathew Beck          5754304957             52809 Mark Forges  
28449       Daniel Lee           9382530370  407 Aaron Crossing Suite 495  
45477       Patrick Wilson       9373222023               3204 Baird Port  
53626       Dustin Merritt       9518926645           143 Amanda Crescent  

[293911 rows x 4 columns]
"""