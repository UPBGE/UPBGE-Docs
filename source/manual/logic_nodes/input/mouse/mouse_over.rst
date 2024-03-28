.. figure:: /images/logic_nodes/input/mouse/ln-mouse_over.png
   :align: right
   :width: 215
   :alt: Mouse Over Node

.. _ln-mouse_over:

==============================
Mouse Over
==============================

Matches the mouse position to an object on screen.

Inputs
++++++++++++++++++++++++++++++

Object
   Which object to monitor, if mouse cursor is over.

Outputs
++++++++++++++++++++++++++++++

On Enter
   *True* on the first frame the mouse position matches the object bounds, else *False*.

On Over
   *True* while the mouse position matches the object bounds, else *False*.

On Exit
   *True* on the first frame the mouse position leaves the object bounds, else *False*.

Point
   *World Position* of the mouse cursor matched to the object (Vector3).

Normal
   Face normal of the targeted mesh face (Vector3).

Example
++++++++++++++++++++++++++++++

.. figure:: /images/logic_nodes/input/mouse/ln-mouse_over-example_apply.png
   :align: center
   :width: 500
   :alt: Mouse Over Node Apply

   Apply To Selected

With Cube object selected, apply the logic tree (click :menuselection:`Apply To Selected` button).

Run the UPBGE from terminal (Linux & mac), or open the console (Windows). See :ref:`lne-system_console` if needed.

Make sure that in :menuselection:`Render > Game Debug > Mouse Cursor` is selected.

.. figure:: /images/logic_nodes/input/mouse/ln-mouse_over-example_terminal.png
   :align: center
   :width: 90%
   :alt: Mouse Over Node Terminal

   Terminal output

Run the example, and move mouse cursor over the Cube which has *logic tree* applied to it. In system terminal/console, see printed results.

.. figure:: /images/logic_nodes/input/mouse/ln-mouse_over-example_once.png
   :align: center
   :width: 500
   :alt: Mouse Over Node Terminal Once

   Added Once node

Add :ln:`Once` node, run and observe different terminal output. Only once per *Mouse Over* is now system message printed. Uncheck ``Repeat`` and exactly once is message printed - on first *Mouse Over* event only.
