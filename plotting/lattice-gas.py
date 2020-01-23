import yaml
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open('test.yaml','r') as stream:
    try:
        data_loaded = yaml.safe_load(stream)
    except yaml.yamlerror as exc:
        print(exc)

time_frame = data_loaded['movies']['time']
entropy_data = data_loaded['movies']['entropy']
hist_data = data_loaded['movies']['histogram']
hist = data_loaded['bins']['histogram']
moves = data_loaded['movies']['time'][7:]
energy_data = data_loaded['movies']['energy']

number_data = np.array(data_loaded['movies']['number'])
energy_resize = np.array(energy_data)

#print('energy_resize size', energy_resize.shape)

nlist = len(energy_data)
print('energy_data.shape', energy_resize.shape)
energy_resize.resize(9, 5)
number_data.resize(9, 5)
print(energy_resize)

E = np.zeros((10, 6))
E[:-1,:-1] = energy_resize
N = np.zeros((10, 6))
N[:-1,:-1] = number_data

dE = abs(E[0,0] - E[1,0]) #change in energy
E -= dE/2
print('dE', dE)

E[-1,:] = E[-2,:] + dE
N[-1,:] = N[-2,:]

E[:,-1] = E[:,-2]
N[:,-1] = N[:,-2] + 1

N -= 0.5

for t in range(len(entropy_data)):
    print('time', moves[t])
    S = np.array(entropy_data[t])
    S.resize(9, 5)
    S0 = S[-1,0] # this is the E=0, N=0 entropy
    S = S - S0
    hist = np.array(hist_data[t])
    hist.resize(9, 5)
    S[hist==0] = np.nan
    plt.figure('entropy')
    plt.clf() #Clear the current figure.
    plt.title(f'{moves[t]} moves')
    plt.pcolor(N,E,S) #pcolor([X, Y,] C, **kwargs) https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolor.html
    plt.xlabel('$N$')
    plt.ylabel('$E$')
    plt.colorbar() #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colorbar.html
    plt.figure('histogram')
    plt.clf()
    plt.title(f'{moves[t]} moves')
    plt.pcolor(N,E,hist)
    plt.colorbar()
    plt.pause(1) #Pause for interval seconds

plt.show()