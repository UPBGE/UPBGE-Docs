
Game Types (bge.types)
======================

.. module:: bge.types

************
Introduction
************

This module contains the classes that appear as instances in the Game Engine. A
script must interact with these classes if it is to affect the behaviour of
objects in a game.

The following example would move an object (i.e. an instance of
:class:`KX_GameObject`) one unit up.

.. code-block:: python

   # bge.types.SCA_PythonController
   cont = bge.logic.getCurrentController()

   # bge.types.KX_GameObject
   obj = cont.owner
   obj.worldPosition.z += 1

To run the code, it could be placed in a Blender text block and executed with
a :class:`SCA_PythonController` logic brick.

**********
Categories
**********

.. _bge-types-objects:

=======
Objects
=======

.. hlist::
   :columns: 3

   * :class:`BL_ArmatureObject`
   * :class:`KX_Camera`
   * :class:`KX_FontObject`
   * :class:`KX_GameObject`
   * :class:`KX_LightObject`
   * :class:`KX_NavMeshObject`

============
Logic Bricks
============

.. hlist::
   :columns: 3

   * :class:`SCA_ILogicBrick`

.. _bge-types-sensors:

-------
Sensors
-------

.. hlist::
   :columns: 3

   * :class:`SCA_ISensor`
   * :class:`KX_CollisionSensor`
   * :class:`KX_MouseFocusSensor`
   * :class:`KX_MovementSensor`
   * :class:`KX_NearSensor`
   * :class:`KX_NetworkMessageSensor`
   * :class:`KX_RadarSensor`
   * :class:`KX_RaySensor`
   * :class:`SCA_ActuatorSensor`
   * :class:`SCA_AlwaysSensor`
   * :class:`SCA_DelaySensor`
   * :class:`SCA_JoystickSensor`
   * :class:`SCA_KeyboardSensor`
   * :class:`SCA_MouseSensor`
   * :class:`SCA_PropertySensor`
   * :class:`SCA_RandomSensor`

.. _bge-types-controllers:

-----------
Controllers
-----------

.. hlist::
   :columns: 3

   * :class:`SCA_IController`
   * :class:`SCA_ANDController`
   * :class:`SCA_NANDController`
   * :class:`SCA_ORController`
   * :class:`SCA_NORController`
   * :class:`SCA_XORController`
   * :class:`SCA_XNORController`
   * :class:`SCA_PythonController`

.. _bge-types-actuators:

---------
Actuators
---------

.. hlist::
   :columns: 3
   
   * :class:`SCA_IActuator`
   * :class:`BL_ActionActuator`
   * :class:`BL_ArmatureActuator`
   * :class:`KX_CameraActuator`
   * :class:`KX_ConstraintActuator`
   * :class:`KX_GameActuator`
   * :class:`KX_MouseActuator`
   * :class:`KX_NetworkMessageActuator`
   * :class:`KX_ObjectActuator`
   * :class:`KX_ParentActuator`
   * :class:`KX_SCA_AddObjectActuator`
   * :class:`KX_SCA_DynamicActuator`
   * :class:`KX_SCA_EndObjectActuator`
   * :class:`KX_SCA_ReplaceMeshActuator`
   * :class:`KX_SceneActuator`
   * :class:`KX_SoundActuator`
   * :class:`KX_StateActuator`
   * :class:`KX_SteeringActuator`
   * :class:`KX_TrackToActuator`
   * :class:`KX_VisibilityActuator`
   * :class:`SCA_2DFilterActuator`
   * :class:`SCA_PropertyActuator`
   * :class:`SCA_RandomActuator`
   * :class:`SCA_VibrationActuator`

.. _bge-types-blender-data:

============
Blender Data
============

.. hlist::
   :columns: 3
   
   * :class:`BL_ArmatureBone`
   * :class:`BL_ArmatureChannel`
   * :class:`BL_ArmatureConstraint`
   * :class:`BL_Texture`
   * :class:`KX_BlenderMaterial`
   * :class:`KX_Mesh`
   * :class:`KX_Scene`
   * :class:`KX_WorldInfo`

.. _bge-types-upbge-data:

==========
UPBGE Data
==========

.. hlist::
   :columns: 3
   
   * :class:`BL_Shader`
   * :class:`EXP_ListValue`
   * :class:`EXP_PropValue`
   * :class:`EXP_PyObjectPlus`
   * :class:`EXP_Value`
   * :class:`KX_2DFilterManager`
   * :class:`KX_2DFilterOffScreen`
   * :class:`KX_2DFilter`
   * :class:`KX_BatchGroup`
   * :class:`KX_BoundingBox`
   * :class:`KX_CharacterWrapper`
   * :class:`KX_CollisionContactPoint`
   * :class:`KX_ConstraintWrapper`
   * :class:`KX_CubeMap`
   * :class:`KX_LibLoadStatus`
   * :class:`KX_LodLevel`
   * :class:`KX_LodManager`
   * :class:`KX_PlanarMap`
   * :class:`KX_PolyProxy`
   * :class:`KX_PythonComponent`
   * :class:`KX_TextureRenderer`
   * :class:`KX_VehicleWrapper`
   * :class:`SCA_IObject`
   * :class:`SCA_InputEvent`
   * :class:`SCA_PythonJoystick`
   * :class:`SCA_PythonKeyboard`
   * :class:`SCA_PythonMouse`

*****
Index
*****

.. toctree::

   bge.types.BL_ActionActuator
   bge.types.BL_ArmatureActuator
   bge.types.BL_ArmatureBone
   bge.types.BL_ArmatureChannel
   bge.types.BL_ArmatureConstraint
   bge.types.BL_ArmatureObject
   bge.types.BL_Shader
   bge.types.BL_Texture
   bge.types.EXP_ListValue
   bge.types.EXP_PropValue
   bge.types.EXP_PyObjectPlus
   bge.types.EXP_Value
   bge.types.KX_2DFilter
   bge.types.KX_2DFilterManager
   bge.types.KX_2DFilterOffScreen
   bge.types.KX_ArmatureSensor
   bge.types.KX_BatchGroup
   bge.types.KX_BlenderMaterial
   bge.types.KX_BoundingBox
   bge.types.KX_Camera
   bge.types.KX_CameraActuator
   bge.types.KX_CharacterWrapper
   bge.types.KX_CollisionContactPoint
   bge.types.KX_CollisionSensor
   bge.types.KX_ConstraintActuator
   bge.types.KX_ConstraintWrapper
   bge.types.KX_CubeMap
   bge.types.KX_FontObject
   bge.types.KX_GameActuator
   bge.types.KX_GameObject
   bge.types.KX_LibLoadStatus
   bge.types.KX_LightObject
   bge.types.KX_LodLevel
   bge.types.KX_LodManager
   bge.types.KX_Mesh
   bge.types.KX_MouseActuator
   bge.types.KX_MouseFocusSensor
   bge.types.KX_MovementSensor
   bge.types.KX_NavMeshObject
   bge.types.KX_NearSensor
   bge.types.KX_NetworkMessageActuator
   bge.types.KX_NetworkMessageSensor
   bge.types.KX_ObjectActuator
   bge.types.KX_ParentActuator
   bge.types.KX_PlanarMap
   bge.types.KX_PolyProxy
   bge.types.KX_PythonComponent
   bge.types.KX_RadarSensor
   bge.types.KX_RaySensor
   bge.types.KX_SCA_AddObjectActuator
   bge.types.KX_SCA_DynamicActuator
   bge.types.KX_SCA_EndObjectActuator
   bge.types.KX_SCA_ReplaceMeshActuator
   bge.types.KX_Scene
   bge.types.KX_SceneActuator
   bge.types.KX_SoundActuator
   bge.types.KX_StateActuator
   bge.types.KX_SteeringActuator
   bge.types.KX_TextureRenderer
   bge.types.KX_TrackToActuator
   bge.types.KX_VehicleWrapper
   bge.types.KX_VertexProxy
   bge.types.KX_VisibilityActuator
   bge.types.KX_WorldInfo
   bge.types.SCA_2DFilterActuator
   bge.types.SCA_ActuatorSensor
   bge.types.SCA_AlwaysSensor
   bge.types.SCA_ANDController
   bge.types.SCA_DelaySensor
   bge.types.SCA_IActuator
   bge.types.SCA_IController
   bge.types.SCA_ILogicBrick
   bge.types.SCA_InputEvent
   bge.types.SCA_IObject
   bge.types.SCA_ISensor
   bge.types.SCA_JoystickSensor
   bge.types.SCA_KeyboardSensor
   bge.types.SCA_MouseSensor
   bge.types.SCA_NANDController
   bge.types.SCA_NORController
   bge.types.SCA_ORController
   bge.types.SCA_PropertyActuator
   bge.types.SCA_PropertySensor
   bge.types.SCA_PythonController
   bge.types.SCA_PythonJoystick
   bge.types.SCA_PythonKeyboard
   bge.types.SCA_PythonMouse
   bge.types.SCA_RandomActuator
   bge.types.SCA_RandomSensor
   bge.types.SCA_VibrationActuator
   bge.types.SCA_XNORController
   bge.types.SCA_XORController

