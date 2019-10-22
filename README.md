# FrogPond

There is a pond

The pond has a number of frogs on its permeter

The pond has a number of lilly pads on the surface

The pond has one lilly pad at its centre

Each frog can jump a maximum distance within a set range

Each lilly pad has a diameter within a set range

Each frog tries to jump to a lilly pad which is:
- the central lilly pad if in range
- otherwise another lilly pad which is:
  - within range
  - not been visited by this frog before
  - doesn't have another frog on it
  
If there are no possible lilly pads to jump to the frog is out

This continues until either the frog lands on the centre lilly pad or all frogs are out
