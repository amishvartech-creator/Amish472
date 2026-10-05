# Create a Pandas DataFrame containing employee names, departments, and salaries for at least 10 employees.
import pandas as pd
import matplotlib.pyplot as plt

employee_data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack"
    ],
    "Department": [
        "HR",
        "IT",
        "Finance",
        "Marketing",
        "IT",
        "HR",
        "Finance",
        "Marketing",
        "IT",
        "Finance"
    ],
    "Salary": [
        50000,
        60000,
        55000,
        65000,
        70000,
        52000,
        58000,
        62000,
        68000,
        54000
    ]
}

employee_df = pd.DataFrame(employee_data)
print(employee_df)
print("-------------------------------------------------------------------")
print("Total Salary Expenditure:", employee_df["Salary"].sum())
print("Average Salary of each department:", employee_df.groupby("Department")["Salary"].mean())
print("find employee whose salary is greater than overall average salary:", employee_df[employee_df["Salary"] > employee_df["Salary"].mean()])

plt.title("Display Data in Bar Chart")
plt.bar(employee_df["Name"], employee_df["Salary"])
plt.bar("the average salary of each department", employee_df.groupby("Department")["Salary"].mean())
plt.show()
