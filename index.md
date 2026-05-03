
(index)=
# GeoClaw Debris Tracking

Work in progress on the development of new tools for tracking debris
in flow fields coming from [GeoClaw](http://www.geoclaw.org) simulations.

In the simplest case, passive advection of particles can be used
to help visualize the flow. Adding more physics such as a grounding
depth (draft), mass of objects, proper drag forces, static and dynamic
bottom friction, etc. is work in progress.

For small debris particles it often works fine to advect the particles
without worrying about collisions with each other or obstacles in the flow.
Large numbers of such particles can be tracked easily.

For large debris objects, adding constraints that they do not overlap with
each other or with obstacles in the flow is also possible, but becomes
time-consuming for more than a few objects. This is still work in progress.

Some initial experiments can be viewed on the webpages built using
Jupyter Book, <https://geoclaw.org/geoclaw_debris/>.

