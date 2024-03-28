.. figure:: /images/logic_nodes/values/ln-formatted_string.png
   :align: right
   :width: 215
   :alt: Formatted String Node

.. _ln-formatted_string:

==============================
Formatted String
==============================

Inputs
++++++++++++++++++++++++++++++

Format String
   Fixed string format, or result from connected socket.

A
   String parameter A.

B
   String parameter B.

Outputs
++++++++++++++++++++++++++++++

String
   Resulting string formated from all input strings.

Example
++++++++++++++++++++++++++++++

.. figure:: /images/logic_nodes/values/ln-formatted_string_nodes.png
   :align: center
   :figwidth: 80%
   :alt: Formatted String Node Example

Above setup will pull text values from two String nodes, format them through Formatted String, and print the resulting string into console, on ``LMB`` click. Additional inputs can be added with ``{}`` string - inputs will be added automatically.

.. figure:: /images/logic_nodes/values/ln-formatted_string_output.png
   :align: center
   :figwidth: 60%
   :alt: Formatted String Node Output 

   Printed resulting string in System Console
