#!/usr/bin/python3
from lib.mr3d import mr3dviewer

poly1 = [[0,0,0],[0,100,0],[100,100,0],[100,0,0],[0,0,100],[0,100,100],[100,100,100],[100,0,100]]
poly2 = [[110,0,30],[110,100,0],[210,100,0],[210,0,0],[160,50,80]]

mr3dviewer(poly1, 0, poly2, 100)
