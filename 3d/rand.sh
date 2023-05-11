#!/bin/bash
which rbox > /dev/null || { echo Package qhull-bin required; exit 1; }
{
EDGES=20

echo "#!/usr/bin/python3"
echo "from lib.mr3d import mr3dviewer"
echo -n "poly1 = ["; rbox t$RANDOM D3 $EDGES  B10 | tail -n +3 | sed s/^/[/ | sed s/.$/],/ | sed s/\ /,/g | tr -d \\n | sed s/,$// ; echo "]"
echo -n "poly2 = ["; rbox t$RANDOM D3 $EDGES  B10 | tail -n +3 | sed s/^/[/ | sed s/.$/],/ | sed s/\ /,/g | tr -d \\n | sed s/,$// ; echo "]"
echo "mr3dviewer(poly1, 0, poly2, 100)"
} > randmr3d.py
chmod a+x randmr3d.py
./randmr3d.py
