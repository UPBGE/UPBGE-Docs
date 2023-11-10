
+++++++++++++++
On Value Changed To
+++++++++++++++

.. figure:: /images/Logic_Nodes/on_value_changed_to_node.png
   :align: right
   :width: 215
   :alt: On Value Changed To Node.

The *On Value Changed To* node stores a value internally, and as soon as the value pulled through
the input matches the target value, it activates. Then the new value is stored.

Inputs
=======

Value
   The connected value is pulled each frame.

Target
   Compare the new value to this value.

Outputs
=======

When Changed To
   *True* if the new value matches the target, else *False*.
