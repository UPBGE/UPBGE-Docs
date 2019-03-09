SpaceSequenceEditor(Space)
==========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceSequenceEditor(Space)

   Sequence editor space data

   .. attribute:: display_channel

      The channel number shown in the image preview. 0 is the result of all strips combined

      :type: int in [-5, 32], default 0

   .. attribute:: display_mode

      View mode to use for displaying sequencer output

      :type: enum in ['IMAGE', 'WAVEFORM', 'VECTOR_SCOPE', 'HISTOGRAM'], default 'IMAGE'

   .. attribute:: draw_overexposed

      Show overexposed areas with zebra stripes

      :type: int in [0, 110], default 0

   .. attribute:: grease_pencil

      Grease pencil data for this space

      :type: :class:`GreasePencil`

   .. attribute:: overlay_type

      Overlay draw type

      * ``RECTANGLE`` Rectangle, Show rectangle area overlay.
      * ``REFERENCE`` Reference, Show reference frame only.
      * ``CURRENT`` Current, Show current frame only.

      :type: enum in ['RECTANGLE', 'REFERENCE', 'CURRENT'], default 'RECTANGLE'

   .. attribute:: preview_channels

      Channels of the preview to draw

      * ``COLOR_ALPHA`` Color and Alpha, Draw image with RGB colors and alpha transparency.
      * ``COLOR`` Color, Draw image with RGB colors.

      :type: enum in ['COLOR_ALPHA', 'COLOR'], default 'COLOR'

   .. attribute:: proxy_render_size

      Draw preview using full resolution or different proxy resolutions

      :type: enum in ['NONE', 'SCENE', 'PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100', 'FULL'], default 'SCENE'

   .. attribute:: show_backdrop

      Display result under strips

      :type: boolean, default False

   .. attribute:: show_frame_indicator

      Show frame number beside the current frame indicator line

      :type: boolean, default False

   .. attribute:: show_frames

      Draw frames rather than seconds

      :type: boolean, default False

   .. attribute:: show_grease_pencil

      Show grease pencil for this view

      :type: boolean, default False

   .. attribute:: show_metadata

      Show metadata of first visible strip

      :type: boolean, default False

   .. attribute:: show_safe_areas

      Show TV title safe and action safe areas in preview

      :type: boolean, default False

   .. attribute:: show_safe_center

      Show safe areas to fit content in a different aspect ratio

      :type: boolean, default False

   .. attribute:: show_seconds

      Show timing in seconds not frames

      :type: boolean, default False

   .. attribute:: show_separate_color

      Separate color channels in preview

      :type: boolean, default False

   .. attribute:: show_strip_offset

      Display strip in/out offsets

      :type: boolean, default False

   .. attribute:: use_marker_sync

      Transform markers as well as strips

      :type: boolean, default False

   .. attribute:: view_type

      Type of the Sequencer view (sequencer, preview or both)

      :type: enum in ['SEQUENCER', 'PREVIEW', 'SEQUENCER_PREVIEW'], default 'SEQUENCER'

   .. attribute:: waveform_draw_type

      How Waveforms are drawn

      * ``NO_WAVEFORMS`` Waveforms Off, No waveforms drawn for any sound strips.
      * ``ALL_WAVEFORMS`` Waveforms On, Waveforms drawn for all sound strips.
      * ``DEFAULT_WAVEFORMS`` Use Strip Option, Waveforms drawn according to strip setting.

      :type: enum in ['NO_WAVEFORMS', 'ALL_WAVEFORMS', 'DEFAULT_WAVEFORMS'], default 'DEFAULT_WAVEFORMS'

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

