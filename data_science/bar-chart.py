import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 3 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()

# -- Bar chart
fruits = ['apple', 'blueberry', 'cherry', 'orange', "kiwi"]
counts = [40, 100, 30, 55, 70]
bar_labels = ['red', 'blue', '_red', 'orange', 'green']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

fig.savefig("bar-chart.png")
plt.show()