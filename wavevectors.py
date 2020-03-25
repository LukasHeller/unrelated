import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()

#%%

angle = 5/360*2*np.pi

k_W_abs = 2*np.pi/100
k_w_abs = 2*np.pi/80

k_R_abs = 2*np.pi/80
k_r_abs = 2*np.pi/100

k_W = [k_W_abs,0]
k_w = [np.cos(angle)*k_w_abs,np.sin(angle)*k_w_abs]

k_R = [-k_R_abs,0]
k_r = [-np.cos(angle)*k_r_abs,-np.sin(angle)*k_r_abs]

#%%

d_write = np.array(k_W) - np.array(k_w)
d_read = np.array(k_R) - np.array(k_r)
d_all = d_write + d_read

U = [a[0] for a in [k_W,k_w,d_write,k_R,k_r,d_read,d_all]]
V = [a[1] for a in [k_W,k_w,d_write,k_R,k_r,d_read,d_all]]

X = [0]*len(U)
Y = [0]*len(V)

U_tracing = [a[0] for a in [k_W,k_w,k_R,k_r]]
V_tracing = [a[1] for a in [k_W,k_w,k_R,k_r]]

X_tracing = [0] + [sum(U_tracing[:i]) for i in range(1,4)]+[0]
Y_tracing = [0] + [sum(V_tracing[:i]) for i in range(1,4)]+[0]

U_tracing = U_tracing + [sum(U_tracing)]
V_tracing = V_tracing + [sum(V_tracing)]

color = ['k']*2 + ['red'] + ['grey']*2 + ['green'] + ["blue"]
linestyle = ['-'] + [':'] + ['-']*2 + [':'] + ['-']

plt.close(4)
plt.figure(num = 4, figsize = (5,5))
# plt.quiver(X_tracing,Y_tracing,U_tracing,V_tracing, angles='xy', scale_units='xy', scale=1., color = ['grey']*4 + ['red'])
plt.quiver(X,Y,U,V, angles='xy', scale_units='xy', scale=1., edgecolor = color, linestyle = linestyle, 
            width = 0.001, linewidth = 2, facecolor = 'none',
            headwidth=15, headlength=15)

lim = (-max(k_W_abs, k_r_abs, k_R_abs, k_w_abs)*1.1,max(k_W_abs, k_r_abs, k_R_abs, k_w_abs)*1.1)
plt.xlim(lim)
plt.ylim(lim)

# plt.xlim((-.2,.2))
# plt.ylim((-.2,.2))

#%% Raman
angle = 5/360*2*np.pi

k_Control_abs = 2*np.pi/80
k_Probe_abs = 2*np.pi/100

k_Control = [k_Control_abs,0]
k_Probe = [np.cos(angle)*k_Probe_abs,np.sin(angle)*k_Probe_abs]

#%% Raman plot

d_write = np.array(k_Probe) - np.array(k_Control)
d_read = np.array(k_Control) - np.array(k_Probe)
d_all = d_write + d_read

U = [a[0] for a in [k_Control,k_Probe,d_write,d_read,d_all]]
V = [a[1] for a in [k_Control,k_Probe,d_write,d_read,d_all]]

X = [0]*len(U)
Y = [0]*len(V)

color = ['k']+['grey']+ ['red'] + ['green'] + ["blue"]
linestyle = ['-'] + [':'] + ['-']*3

plt.close(5)
plt.figure(num = 5, figsize = (5,5))
plt.quiver(X,Y,U,V, angles='xy', scale_units='xy', scale=1., edgecolor = color, linestyle = linestyle, 
           width = 0.001, linewidth = 2, facecolor = 'none',
           headwidth=15, headlength=15)
lim = (-max(k_Control_abs, k_Probe_abs)*1.1,max(k_Control_abs, k_Probe_abs)*1.1)
plt.xlim(lim)
plt.ylim(lim)
