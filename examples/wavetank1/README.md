(wavetank1_README)=
# Wavetank with one obstacle

This example uses GeoClaw to compute the flow in a wavetank containing
a rectangular object.  The original water velocity is 0 but there is a jump
discontinuity in the water depth so that the water starts to flow from left
to right. 

The notebook `wavetank1_obstacles.ipynb`, rendered as
[](#wavetank1_obstacles), illustrates the post-processing
debris tracking for this example.

## GeoClaw code

The script `setrun.py` specifies GeoClaw inputs.  See the
[GeoClaw Tsunami
Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial/)
for tips on getting started, and the
[Clawpack documentation](https://www.clawpack.org/) for more details.

## Topography

The obstacle is incorporated into the topography.  The script `maketopo.py`
creates two topo files, one for the wave tank (uniform flat bottom) on a
coarse grid (`wavetank.tt3`), and one for the obstacle (`block.tt3`),
which is on a finer grid (so that this is the
topofile used by GeoClaw in the region it covers).

## Initial conditions

The script `makeqinit.py` creates the file `qinit.xyz` that is read in by
GeoClaw as a perturbation to the uniform flat surface at elevation $z = 0$
as specified by the `sea_level` parameter in GeoClaw.

## Running GeoClaw and making plots

Assuming you have the prerequisites and GeoClaw running, this should work:

    make  # compiles the Fortran
    make data  # uses setrun.py to make several .data files for Fortran
    make output  # runs the code and puts output in _output
    make plots  # uses setplot.py to make plots in _plots

Or simply

    make .plots

which checks dependencies to do what's needed to make plots see
[Testing GeoClaw --
chile2010](https://rjleveque.github.io/geoclaw_tsunami_tutorial/docs/testing-chile2010/).

## Debris tracking

The `_output` directory contains a set of fgout grids,
which contain the solution interpolated to the same uniform grid
at each time as specified in `setrun.py`.

The script `combine_fgout_nc.py` reads in all the fgout frames and produces
a single netCDF file that contains the solution on an x-y grid at all frames.

The notebook `wavetank1_obstacles.ipynb`, rendered as
[](#wavetank1_obstacles), reads these in and creates
interpolating functions `depth_fcn(x,y,t)` for the depth and similarly for
the velocities.  These can then be used to track debris.
