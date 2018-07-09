.. _bpy.types.RandomSensor:

*************
Random Sensor
*************

The *Random Sensor* generates random pulses.

.. figure:: /images/game-engine_logic_sensors_types_random_node.jpg
   :width: 300px

   Random sensor.


Properties
==========

See :ref:`Sensor Common Options <game-engine-logic-sensors-common-options>` for common options.

Seed
   This field to enter the initial seed for the random number algorithm.

.. note::

   0 is not random, but is useful for testing and debugging purposes.

.. note::

   If you run several times with the same Seed, the sequence of intervals you get
   will be the same for each run, although the intervals will be randomly distributed.


Example
=======
