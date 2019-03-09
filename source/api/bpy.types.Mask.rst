Mask(ID)
========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Mask(ID)

   Mask data-block defining mask for compositing

   .. attribute:: active_layer_index

      Index of active layer in list of all mask's layers

      :type: int in [-inf, inf], default 0

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: frame_end

      Final frame of the mask (used for sequencer)

      :type: int in [0, 1048574], default 0

   .. attribute:: frame_start

      First frame of the mask (used for sequencer)

      :type: int in [0, 1048574], default 0

   .. data:: layers

      Collection of layers which defines this mask

      :type: :class:`MaskLayers` :class:`bpy_prop_collection` of :class:`MaskLayer`, (readonly)

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

   * :mod:`bpy.context.edit_mask`
   * :class:`BlendData.masks`
   * :class:`BlendDataMasks.new`
   * :class:`BlendDataMasks.remove`
   * :class:`CompositorNodeMask.mask`
   * :class:`MaskSequence.mask`
   * :class:`SequenceModifier.input_mask_id`
   * :class:`Sequences.new_mask`
   * :class:`SpaceClipEditor.mask`
   * :class:`SpaceImageEditor.mask`

