.. figure:: /images/logic_nodes/ui/widgets/ln-create_image.png
   :align: right
   :width: 215
   :alt: Create Image Node

.. _ln-create_image:

==============================
Create Image
==============================

Parameters
++++++++++++++++++++++++++++++

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
   todo

Position
   X and Y position of this Widget.

Relative Size
   If enabled, Size will use a factor value (0-1) instead of pixels.

Size
   Width and Height of this Widget.

Angle
   Widget tilt Angle.

Image
   Path to the image to use.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

Image
   Created Widget.
