import numpy as np
import matplotlib.pyplot as plt

n_pts = 1001
N_x = 200
N_y = 150

def T_binodal(phi):
    chi_binodal = -(1/(1-2*phi)) * ((1+np.log(phi))/200 - (1/150)*( 1 + np.log(1-phi)))
    return 2.8 / (chi_binodal - 0.003)

def T_spinodal(phi):
    chi_spinodal = 1/2 * (1/(200*phi) + 1/(150*(1-phi)))
    return 2.8 / (chi_spinodal - 0.003)

phi = np.linspace(0, 1, n_pts)

T_B = np.zeros(n_pts)
T_S = np.zeros(n_pts)

T_B = T_binodal(phi)
T_S = T_spinodal(phi)

plt.plot(phi, T_B, label="Binodal Line")
plt.plot(phi, T_S, label="Spinodal Line")
plt.plot(0.536)
plt.xlabel("Phi, The Volume Fraction")
plt.ylabel("T, Temperature (K)")
plt.xlim(0, 1)
plt.ylim(bottom=0, top=500)
plt.title("A phase diagram of our two polymers")
plt.legend()
plt.show()
