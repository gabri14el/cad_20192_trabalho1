#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:43:42 2019

@author: gabriel
"""
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
path = '~/log_m.csv'
df = pd.read_csv(path)
sufix = '/home/gabriel/matheus_'

omp = df[df['algoritmo'] == 'omp_12']
serial = df[df['algoritmo'] == 'serial']
vec = df[df['algoritmo'] == 'vec']
omp_vec =  df[df['algoritmo'] == 'omp_vec']

speed = []
efficiency = []
threads = []
algoritmo = []
for index, row in df.iterrows():
    if 'omp_vec' in row['algoritmo']:
        row['threads'] = 1
    elif 'omp' in row['algoritmo']:
        aux = row['algoritmo']
        row['algoritmo'] = 'omp'
        row['threads'] = int(aux.split('_')[-1])
    else:
        row['threads'] = 1
    trabalho = row['trabalho']
    ts = serial[serial['trabalho'] == trabalho]['twall'].values[0]
    tp = row['twall']
    s = ts/tp
    speed.append(s)
    efficiency.append(s/row['threads'])
    threads.append(row['threads'])
    algoritmo.append(row['algoritmo'])

df['speed'] = speed
df['efficiency'] = efficiency
df['algoritmo'] = algoritmo
df['threads'] = threads

#######################################
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
fig.savefig(sufix+'tcpu.jpg', dpi=400)

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
 
fig.savefig(sufix+'texec.jpg', dpi=400)

#########################

df_omp = df[df['algoritmo'] == 'omp']
omps = []
for i in range(12):
    omps.append(df_omp[df_omp['threads'] == i+1])

exe = plt.figure(figsize=(10,15))
ax = plt.subplot(111)
for i in range(12):
    ax.plot(x, omps[i]['twall'].values, label='omp_'+str(i+1))
ax.legend()
plt.title('Tempo de Execução (openmp dinâmico)')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
exe.savefig(sufix+'texec_ompe.jpg', dpi=400)

acl = plt.figure(figsize=(10,5))
ax = plt.subplot(111)

for i in range(12):
    ax.plot(omps[i]['trabalho'].values, omps[i]['speed'].values, label='omp_'+str(i+1))
ax.legend()
plt.title('Aceleração (openmp dinâmico)')
plt.xlabel('Trabalho')
plt.ylabel('Aceleração')
exe.savefig(sufix+'texec_ompe.jpg', dpi=400)

efc = plt.figure(figsize=(10,5))
ax = plt.subplot(111)

for i in range(12):
    ax.plot(omps[i]['trabalho'].values, omps[i]['efficiency'].values, label='omp_'+str(i+1))
ax.legend()
plt.title('Eficiência (openmp dinâmico)')
plt.xlabel('Trabalho')
plt.ylabel('Eficiência')
efc.savefig('/home/gabriel/efic_ompe.jpg', dpi=400)

cpu = plt.figure(figsize=(10,15))
ax = plt.subplot(111)
for i in range(12):
    ax.plot(x, omps[i]['tcpu'].values, label='omp_'+str(i+1))
ax.legend()
plt.title('Tempo de CPU (openmp dinâmico)')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
exe.savefig(sufix+'tcpu_ompe.jpg', dpi=400)

omp6 = df_omp[df_omp['trabalho'] == 60000]
fig = plt.figure()
ax = plt.subplot(111)
x2 = omp6['threads'].values
ax.plot(x2, omp6['efficiency'].values, label='60000')
plt.xticks(x2)
plt.title('Eficiência com maior carga de trabalho (openmp dinâmico)')
plt.xlabel('Threads')
plt.ylabel('Eficiência')
fig.savefig(sufix+'efic_ompe_6000.jpg', dpi=400)

fig = plt.figure()
ax = plt.subplot(111)
x2 = omp6['threads'].values
ax.plot(x2, omp6['speed'].values, label='60000')
plt.xticks(x2)
plt.title('Aceleração com maior carga de trabalho (openmp dinâmico)')
plt.xlabel('Threads')
plt.ylabel('Aceleração')
fig.savefig(sufix+'acel_ompe_6000.jpg', dpi=400)



    

