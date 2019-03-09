World(ID)
=========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: World(ID)

   World data-block describing the environment and ambient lighting of a scene

   .. attribute:: active_texture

      Active texture slot being displayed

      :type: :class:`Texture`

   .. attribute:: active_texture_index

      Index of active texture slot

      :type: int in [0, 17], default 0

   .. attribute:: ambient_color

      Ambient color of the world

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: color_range

      The color range that will be mapped to 0-1

      :type: float in [0.2, 5], default 0.0

   .. data:: cycles

      Cycles world settings

      :type: :class:`CyclesWorldSettings`, (readonly)

   .. data:: cycles_visibility

      Cycles visibility settings

      :type: :class:`CyclesVisibilitySettings`, (readonly)

   .. attribute:: exposure

      Amount of exponential color correction for light

      :type: float in [0, 1], default 0.0

   .. attribute:: horizon_color

      Color at the horizon

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: light_settings

      World lighting settings

      :type: :class:`WorldLighting`, (readonly, never None)

   .. data:: mist_settings

      World mist settings

      :type: :class:`WorldMistSettings`, (readonly, never None)

   .. data:: node_tree

      Node tree for node based worlds

      :type: :class:`NodeTree`, (readonly)

   .. data:: texture_slots

      Texture slots defining the mapping and influence of textures

      :type: :class:`WorldTextureSlots` :class:`bpy_prop_collection` of :class:`WorldTextureSlot`, (readonly)

   .. attribute:: use_nodes

      Use shader nodes to render the world

      :type: boolean, default False

   .. attribute:: use_sky_blend

      Render background with natural progression from horizon to zenith

      :type: boolean, default False

   .. attribute:: use_sky_paper

      Flatten blend or texture coordinates

      :type: boolean, default False

   .. attribute:: use_sky_real

      Render background with a real horizon, relative to the camera angle

      :type: boolean, default False

   .. attribute:: zenith_color

      Color at the zenith

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

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

   * :mod:`bpy.context.world`
   * :class:`BlendData.worlds`
   * :class:`BlendDataWorlds.new`
   * :class:`BlendDataWorlds.remove`
   * :class:`Scene.world`

