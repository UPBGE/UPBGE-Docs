.. figure:: /images/logic_nodes/nodes/groups/ln-set_node_value.png
   :align: right
   :width: 215
   :alt: Set Node Value Node

.. _ln-gro-set_node_value:

==============================
Set Node Value
==============================

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Node Tree
   Group node to use.

Node Name
   String representation of node name.

Internal
   The internal socket is for modifying attributes that aren't stored directly on the node but in another container (i.e. ShaderNodeTexImage.image_user.offset > image_user would be the internal entry).

Attribute
   todo

Value
   Type and value to set.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.
