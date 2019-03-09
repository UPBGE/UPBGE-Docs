ControlFluidSettings(FluidSettings)
===================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`FluidSettings`

.. class:: ControlFluidSettings(FluidSettings)

   Fluid simulation settings for objects controlling the motion of fluid in the simulation

   .. attribute:: attraction_radius

      Force field radius around the control object

      :type: float in [0, 10], default 0.0

   .. attribute:: attraction_strength

      Force strength for directional attraction towards the control object

      :type: float in [-10, 10], default 0.0

   .. attribute:: end_time

      Time when the control particles are deactivated

      :type: float in [0, inf], default 0.0

   .. attribute:: quality

      Quality which is used for object sampling (higher = better but slower)

      :type: float in [5, 100], default 0.0

   .. attribute:: start_time

      Time when the control particles are activated

      :type: float in [0, inf], default 0.0

   .. attribute:: use

      Object contributes to the fluid simulation

      :type: boolean, default False

   .. attribute:: use_reverse_frames

      Reverse control object movement

      :type: boolean, default False

   .. attribute:: velocity_radius

      Force field radius around the control object

      :type: float in [0, 10], default 0.0

   .. attribute:: velocity_strength

      Force strength of how much of the control object's velocity is influencing the fluid velocity

      :type: float in [0, 10], default 0.0

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
   * :class:`FluidSettings.type`

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

