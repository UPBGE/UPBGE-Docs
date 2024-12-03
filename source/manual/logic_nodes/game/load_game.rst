.. figure:: /images/logic_nodes/game/ln-load_game.png
   :align: right
   :width: 215
   :alt: Load Game Node

.. _ln-load_game:

==============================
Load Game
==============================

Reads information about the state of the current scene from a previously saved ``.json`` file.

Parameters
++++++++++++++++++++++++++++++

File Path/Saves
   Path to where the save files are stored.

Inputs
++++++++++++++++++++++++++++++

Condition
   The condition for this node to activate.

Slot
   Index of this save file.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if the node performed successfully, else *False*.

.. important::
    No information is read about which scene is loaded, so this node can only be used per scene.
