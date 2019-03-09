MirrorModifier(Modifier)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: MirrorModifier(Modifier)

   Mirroring modifier

   .. attribute:: merge_threshold

      Distance within which mirrored vertices are merged

      :type: float in [0, inf], default 0.0

   .. attribute:: mirror_object

      Object to use as mirror

      :type: :class:`Object`

   .. attribute:: mirror_offset_u

      Amount to offset mirrored UVs flipping point from the 0.5 on the U axis

      :type: float in [-1, 1], default 0.0

   .. attribute:: mirror_offset_v

      Amount to offset mirrored UVs flipping point from the 0.5 point on the V axis

      :type: float in [-1, 1], default 0.0

   .. attribute:: offset_u

      Mirrored UV offset on the U axis

      :type: float in [-10000, 10000], default 0.0

   .. attribute:: offset_v

      Mirrored UV offset on the V axis

      :type: float in [-10000, 10000], default 0.0

   .. attribute:: use_clip

      Prevent vertices from going through the mirror during transform

      :type: boolean, default False

   .. attribute:: use_mirror_merge

      Merge vertices within the merge threshold

      :type: boolean, default False

   .. attribute:: use_mirror_u

      Mirror the U texture coordinate around the flip offset point

      :type: boolean, default False

   .. attribute:: use_mirror_v

      Mirror the V texture coordinate around the flip offset point

      :type: boolean, default False

   .. attribute:: use_mirror_vertex_groups

      Mirror vertex groups (e.g. .R->.L)

      :type: boolean, default False

   .. attribute:: use_x

      Enable X axis mirror

      :type: boolean, default False

   .. attribute:: use_y

      Enable Y axis mirror

      :type: boolean, default False

   .. attribute:: use_z

      Enable Z axis mirror

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

