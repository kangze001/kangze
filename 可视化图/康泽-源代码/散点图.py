import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square number", fontsize=24)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.savefig('散点图.png', bbox_inches='tight')
