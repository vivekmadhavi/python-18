import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("mp.csv")
months = data["months"]
sales = data["sales"]


plt.plot(months,sales,linewidth=5, marker="o" , markersize=20,markerfacecolor="red")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid()
plt.show()
