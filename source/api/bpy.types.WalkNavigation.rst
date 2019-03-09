WalkNavigation(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: WalkNavigation(bpy_struct)

   Walk navigation settings

   .. attribute:: jump_height

      Maximum height of a jump

      :type: float in [0.1, 100], default 0.0

   .. attribute:: mouse_speed

      Speed factor for when looking around, high values mean faster mouse movement

      :type: float in [0.01, 10], default 0.0

   .. attribute:: teleport_time

      Interval of time warp when teleporting in navigation mode

      :type: float in [0, 10], default 0.0

   .. attribute:: use_gravity

      Walk with gravity, or free navigate

      :type: boolean, default False

   .. attribute:: use_mouse_reverse

      Reverse the vertical movement of the mouse

      :type: boolean, default False

   .. attribute:: view_height

      View distance from the floor when walking

      :type: float in [0, 1000], default 0.0

   .. attribute:: walk_speed

      Base speed for walking and flying

      :type: float in [0.01, 100], default 0.0

   .. attribute:: walk_speed_factor

      Multiplication factor when using the fast or slow modifiers

      :type: float in [0.01, 10], default 0.0

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

   * :class:`UserPreferencesInput.walk_navigation`

