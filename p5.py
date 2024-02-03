import matplotlib.pyplot as plt


months = ["aug","sep","oct","nov","dec"]
sales = [89.71,79.77,84.44,72.94,80.21]


plt.plot(months,sales,linewidth=5, marker="o" , markersize=20,markerfacecolor="red")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid()
plt.show()
