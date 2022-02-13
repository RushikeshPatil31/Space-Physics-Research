import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
filename_1 = 'C:\\Users\\Rushi\\Downloads\\Research\\16 Jan 2018\\themisdata.txt'
filename_2 = 'C:\\Users\\Rushi\\Downloads\\Research\\16 Jan 2018\\Omnidata.txt'
f = open(filename_1, 'r')
lines = f.readlines()
Data = lines[0:len(lines)]
N = len(Data)
dataD = {}
varName= ['Bz']
for v in varName:
    dataD[v] = np.zeros((N,), dtype=float)
dataD['time'] = np.zeros((N,), dtype=object)
for l in range(len(Data)):
    parts = Data[l].split()
    time = parts[0] + ' ' + parts[1][:5]
    dataD['time'][l] = dt.datetime.strptime(time, '%d-%m-%Y %H:%M')
    for v in varName:
        dataD[v][l] = float(parts[2 + varName.index(v)])
#print(dataD['time'][0])
f_2 = open(filename_2, 'r')
lines_2 = f_2.readlines()
Data_2 = lines_2[0:len(lines_2)]
N_2 = len(Data_2)
dataD_2 = {}
varName_2= ['Bz']
for v in varName_2:
    dataD_2[v] = np.zeros((N_2,), dtype=float)
dataD_2['time'] = np.zeros((N_2,), dtype=object)
for l in range(len(Data_2)):
    parts_2 = Data_2[l].split()
    time_2 = parts_2[0] + ' ' + parts_2[1][:5]
    dataD_2['time'][l] = dt.datetime.strptime(time_2, '%d-%m-%Y %H:%M')

    for v in varName_2:
        dataD_2[v][l] = float(parts_2[2 + varName_2.index(v)])
#print(dataD['time'][0])

fig = plt.figure(figsize=(20,10))

plt.subplot(2, 1, 1)
plt.plot(dataD['time'], dataD['Bz'], label='THEMIS B', color='red')
plt.xlabel('time', fontsize=14)
plt.ylabel('Bz', fontsize=14)
plt.legend(fontsize=10)
plt.grid('True')

plt.subplot(2, 1, 2)
plt.plot(dataD_2['time'], dataD_2['Bz'], label='OMNI', color='blue')
plt.xlabel('time', fontsize=14)
plt.ylabel('Bz', fontsize=14)
plt.legend(fontsize=10)
plt.grid('True')
plt.show()

