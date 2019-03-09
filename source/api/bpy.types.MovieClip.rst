MovieClip(ID)
=============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: MovieClip(ID)

   MovieClip data-block referencing an external movie file

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: colorspace_settings

      Input color space settings

      :type: :class:`ColorManagedInputColorspaceSettings`, (readonly)

   .. attribute:: display_aspect

      Display Aspect for this clip, does not affect rendering

      :type: float array of 2 items in [0.1, inf], default (0.0, 0.0)

   .. attribute:: filepath

      Filename of the movie or sequence file

      :type: string, default "", (never None)

   .. data:: frame_duration

      Detected duration of movie clip in frames

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: frame_offset

      Offset of footage first frame relative to it's file name (affects only how footage is loading, does not change data associated with a clip)

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      Global scene frame number at which this movie starts playing (affects all data associated with a clip)

      :type: int in [-inf, inf], default 0

   .. attribute:: grease_pencil

      Grease pencil data for this movie clip

      :type: :class:`GreasePencil`

   .. data:: proxy

      :type: :class:`MovieClipProxy`, (readonly)

   .. data:: size

      Width and height in pixels, zero when image data cant be loaded

      :type: int array of 2 items in [-inf, inf], default (0, 0), (readonly)

   .. data:: source

      Where the clip comes from

      * ``SEQUENCE`` Image Sequence, Multiple image files, as a sequence.
      * ``MOVIE`` Movie File, Movie file.

      :type: enum in ['SEQUENCE', 'MOVIE'], default 'SEQUENCE', (readonly)

   .. data:: tracking

      :type: :class:`MovieTracking`, (readonly)

   .. attribute:: use_proxy

      Use a preview proxy and/or timecode index for this clip

      :type: boolean, default False

   .. attribute:: use_proxy_custom_directory

      Create proxy images in a custom directory (default is movie location)

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.edit_movieclip`
   * :class:`BackgroundImage.clip`
   * :class:`BlendData.movieclips`
   * :class:`BlendDataMovieClips.load`
   * :class:`BlendDataMovieClips.remove`
   * :class:`CameraSolverConstraint.clip`
   * :class:`CompositorNodeKeyingScreen.clip`
   * :class:`CompositorNodeMovieClip.clip`
   * :class:`CompositorNodeMovieDistortion.clip`
   * :class:`CompositorNodePlaneTrackDeform.clip`
   * :class:`CompositorNodeStabilize.clip`
   * :class:`CompositorNodeTrackPos.clip`
   * :class:`FollowTrackConstraint.clip`
   * :class:`ObjectSolverConstraint.clip`
   * :class:`Scene.active_clip`
   * :class:`Sequences.new_clip`
   * :class:`SpaceClipEditor.clip`

