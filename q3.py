import numpy as np
import matplotlib.pyplot as plt

D_O2 = 1.0E-9

t = np.linspace(0, 86400, 13)
d1 = np.array([0, 2.66E-03, 3.69E-03, 5.69E-03, 4.27E-03, 4.89E-03, 5.73E-03, 5.30E-03, 7.59E-03, 6.99E-03, 7.41E-03, 9.79E-03, 9.91E-03])
d2 = np.array([0, 5.91E-03, 6.36E-03, 6.89E-03, 8.44E-03, 9.46E-03, 7.98E-03, 8.56E-03, 9.32E-03, 7.19E-03, 7.43E-03, 9.27E-03, 1.20E-02])
perfect_d = np.zeros(13)
D1 = np.zeros(12)
D2 = np.zeros(12)
D = np.full(12, D_O2)

def d_t(t):
    return np.sqrt(D_O2 * t)

def D_t(d, t):
    return np.power(d, 2) / t

perfect_d = d_t(t)

for i in range(1, len(t)):
    D1[i-1] = D_t(d1[i], t[i])
    D2[i-1] = D_t(d2[i], t[i])

D1_mean = np.mean(D1)
D2_mean = np.mean(D2)
d1_mean = np.mean(d1)
d2_mean = np.mean(d2)
SS_tot_1 = 0
SS_res_1 = 0
SS_tot_2 = 0
SS_res_2 = 0

for i in range(len(D1)):
    SS_tot_1 += (d1[i] - d1_mean)**2
    SS_tot_2 += (d2[i] - d2_mean)**2
    SS_res_1 += (d1[i] - perfect_d[i])**2
    SS_res_2 += (d2[i] - perfect_d[i])**2

R_1_sqr = 1-(SS_res_1/SS_tot_1)
R_2_sqr = 1-(SS_res_2/SS_tot_2)

print("\nThe mean value of Diffusion Constant 1: ", np.mean(D1), "\nThe std of Diffusion Constant 1: ", np.std(D1), "\nThe variation of Diffusion constant 1: ", np.var(D1))
print("\nThe mean value of Diffusion Constant 2: ", np.mean(D2), "\nThe std of Diffusion Constant 2: ", np.std(D2), "\nThe variation of Diffusion constant 2: ", np.var(D2))
print("\nThe R squared value for Diffusion Constant 1: ", R_1_sqr)
print("\nThe R squared value for Diffusion Constant 2: ", R_2_sqr)

fig, axs = plt.subplots(2)

axs[0].plot(t, perfect_d, label="d(t)")
axs[0].plot(t, d1, label="d1")
axs[0].plot(t, d2, label="d2")
axs[0].legend()
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Dispersion d(t) (m)")
axs[0].set_title("Dispersion at time t with a model line with constant Dispersion 1e-9")

axs[1].scatter(t[1:], D1, label="D1(t)")
axs[1].scatter(t[1:], D2, label="D2(t)")
axs[1].plot(t[1:], D, label="D_O2 Constant", linestyle="dashed", color="yellow")
axs[1].legend()
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Calculated Dispersion Constant (m^2/s)")
axs[1].set_title("Calculated Dispersion constant at time t with constant Dispersion 1e-9 line")

plt.show()