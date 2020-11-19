import numpy as np
import matplotlib.pyplot as plt

n_pts = 101

def T_binodal(phi):
    chi_binodal = -(1/(1-2*phi)) * ((1+np.log(phi))/200 + (1/150)*( (phi-1)/(1-phi) - np.log(1-phi)))
    return 2.8 / (chi_binodal - 0.003)

def T_spinodal(phi):
    chi_spinodal = 1/2 * (1/(200*phi) + 1/(150*(1-phi)))
    return 2.8 / (chi_spinodal - 0.003)

phi = np.linspace(0, 1, n_pts)

T_B = np.zeros(n_pts)
T_S = np.zeros(n_pts)

for i in range(n_pts):
    print("Step", i)
    T_B[i] = T_binodal(phi[i])
    T_S[i] = T_spinodal(phi[i])

plt.plot(phi, T_B)
plt.plot(phi, T_S)
plt.show()
