# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:06:44 2021

@author: YBurakD
"""
import argparse

start = """# .PCD v.7 - Point Cloud Data file format
VERSION .7
FIELDS x y z
SIZE 4 4 4
TYPE F F F
COUNT 1 1 1
WIDTH {0}
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS {0}
DATA ascii
"""
parser = argparse.ArgumentParser(description='Convert an obj file to a pcd file.')
parser.add_argument('-i', "--input", type=str, nargs=1, help='Input file(*.obj)')
parser.add_argument('-o', "--output", type=str, nargs=1, help='Output file(*.pcd)')

args = parser.parse_args()

input_file = args.input[0]
output_file = args.output[0]

with open(input_file, "r") as infile:
    obj = infile.read()
points = []
for line in obj.split("\n"):
    if(line != ""):
        line = line.split()
        if(line[0] == "v"):
            point = [float(line[1]),float(line[2]),float(line[3])]
            points.append(point)
with open(output_file, "w") as outfile:
    outfile.write(start.format(len(points)))

    for point in points:
        outfile.write("{} {} {}\n".format(point[0],point[1],point[2]))
