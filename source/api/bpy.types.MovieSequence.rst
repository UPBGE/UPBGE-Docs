MovieSequence(Sequence)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sequence`

.. class:: MovieSequence(Sequence)

   Sequence strip to load a video

   .. attribute:: alpha_mode

      Representation of alpha information in the RGBA pixels

      * ``STRAIGHT`` Straight, RGB channels in transparent pixels are unaffected by the alpha channel.
      * ``PREMUL`` Premultiplied, RGB channels in transparent pixels are multiplied by the alpha channel.

      :type: enum in ['STRAIGHT', 'PREMUL'], default 'STRAIGHT'

   .. attribute:: animation_offset_end

      Animation end offset (trim end)

      :type: int in [0, inf], default 0

   .. attribute:: animation_offset_start

      Animation start offset (trim start)

      :type: int in [0, inf], default 0

   .. attribute:: color_multiply

      :type: float in [0, 20], default 1.0

   .. attribute:: color_saturation

      Adjust the intensity of the input's color

      :type: float in [0, 20], default 1.0

   .. data:: colorspace_settings

      Input color space settings

      :type: :class:`ColorManagedInputColorspaceSettings`, (readonly)

   .. data:: crop

      :type: :class:`SequenceCrop`, (readonly)

   .. data:: elements

      :type: :class:`bpy_prop_collection` of :class:`SequenceElement`, (readonly)

   .. attribute:: filepath

      :type: string, default "", (never None)

   .. attribute:: mpeg_preseek

      For MPEG movies, preseek this many frames

      :type: int in [0, 50], default 0

   .. data:: proxy

      :type: :class:`SequenceProxy`, (readonly)

   .. data:: stereo_3d_format

      Settings for stereo 3d

      :type: :class:`Stereo3dFormat`, (readonly, never None)

   .. attribute:: stream_index

      For files with several movie streams, use the stream with the given index

      :type: int in [0, 20], default 0

   .. attribute:: strobe

      Only display every nth frame

      :type: float in [1, 30], default 0.0

   .. data:: transform

      :type: :class:`SequenceTransform`, (readonly)

   .. attribute:: use_crop

      Crop image before processing

      :type: boolean, default False

   .. attribute:: use_deinterlace

      Remove fields from video movies

      :type: boolean, default False

   .. attribute:: use_flip_x

      Flip on the X axis

      :type: boolean, default False

   .. attribute:: use_flip_y

      Flip on the Y axis

      :type: boolean, default False

   .. attribute:: use_float

      Convert input to float data

      :type: boolean, default False

   .. attribute:: use_multiview

      Use Multiple Views (when available)

      :type: boolean, default False

   .. attribute:: use_proxy

      Use a preview proxy and/or timecode index for this strip

      :type: boolean, default False

   .. attribute:: use_reverse_frames

      Reverse frame order

      :type: boolean, default False

   .. attribute:: use_translation

      Translate image before processing

      :type: boolean, default False

   .. attribute:: views_format

      Mode to load movie views

      * ``INDIVIDUAL`` Individual, Individual files for each view with the prefix as defined by the scene views.
      * ``STEREO_3D`` Stereo 3D, Single file with an encoded stereo pair.

      :type: enum in ['INDIVIDUAL', 'STEREO_3D'], default 'INDIVIDUAL'

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
   * :class:`Sequence.name`
   * :class:`Sequence.type`
   * :class:`Sequence.select`
   * :class:`Sequence.select_left_handle`
   * :class:`Sequence.select_right_handle`
   * :class:`Sequence.mute`
   * :class:`Sequence.lock`
   * :class:`Sequence.frame_final_duration`
   * :class:`Sequence.frame_duration`
   * :class:`Sequence.frame_start`
   * :class:`Sequence.frame_final_start`
   * :class:`Sequence.frame_final_end`
   * :class:`Sequence.frame_offset_start`
   * :class:`Sequence.frame_offset_end`
   * :class:`Sequence.frame_still_start`
   * :class:`Sequence.frame_still_end`
   * :class:`Sequence.channel`
   * :class:`Sequence.use_linear_modifiers`
   * :class:`Sequence.blend_type`
   * :class:`Sequence.blend_alpha`
   * :class:`Sequence.effect_fader`
   * :class:`Sequence.use_default_fade`
   * :class:`Sequence.speed_factor`
   * :class:`Sequence.modifiers`

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
   * :class:`Sequence.update`
   * :class:`Sequence.strip_elem_from_frame`
   * :class:`Sequence.swap`

