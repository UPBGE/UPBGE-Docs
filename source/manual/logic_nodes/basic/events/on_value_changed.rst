+++++++++++++++
On Value Changed
+++++++++++++++

.. figure:: /images/Logic_Nodes/on_value_changed_node.png
   :align: right
   :alt: On Value Changed Node.

The *On Value Changed* node stores a value internally, and as soon as a value other than
the stored one is pulled through the input, it activates. Then the new value is stored.

Inputs
=======

Value
   The connected value is pulled each frame.

Outputs
=======

If Changed
   *True* if the new value is different from the stored one, else *False*.

Old Value
   The stored value.

If Changed
   The value pulled from the input socket.
