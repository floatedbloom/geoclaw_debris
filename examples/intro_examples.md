(intro_examples)=
# Examples

Some initial experiments...

## Without collision avoidance

For small debris particles it often works fine to advect the particles
without worrying about collisions with each other or obstacles in the flow.
Large numbers of such particles can be tracked easily.

- To appear.

## With collision avoidance

For large debris objects, adding constraints that they do not overlap with
each other or with obstacles in the flow is also possible, but becomes
time-consuming for more than a few objects. This is still work in progress.

- [](../src/geoclaw_debris/Test1) Initial tests of `debris_tracking.py`
  module with some discussion of how to set things up.

- [](flow_around_cylinder/DebrisCylinder)

- [](wavetank1/wavetank1_README) and [](wavetank1/wavetank1_obstacles)

