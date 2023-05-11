import time
from vpython import *
from scipy.spatial import ConvexHull

# Cut the 4d line from 4d point p1 to p2 with a hyperplane at time coordinate t
def line_cut (p1, p2, t):
  # calculate the fraction of the time interval at which to cut the 4d line
  frac = (t - p1[3]) / (p2[3] - p1[3])
  # Determine the intersection point between hyperplane and line
  p = [p1[i] + (p2[i] - p1[i])*frac for i in range(0,3)]
  return p

# Cut the simplex defined by the vertexes with a hyperplane orthogonal
# to the time axis through point t
# vertices: simplex vertices
# t: the time coordinate
def plane_cut (vertices, t):
  ret = []
  for i1 in range(0, 4):
    for i2 in range(i1+1, 4):
      if (vertices[i1][3] == vertices[i2][3]): continue; # same time, ignore
      # Cut each 4d line of the simplex at the given t coordinate
      # The result is a 3d point
      p = line_cut(vertices[i1], vertices[i2], t)
      ret.append(p)
  # Return the corner points of the intersection area between
  # simplex and hyperplane
  return ret

# Get the index of element e in list l. Append e to list if it
# is not present yet.
def getindex (l, e):
  try: return l.index(e)
  except: 
    l.append(e)
    return len(l)-1

# Calculate the atinstant operation on the 3d moving region
# mr3d: The 3d moving region in polytope representation (4d region)
# t:    The instant
def atinstant(mr3d, t):
  # The points and facets for the 3d region, that is the result of
  # the atinstant operation on the 3d moving region
  points, facets = [], []
  for simplex in mr3d.simplices:
    # Iterate over all 4d simplices and intersect with a hyperplane
    # orthogonal to the time axis through coordinate t
    ps = plane_cut([mr3d.points[idx] for idx in simplex], t)
    if (len(ps) == 0): continue # No intersection 
    facet, pt = [], []
    for p in ps:
      facet.append(getindex(points, p))
      pt.append(p)
    facets.append(facet)
  return [points, facets]

# Create interpolation between two convex 3d regions (polyhedra)
# poly1, poly2: Convex polyhedra to interpolate
# t1, t2: initial and final instant
def interpolate(poly1, t1, poly2, t2):
  points = []
  # Elevate the 3d points to 4d and add them into a single set
  for p in poly1: p.append(t1), points.append(p)
  for p in poly2: p.append(t2), points.append(p)
  # Calculate the 4d convex hull
  ret = ConvexHull(points, qhull_options='Qt')
  # Return the 4d region, which is the polytope representation
  # of the 3d moving region
  return ret

###################################
# Visualization part with vpython #
###################################

# Generate the vpython objects for visualization
# poly: the polyhedron to show
def showvpython(poly):

  # Remove all previous objects from canvas
  global canv
  for i in canv.objects: i.visible = False; del i

  # Create triangles and quads from points and facets
  points, facets = poly[0], poly[1]
  for f in facets:
    vs = []
    for pt in f:
      p = points[pt]
      vx, vx.color = vertex(pos=vec(p[0],p[1],p[2])), color.yellow
      vs.append(vx)
    if len(vs) == 3:
      t = triangle(v0=vs[0], v1=vs[1], v2=vs[2])
      n = (vs[1].pos-vs[0].pos).cross(vs[2].pos-vs[1].pos).norm()
      if n.z < 0: n = -n
      vs[0].normal = vs[1].normal = vs[2].normal = n
    elif len(vs) == 4:
      t = quad(v0=vs[0], v1=vs[1], v2=vs[3], v3=vs[2])
      n = (vs[1].pos-vs[0].pos).cross(vs[2].pos-vs[1].pos).norm()
      if n.z < 0: n = -n
      vs[0].normal = vs[1].normal = vs[2].normal = vs[3].normal = n

# Called when the slider moves
# t: The slider value
in_settime = False
def settime(t):
  global in_settime
  if (not in_settime): # We do not want this to be executed twice in parallel
    in_settime = True
    showvpython(atinstant(mr3d, t.value))
    in_settime = False

# The main function to interpolate and visualize two convex 3d regions (polyhedra)
# poly1, poly2: The convex polyhedra to interpolate
# t1, t2: The initial and final instant
def mr3dviewer(poly1, t1, poly2, t2):
   global mr3d, canv
   canv = canvas(width=1200, height=800)
   mr3d = interpolate(poly1, t1, poly2, t2)
   slider(min=t1, max=t2, step=(t2-t1)/100, value=t1, length=220, bind=settime, right=15)
   settime(type('',(object,),{"value": t1})())
   time.sleep(1000000);

