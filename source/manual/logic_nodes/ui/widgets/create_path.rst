.. figure:: /images/logic_nodes/ui/widgets/ln-create_path.png
   :align: right
   :width: 215
   :alt: Create Path Node

.. _ln-create_path:

==============================
Create Path
==============================

Parameters
++++++++++++++++++++++++++++++

World:
   Draw the path in screen or world coordinates.
   
Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Parent
   If connected, the created widget will be added as a child to this parent.

Relative Position
   If enabled, position will use a factor value (0-1) instead of pixels.

Position
   X and Y position of this Widget.

Relative Points
   If enabled, each point in Points will use a factor value for its position (0-1) instead of pixels.

Points
   List of points.

Line Color
   Color to draw the line with.

Line Width
   Width of Path line, in pixels.

Angle
   Widget tilt Angle.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

Button
   Created widget.
