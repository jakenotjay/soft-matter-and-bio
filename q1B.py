import numpy as np
import matplotlib.pyplot as plt

def chi(x):
    return 1/2 * ((1/(200 * x)) + 1 / (150 * (1 - x)))

x = np.linspace(0, 1, 21)
y = np.zeros(21)

for i in range(len(x)):
    print("x: ", x[i])
    print("chi: ",chi(x[i]))
    y[i] = chi(x[i])

plt.plot(x, y)
plt.show()