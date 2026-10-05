# file handling removed any file used a os module
import os
path="data.txt"
if path:
    result=os.remove("data.txt")
    print("file successfully deleted",result)
else:
    print("file does not removed something is wrong")
        
