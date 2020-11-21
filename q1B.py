import numpy as np
import matplotlib.pyplot as plt

n_pts = 1001

def chi(x):
    return 1/2 * ((1/(200 * x)) + 1 / (150 * (1 - x)))

x = np.linspace(0, 1, n_pts)
y = np.zeros(n_pts)

for i in range(len(x)):
    print("x: ", x[i])
    print("chi: ",chi(x[i]))
    y[i] = chi(x[i])

plt.plot(x, y, label="Chi Spinodal (phi)")
plt.scatter(0.536, 0.0118, color="orange", marker="X", label="The Critical Point")
plt.ylim(0, 0.05)
plt.xlim(0, 1)
plt.xlabel("Phi, The Volume Fraction")
plt.ylabel("Chi Spinodal, Interaction Parameter")
plt.title("Calculating the spinodal interaction parameter as a function of phi")
plt.legend()

plt.show()