.. figure:: /images/logic_nodes/ui/widgets/ln-create_label.png
   :align: right
   :width: 215
   :alt: Create Label Node

.. _ln-create_label:

==============================
Create Label
==============================

Parameters
++++++++++++++++++++++++++++++

X:
   Text horizontal alignment

Y:
   Text vertical alignment
   
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

Angle
   Widget tilt Angle.

Text
   Text content as string.

Font
   Graphical font to use for the text.

Font Size
   Display size for the text.

Line Height
   Line spacing in factor (1.5 = 1.5 x Font Size).

Font Color
   Color to use for font.

Use Shadow
   If checked, text will drop a shadow on background.

Shadow Offset
   Offset of the drop shadow in pixels.

Shadow Color
   Color of the shadow drawn behind the text.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

Label
   Created widget.
