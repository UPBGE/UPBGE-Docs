Scopes(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Scopes(bpy_struct)

   Scopes for statistical view of an image

   .. attribute:: accuracy

      Proportion of original image source pixel lines to sample

      :type: float in [0, 100], default 0.0

   .. data:: histogram

      Histogram for viewing image statistics

      :type: :class:`Histogram`, (readonly)

   .. attribute:: use_full_resolution

      Sample every pixel of the image

      :type: boolean, default False

   .. attribute:: vectorscope_alpha

      Opacity of the points

      :type: float in [0, 1], default 0.0

   .. attribute:: waveform_alpha

      Opacity of the points

      :type: float in [0, 1], default 0.0

   .. attribute:: waveform_mode

      :type: enum in ['LUMA', 'PARADE', 'YCBCR601', 'YCBCR709', 'YCBCRJPG', 'RGB'], default 'LUMA'

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

   * :class:`SpaceImageEditor.scopes`

