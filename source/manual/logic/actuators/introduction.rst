
************
Introduction
************

Actuators perform actions, such as move, create objects, play a sound.
The actuators initiate their functions when they get a positive pulse from one (or more)
of their controllers.

The logic blocks for all types of actuator may be constructed and changed using
the Logic Editor; details of this process are given
in the :doc:`Actuator Editing </manual/logic/actuators/editing>` page.


.. _game-engine-logic-actuators-common-options:

Common Options
==============

.. figure:: /images/game-engine_logic_actuators_common-options_column3.png
   :width: 292px

   Common Actuator options.

All actuators have a set of common buttons, fields and menus. They are organized as follows:

Triangle button
   Collapses the sensor information to a single line (toggle).
Actuator type menu
   Specifies the type of the sensor.
Actuator name
   The name of the actuator. This can be selected by the user.
   It is used to access actuators with Python; it needs to be unique among the selected objects.
``X`` *Button*
   Deletes the actuator.
