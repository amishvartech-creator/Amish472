# file handling removed any file used a os module
import os
path="employee_data.xlsx"
if path:
    result=os.remove("employee_data.xlsx")
    print("file successfully deleted",result)
else:
    print("file does not removed somethin is wrong")
        