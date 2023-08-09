# A Data Model and Operations for Higher-Dimensional Moving Objects in Databases

These files demonstrate the algorithms described in the work
"A Data Model and Operations for Higher-Dimensional Moving Objects in Databases"

## 2D moving regions

File: 2d/2dinterpolate.scad

This example shows the steps of the algorithms for the case of 2d regions being
interpolated to a 2d moving region.

Prerequisites: openscad

Start with:
openscad 2dinterpolate.scad

## 3D moving regions

File: 3d/box.py
File: 3d/rand.sh

These examples implement and illustrate the algorithm to interpolate two convex 3d
regions to a 3d moving region.

Prerequisites: python3 python3-scipy vpython

Example 1: Interpolation between tetrahedron and cube (example from the manuscript)

Start with: python3 box.py

Example 2: Interpolation between two random convex polyhedra

Start with: ./rand.sh

Author: Florian Heinz <florian.heinz@oth-regensburg.de>

Regensburg, 2023-05-11
