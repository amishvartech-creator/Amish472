import tkinter as tk
# create a windows using tk
window = tk.Tk()
# create a title of windows 
window.title("My Name is : Amish")
# create a geometry of windows 
window.geometry("550x550")
# create a label of windows app
lable = tk.Label(window, text="Hello, Amish!", font=("Arial", 20),fg="blue")
lable.pack(pady=20)
# print a windows 

tk.mainloop()



