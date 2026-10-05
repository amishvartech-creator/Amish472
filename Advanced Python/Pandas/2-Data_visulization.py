'''
bash
pip install matplotlib
or
pip show matplotlib

python
import matplotlib.pyplot as plt

'''

import pandas as pd
import matplotlib.pyplot as plt
employee={
    "name":["om","nimavat","aryan","brijesh","amish","mishri"],
    "age":[21,25,19,35,30,20],
    "salary":[21000,30000,18500,115000,45000,14500]
}

# Bar Chart
# plt.title("Display Data in Bar Chart")
# plt.bar(employee["name"],employee["salary"])
# # print chart
# plt.show()

# Pie Chart
# plt.title("Display Data in Pie Chart")
# plt.pie(employee["salary"],labels=employee["name"], autopct="%1.1f%%")
# # print chart
# plt.show()

# generate excel
employee["name","salary"].to_excel("employee.xlsx",index=False)
print("Excel Generated Successfully")
