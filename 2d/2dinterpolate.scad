// Snapshot region 1
t1 = 10; // Instant t1 of snapshot
r1 = [[513,412],[751,640],[1014,418],[1004,818],[513,827]]; // Polygon

// Snapshot region 2
t2 = 500; // Instant t2 of snapshot
r2 = [[772,338], [800,340], [917,618], [1010,423],[1078,667],
      [780,921],[459,649],[515,414],[674,649]]; // Polygon

eps = 0.0001; // Let \epsilon < 0 ;)

// Replace by numbers 1-12 to see all steps.
// Step 12 is meant to be animated (View -> Animate, fps:10, steps:100)
step = 1;

// Step 1:
// show the two regions to be interpolated
module step1() {
    polygon(r1);
    translate([800, 0, 0])
        polygon(r2);
}

// Step 2:
// Construct convex hulls and identify concavities:
module step2() {
    difference() {
        hull() polygon(r1);
        polygon(r1);
    }
    translate([800, 0, 0])
    difference() {
        hull() polygon(r2);
        polygon(r2);
    }
}

// Step 3:
// Add t coordinate to the convex regions
module step3() {
    translate([0, 0, t1]) linear_extrude(eps) polygon(r1);
    translate([0, 0, t2]) linear_extrude(eps) polygon(r2);
}

// Step 4:
// Construct convex hull from regions
// (note: linear extrude, because CGAL needs 3d objects to calculate a
//  3d convex hull)
module step4() {
    hull() {
        translate([0, 0, t1]) linear_extrude(eps) polygon(r1);
        translate([0, 0, t2]) linear_extrude(eps) polygon(r2);
    }
}

// Step 5:
// Add t coordinate to concavities
module step5() {
    translate([0, 0, t1]) linear_extrude(eps) difference() { hull() polygon(r1); polygon(r1); }    port = [0,0,0];

    translate([0, 0, t2]) linear_extrude(eps) difference() { hull() polygon(r2); polygon(r2); }
}

// Step 6:
// Construct convex hull between concavity pair 1
module step6() {
  hull() {
    translate([0, 0, t1]) linear_extrude(eps) difference() { hull() polygon(r1); polygon(r1); }
    translate([0, 0, t2]) linear_extrude(eps) difference() { hull() polygon(r2); polygon(r2); square([790, 790]); }
  }
}

// Step 7:
// Construct convex hull between concavity pair 2
module step7() {
  hull() {
    translate([0, 0, t1]) linear_extrude(eps) difference() { hull() polygon(r1); polygon(r1); }
    translate([0, 0, t2]) linear_extrude(eps) difference() { hull() polygon(r2); polygon(r2); translate([790,0,0]) square([790, 790]); }
  }
}

// Step 8:
// Calculate the difference between step 4 and step 6
// The minkowski sum is used to enlarge the subtracted item a bit, otherwise there are
// artifacts in the preview. Rendering will work without this, however.
module step8() {
    difference() {
        step4();
        minkowski() { step6(); cube(1); }
    }
}

// Step 9:
// Calculate the difference between step 8 and step 7
// The minkowski sum is used to enlarge the subtracted item a bit, otherwise there are
// artifacts in the preview. Rendering will work without this, however.
module step9() {
    difference() {
        step8();
        minkowski() { step7(); cube(1); }
    }
}

// Step 10:
// Show plane intersection with step 9 at height h
module step10(h) {
    step9();
    translate([400, 200, h]) cube([700, 700, 0.1]);
}

// Step 11:
// Calculate plane intersection with step 9 at height h
module step11(h) {
    translate([0, 0, -h]) {
        intersection() {
            step9();
            translate([400, 200, h]) cube([700, 700, 0.1]);
        }
    }
}

// Step 12:
// Animate plane intersection
// Choose View -> animate
// FPS:10, Steps:100
module step12() {
    translate([800, 0, 0])
        step10($t*(t2-t1)+t1);
    step11($t*(t2-t1)+t1);
}

if (step == 1) {
    step1();
} else if (step == 2) {
    step2();
} else if (step == 3) {
    step3();
} else if (step == 4) {
    step4();
} else if (step == 5) {
    step5();
} else if (step == 6) {
    step6();
} else if (step == 7) {
    step7();
} else if (step == 8) {
    step8();
} else if (step == 9) {
    step9();
} else if (step == 10) {
    step10((t1+t2)/2);
} else if (step == 11) {
    step11((t1+t2)/2);
} else if (step == 12) {
    step12();
}
