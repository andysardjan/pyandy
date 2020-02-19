
"""
Author: Andy Sardjan
Date: 19-02-2019
Goal: Converts (wavenumber, intensity) lists to spectra, which can be
opened in spectrogrpyh. 
"""
# =============================================================================
# Files and packges to import, global variables
# =============================================================================
import pandas as pd
import numpy as np

inputfile_name = 'input.txt'
outputfile_name = 'spectrum.txt'
frequency_scaling_factor = 1.0 #can be obtained from trying
broadening = 20 #in cm-1, FWHM
number_of_points = 2000 #on the x-axis
lower_lim_x = 0 # in cm-1
upper_lim_x = 3500 # in cm-1
seperator = '\t' #means tab seperated

# =============================================================================
# Program
# =============================================================================
broadening = broadening / 2.355 #converts it to standard deviations
imp = pd.read_csv(inputfile_name, sep = seperator, header = None) #import files

shifts = np.linspace(lower_lim_x, upper_lim_x,number_of_points)#calculates x-points

def gaussianatpoints(peak_intensities, peak_frequencies, broadening, shifts):
    """Takes imported frequency, intensity data and adds a gaussian peak at all 
    peak positions"""
    output_intensities = np.zeros(len(shifts))
    
    for pos, intensity in zip(peak_intensities, peak_frequencies * frequency_scaling_factor):
        single_peak_spectrum = []
        for x in shifts:
            single_peak_spectrum.append( intensity*np.exp(-(x
            - pos)**2/(2*broadening**2)) )
    
        output_intensities += np.array(single_peak_spectrum) #adding all singles peaks to produce full spectrum

    
    
    output = np.array([shifts, output_intensities])
    return(output)

dat = gaussianatpoints(imp[0], imp[1], broadening, shifts)

np.savetxt(outputfile_name, dat.T, delimiter = '\t')


