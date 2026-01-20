import matplotlib.pyplot as plt  # Visualize fit
import numpy as np

wl = np.array([280, 300, 320, 334, 340, 360])  # Example digitized
A_raw = np.array([0.1, 0.3, 0.8, 1.0, 0.85, 0.2])  # Normalized
plt.plot(wl, A_raw, 'o', label='Experimental')


from scipy.optimize import curve_fit
def gaussian(x, amp, cen, wid):
    return amp * np.exp( -(x - cen)**2 / (2 * wid**2) )

popt, _ = curve_fit(gaussian, wl, A_raw, p0=[1, 334, 12])
A_fit = gaussian(wl, *popt)
plt.plot(wl, A_fit, '-', label=f'Fit: λ_max={popt[1]:.1f} nm')
