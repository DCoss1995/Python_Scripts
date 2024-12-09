# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:11:32 2024

@author: Wetlab
"""
"""
Use when you need to normalize the triplets RGB from 255 to 1.

"""

while True:
    num1 = int(input("Type the first (red channel) number: "))
    num2 = int(input("Type the second (green channel) number: "))
    num3 = int(input("Type the third (blue channel) number: "))

    print("The normalized red value is: ", num1/255)
    print("The normalized green value is: ", num2/255)
    print("The normalized blue value is: ", num3/255)
    print("If you want to compute another RGB triplet, keep going. Press enter if you want to end the script.")
input()