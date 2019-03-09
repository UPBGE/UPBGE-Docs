SpaceImageEditor(Space)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceImageEditor(Space)

   Image and UV editor space data

   .. attribute:: cursor_location

      2D cursor location for this view

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: draw_channels

      Channels of the image to draw

      * ``COLOR_ALPHA`` Color and Alpha, Draw image with RGB colors and alpha transparency.
      * ``COLOR`` Color, Draw image with RGB colors.
      * ``ALPHA`` Alpha, Draw alpha transparency channel.
      * ``Z_BUFFER`` Z-Buffer, Draw Z-buffer associated with image (mapped from camera clip start to end).
      * ``RED`` Red.
      * ``GREEN`` Green.
      * ``BLUE`` Blue.

      :type: enum in ['COLOR_ALPHA', 'COLOR', 'ALPHA', 'Z_BUFFER', 'RED', 'GREEN', 'BLUE'], default 'COLOR'

   .. attribute:: grease_pencil

      Grease pencil data for this space

      :type: :class:`GreasePencil`

   .. attribute:: image

      Image displayed and edited in this space

      :type: :class:`Image`

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly, never None)

   .. attribute:: mask

      Mask displayed and edited in this space

      :type: :class:`Mask`

   .. attribute:: mask_draw_type

      Draw type for mask splines

      * ``OUTLINE`` Outline, Draw white edges with black outline.
      * ``DASH`` Dash, Draw dashed black-white edges.
      * ``BLACK`` Black, Draw black edges.
      * ``WHITE`` White, Draw white edges.

      :type: enum in ['OUTLINE', 'DASH', 'BLACK', 'WHITE'], default 'OUTLINE'

   .. attribute:: mask_overlay_mode

      Overlay mode of rasterized mask

      * ``ALPHACHANNEL`` Alpha Channel, Show alpha channel of the mask.
      * ``COMBINED`` Combined, Combine space background image with the mask.

      :type: enum in ['ALPHACHANNEL', 'COMBINED'], default 'ALPHACHANNEL'

   .. attribute:: mode

      Editing context being displayed

      * ``VIEW`` View, View the image and UV edit in mesh editmode.
      * ``PAINT`` Paint, 2D image painting mode.
      * ``MASK`` Mask, Mask editing.

      :type: enum in ['VIEW', 'PAINT', 'MASK'], default 'VIEW'

   .. attribute:: pivot_point

      Rotation/Scaling Pivot

      * ``BOUNDING_BOX_CENTER`` Bounding Box Center, Pivot around bounding box center of selected object(s).
      * ``CURSOR`` 3D Cursor, Pivot around the 3D cursor.
      * ``INDIVIDUAL_ORIGINS`` Individual Origins, Pivot around each object's own origin.
      * ``MEDIAN_POINT`` Median Point, Pivot around the median point of selected objects.
      * ``ACTIVE_ELEMENT`` Active Element, Pivot around active object.

      :type: enum in ['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT'], default 'BOUNDING_BOX_CENTER'

   .. data:: sample_histogram

      Sampled colors along line

      :type: :class:`Histogram`, (readonly)

   .. data:: scopes

      Scopes to visualize image statistics

      :type: :class:`Scopes`, (readonly)

   .. attribute:: show_grease_pencil

      Show grease pencil for this view

      :type: boolean, default False

   .. attribute:: show_mask_overlay

      :type: boolean, default False

   .. attribute:: show_mask_smooth

      :type: boolean, default False

   .. data:: show_maskedit

      Show Mask editing related properties

      :type: boolean, default False, (readonly)

   .. data:: show_paint

      Show paint related properties

      :type: boolean, default False, (readonly)

   .. data:: show_render

      Show render related properties

      :type: boolean, default False, (readonly)

   .. attribute:: show_repeat

      Draw the image repeated outside of the main view

      :type: boolean, default False

   .. attribute:: show_stereo_3d

      Display the image in Stereo 3D

      :type: boolean, default False

   .. data:: show_uvedit

      Show UV editing related properties

      :type: boolean, default False, (readonly)

   .. attribute:: use_image_pin

      Display current image regardless of object selection

      :type: boolean, default False

   .. attribute:: use_realtime_update

      Update other affected window spaces automatically to reflect changes during interactive operations such as transform

      :type: boolean, default False

   .. data:: uv_editor

      UV editor settings

      :type: :class:`SpaceUVEditor`, (readonly, never None)

   .. data:: zoom

      Zoom factor

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0), (readonly)

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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

