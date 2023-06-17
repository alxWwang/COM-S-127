#Nicholas Alexander Wang          9-8-2022
# Lab Week 3 - Exercise #2
import math

rad = int(input("radius of spere : "))

area = 4*math.pi*pow(rad,2)

volume = (4*math.pi*pow(rad,3))/3

print("the area of the spere is {0}, and the volume is {1}".format(area, volume))