# TAMU GIS Programming - Homework 03 / Lab 3
# Name: Anjan Tiwari

import os
import math

# ---------- Classes ----------
class Shape:
    def getArea(self):
        return 0


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = float(l)
        self.w = float(w)

    def getArea(self):
        return self.l * self.w


class Circle(Shape):
    def __init__(self, r):
        self.r = float(r)

    def getArea(self):
        return math.pi * (self.r ** 2)


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = float(b)
        self.h = float(h)

    def getArea(self):
        return 0.5 * self.b * self.h


# ---------- Read file safely (works no matter where you run from) ----------
script_folder = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_folder, "shape.txt")

shapes = []

with open(filename, "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue  # skip blank lines

        parts = line.split(",")

        shape_name = parts[0].strip().lower()

        # Create the correct object based on the first word
        if shape_name == "rectangle":
            # Rectangle,l,w
            l = parts[1]
            w = parts[2]
            shapes.append(Rectangle(l, w))

        elif shape_name == "circle":
            # Circle,r
            r = parts[1]
            shapes.append(Circle(r))

        elif shape_name == "triangle":
            # Triangle,b,h
            b = parts[1]
            h = parts[2]
            shapes.append(Triangle(b, h))

        else:
            print("Unknown shape found in file:", line)


# ---------- Print areas ----------
print("Shapes found:", len(shapes))
total_area = 0

for i, s in enumerate(shapes, start=1):
    area = s.getArea()
    total_area += area
    print(f"{i}. {s.__class__.__name__} area = {area}")

print("Total area =", total_area)
