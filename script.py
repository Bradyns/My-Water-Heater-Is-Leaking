import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

data = pd.read_csv("data.csv")

data["Time (diff)"] = (pd.to_datetime(data["Time (t_final)"], format="%H%M") - pd.to_datetime(data["Time (t_0)"], format="%H%M")).dt.seconds / 3600
data["mL/h"] = data["Measurement (mL)"] / data["Time (diff)"]

data["Average (mL/h)"] = data["mL/h"].expanding().mean()
data["mL/day"] = data["mL/h"] * 24
data["Average (mL/day)"] = data["mL/day"].expanding().mean()
data["Average (Average (mL/h) over 24 hours)"] = data["Average (mL/h)"].expanding().mean() * 24

data.to_csv("results.csv", index=False)

plt.figure()
plt.plot(data["Number"].astype(int), data["Measurement (mL)"], marker="o")
plt.xlabel("Measurement Number")
plt.ylabel("Measurement (mL)")
plt.title("Change Over Time for Each New Measurement")
plt.grid()
plt.savefig("./plots/line_plot.png")
plt.show()

plt.figure()
plt.plot(data["Number"].astype(int), data["Average (mL/day)"], marker="o", color="orange")
plt.xlabel("Measurement Number")
plt.ylabel("Average (mL/day)")
plt.title("Average (mL/day) for each new Measurement")
plt.grid()
plt.savefig("./plots/average_mL_day_plot.png")
plt.show()

plt.figure()
plt.plot(data["Number"].astype(int), data["Average (Average (mL/h) over 24 hours)"], marker="o", color="green")
plt.xlabel("Measurement Number")
plt.ylabel("Average (Average (mL/h) over 24 hours)")
plt.title("Average (Average (mL/h) over 24 hours) for each Measurement")
plt.grid()

x = data["Number"].astype(int)
y = data["Average (Average (mL/h) over 24 hours)"]
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)
plt.plot(x, poly(x), linestyle="--", color="blue")

plt.savefig("./plots/average_average_mL_h_over_24_hours_plot.png")
plt.show()
