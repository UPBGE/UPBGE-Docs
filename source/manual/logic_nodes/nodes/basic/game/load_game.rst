

+++++++++++++++
Load Game
+++++++++++++++

.. figure:: /images/Logic_Nodes/load_game_node.png
   :align: right
   :width: 215
   :alt: Load Game Node.

The *Load Game* node reads information about the state of the current scene
from a previously saved ``.json`` file.

.. note::
    No information is read about which scene is loaded, so this node can only be used per scene.

Parameters
==========

Filepath
   The path to where the save files are stored.

Inputs
=======

Condition
   Input Condition.

Slot
   Index of this save file.

Outputs
=======

Done
   *True* if the node performed successfully, else *False*
