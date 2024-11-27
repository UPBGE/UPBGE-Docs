.. figure:: /images/logic_nodes/ui/widgets/ln-create_layout.png
   :align: right
   :width: 215
   :alt: Create Layout Node

.. _ln-create_layout:

==============================
Create Layout
==============================

Parameters
++++++++++++++++++++++++++++++

Layout Type
   Selected layout type.

X:
   Widget horizontal alignment

Y:
   Widget vertical alignment

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

Relative Size
   If enabled, Size will use a factor value (0-1) instead of pixels.

Size
   Width and Height of this Widget.

Angle
   Widget tilt Angle.

Color
   Background color of this widget.

Border Width
   Width of border line, in pixels.

Border Color
   Color of border line.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

Layout
   Created widget.
