.. |info-button| image:: /images/logic_bricks/logic-common-options-icons-info.png

.. |movement-button| image:: /images/logic_bricks/logic-common-options-icons-movement.png

.. _logic-properties:

==============================
Properties
==============================

Properties are the game logic equivalent to variables. They are stored with the object, and can be used to represent things about them such as ammo, health, name, and so on.

.. _game-engine-property-types:

.. _logic-properties-types:

Property Types
++++++++++++++++++++++++++++++

There are five types of properties:

Timer
   Starts at the property value and counts upwards as long as the object exists. It can for example be used if you want to know how long time it takes the player to complete a level.

   .. note::
      This timer uses the simulation time (or frame time) not the real time. When we have 60 fps both times are equal but in other circunstances not.

Float
   Uses decimal numbers as values, can range from -10000.000 to 10000.000. It is useful for precision values.

Integer
   Uses integers (whole numbers) as values, between -10000 and 10000. Useful for counting things such as ammunition, where decimals are unnecessary.

String
   Takes text as value. Can store 128 characters.

Boolean
   Boolean variable, has two values: ``TRUE`` or ``FALSE``. This is useful for things that have only two modes, like a light switch.

Using Properties
++++++++++++++++++++++++++++++

When a game is running, values of properties are set, manipulated, and evaluated using the :doc:`Property Sensor </manual/logic_bricks/sensors/types/property>` and the :doc:`Property Actuator </manual/logic_bricks/actuators/types/property>`.

Logic Properties are created and edited using the panel on the right (although it can be moved to the left with F5) of the Logic Bricks Editor panel. The top menu provides a list of the available property types.

.. figure:: /images/logic_bricks/logic-logic_properties-panel.png

   Properties Panel of the Logic Editor

Add Game Property button
   This button adds a new property to the list, default is a *Float* property named ``prop``, followed by a number if there already is one with this name.

Name field
   Where you give your property its name, this is how you are going to access it through Python or expressions. The way to do so in Python is by dictionary style look-up (``GameObject["propname"]``). The name is case sensitive.

Type menu
   This menu determines which type of property it is. The available options are in `Property Types`_.

Value field
   Sets the initial value of the property.

Information |info-button|
   Display property value in debug information. If debugging is turned on, the value of the property is given in the top left-hand corner of the screen while the game is running. To turn debugging on, tick the *Debug Properties* checkbox in the Game Debug panel of the Render Properties. All properties with debugging activated will then be presented with their object name, property name and value during gameplay. This is useful if you suspect something with your properties is causing problems.

Movement buttons |movement-button|
   Move the property up or down over other properties within the column.

X button
   Deletes the property.
