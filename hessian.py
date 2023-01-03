# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:00:16 2022

@author: Andy
"""

import numpy as np 
import os
pol_der = []


with open('job.hess') as file:
    while 1:
        line = file.readline()
        
        if not line: break
    
        if 'polarizability_derivatives' in line:
            line = file.readline()
            # print(line)
            N = int(line)
            
            for _ in range(N):
                line = file.readline().strip('\n')
                
                line = line.split('  ')
                # lines[:] = [i for i in lines if not i == '']
                line = [x for x in line if x != '']
                # print(line)
                line = [float(i) for i in line]
                pol_der.append(line)
            pol_der = np.array(pol_der)
            
        if 'normal_modes' in line:
            nmodes = []
            line = file.readline().strip('\n')
            line = line.split(' ')
            line = [int(i) for i in line]
            n, m = line
            
            while 1:
                line = file.readline()
                
                if line == '\n': break
                if 'E' in line:
                    nmodes.append(line[7:].strip('\n'))
            
            a_nmodes = np.zeros(shape = (((n // 5) + 1)* m, 5) )
            for i, line in enumerate(nmodes):
                index = i%n
                d = line.split('  ')
                d = [float(i) for i in d if not i == '']
                to_remove = 0
                while len(d) < 5:
                    d = np.append(d, 0)
                    to_remove += 1 
                a_nmodes[i] = d

            a_nmodes = a_nmodes.T
            first = a_nmodes[:,:n]
            for i in range(1, n//5 + 1):
                new = a_nmodes[:,i*n:(i+1)*n]
                first = np.concatenate([first, new])
            final = first[0:-to_remove]

            nmodes = final
            
        if '$hessian' in line:
            nmodes = []
            line = file.readline().strip('\n')
            # line = line.split(' ')
            # line = [int(i) for i in line]
            n = int(line)
            
            while 1:
                line = file.readline()
                
                if line == '\n': break
                if 'E' in line:
                    nmodes.append(line[7:].strip('\n'))
            
            a_nmodes = np.zeros(shape = (((n // 5) + 1)* m, 5) )
            for i, line in enumerate(nmodes):
                index = i%n
                d = line.split('  ')
                d = [float(i) for i in d if not i == '']
                to_remove = 0
                while len(d) < 5:
                    d = np.append(d, 0)
                    to_remove += 1 
                a_nmodes[i] = d

            a_nmodes = a_nmodes.T
            first = a_nmodes[:,:n]
            for i in range(1, n//5 + 1):
                new = a_nmodes[:,i*n:(i+1)*n]
                first = np.concatenate([first, new])
            final = first[0:-to_remove]

            hessian = final            


            # a_nmodes = a_nmodes.T
            # first = a_nmodes[:,:n]
            # for i in range(1, n//5 + 1):
            #     new = a_nmodes[:,i*n:(i+1)*n]
            #     first = np.concatenate([first, new])
            # final = first[0:-to_remove]
            # print(final)
    
# lines = np.array(lines)

# print(lines)











#%%

# rtensors = np.matmul(nmodes.T, pol_der )
# rtensors = np.matmul(rtensors, nmodes )
# print(rtensors)

for mode in pol_der:
    rT = np.zeros(shape = (3,3))
    rT[0,0] = mode[0]
    rT[1,1] = mode[1]
    rT[2,2] = mode[2]
    rT[0,1] = mode[3]
    rT[0,2] = mode[4]
    rT[1,2] = mode[5]
    
    
    
    
    
    ap = rT.diagonal().sum()/3
    gamma2 = 1/2 * ((rT[0,0] - rT[1,1])**2 + (rT[0,0] - rT[2,2])**2 + 
                 (rT[1,1] - rT[2,2])**2 + 6 * (rT[1,2]**2 + rT[0,2] **2 
                                               + rT[0, 1]**2) )
 
    S = 45 * ap**2 + 7 * gamma2 
    if S < 10E-7:
        dep = 3 
    else:
        dep = 3 * gamma2 / (45 * ap**2 + 4 * gamma2)
    
    print(S)
    # print(dep)
    # print(dep)
    
    
0              
0              
0              
0              
0              
0              
2.85859        
2.878364       
4.099049       
0.002014       
0.002409       
6.619363       
8.106377       
8.078048       
65.066993      
168.902758     
62.472966      
62.602741      







