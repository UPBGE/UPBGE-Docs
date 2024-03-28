.. figure:: /images/logic_nodes/game/ln-load_blender_file.png
   :align: right
   :width: 215
   :alt: Load Blender File Node

.. _ln-load_blender_file:

==============================
Load Blender File
==============================

This is the in-game equivalent of *File Open*. It loads directly into the runtime version of another .blend file.

Inputs
++++++++++++++++++++++++++++++

Condition
   Input condition needed for node to activate.

File Name
   Full path to the target .blend file; supports relative paths.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if the node performed successfully, else *False*.

   .. important::
      Output exists, but is disabled in code, therefore it is not visible.
