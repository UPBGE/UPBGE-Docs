MaterialStrand(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialStrand(bpy_struct)

   Strand settings for a Material data-block

   .. attribute:: blend_distance

      Worldspace distance over which to blend in the surface normal

      :type: float in [0, 10], default 0.0

   .. attribute:: root_size

      Start size of strands in pixels or Blender units

      :type: float in [0, inf], default 0.0

   .. attribute:: shape

      Positive values make strands rounder, negative ones make strands spiky

      :type: float in [-0.9, 0.9], default 0.0

   .. attribute:: size_min

      Minimum size of strands in pixels

      :type: float in [0.001, 10], default 0.0

   .. attribute:: tip_size

      End size of strands in pixels or Blender units

      :type: float in [0, inf], default 0.0

   .. attribute:: use_blender_units

      Use Blender units for widths instead of pixels

      :type: boolean, default False

   .. data:: use_surface_diffuse

      Make diffuse shading more similar to shading the surface

      :type: boolean, default False, (readonly)

   .. attribute:: use_tangent_shading

      Use direction of strands as normal for tangent-shading

      :type: boolean, default False

   .. attribute:: uv_layer

      Name of UV map to override

      :type: string, default "", (never None)

   .. attribute:: width_fade

      Transparency along the width of the strand

      :type: float in [0, 2], default 0.0

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

   * :class:`Material.strand`

