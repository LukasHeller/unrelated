"""
A few plots and simple calculations, for the record
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.constants as con

mass_u = con.value('atomic mass constant')
kb = con.value('Boltzmann constant')
c_vac = con.value('speed of light in vacuum')

#%% Exponential decay of transmission probabilities

x = np.linspace(0,1000,1001)
I = np.exp(-x/22)
I2 = 10**(-x*0.2/10)
f = 14

plt.figure(0, figsize = (10,3))
plt.plot(x,I2, lw = 4)
plt.xlabel("Channel length l (km)", fontsize = f)
plt.ylabel("Transmission Probability", fontsize = f)
plt.gca().tick_params(axis='both', labelsize=14)
plt.xlim((0,1000))
plt.ylim(bottom = 0)
plt.savefig("loss.png", dp1i = 300, bbox_inches = "tight")

#plt.plot(x,I)
#plt.figure(1, figsize = (10,3))
#plt.semilogy(x,I2)
#plt.xlabel("Channel length l (km)", fontsize = f)
#plt.ylabel("Transmission Probability", fontsize = f)
#plt.xlim(left = 0)
#plt.ylim(bottom = 0)
#plt.savefig("loss_semilog.png", dpi = 300, bbox_inches = "tight")

#%% Scaling of repetition rate with modenumber

n = np.array(range(0,100))
ratio = 1/20
rep_single = n/(n+1)
rep_multi = n/(2+(n-1)*ratio)

plt.figure(2, figsize=(12,8))
plt.bar(n,rep_multi, label = r'Cavity enhanced emission, $ \beta_w/\beta_r = 20$')
plt.bar(n,rep_single, label = r'No Cavity enhancement, $ \beta_w/\beta_r = 1$')
plt.xlabel('Mode number')
plt.ylabel('$R_{ent}/\epsilon$')
plt.legend()
plt.show()
plt.savefig('\modescaling.png',dpi =300, transparent = False, bbox_inches='tight')

#%% Loss due to atomic motion

temperature = 30*con.micro
mass = 87*mass_u
v_aver = np.sqrt(temperature*3*kb/mass)
print('Average atom velocity in the cloud: {}m'.format(v_aver))

focus = 100*con.micro
t_aver = focus/v_aver
print('Average atom time in the cloud: {} milli s'.format(t_aver/con.milli))

#%% Temperature of the gas

m = 87*mass_u
ts = 137*con.micro
w = 780*con.nano
Temp =m/(kb*ts**2)*(w/(4*np.pi*np.sin(2*np.pi/360/2)))**2
print('Temperature of the gas is {} uK.'.format(Temp/con.micro))

#%% Cavity Shaking in absolute distance
FSR = 342*con.mega
shake_freq = 20*con.mega
w = 780*con.nano
shake_length = shake_freq/FSR*w
print('Cavity shaking length is {} nm.'.format(shake_length/con.nano))
print('Mirror shaking length is {} nm.'.format(shake_length/con.nano*np.sin(2*np.pi/360*67.5)/2))

#%% Plotting the different Fock state contributions

delta_p = 0.01
p =np.arange(delta_p,1,delta_p*5)
excitations = 24

def excite(n=10):
    powers = range(1,n)
    for power in powers:
        yield lambda x: x**power*(1-x), power
        
def excited_photons(n=10):
    powers = range(1,n)
    for power in powers:
        yield lambda x: x**power*(1-x)*power, power
    
for i, power in excite(5):
    plt.plot(p,i(p)*100, label = str(power))

plt.legend(title = r'# of excitations ...')
plt.xlabel('Excitation probability p')
plt.ylabel('Contribution of n\'th component [%] ')