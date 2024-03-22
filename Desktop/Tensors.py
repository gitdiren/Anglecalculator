#import libraries

import numpy

x=3
y=4
z=3

import math

k=round(math.sqrt(x**2 + y**2),2)
m=round(math.sqrt((x**2)+ (y**2)+ (z**2)),2)
print(f'The magnitude of a vector defined by x = {x} and y={y} is {k}')
print(f'The magnitude of a vector defined by x = {x} and y={y} and z={z} is {m}')

theta = round(math.degrees(math.atan(y/x)),2)
print (theta)
