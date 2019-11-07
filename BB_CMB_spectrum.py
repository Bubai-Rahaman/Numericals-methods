import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#Data taking as input from .txt file
frequency = np.loadtxt('firas_monopole_spec_v1.txt', usecols = 0)
cmb_flux = np.loadtxt('firas_monopole_spec_v1.txt', usecols = 1)

#define constants
c = 3.e8
T = 2.725
h = 6.626e-34
k = 1.38e-23

#changing frequency from (cm)^-1 to Hz
frequency = frequency*c*100
#Black body radiation formula
BB = (2.*h*(frequency**3)/(c**2))*(1./(np.exp(frequency*h/(k*T))-1.))

peaks,_=find_peaks(BB)
print("The wavelength corresponding to the peak is ", 299792458/frequency[peaks],"m")
print("It is in the microwave region")

print("")

#Ploting the spectrum
plt.plot(frequency, cmb_flux*(10**-20),'k.',label = 'CMB Data')
plt.plot(frequency, BB,'r-', label = 'BB spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Flux(SI unit)')
plt.legend()
plt.show()



