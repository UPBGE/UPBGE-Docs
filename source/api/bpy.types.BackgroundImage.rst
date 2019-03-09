BackgroundImage(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BackgroundImage(bpy_struct)

   Image and settings for display in the 3D View background

   .. attribute:: clip

      Movie clip displayed and edited in this space

      :type: :class:`MovieClip`

   .. data:: clip_user

      Parameters defining which frame of the movie clip is displayed

      :type: :class:`MovieClipUser`, (readonly, never None)

   .. attribute:: draw_depth

      Draw under or over everything

      :type: enum in ['BACK', 'FRONT'], default 'BACK'

   .. attribute:: frame_method

      How the image fits in the camera frame

      :type: enum in ['STRETCH', 'FIT', 'CROP'], default 'STRETCH'

   .. attribute:: image

      Image displayed and edited in this space

      :type: :class:`Image`

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly, never None)

   .. attribute:: offset_x

      Offset image horizontally from the world origin

      :type: float in [-inf, inf], default 0.0

   .. attribute:: offset_y

      Offset image vertically from the world origin

      :type: float in [-inf, inf], default 0.0

   .. attribute:: opacity

      Image opacity to blend the image against the background color

      :type: float in [0, 1], default 0.0

   .. attribute:: rotation

      Rotation for the background image (ortho view only)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: show_background_image

      Show this image as background

      :type: boolean, default False

   .. attribute:: show_expanded

      Show the expanded in the user interface

      :type: boolean, default False

   .. attribute:: show_on_foreground

      Show this image in front of objects in viewport

      :type: boolean, default False

   .. attribute:: size

      Size of the background image (ortho view only)

      :type: float in [0, inf], default 0.0

   .. attribute:: source

      Data source used for background

      :type: enum in ['IMAGE', 'MOVIE_CLIP'], default 'IMAGE'

   .. attribute:: use_camera_clip

      Use movie clip from active scene camera

      :type: boolean, default False

   .. attribute:: use_flip_x

      Flip the background image horizontally

      :type: boolean, default False

   .. attribute:: use_flip_y

      Flip the background image vertically

      :type: boolean, default False

   .. attribute:: view_axis

      The axis to display the image on

      * ``LEFT`` Left, Show background image while looking to the left.
      * ``RIGHT`` Right, Show background image while looking to the right.
      * ``BACK`` Back, Show background image in back view.
      * ``FRONT`` Front, Show background image in front view.
      * ``BOTTOM`` Bottom, Show background image in bottom view.
      * ``TOP`` Top, Show background image in top view.
      * ``ALL`` All Views, Show background image in all views.
      * ``CAMERA`` Camera, Show background image in camera view.

      :type: enum in ['LEFT', 'RIGHT', 'BACK', 'FRONT', 'BOTTOM', 'TOP', 'ALL', 'CAMERA'], default 'ALL'

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

   * :class:`BackgroundImages.new`
   * :class:`BackgroundImages.remove`
   * :class:`SpaceView3D.background_images`

