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
plt.plot(x, serial['tcpu'].values, label='serial')
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
plt.plot(x, serial['twall'].values, label='serial')
ax.plot(x, vec['twall'].values, label='vec')
ax.plot(x, omp_vec['twall'].values, label='omp_vec')
ax.legend()
plt.title('Tempo de Execução')
plt.xlabel('Trabalho')
plt.ylabel('Tempo (s)')
 
fig.savefig('/home/gabriel/texec.jpg', dpi=400)