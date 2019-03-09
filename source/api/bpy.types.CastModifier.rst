CastModifier(Modifier)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: CastModifier(Modifier)

   Modifier to cast to other shapes

   .. attribute:: cast_type

      Target object shape

      :type: enum in ['SPHERE', 'CYLINDER', 'CUBOID'], default 'SPHERE'

   .. attribute:: factor

      :type: float in [-inf, inf], default 0.0

   .. attribute:: object

      Control object: if available, its location determines the center of the effect

      :type: :class:`Object`

   .. attribute:: radius

      Only deform vertices within this distance from the center of the effect (leave as 0 for infinite.)

      :type: float in [0, inf], default 0.0

   .. attribute:: size

      Size of projection shape (leave as 0 for auto)

      :type: float in [0, inf], default 0.0

   .. attribute:: use_radius_as_size

      Use radius as size of projection shape (0 = auto)

      :type: boolean, default False

   .. attribute:: use_transform

      Use object transform to control projection shape

      :type: boolean, default False

   .. attribute:: use_x

      :type: boolean, default False

   .. attribute:: use_y

      :type: boolean, default False

   .. attribute:: use_z

      :type: boolean, default False

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

