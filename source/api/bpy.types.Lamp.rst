Lamp(ID)
========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

subclasses --- 
:class:`AreaLamp`, :class:`HemiLamp`, :class:`PointLamp`, :class:`SpotLamp`, :class:`SunLamp`

.. class:: Lamp(ID)

   Lamp data-block for lighting a scene

   .. attribute:: active_texture

      Active texture slot being displayed

      :type: :class:`Texture`

   .. attribute:: active_texture_index

      Index of active texture slot

      :type: int in [0, 17], default 0

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: color

      Light color

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: cycles

      Cycles lamp settings

      :type: :class:`CyclesLampSettings`, (readonly)

   .. attribute:: distance

      Falloff distance - the light is at half the original intensity at this point

      :type: float in [0, inf], default 0.0

   .. attribute:: energy

      Amount of light that the lamp emits

      :type: float in [-inf, inf], default 0.0

   .. data:: node_tree

      Node tree for node based lamps

      :type: :class:`NodeTree`, (readonly)

   .. data:: texture_slots

      Texture slots defining the mapping and influence of textures

      :type: :class:`LampTextureSlots` :class:`bpy_prop_collection` of :class:`LampTextureSlot`, (readonly)

   .. attribute:: type

      Type of Lamp

      * ``POINT`` Point, Omnidirectional point light source.
      * ``SUN`` Sun, Constant direction parallel ray light source.
      * ``SPOT`` Spot, Directional cone light source.
      * ``HEMI`` Hemi, 180 degree constant light source.
      * ``AREA`` Area, Directional area light source.

      :type: enum in ['POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'], default 'POINT'

   .. attribute:: use_diffuse

      Do diffuse shading

      :type: boolean, default False

   .. attribute:: use_negative

      Cast negative light

      :type: boolean, default False

   .. attribute:: use_nodes

      Use shader nodes to render the lamp

      :type: boolean, default False

   .. attribute:: use_own_layer

      Illuminate objects only on the same layers the lamp is on

      :type: boolean, default False

   .. attribute:: use_specular

      Create specular highlights

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

   * :mod:`bpy.context.lamp`
   * :class:`BlendData.lamps`
   * :class:`BlendDataLamps.new`
   * :class:`BlendDataLamps.remove`

