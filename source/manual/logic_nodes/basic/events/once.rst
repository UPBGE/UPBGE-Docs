+++++++++++++++
Once
+++++++++++++++

.. figure:: /images/Logic_Nodes/once_node.png
   :align: right
   :width: 215
   :alt: Once Node.

The *Once* node restricts a continuous *True* condition to only the first frame.

*Example*: An :doc:`./on_update` linked to a *Once* node would be equal to the :doc:`./on_init`.

Inputs
=======

Condition
   Input Condition.

Repeat
   Allow another activation after the input condition is reset to false.

Reset After
   Reset this node after X seconds. Only relevant if the *Timer* parameter is active.

Parameters
=======

Timer
   Reset this node after a time of tree inactivity. This is only needed when stopping
   and starting logic trees.

Outputs
=======

Once
   *True* for the first frame of a *True* input condition, else *False*.
