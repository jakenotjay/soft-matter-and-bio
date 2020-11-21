import numpy as np
import matplotlib.pyplot as plt

n_pts = 1001

def F_mix(phi):
    phiTerm = (phi * np.log(phi) / 200) + (((1-phi) / 150) * np.log(1-phi)) + (0.013 * phi * (1-phi))
    return 1.38e-23 * 280 * phiTerm

phi = np.linspace(0, 1, n_pts)
y = np.zeros(n_pts)

y = F_mix(phi)

plt.plot(phi, y)
plt.xlim(0, 1)
plt.ylim(top=-1.5e-24)
plt.xlabel("Phi, The Volume Fraction")
plt.ylabel("Free Energy")
plt.title("Plotting the free energy as a function of the volume fraction to find the common Tangent")
plt.show()
    
