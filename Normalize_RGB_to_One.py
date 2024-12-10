# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:11:32 2024

@author: Wetlab
"""
"""
Use when you need to normalize the RGB triplets from 255 to 1.

"""

while True: # Allows to keep the script going until the user press two times enter.
    num1 = int(input("Type the first (red channel) number: ")) # Type the red channel number (0-255)
    num2 = int(input("Type the second (green channel) number: ")) # Type the green channel number (0-255)
    num3 = int(input("Type the third (blue channel) number: ")) # Type the blue channel number (0-255)

    print("The normalized red value is: ", num1/255) # Return the red value normalized to 1.
    print("The normalized green value is: ", num2/255) # Return the green value normalized to 1.
    print("The normalized blue value is: ", num3/255) # Return the blue value normalized to 1.
    print("If you want to compute another RGB triplet, keep going. Press enter if you want to end the script.")
input() # Pressing enter, the user quits the script.
