CacheFile(ID)
=============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: CacheFile(ID)

   

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: filepath

      Path to external displacements file

      :type: string, default "", (never None)

   .. attribute:: forward_axis

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

   .. attribute:: frame

      The time to use for looking up the data in the cache file, or to determine which file to use in a file sequence

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: frame_offset

      Subtracted from the current frame to use for looking up the data in the cache file, or to determine which file to use in a file sequence

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: is_sequence

      Whether the cache is separated in a series of files

      :type: boolean, default False

   .. data:: object_paths

      Paths of the objects inside the Alembic archive

      :type: :class:`AlembicObjectPaths` :class:`bpy_prop_collection` of :class:`AlembicObjectPath`, (readonly)

   .. attribute:: override_frame

      Whether to use a custom frame for looking up data in the cache file, instead of using the current scene frame

      :type: boolean, default False

   .. attribute:: scale

      Value by which to enlarge or shrink the object with respect to the world's origin (only applicable through a Transform Cache constraint)

      :type: float in [0.0001, 1000], default 0.0

   .. attribute:: up_axis

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

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

   * :class:`BlendData.cache_files`
   * :class:`MeshSequenceCacheModifier.cache_file`
   * :class:`TransformCacheConstraint.cache_file`

