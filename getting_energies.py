# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:27:26 2020

@author: Andy
"""


import os
import numpy as np
import pandas as pd
import re


def search(term, line):
    if re.search(term, line):       
        line = line[:-2]
        for j in line.split(' '):
            try:
                j = float(j)
                if j != '':
                    return(j)                 
            except:
                pass
        
def try_to_read(line, keyword, is_number = True):
    l = len(keyword)
    
    try:
        if line[:l] == keyword:
            
            if is_number:
                return(float(line.split('=')[-1]))
            elif is_number == False:
                return(i.split('=')[-1])
        
    except:
        return(None)
    
        
    


def reading_outputfile(name):
    file = open(name, 'r')
    i = 0

    summary = []
    "first we find the last line with ' -----' "
    while 1:
        line = file.readline()
        i += 1
        
        if line[:6] == ' -----':
            i_final = i    
    
        if not line:
            break
        
    summary = []
    i = 0
    
    file.close()
    file = open(name, 'r')
    "Then we read and copy until a blank line"
    while 1:
        line = file.readline()
        i += 1
        
        
 
        if line == '\n' and i > i_final:
            break
        
        if i > i_final:
            summary.append(line[1:-1])
        
    file.close()
    
    
    "Then seperating the information starts"
    
    summary = ''.join(summary).split('\\')
    output = {}
    output['Method'] = summary[11]
    output['Title'] = summary[13]
    output['Charge,Mult'] = summary[15]
    output['MolForm'] = summary[6]
    # output['Geometry'] = geom
    
    unique_atoms = [str(i) + ',' for i in list(summary[6]) if i not in [str(i) for i in range(10)] ] # this is done mostly for fun
    geometry = []
    
    for i in summary:
        if len(i) > 0:
            if i[:2] in unique_atoms:
                geometry.append(i)
                
        if i[:3] == 'HF=':
            output['ElecEnergy'] = float(i.split('=')[-1])
        if i[:5] == 'RMSD=':
            output['RMSD'] = float(i.split('=')[-1])
        if i[:5] == 'RMSF=':
            output['RMSF'] = float(i.split('=')[-1])
        if i[:10] == 'ZeroPoint=':
            output['ZPVE'] = float(i.split('=')[-1])
            
        if i[:7] == 'Dipole=':
            output['Dipole'] = i.split('=')[-1]
        if i[:8] == 'Thermal=':
            output['ThermEnergy'] = float(i.split('=')[-1])
            
            
    "Now looking for Frequencies, which are not in the summary"
    i = 0
    file = open(name, 'r')
    freqs = []
    IR_int = []
    Raman_act = []
    while 1:
        
        line = file.readline()
        i += 1
        
        if search(r'Frequencies', line):
            freqs.append(search(r'Frequencies', line))
        if search(r'IR Inten', line):
            IR_int.append(search(r'IR Inten', line))
        if search(r'Raman Activ', line):
            Raman_act.append(search(r'Raman Activ', line))
         
        if not line:
            break
    file.close()    
        
            
    output['Frequencies'] = freqs     
    output['IR Inten'] = IR_int 
    output['Raman Act'] = Raman_act 
    output['Geometry'] = geometry
    
    return(output)

   

diene = reading_outputfile('job.out')
print(diene)

