Group(ID)
=========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Group(ID)

   Group of Object data-blocks

   .. attribute:: dupli_offset

      Offset from the origin to use when instancing as DupliGroup

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: layers

      Layers visible when this group is instanced as a dupli

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. data:: objects

      A collection of this groups objects

      :type: :class:`GroupObjects` :class:`bpy_prop_collection` of :class:`Object`, (readonly)

   .. data:: users_dupli_group

      The dupli group this group is used in
      (readonly)

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

   * :class:`BlendData.groups`
   * :class:`BlendDataGroups.new`
   * :class:`BlendDataGroups.remove`
   * :class:`ClothCollisionSettings.group`
   * :class:`DopeSheet.filter_group`
   * :class:`DynamicPaintSurface.brush_group`
   * :class:`EffectorWeights.group`
   * :class:`FreestyleLineSet.group`
   * :class:`Material.light_group`
   * :class:`Object.dupli_group`
   * :class:`ParticleSettings.collision_group`
   * :class:`ParticleSettings.dupli_group`
   * :class:`RenderLayer.light_override`
   * :class:`RigidBodyWorld.constraints`
   * :class:`RigidBodyWorld.group`
   * :class:`SceneRenderLayer.light_override`
   * :class:`SmokeDomainSettings.collision_group`
   * :class:`SmokeDomainSettings.effector_group`
   * :class:`SmokeDomainSettings.fluid_group`
   * :class:`SoftBodySettings.collision_group`

