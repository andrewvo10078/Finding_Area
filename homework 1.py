# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:34:53 2020
Andrew Castro 1809608 
Homework #1
COSC 1306
"""

# sq.ft per gallon (constant)
sq = 400
#variables
length = int(input("Please enter the length of the room:"))
width = int(input("Please enter the width of the room:"))
height = int(input("Please enter the height of the room:"))

print("the length is", length)
print("the width is", width)
print("the height is", height)

#Compute the areas of the walls
wall_area = width * height + length * height
#Compute the area of the walls
print("the area of the walls is", wall_area, "m2.")

#Compute the area of the ceiling and floor
area_ceil = length * width
print("the area of the ceiling is", area_ceil, "m2.")

total_area = 2 * wall_area + area_ceil
print("the total_area is", total_area, "m2.")

gallons = int(total_area / sq + 0.9999)
print("the number of gallons is", gallons, "L.")

#9 tiles per square feet
tiles = 9 * area_ceil
print("the number of tiles required for the floor is", tiles)
