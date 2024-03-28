.. |movement-button| image:: /images/logic_bricks/logic-common-options-icons-movement.png

.. |pin-button| image:: /images/logic_bricks/logic-common-options-icons-pin.png

.. |down-button| image:: /images/logic_bricks/logic-common-options-icons-down.png

==============================
Introduction
==============================

Actuators perform actions, such as move, create objects, play a sound. The actuators initiate their functions when they get a positive pulse from one (or more) of their controllers.

The logic blocks for all types of actuator may be constructed and changed using the Logic Bricks Editor; details of this process are given in the :doc:`Actuator Editing <./editing>` page.

.. _game-engine-logic-actuators-common-options:

Common Options
++++++++++++++++++++++++++++++

.. figure:: /images/logic_bricks/actuators/logic-actuators-common_options-column.png

   Common Actuator options

All actuators have a set of common buttons, fields and menus. They are organized as follows:

Triangle button |down-button|
   Collapses the sensor information to a single line (toggle).
Actuator type menu
   Specifies the type of the sensor.
Actuator name
   The name of the actuator. This can be selected by the user. It is used to access actuators with Python; it needs to be unique among the selected objects.
Pin button |pin-button|
   Display the actuator even when it is not linked to a visible states controller.
Movement buttons |movement-button|
   Move the actuator up or down over other actuators within the column.
Checkbox button
   When unchecked the actuator is deactivated, no action will be done. Very useful to check different logics without unlink or delete the actuator.
X button
   Deletes the actuator.
