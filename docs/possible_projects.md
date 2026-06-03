
# Possible projects

## Debris tracking with avoidance

### Pure advection

For buoyant massless debris, the debris should be transported with the
fluid velocity (as modified to satisfy constraints of fixed shape and
non-overlapping).

The code in `src/geoclaw_debris/debris_tracking.py` should be further tested
and improved.  Some possible tests:

- Try a time-dependent velocity field, e.g. for the swirling flow shown
  in the [Test1 notebook](../src/geoclaw_debris/Test1), try

        u = lambda x,y,t: -2*sin(pi*y)*cos(pi*y)*sin(pi*x)**2 * cos(2*pi*t / 4)
        v = lambda x,y,t: 2*sin(pi*x)*cos(pi*x)*sin(pi*y)**2 * cos(2*pi*t / 4)

  which reverses direction with period 4, as in the
  Clawpack [`advection_2d_swirl`
  example](https://www.clawpack.org/gallery/_static/amrclaw/examples/advection_2d_swirl/_plots/_PlotIndex.html).

- Experiment with other analytic velocity fields.  Note that a nice way
  to determine a divergence-free velocity field (e.g. an
  incompressible fluid with a uniform depth) is by using
  a stream function $\psi(x,y)$  chosen so that contours of $\psi$ are the
  desired streamlines of the flow.  Then set

  \begin{equation}
  \begin{split}      
    u &= -\psi_y \\
    v &= \psi_x
  \end{split}
  \end{equation}
  so that $u_x + v_y = 0$. The swirling flow velocity was obtained this way from
  the stream function
  $$\psi(x,y) = (\sin^2(\pi x) + \sin^2(\pi y)) / \pi. $$
  Note that $\psi(x,y) = 0$ for $x$ or $y$ equal to 0 or 1, so the
  the boundary of the square domain used in this example is a streamline.


- Experiment with more debris particles and/or obstacles

- Use a flow field computed using GeoClaw, for example:

  - Wavetank simulation with some stationary obstacles as part of the topo,
    with inflow/outflow boundary conditions so the flow reaches a steady
    state.
  
    **Update:** See [](wavetank1_README).

  - Time-dependent flow field captured using fgout frames.

The least squares approach used to remap vertices (to enforce fixed shapes
and non-overlapping conditions) works ok in simple cases but could be
improved, and may break down with more objects.

With lots of objects it may be too slow and perhaps there are better
approaches.

### Adding mass

If bouyant debris has mass, then it should be accelerated based on the
difference in speed between the debris and the fluid.  Some drag factor has
to be included in this that ideally would be based on the shape of the
debris and its orientation relative to the flow.

A first attempt at this is included in the code, but needs more testing
and validation and probably needs improving.

### Adding bottom friction

Debris with mass will have some "grounding depth" (e.g. the draft of a ship)
and in still water that is shallower than this depth it will be sitting on
the bottom, in deeper water it will be floating.  Bouyant debris is assumed
to be floating, but more generally we should include both:

- static friction, if the object is not moving it will be stationary unless
  the force on it is sufficient to overcome the static friction,
- dynamic friction, if the object is moving but touching the bottom, then
  there is a bottom drag term that must be included.

A first attempt at this is included in the code, but probably needs improvement.

### More complex examples

- Using a more realistic GeoClaw tsunami simulation to generate the flow
  field, with some structures in the flow that should be avoided by debris
  (e.g. large buildings or bridge piers).

- Examples from the [NTHMP Tsunami Debris workshop](http://tsunamiworkshop.org).
  Some initial work on these problems using GeoClaw was presented at the
  workshop in 2023.  Some code is available [in this
  repo](https://github.com/rjleveque/tsunami_benchmarks/tree/master/nthmp_debris_2023)
  but does not use the tools developed more recently for tracking large debris.  

## Tracking large sets of point particles


The code in `src/geoclaw_debris/debris_tools.py` has been used for some
problems to track single point particles, either with passive advection or
with the addition of mass and a grounding depth (but no static or dynamic
friction).

This code needs to be cleaned up, and perhaps combined more directly with
the code in `debris_tracking.py` (which was written more recently).

Examples from past work:
  - Modeling a tsunami at Nu'u in Hawaii,
    [figures and animations](https://faculty.washington.edu/rjl/pubs/NuuRefugeTsunami/index.html)
  - [Westport, WA maritime study](https://depts.washington.edu/ptha/debris/particle_tracking.html)
  - [Eagle Harbor on Bainbridge Island](https://depts.washington.edu/ptha/EagleHarbor/)


For the simulations with "ships", two particles (ship ends) were tracked,
with the constraint that the distance between them should remain constant.

It would be interesting to redo some of the simulations with the newer
avoidance algorithm for large ships (e.g. Bainbridge Island ferry).

## Modeling large sets of particles with a continuum density function

For large sets of particles (e.g. in the Seaside study of
https://doi.org/10.1016/j.coastaleng.2019.103541)
it would be interesting to compare tracking individual particles with using
the velocity field to solve an advection equation for the density of debris
(e.g. doing a simulation like the Clawpack advection with swirling flow example
cited above, but with the velocity field coming from a tsunami simulation).

In fact it might be interesting to put lots of particles in the swirling flow
velocity field and see how that compares to the advected density shown in the
Clawpack [`advection_2d_swirl`
example](https://www.clawpack.org/gallery/_static/amrclaw/examples/advection_2d_swirl/_plots/_PlotIndex.html).
