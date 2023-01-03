#!/apps/haswell/software/Anaconda3/2022.10/bin/python

"""
2022-01-03
Changes:
    added shebang for anaconda on peregrine
    added prints to show what the program is doing
    changed cuttoff from 0.1 to 0.05

To do:
    possibility to generation spin-flip diagrams of important flips
"""

import os
from glob import glob
import numpy as np
import sys

current_files = glob('./*')
mo_s = glob('*o.mo')



print(current_files)

'make file_name the first argument or job.out when none given'
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'job.out'

with open(file_name) as file:  
    print('opening job.out')
    output = []
    for i in file:
        if 'amplitude = ' in i:
            S = i.split('=')[1]
            S = S.strip('alpha\n').strip('beta\n')
            S = float(S)
            S = np.abs(S)

            if S > 0.05: #ignore when the amplitude is too small
                output.append(i)

        else:
            output.append(i)
			

with open('output.out', 'w') as file:
    print('Writing output.out')
    for i in output:
        file.write(i)

print('Done Writing output.out')
print('renaming .mo files to .molden')

for mo in mo_s:
    
	os.system(f'cp {mo} {mo.replace(".mo", ".molden")}')
    
print('Done with everything!')




