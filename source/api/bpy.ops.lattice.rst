Lattice Operators
=================

.. module:: bpy.ops.lattice

.. function:: flip(axis='U')

   Mirror all control points without inverting the lattice deform

   :arg axis:

      Flip Axis, Coordinates along this axis get flipped

   :type axis: enum in ['U', 'V', 'W'], (optional)

.. function:: make_regular()

   Set UVW control points a uniform distance apart

.. function:: select_all(action='TOGGLE')

   Change selection of all UVW control points

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_less()

   Deselect vertices at the boundary of each selection region

.. function:: select_mirror(axis={'X'}, extend=False)

   Select mirrored lattice points

   :arg axis:

      Axis

   :type axis: enum set in {'X', 'Y', 'Z'}, (optional)
   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)

.. function:: select_more()

   Select vertex directly linked to already selected ones

.. function:: select_random(percent=50.0, seed=0, action='SELECT')

   Randomly select UVW control points

   :arg percent:

      Percent, Percentage of objects to select randomly

   :type percent: float in [0, 100], (optional)
   :arg seed:

      Random Seed, Seed for the random number generator

   :type seed: int in [0, inf], (optional)
   :arg action:

      Action, Selection action to execute

      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.

   :type action: enum in ['SELECT', 'DESELECT'], (optional)

.. function:: select_ungrouped(extend=False)

   Select vertices without a group

   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)

