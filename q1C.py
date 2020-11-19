import numpy as np
import matplotlib.pyplot as plt

n_pts = 101

def F_mix(phi):
    phiTerm = (phi * np.log(phi) / 200) + ((1-phi) / 150 * np.log(1-phi)) + (0.013 * phi * (1-phi))
    #return 1.38e-23 * 280 * phiTerm
    return phiTerm

phi = np.linspace(0, 1, n_pts)
y = np.zeros(n_pts)

for i in range(len(phi)):
    y[i] = F_mix(phi[i])
    print("phi: ", phi[i])
    print("Free energy: ", y[i])

plt.plot(phi, y)
plt.show()
    
