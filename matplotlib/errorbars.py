
from matplotlib import pyplot as plt

plt.figure()

# scatterplot with error bars
x1 = [0.1, 0.3, 0.5, 0.6, 0.7]
y1 = [1, 5, 5, 10, 20]
err1 = [3, 3, 3, 10, 12]
plt.errorbar(x1, y1, err1 , fmt='ro')

# barplot with error bars
x2 = [1.1, 1.2, 1.3, 1.4, 1.5]
y2 = [10, 15, 10, 15, 17]
err2 = (2, 3, 4, 1, 2)
width = 0.05
plt.bar(x2, y2, width, color='r', yerr=err2, ecolor="black")

plt.savefig('errorbars.png')
