Paintcurve Operators
====================

.. module:: bpy.ops.paintcurve

.. function:: add_point(location=(0, 0))

   Add New Paint Curve Point

   :arg location:

      Location, Location of vertex in area space

   :type location: int array of 2 items in [0, 32767], (optional)

.. function:: add_point_slide(PAINTCURVE_OT_add_point=None, PAINTCURVE_OT_slide=None)

   Add new curve point and slide it

   :arg PAINTCURVE_OT_add_point:

      Add New Paint Curve Point, Add New Paint Curve Point

   :type PAINTCURVE_OT_add_point: :class:`PAINTCURVE_OT_add_point`, (optional)
   :arg PAINTCURVE_OT_slide:

      Slide Paint Curve Point, Select and slide paint curve point

   :type PAINTCURVE_OT_slide: :class:`PAINTCURVE_OT_slide`, (optional)

.. function:: cursor()

   Place cursor

.. function:: delete_point()

   Remove Paint Curve Point

.. function:: draw()

   Draw curve

.. function:: new()

   Add new paint curve

.. function:: select(location=(0, 0), toggle=False, extend=False)

   Select a paint curve point

   :arg location:

      Location, Location of vertex in area space

   :type location: int array of 2 items in [0, 32767], (optional)
   :arg toggle:

      Toggle, (De)select all

   :type toggle: boolean, (optional)
   :arg extend:

      Extend, Extend selection

   :type extend: boolean, (optional)

.. function:: slide(align=False, select=True)

   Select and slide paint curve point

   :arg align:

      Align Handles, Aligns opposite point handle during transform

   :type align: boolean, (optional)
   :arg select:

      Select, Attempt to select a point handle before transform

   :type select: boolean, (optional)

