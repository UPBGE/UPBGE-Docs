.. _bpy.types.ArmatureSensor:

==============================
Armature Sensor
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_ArmatureSensor`.

The *Armature Sensor* is used to detect changes in values of an IK solver.

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-armature-armature.png

   Armature Sensor

.. note::
   The *Armature Sensor* is available for armature objects only.

Properties
++++++++++++++++++++++++++++++

Bone Name
   The bone to check for changes in value.

Constraint Name
   The bone constraint to check for changes in value.

Test
   How the sensor checks for changes in the bone.

   State Changed
      Any changes will invoke the sensor.
   Lin error below
      Any value below of the amount of residual error in Blender space unit for constraints that work on position will invoke the sensor.
   Lin error above
      Any value above of the amount of residual error in Blender space unit for constraints that work on position will invoke the sensor.
   Rot error below
      Any value below of the amount of residual error in radians for constraints that work on orientation will invoke the sensor.
   Rot error above
      Any value above of the amount of residual error in radians for constraints that work on orientation will invoke the sensor.
   Value
      Some tests will take a value, this value is used in the comparison when detecting changes.

Example
++++++++++++++++++++++++++++++
