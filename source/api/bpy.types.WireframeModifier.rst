WireframeModifier(Modifier)
===========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: WireframeModifier(Modifier)

   Wireframe effect modifier

   .. attribute:: crease_weight

      Crease weight (if active)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: material_offset

      Offset material index of generated faces

      :type: int in [-32768, 32767], default 0

   .. attribute:: offset

      Offset the thickness from the center

      :type: float in [-inf, inf], default 0.0

   .. attribute:: thickness

      Thickness factor

      :type: float in [-inf, inf], default 0.0

   .. attribute:: thickness_vertex_group

      Thickness factor to use for zero vertex group influence

      :type: float in [0, 1], default 0.0

   .. attribute:: use_boundary

      Support face boundaries

      :type: boolean, default False

   .. attribute:: use_crease

      Crease hub edges for improved subsurf

      :type: boolean, default False

   .. attribute:: use_even_offset

      Scale the offset to give more even thickness

      :type: boolean, default False

   .. attribute:: use_relative_offset

      Scale the offset by surrounding geometry

      :type: boolean, default False

   .. attribute:: use_replace

      Remove original geometry

      :type: boolean, default False

   .. attribute:: vertex_group

      Vertex group name for selecting the affected areas

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

