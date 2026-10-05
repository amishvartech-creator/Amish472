'''
bash
pip install pandas
or
pip show pandas 

python
import pandas as pd

'''

import pandas as pd
Employee={
   "Name":["Amish","Priya","Dhairya","Om","Heer","Anu"],
   "Age":[47,43,14,13,13,39],
   "Salary":[27600,46500,35000,10000,13000,23000]
}


# create a data frames 
df=pd.DataFrame(Employee)
print(df)
print("----------------------")
print("sum of salary :",df["Salary"].sum())
