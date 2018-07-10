
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

*****
Types
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

