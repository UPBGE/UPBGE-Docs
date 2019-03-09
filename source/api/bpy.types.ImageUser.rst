ImageUser(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ImageUser(bpy_struct)

   Parameters defining how an Image data-block is used by another data-block

   .. attribute:: fields_per_frame

      Number of fields per rendered frame (2 fields is 1 image)

      :type: int in [1, 200], default 0

   .. attribute:: frame_current

      Current frame number in image sequence or movie

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: frame_duration

      Number of images of a movie to use

      :type: int in [0, 1048574], default 0

   .. attribute:: frame_offset

      Offset the number of the frame to use in the animation

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      Global starting frame of the movie/sequence, assuming first picture has a #1

      :type: int in [-1048574, 1048574], default 0

   .. data:: multilayer_layer

      Layer in multilayer image

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: multilayer_pass

      Pass in multilayer image

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: multilayer_view

      View in multilayer image

      :type: int in [0, 32767], default 0, (readonly)

   .. attribute:: use_auto_refresh

      Always refresh image on frame changes

      :type: boolean, default False

   .. attribute:: use_cyclic

      Cycle the images in the movie

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

   * :class:`BackgroundImage.image_user`
   * :class:`EnvironmentMapTexture.image_user`
   * :class:`Image.filepath_from_user`
   * :class:`ImageTexture.image_user`
   * :class:`Object.image_user`
   * :class:`ShaderNodeTexEnvironment.image_user`
   * :class:`ShaderNodeTexImage.image_user`
   * :class:`SpaceImageEditor.image_user`
   * :class:`TextureNodeImage.image_user`
   * :class:`UILayout.template_image`
   * :class:`UILayout.template_image_layers`
   * :class:`VoxelDataTexture.image_user`

