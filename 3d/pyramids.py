#!/usr/bin/python3
from lib.mr3d import mr3dviewer
poly1 = [
  [   0,   0,   0],
  [   0,   0, 100],
  [   0, 100, 100],
  [   0, 100,   0],
  [  70,  50,  50]
]
poly2 = [
  [ 150,   0,   0],
  [ 150,   0, 100],
  [ 150, 100, 100],
  [ 150, 100,   0],
  [  80,  50,  50]
]
mr3dviewer(poly1, 0, poly2, 100)
