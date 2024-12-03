.. figure:: /images/logic_nodes/game/ln-save_game.png
   :align: right
   :width: 215
   :alt: Save Game Node

.. _ln-save_game:

==============================
Save Game
==============================

Stores information about the state of the scene in a ``.json`` file.

Parameters
++++++++++++++++++++++++++++++

File Path/Saves
   Path to where the save files are stored.

Inputs
++++++++++++++++++++++++++++++

Condition
   The condition for this node to activate.

Slot
   Index of this save file. If a save file already exists at this index, it will be overwritten.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if the node performed successfully, else *False*.

.. important::
    No information is saved about which scene is loaded, so this node can only be used per scene.
