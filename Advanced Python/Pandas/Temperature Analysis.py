# Create a Pandas DataFrame containing the daily temperatures recorded for 15 days.
import pandas as pd
import matplotlib.pyplot as plt

temperature_data = {
    "Day": list(range(1, 16)),
    "Temperature": [25, 28, 30, 27, 29, 31, 33, 30, 28, 26, 24, 23, 25, 27, 29]
}

temperature_df = pd.DataFrame(temperature_data)
print(temperature_df)
print("calculate the max temperature:", temperature_df["Temperature"].max())
print("calculate the min temperature:", temperature_df["Temperature"].min())
print("calculate the average temperature:", temperature_df["Temperature"].mean())

# Line plot showing temperature variation over 15 days
plt.figure(figsize=(10, 6))
plt.plot(temperature_df["Day"], temperature_df["Temperature"], marker="o", color="red", linewidth=2)
plt.title("Temperature Variation Over 15 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

