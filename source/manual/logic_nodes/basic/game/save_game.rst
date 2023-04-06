

+++++++++++++++
Save Game
+++++++++++++++

.. figure:: /images/Logic_Nodes/save_game_node.png
   :align: right
   :width: 215
   :alt: Save Game Node.

The *Save Game* node stores information about the state of the scene in a ``.json`` file.

.. note::
    No information is saved about which scene is loaded, so this node can only be used per scene.

Inputs
=======

Condition
   Input Condition.

Slot
   Index of this save file.

Parameters
==========

Filepath
   The path to where the save files are stored.

Outputs
=======

Done
   *True* if the node performed successfully, else *False*
