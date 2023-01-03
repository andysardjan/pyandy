import os
from glob import glob
import numpy as np

current_files = glob('./*')
mo_s = glob('*o.mo*')

#print(current_files)

if not './output.out' in current_files:
	with open('job.out') as file:
		output = []
		for i in file:
			if 'amplitude = ' in i:
				S = i.split('=')[1]
				S = S.strip('alpha\n').strip('beta\n')
				S = float(S)
				S = np.abs(S)

				if S > 0.1:
					output.append(i)

			else:
				output.append(i)
			

	with open('output.out', 'w') as file:
		for i in output:
			file.write(i)


#for mo in mo_s:
#	os.system(f'cp {mo} {mo.replace(".mo", ".molden")}')




