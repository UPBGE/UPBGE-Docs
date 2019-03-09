CameraActuator(Actuator)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: CameraActuator(Actuator)

   

   .. attribute:: axis

      Axis the Camera will try to get behind

      * ``POS_X`` +X, Camera tries to get behind the X axis.
      * ``POS_Y`` +Y, Camera tries to get behind the Y axis.
      * ``NEG_X`` -X, Camera tries to get behind the -X axis.
      * ``NEG_Y`` -Y, Camera tries to get behind the -Y axis.

      :type: enum in ['POS_X', 'POS_Y', 'NEG_X', 'NEG_Y'], default 'POS_X'

   .. attribute:: damping

      Strength of the constraint that drives the camera behind the target

      :type: float in [0, 10], default 0.0

   .. attribute:: height

      :type: float in [-inf, inf], default 0.0

   .. attribute:: max

      :type: float in [-inf, inf], default 0.0

   .. attribute:: min

      :type: float in [-inf, inf], default 0.0

   .. attribute:: object

      Look at this Object

      :type: :class:`Object`

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
   * :class:`Actuator.name`
   * :class:`Actuator.type`
   * :class:`Actuator.pin`
   * :class:`Actuator.show_expanded`
   * :class:`Actuator.active`

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
   * :class:`Actuator.link`
   * :class:`Actuator.unlink`

