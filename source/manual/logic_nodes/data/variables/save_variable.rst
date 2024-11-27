.. figure:: /images/logic_nodes/data/variables/ln-save_variable.png
   :align: right
   :width: 215
   :alt: Save Variable Node

.. _ln-save_variable:

==============================
Save Variable
==============================

Save a value into an external `.json` file.

Inputs
++++++++++++++++++++++++++++++

Condition
   Which condition will be used for node to activate.

Path
   Path to the directory containing the requested file.

File
   Name of the file itself, ending can be omitted.

Name
   Lookup key.

Type
   Which type and value to save.
   
Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.
