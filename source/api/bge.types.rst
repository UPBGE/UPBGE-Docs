
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

   bge_types/bge.types.BL_ActionActuator
   bge_types/bge.types.BL_ArmatureActuator
   bge_types/bge.types.BL_ArmatureBone
   bge_types/bge.types.BL_ArmatureChannel
   bge_types/bge.types.BL_ArmatureConstraint
   bge_types/bge.types.BL_ArmatureObject
   bge_types/bge.types.BL_Shader
   bge_types/bge.types.BL_Texture
   bge_types/bge.types.EXP_ListValue
   bge_types/bge.types.EXP_PropValue
   bge_types/bge.types.EXP_PyObjectPlus
   bge_types/bge.types.EXP_Value
   bge_types/bge.types.KX_2DFilter
   bge_types/bge.types.KX_2DFilterManager
   bge_types/bge.types.KX_2DFilterOffScreen
   bge_types/bge.types.KX_ArmatureSensor
   bge_types/bge.types.KX_BatchGroup
   bge_types/bge.types.KX_BlenderMaterial
   bge_types/bge.types.KX_BoundingBox
   bge_types/bge.types.KX_Camera
   bge_types/bge.types.KX_CameraActuator
   bge_types/bge.types.KX_CharacterWrapper
   bge_types/bge.types.KX_CollisionContactPoint
   bge_types/bge.types.KX_CollisionSensor
   bge_types/bge.types.KX_ConstraintActuator
   bge_types/bge.types.KX_ConstraintWrapper
   bge_types/bge.types.KX_CubeMap
   bge_types/bge.types.KX_FontObject
   bge_types/bge.types.KX_GameActuator
   bge_types/bge.types.KX_GameObject
   bge_types/bge.types.KX_LibLoadStatus
   bge_types/bge.types.KX_LightObject
   bge_types/bge.types.KX_LodLevel
   bge_types/bge.types.KX_LodManager
   bge_types/bge.types.KX_Mesh
   bge_types/bge.types.KX_MouseActuator
   bge_types/bge.types.KX_MouseFocusSensor
   bge_types/bge.types.KX_NavMeshObject
   bge_types/bge.types.KX_NearSensor
   bge_types/bge.types.KX_NetworkMessageActuator
   bge_types/bge.types.KX_NetworkMessageSensor
   bge_types/bge.types.KX_ObjectActuator
   bge_types/bge.types.KX_ParentActuator
   bge_types/bge.types.KX_PlanarMap
   bge_types/bge.types.KX_PolyProxy
   bge_types/bge.types.KX_PythonComponent
   bge_types/bge.types.KX_RadarSensor
   bge_types/bge.types.KX_RaySensor
   bge_types/bge.types.KX_SCA_AddObjectActuator
   bge_types/bge.types.KX_SCA_DynamicActuator
   bge_types/bge.types.KX_SCA_EndObjectActuator
   bge_types/bge.types.KX_SCA_ReplaceMeshActuator
   bge_types/bge.types.KX_Scene
   bge_types/bge.types.KX_SceneActuator
   bge_types/bge.types.KX_SoundActuator
   bge_types/bge.types.KX_StateActuator
   bge_types/bge.types.KX_SteeringActuator
   bge_types/bge.types.KX_TextureRenderer
   bge_types/bge.types.KX_TrackToActuator
   bge_types/bge.types.KX_VehicleWrapper
   bge_types/bge.types.KX_VertexProxy
   bge_types/bge.types.KX_VisibilityActuator
   bge_types/bge.types.KX_WorldInfo
   bge_types/bge.types.SCA_2DFilterActuator
   bge_types/bge.types.SCA_ActuatorSensor
   bge_types/bge.types.SCA_AlwaysSensor
   bge_types/bge.types.SCA_ANDController
   bge_types/bge.types.SCA_DelaySensor
   bge_types/bge.types.SCA_IActuator
   bge_types/bge.types.SCA_IController
   bge_types/bge.types.SCA_ILogicBrick
   bge_types/bge.types.SCA_InputEvent
   bge_types/bge.types.SCA_IObject
   bge_types/bge.types.SCA_ISensor
   bge_types/bge.types.SCA_JoystickSensor
   bge_types/bge.types.SCA_KeyboardSensor
   bge_types/bge.types.SCA_MouseSensor
   bge_types/bge.types.SCA_NANDController
   bge_types/bge.types.SCA_NORController
   bge_types/bge.types.SCA_ORController
   bge_types/bge.types.SCA_PropertyActuator
   bge_types/bge.types.SCA_PropertySensor
   bge_types/bge.types.SCA_PythonController
   bge_types/bge.types.SCA_PythonJoystick
   bge_types/bge.types.SCA_PythonKeyboard
   bge_types/bge.types.SCA_PythonMouse
   bge_types/bge.types.SCA_RandomActuator
   bge_types/bge.types.SCA_RandomSensor
   bge_types/bge.types.SCA_VibrationActuator
   bge_types/bge.types.SCA_XNORController
   bge_types/bge.types.SCA_XORController

