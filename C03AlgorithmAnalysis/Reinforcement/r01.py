import matplotlib.pyplot as plt
from math import log2

plt.xkcd()

x = range(2, 101)
y1 = [8 * n for n in x]
y2 = [4 * n * log2(n) for n in x]
y3 = [2 * n ** 2 for n in x]
y4 = [n ** 3 for n in x]
y5 = [2 ** n for n in x]

plt.loglog(x, y1, label="8n")
plt.loglog(x, y2, label="4n log n")
plt.loglog(x, y3, label="2n^2")
plt.loglog(x, y4, label="n^3")
plt.loglog(x, y5, label="2^n")

plt.axis([2, 100, 1, 10000000])
plt.xlabel("n")
plt.ylabel("Some functions")

plt.legend()
plt.show()
