import numpy as np
import matplotlib.pyplot as plt

angle = np.linspace(0,2*np.pi, 1000)

N = 10000

a = np.zeros(N)

for i in range(N):
    angles = np.random.rand(1000)*2*np.pi
    a[i] = sum(angles)/1000
#%%
# plt.close(1)
plt.figure(1)
plt.hist(a, 60, rwidth = 0.9)

