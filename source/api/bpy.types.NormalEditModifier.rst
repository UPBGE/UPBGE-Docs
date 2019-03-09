NormalEditModifier(Modifier)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: NormalEditModifier(Modifier)

   Modifier affecting/generating custom normals

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: mix_factor

      How much of generated normals to mix with exiting ones

      :type: float in [0, 1], default 1.0

   .. attribute:: mix_limit

      Maximum angle between old and new normals

      :type: float in [0, 3.14159], default 1.0

   .. attribute:: mix_mode

      How to mix generated normals with existing ones

      * ``COPY`` Copy, Copy new normals (overwrite existing).
      * ``ADD`` Add, Copy sum of new and old normals.
      * ``SUB`` Subtract, Copy new normals minus old normals.
      * ``MUL`` Multiply, Copy product of old and new normals (\*not\* cross product).

      :type: enum in ['COPY', 'ADD', 'SUB', 'MUL'], default 'COPY'

   .. attribute:: mode

      How to affect (generate) normals

      * ``RADIAL`` Radial, From an ellipsoid (shape defined by the boundbox's dimensions, target is optional).
      * ``DIRECTIONAL`` Directional, Normals 'track' (point to) the target object.

      :type: enum in ['RADIAL', 'DIRECTIONAL'], default 'RADIAL'

   .. attribute:: offset

      Offset from object's center

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: target

      Target object used to affect normals

      :type: :class:`Object`

   .. attribute:: use_direction_parallel

      Use same direction for all normals, from origin to target's center (Directional mode only)

      :type: boolean, default True

   .. attribute:: vertex_group

      Vertex group name for selecting/weighting the affected areas

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

