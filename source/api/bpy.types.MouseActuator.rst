MouseActuator(Actuator)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: MouseActuator(Actuator)

   

   .. attribute:: local_x

      Apply rotation locally

      :type: boolean, default False

   .. attribute:: local_y

      Apply rotation locally

      :type: boolean, default False

   .. attribute:: max_x

      Maximum positive rotation allowed by X mouse movement (0 for infinite)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: max_y

      Maximum positive rotation allowed by Y mouse movement (0 for infinite)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: min_x

      Maximum negative rotation allowed by X mouse movement (0 for infinite)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: min_y

      Maximum negative rotation allowed by Y mouse movement (0 for infinite)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: mode

      :type: enum in ['VISIBILITY', 'LOOK'], default 'VISIBILITY'

   .. attribute:: object_axis_x

      Local object axis mouse movement in the X direction will apply to

      :type: enum in ['OBJECT_AXIS_X', 'OBJECT_AXIS_Y', 'OBJECT_AXIS_Z'], default 'OBJECT_AXIS_X'

   .. attribute:: object_axis_y

      Local object axis mouse movement in the Y direction will apply to

      :type: enum in ['OBJECT_AXIS_X', 'OBJECT_AXIS_Y', 'OBJECT_AXIS_Z'], default 'OBJECT_AXIS_X'

   .. attribute:: reset_x

      Reset the cursor's X position to the center of the screen space after calculating

      :type: boolean, default False

   .. attribute:: reset_y

      Reset the cursor's Y position to the center of the screen space after calculating

      :type: boolean, default False

   .. attribute:: sensitivity_x

      Sensitivity of the X axis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: sensitivity_y

      Sensitivity of the Y axis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: threshold_x

      Amount of X motion before mouse movement will register

      :type: float in [-inf, inf], default 0.0

   .. attribute:: threshold_y

      Amount of Y motion before mouse movement will register

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use_axis_x

      Calculate mouse movement on the X axis

      :type: boolean, default False

   .. attribute:: use_axis_y

      Calculate mouse movement on the Y axis

      :type: boolean, default False

   .. attribute:: visible

      Make mouse cursor visible

      :type: boolean, default False

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

