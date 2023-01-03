# pyandy

The goal of this python program is to parse through the output files of orca (and others) to parse through useful information, like Gibbs energy, frequencies, IR intensities, raman activities (and calculating raman intensities). Futhermore calculating spectra from these frequencies and intensities/wavelenghts and f_osc's. Using 
Extracting hessian, normal modes and polarizability derivatives from .hess file
For calculating the raman polarizability tensor (when i figure out how)

Todo:
SMILES to orca calculation scripts (to add)



# Currently works:
## compress.py 
which compresses the HUGE qchem output files with SF-TD-DFT optimization
## hessian.py
which extracts the hessian, normal modes and polarizability derivatives from .hess files



all orca scripts assume:
Orca version 5.0.3

pip install --upgrade https://github.com/jkbr/httpie/tarball/master
