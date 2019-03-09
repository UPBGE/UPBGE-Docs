UVWarpModifier(Modifier)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: UVWarpModifier(Modifier)

   Add target position to uv coordinates

   .. attribute:: axis_u

      Pole axis for rotation

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: axis_v

      Pole axis for rotation

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: bone_from

      Bone defining offset

      :type: string, default "", (never None)

   .. attribute:: bone_to

      Bone defining offset

      :type: string, default "", (never None)

   .. attribute:: center

      Center point for rotate/scale

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: object_from

      Object defining offset

      :type: :class:`Object`

   .. attribute:: object_to

      Object defining offset

      :type: :class:`Object`

   .. attribute:: uv_layer

      UV Layer name

      :type: string, default "", (never None)

   .. attribute:: vertex_group

      Vertex group name

      :type: string, default "", (never None)

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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

