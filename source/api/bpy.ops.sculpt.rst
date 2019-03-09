Sculpt Operators
================

.. module:: bpy.ops.sculpt

.. function:: brush_stroke(stroke=None, mode='NORMAL', ignore_background_click=False)

   Sculpt a stroke into the geometry

   :arg stroke:

      Stroke

   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode:

      Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL`` Normal, Apply brush normally.
      * ``INVERT`` Invert, Invert action of brush for duration of stroke.
      * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.

   :type mode: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)
   :arg ignore_background_click:

      Ignore Background Click, Clicks on the background do not start the stroke

   :type ignore_background_click: boolean, (optional)

.. function:: detail_flood_fill()

   Flood fill the mesh with the selected detail setting

.. function:: dynamic_topology_toggle()

   Dynamic topology alters the mesh topology while sculpting

.. function:: optimize()

   Recalculate the sculpt BVH to improve performance

.. function:: sample_detail_size(location=(0, 0))

   Sample the mesh detail on clicked point

   :arg location:

      Location, Screen Coordinates of sampling

   :type location: int array of 2 items in [0, 32767], (optional)

.. function:: sculptmode_toggle()

   Toggle sculpt mode in 3D view

.. function:: set_detail_size()

   Set the mesh detail (either relative or constant one, depending on current dyntopo mode)

.. function:: set_persistent_base()

   Reset the copy of the mesh that is being sculpted on

.. function:: symmetrize()

   Symmetrize the topology modifications

.. function:: uv_sculpt_stroke(mode='NORMAL')

   Sculpt UVs using a brush

   :arg mode:

      Mode, Stroke Mode

      * ``NORMAL`` Normal, Apply brush normally.
      * ``INVERT`` Invert, Invert action of brush for duration of stroke.
      * ``RELAX`` Relax, Switch brush to relax mode for duration of stroke.

   :type mode: enum in ['NORMAL', 'INVERT', 'RELAX'], (optional)

