Actuator(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ActionActuator`, :class:`ArmatureActuator`, :class:`CameraActuator`, :class:`ConstraintActuator`, :class:`EditObjectActuator`, :class:`Filter2DActuator`, :class:`GameActuator`, :class:`MessageActuator`, :class:`MouseActuator`, :class:`ObjectActuator`, :class:`ParentActuator`, :class:`PropertyActuator`, :class:`RandomActuator`, :class:`SceneActuator`, :class:`SoundActuator`, :class:`StateActuator`, :class:`SteeringActuator`, :class:`VibrationActuator`, :class:`VisibilityActuator`

.. class:: Actuator(bpy_struct)

   Actuator to apply actions in the game engine

   .. attribute:: active

      Set the active state of the actuator

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: pin

      Display when not linked to a visible states controller

      :type: boolean, default False

   .. attribute:: show_expanded

      Set actuator expanded in the user interface

      :type: boolean, default False

   .. attribute:: type

      :type: enum in ['ACTION', 'ARMATURE', 'CAMERA', 'CONSTRAINT', 'EDIT_OBJECT', 'FILTER_2D', 'GAME', 'MESSAGE', 'MOTION', 'MOUSE', 'PARENT', 'PROPERTY', 'RANDOM', 'SCENE', 'SOUND', 'STATE', 'STEERING', 'VIBRATION', 'VISIBILITY'], default 'MOTION'

   .. method:: link(controller)

      Link the actuator to a controller

      :arg controller:

         Controller to link to

      :type controller: :class:`Controller`

   .. method:: unlink(controller)

      Unlink the actuator from a controller

      :arg controller:

         Controller to unlink from

      :type controller: :class:`Controller`

   .. classmethod:: bl_rna_get_subclass(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The class or default when not found.
      :rtype: type


.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

.. rubric:: Inherited Functions

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`Controller.actuators`
   * :class:`Controller.link`
   * :class:`Controller.unlink`
   * :class:`GameObjectSettings.actuators`

