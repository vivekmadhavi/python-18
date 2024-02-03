import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("mp1.csv")
months = data["months"]
mp = data["mp"]
pi = data["pizza"]


plt.figure(figsize=(10,5))
plt.plot(months, mp , linewidth=5, marker="^",markersize=12, markerfacecolor="red", label="Missal pav", color="black")

plt.plot(months, pi , linewidth=5, marker="v",markersize=12, markerfacecolor="red", label="Pizza", color="green")

plt.xlabel("month")
plt.ylabel("sales")
plt.title("misal pav vs pizza")
plt.grid()
plt.legend(shadow=True)

plt.savefig("s1.png")
plt.savefig("s1.pdf")
plt.show()
