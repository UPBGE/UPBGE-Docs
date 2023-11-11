+++++++++++++++
Over
+++++++++++++++

.. figure:: /images/Logic_Nodes/mouse_over_node.png
   :align: right
   :alt: Mouse Over Node.

The Mouse -> *Over* node matches the mouse position to an object on screen.

Inputs
==========

Object
   The object to monitor.

Outputs
=======

On Mouse Enter
   *True* on the first frame the mouse position matches the object bounds, else *False*

On Mouse Over
   *True* while the mouse position matches the object bounds, else *False*

On Mouse Exit
   *True* on the first frame the mouse position leaves the object bounds, else *False*

Point
   World Position of the mouse cursor matched to the object (Vec3).

Normal
   Face normal of the targeted mesh face (Vec3).
