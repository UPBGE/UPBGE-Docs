MaterialHalo(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialHalo(bpy_struct)

   Halo particle effect settings for a Material data-block

   .. attribute:: add

      Strength of the add effect

      :type: float in [0, 1], default 0.0

   .. attribute:: flare_boost

      Give the flare extra strength

      :type: float in [0.1, 10], default 0.0

   .. attribute:: flare_seed

      Offset in the flare seed table

      :type: int in [0, 255], default 0

   .. attribute:: flare_size

      Factor by which the flare is larger than the halo

      :type: float in [0.1, 25], default 0.0

   .. attribute:: flare_subflare_count

      Number of sub-flares

      :type: int in [1, 32], default 0

   .. attribute:: flare_subflare_size

      Dimension of the sub-flares, dots and circles

      :type: float in [0.1, 25], default 0.0

   .. attribute:: hardness

      Hardness of the halo

      :type: int in [0, 127], default 0

   .. attribute:: line_count

      Number of star shaped lines rendered over the halo

      :type: int in [0, 250], default 0

   .. attribute:: ring_count

      Number of rings rendered over the halo

      :type: int in [0, 24], default 0

   .. attribute:: seed

      Randomize ring dimension and line location

      :type: int in [0, 255], default 0

   .. attribute:: size

      Dimension of the halo

      :type: float in [0, 100], default 0.0

   .. attribute:: star_tip_count

      Number of points on the star shaped halo

      :type: int in [3, 50], default 0

   .. attribute:: use_extreme_alpha

      Use extreme alpha

      :type: boolean, default False

   .. attribute:: use_flare_mode

      Render halo as a lens flare

      :type: boolean, default False

   .. attribute:: use_lines

      Render star shaped lines over halo

      :type: boolean, default False

   .. attribute:: use_ring

      Render rings over halo

      :type: boolean, default False

   .. attribute:: use_shaded

      Let halo receive light and shadows from external objects

      :type: boolean, default False

   .. attribute:: use_soft

      Soften the edges of halos at intersections with other geometry

      :type: boolean, default False

   .. attribute:: use_star

      Render halo as a star

      :type: boolean, default False

   .. attribute:: use_texture

      Give halo a texture

      :type: boolean, default False

   .. attribute:: use_vertex_normal

      Use the vertex normal to specify the dimension of the halo

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

   * :class:`Material.halo`

