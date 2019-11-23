#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:58:48 2019

@author: gabriel
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


algoritmos = ['omp', 'serial', 'vec', 'omp_vec']
path = '/home/gabriel/log.csv'
df = pd.read_csv(path)

omp = df[df['algoritmo'] == 'omp']
serial = df[df['algoritmo'] == 'serial']
vec = df[df['algoritmo'] == 'vec']
omp_vec =  df[df['algoritmo'] == 'omp_vec']


x = omp['trabalho'].values

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp['tcpu'].values, label='omp')
ax.plot(x, serial['tcpu'].values, label='serial')
ax.plot(x, vec['tcpu'].values, label='vec')
ax.plot(x, omp_vec['tcpu'].values, label='omp_vec')
ax.legend()
plt.title('Tempo de CPU')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
 
fig.savefig('/home/gabriel/tcpu.jpg', dpi=400)


fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp['twall'].values, label='omp')
ax.plot(x, serial['twall'].values, label='serial')
ax.plot(x, vec['twall'].values, label='vec')
ax.plot(x, omp_vec['twall'].values, label='omp_vec')
ax.legend()
plt.title('Tempo de Execução')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
 
fig.savefig('/home/gabriel/texec.jpg', dpi=400)



#################################################
serial['threads'] = 1
pathomp = '/home/gabriel/log_omp.csv'
df = pd.read_csv(pathomp)

speed = []
efficiency = []
for index, row in df.iterrows():
    trabalho = row['trabalho']
    ts = serial[serial['trabalho'] == trabalho]['twall'].values[0]
    tp = row['twall']
    s = ts/tp
    speed.append(s)
    efficiency.append(s/row['threads'])
    
df['speed'] = speed
df['efficiency'] = efficiency    

omp1 = df[df['threads'] == 1]
omp2 = df[df['threads'] == 2]
omp3 = df[df['threads'] == 3]
omp4 = df[df['threads'] == 4]

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp1['twall'].values, label='omp1')
ax.plot(x, omp2['twall'].values, label='omp2')
ax.plot(x, omp3['twall'].values, label='omp3')
ax.plot(x, omp4['twall'].values, label='omp4')
ax.plot(x, serial['twall'].values, label='serial')
ax.legend()
plt.title('Tempo de Execução (openmp estático)')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
fig.savefig('/home/gabriel/texec_ompe.jpg', dpi=400)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp1['tcpu'].values, label='omp1')
ax.plot(x, omp2['tcpu'].values, label='omp2')
ax.plot(x, omp3['tcpu'].values, label='omp3')
ax.plot(x, omp4['tcpu'].values, label='omp4')
ax.plot(x, serial['tcpu'].values, label='serial')
ax.legend()
plt.title('Tempo de CPU (openmp estático)')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
fig.savefig('/home/gabriel/tcpu_ompe.jpg', dpi=400)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp1['speed'].values, label='omp1')
ax.plot(x, omp2['speed'].values, label='omp2')
ax.plot(x, omp3['speed'].values, label='omp3')
ax.plot(x, omp4['speed'].values, label='omp4')
ax.legend()
plt.title('Aceleração (openmp estático)')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
fig.savefig('/home/gabriel/acel_ompe.jpg', dpi=400)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp1['efficiency'].values, label='omp1')
ax.plot(x, omp2['efficiency'].values, label='omp2')
ax.plot(x, omp3['efficiency'].values, label='omp3')
ax.plot(x, omp4['efficiency'].values, label='omp4')
ax.legend()
plt.title('Eficiência (openmp estático)')
plt.xlabel('Trabalho')
plt.ylabel('Eficiência')
fig.savefig('/home/gabriel/efic_ompe.jpg', dpi=400)

omp6 = df[df['trabalho'] == 60000]
x = omp6['threads'].values
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp6['speed'].values, label='60000')
plt.xticks(x)
plt.title('Aceleração com maior carga de trabalho (openmp estático)')
plt.xlabel('Threads')
plt.ylabel('Acerelação')
fig.savefig('/home/gabriel/acel_ompe_6000.jpg', dpi=400)


fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp6['efficiency'].values, label='60000')
plt.xticks(x)
plt.title('Eficiência com maior carga de trabalho (openmp estático)')
plt.xlabel('Threads')
plt.ylabel('Eficiência')
fig.savefig('/home/gabriel/efic_ompe_6000.jpg', dpi=400)

#########################################
omp60000 = df[df['trabalho'] == 60000]
x = omp60000['threads'].values
omp50000 = df[df['trabalho'] == 50000]
omp40000 = df[df['trabalho'] == 40000]
omp30000 = df[df['trabalho'] == 30000]

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp60000['twall'].values,'o-', label='60000')
ax.plot(x, omp50000['twall'].values, 'o-',label='50000')
ax.plot(x, omp40000['twall'].values, 'o-',label='40000')
ax.plot(x, omp30000['twall'].values, 'o-',label='30000')
ax.legend()
plt.title('Tempo de Execução (openmp estático)')
plt.xlabel('Threads')
plt.xticks(x)
plt.ylabel('Tempo (s)')
fig.savefig('/home/gabriel/exec_omp_o.jpg', dpi=400)



barWidth = 0.15
r1 = np.arange(len(omp60000['tcpu'].values))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
fig = plt.figure(figsize=(10,5))
ax = plt.subplot(111)
ax.bar(r1, omp60000['tcpu'].values, label='60000', width=barWidth)
ax.bar(r2, omp50000['tcpu'].values, label='50000', width=barWidth)
ax.bar(r3, omp40000['tcpu'].values, label='40000', width=barWidth)
ax.bar(r4, omp30000['tcpu'].values, label='30000', width=barWidth)
ax.legend()
plt.title('Tempo de Execução (openmp estático)')
plt.xticks([r + barWidth for r in range(len(omp60000['tcpu'].values))], x)
plt.xlabel('Threads')
plt.ylabel('Tempo (s)')
fig.savefig('/home/gabriel/exec_omp2.jpg', dpi=400)


#fig = plt.figure()
#ax = plt.subplot(111)
#ax.bar(x, omp60000['twall'].values, label='60000')
#ax.bar(x, omp50000['twall'].values, label='50000')
#ax.bar(x, omp40000['twall'].values, label='40000')
#ax.bar(x, omp30000['twall'].values, label='30000')
#ax.legend()
#plt.title('Tempo de Execução')
#plt.xlabel('Threads')
#plt.xticks(x)
#plt.ylabel('Tempo (s)')



pathdf = '/home/gabriel/log_omp2.csv'
df = pd.read_csv(pathdf)
omp1 = df[df['threads'] == 1]
omp2 = df[df['threads'] == 2]
omp3 = df[df['threads'] == 3]
omp4 = df[df['threads'] == 4]
x = omp1['trabalho'].values
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp1['twall'].values, label='omp1')
ax.plot(x, omp2['twall'].values, label='omp2')
ax.plot(x, omp3['twall'].values, label='omp3')
ax.plot(x, omp4['twall'].values, label='omp4')
ax.plot(x, serial['twall'].values, label='serial')
ax.legend()
plt.title('Tempo de Execução (openmp dinâmico)')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
fig.savefig('/home/gabriel/texec_ompd.jpg', dpi=400)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, omp1['tcpu'].values, label='omp1')
ax.plot(x, omp2['tcpu'].values, label='omp2')
ax.plot(x, omp3['tcpu'].values, label='omp3')
ax.plot(x, omp4['tcpu'].values, label='omp4')
ax.plot(x, serial['tcpu'].values, label='serial')
ax.legend()
plt.title('Tempo de CPU (openmp dinâmico)')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
fig.savefig('/home/gabriel/tcpu_ompd.jpg', dpi=400)




