Sound(ID)
=========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Sound(ID)

   Sound data-block referencing an external or packed sound file

   .. attribute:: filepath

      Sound sample file used by this Sound data-block

      :type: string, default "", (never None)

   .. data:: packed_file

      :type: :class:`PackedFile`, (readonly)

   .. attribute:: use_memory_cache

      The sound file is decoded and loaded into RAM

      :type: boolean, default False

   .. attribute:: use_mono

      If the file contains multiple audio channels they are rendered to a single one

      :type: boolean, default False

   .. data:: factory

      The aud.Factory object of the sound.
      (readonly)

   .. method:: pack()

      Pack the sound into the current blend file


   .. method:: unpack(method='USE_LOCAL')

      Unpack the sound to the samples filename

      :arg method:

         method, How to unpack

      :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)

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

   * :class:`BlendData.sounds`
   * :class:`BlendDataSounds.load`
   * :class:`BlendDataSounds.remove`
   * :class:`SoundActuator.sound`
   * :class:`SoundSequence.sound`
   * :class:`Speaker.sound`

