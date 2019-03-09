Marker Operators
================

.. module:: bpy.ops.marker

.. function:: add()

   Add a new time marker

.. function:: camera_bind()

   Bind the active camera to selected marker(s)

.. function:: delete()

   Delete selected time marker(s)

.. function:: duplicate(frames=0)

   Duplicate selected time marker(s)

   :arg frames:

      Frames

   :type frames: int in [-inf, inf], (optional)

.. function:: make_links_scene(scene='')

   Copy selected markers to another scene

   :arg scene:

      Scene

   :type scene: enum in [], (optional)

.. function:: move(frames=0)

   Move selected time marker(s)

   :arg frames:

      Frames

   :type frames: int in [-inf, inf], (optional)

.. function:: rename(name="RenamedMarker")

   Rename first selected time marker

   :arg name:

      Name, New name for marker

   :type name: string, (optional, never None)

.. function:: select(extend=False, camera=False)

   Select time marker(s)

   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)
   :arg camera:

      Camera, Select the camera

   :type camera: boolean, (optional)

.. function:: select_all(action='TOGGLE')

   Change selection of all time markers

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select all time markers using border selection

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

