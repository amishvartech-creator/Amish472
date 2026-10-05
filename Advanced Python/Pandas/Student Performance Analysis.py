import pandas as pd
import matplotlib.pyplot as plt
student_data = {
    "Name": [
        "Aarav",
        "Diya",
        "Ishaan",
        "Kavya",
        "Meera",
        "Rohan",
        "Sana",
        "Vikram",
        "Ananya",
        "Kabir",
    ],
    "Mathematics": [92, 85, 78, 96, 88, 74, 91, 83, 89, 80],
    "Science": [88, 90, 82, 94, 91, 79, 87, 85, 93, 76],
    "English": [85, 92, 86, 89, 95, 81, 90, 78, 88, 84],
}

student_df = pd.DataFrame(student_data)

print(student_df)
print("-----------------------------------------------")
# Calculate average scores for each subject
print("Average Mathematics Score:", student_df["Mathematics"].mean())
print("Average Science Score:", student_df["Science"].mean())
print("Average English Score:", student_df["English"].mean())
print("sum of Mathematics Score:", student_df["Mathematics"].sum())
print("sum of Science Score:", student_df["Science"].sum())
print("sum of English Score:", student_df["English"].sum())
print("highest score in Mathematics:", student_df["Mathematics"].max())
print("highest score in Science:", student_df["Science"].max())
print("highest score in English:", student_df["English"].max())

# plt.title("Display Data in Bar Chart")
# plt.bar(student_df["Name"],student_df["Mathematics"])
# plt.bar(student_df["Name"],student_df["Science"])
# plt.bar(student_df["Name"],student_df["English"])
# plt.show()


plt.title("Display Data in Pie Chart")
plt.pie(student_df["Mathematics"], labels=student_df["Name"], autopct="%1.1f%%")
plt.pie(student_df["Science"], labels=student_df["Name"], autopct="%1.1f%%")
plt.pie(student_df["English"], labels=student_df["Name"], autopct="%1.1f%%")
plt.show()

