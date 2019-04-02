# This calculator deduces the angular range measured by our MAR345
# XRD camera for use in our powder XRD/XANES investigations.
# This can be generalized for any transmission pXRD setup.
# Reciprocal and 2theta range, and maximum interplanar distance are returned.

from math import *
import decimal

hc = 12.3984 # Planck constant * speed of light: UNITS of [KeV/Angstrom]

# Input values as float
while True:
    try:
        sample_dist = float(input("Enter the sample to detector distance: (cm)")) # sample to detector distance
        imgplate_diam = float(input("Enter the diameter of the image plate in mm (MAR345 = 345mm)")) # diameter of XRD image plate
        user_wavelength = float(input("Enter the wavelength (Angstrom): If you don't have wavelength enter 0, then enter the energy on next prompt.")) # wavelength, if unknown enter energy
        break
    except ValueError:
        print("Check input. Enter a float.")
        continue


# Calculate outputs
theta = round(0.5*degrees(atan((imgplate_diam*0.5)/sample_dist)),2) # calculate theta
twotheta = round(theta * 2,2) #two theta


# Output
if user_wavelength == 0:
    user_energy = float(input("Enter the beam energy: ")) # input energy determined from mono.
    wavelength_con = round(hc / user_energy,3) # Use to determine wavelength of incoming beam
    q = round(4 * pi *sin(theta)/wavelength_con,3) # reciprocal lattice vector length
    interplane_d = round(2 * pi / q,2) #maximum interplanar distance probed
    print("")
    print("The wavelength is: {}A".format(str(wavelength_con)))
    print("The max Q = " + str(q))
    print("The max theta is: " + str(theta) + "deg")
    print("The max 2theta angle is: {}deg".format(str(twotheta)))
    print("The max interplanar spacing d is: {}A".format(str(interplane_d)))

else:
    E = round(hc / user_wavelength,3) #calculate energy
    q = round(4 * pi * sin(theta) / user_wavelength,3) # reciprocal lattice vector length
    interplane_d = round(2 * pi / q,2) #maximum interplanar distance probed
    print("")
    print("The beam energy is: " + str(E) + "KeV")
    print("The max Q = " + str(q))
    print("The max theta is: " + str(theta) + "deg")
    print("The max 2theta angle is: {}deg".format(str(twotheta)))
    print("The max interplanar spacing d is: " + str(interplane_d)+"A")
