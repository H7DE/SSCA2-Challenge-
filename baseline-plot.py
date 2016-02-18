import math
import matplotlib.pyplot as plt

xVals = [x for x in range(4, 9)]
yVals = [45850156.33890667, 55317227.636973, 59264363.53932733, 64132061.76222667, 9344465.309197335]

plt.title("Average TEPS score vs thread count")
plt.ylabel("avg TEPS")
plt.xlabel("thread count")
plt.plot(xVals, yVals)
plt.show()

