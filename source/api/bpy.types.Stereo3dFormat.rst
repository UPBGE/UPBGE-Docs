Stereo3dFormat(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Stereo3dFormat(bpy_struct)

   Settings for stereo output

   .. attribute:: anaglyph_type

      :type: enum in ['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE'], default 'RED_CYAN'

   .. attribute:: display_mode

      * ``ANAGLYPH`` Anaglyph, Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).
      * ``INTERLACE`` Interlace, Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).
      * ``SIDEBYSIDE`` Side-by-Side, Render views for left and right eyes side-by-side.
      * ``TOPBOTTOM`` Top-Bottom, Render views for left and right eyes one above another.

      :type: enum in ['ANAGLYPH', 'INTERLACE', 'SIDEBYSIDE', 'TOPBOTTOM'], default 'ANAGLYPH'

   .. attribute:: interlace_type

      :type: enum in ['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED'], default 'ROW_INTERLEAVED'

   .. attribute:: use_interlace_swap

      Swap left and right stereo channels

      :type: boolean, default False

   .. attribute:: use_sidebyside_crosseyed

      Right eye should see left image and vice-versa

      :type: boolean, default False

   .. attribute:: use_squeezed_frame

      Combine both views in a squeezed image

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

   * :class:`Image.stereo_3d_format`
   * :class:`ImageSequence.stereo_3d_format`
   * :class:`MovieSequence.stereo_3d_format`
   * :class:`ImageFormatSettings.stereo_3d_format`
   * :class:`UILayout.template_image_stereo_3d`

