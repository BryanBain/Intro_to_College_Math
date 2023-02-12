import matplotlib.pyplot as plt 
import numpy as np 
import random as rd 

grades = ['A', 'B', 'C', 'D', 'F']
before = [5, 8, 11, 9, 7]
after = [7, 9, 13, 1, 0]

x = np.arange(len(grades))
width = 0.35  # width of the bars
fig, ax = plt.subplots()

rects1 = ax.bar(x-width/2, before, width, color = 'w', ec = 'k', hatch = '/', label="Before")
rects2 = ax.bar(x+width/2, after, width, color = 'b', ec = 'k', hatch = '', label="After")

ax.set_ylabel("Frequency")
ax.set_title("Test Scores Before an After a New Studying Technique")
ax.set_xticks(x, grades)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()
