SolidifyModifier(Modifier)
==========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SolidifyModifier(Modifier)

   Create a solid skin by extruding, compensating for sharp angles

   .. attribute:: edge_crease_inner

      Assign a crease to inner edges

      :type: float in [0, 1], default 0.0

   .. attribute:: edge_crease_outer

      Assign a crease to outer edges

      :type: float in [0, 1], default 0.0

   .. attribute:: edge_crease_rim

      Assign a crease to the edges making up the rim

      :type: float in [0, 1], default 0.0

   .. attribute:: invert_vertex_group

      Invert the vertex group influence

      :type: boolean, default False

   .. attribute:: material_offset

      Offset material index of generated faces

      :type: int in [-32768, 32767], default 0

   .. attribute:: material_offset_rim

      Offset material index of generated rim faces

      :type: int in [-32768, 32767], default 0

   .. attribute:: offset

      Offset the thickness from the center

      :type: float in [-inf, inf], default 0.0

   .. attribute:: thickness

      Thickness of the shell

      :type: float in [-inf, inf], default 0.0

   .. attribute:: thickness_clamp

      Offset clamp based on geometry scale

      :type: float in [0, 100], default 0.0

   .. attribute:: thickness_vertex_group

      Thickness factor to use for zero vertex group influence

      :type: float in [0, 1], default 0.0

   .. attribute:: use_even_offset

      Maintain thickness by adjusting for sharp corners (slow, disable when not needed)

      :type: boolean, default False

   .. attribute:: use_flip_normals

      Invert the face direction

      :type: boolean, default False

   .. attribute:: use_quality_normals

      Calculate normals which result in more even thickness (slow, disable when not needed)

      :type: boolean, default False

   .. attribute:: use_rim

      Create edge loops between the inner and outer surfaces on face edges (slow, disable when not needed)

      :type: boolean, default False

   .. attribute:: use_rim_only

      Only add the rim to the original data

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

