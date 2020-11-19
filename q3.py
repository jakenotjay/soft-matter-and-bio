import numpy as np
import matplotlib.pyplot as plt

D_O2 = 1.0E-9

t = np.linspace(0, 86400, 13)
d1 = np.array([0, 2.66E-03, 3.69E-03, 5.69E-03, 4.27E-03, 4.89E-03, 5.73E-03, 5.30E-03, 7.59E-03, 6.99E-03, 7.41E-03, 9.79E-03, 9.91E-03])
d2 = np.array([0, 5.91E-03, 6.36E-03, 6.89E-03, 8.44E-03, 9.46E-03, 7.98E-03, 8.56E-03, 9.32E-03, 7.19E-03, 7.43E-03, 9.27E-03, 1.20E-02])
perfect_d = np.zeros(13)
D1 = np.zeros(12)
D2 = np.zeros(12)

def d_t(t):
    return np.sqrt(D_O2 * t)

def D_t(d, t):
    return np.power(d, 2) / t

perfect_d = d_t(t)

for i in range(1, len(t)):
    D1[i-1] = D_t(d1[i], t[i])
    D2[i-1] = D_t(d2[i], t[i])

print("\nThe mean value of Diffusion Constant 1: ", np.mean(D1), "\nThe std of Diffusion Constant 1: ", np.std(D1))
print("\nThe mean value of Diffusion Constant 2: ", np.mean(D2), "\nThe std of Diffusion Constant 2: ", np.std(D2))

plt.plot(t, perfect_d, label="d(t)")
plt.plot(t, d1, label="d1")
plt.plot(t, d2, label="d2")

plt.legend()
plt.show()