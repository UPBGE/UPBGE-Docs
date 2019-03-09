SpaceProperties(Space)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceProperties(Space)

   Properties space data

   .. attribute:: align

      Arrangement of the panels

      :type: enum in ['HORIZONTAL', 'VERTICAL'], default 'HORIZONTAL'

   .. attribute:: context

      Type of active data to display and edit

      * ``SCENE`` Scene, Scene.
      * ``RENDER`` Render, Render.
      * ``RENDER_LAYER`` Render Layers, Render layers.
      * ``WORLD`` World, World.
      * ``OBJECT`` Object, Object.
      * ``CONSTRAINT`` Constraints, Object constraints.
      * ``MODIFIER`` Modifiers, Object modifiers.
      * ``DATA`` Data, Object data.
      * ``BONE`` Bone, Bone.
      * ``BONE_CONSTRAINT`` Bone Constraints, Bone constraints.
      * ``MATERIAL`` Material, Material.
      * ``TEXTURE`` Texture, Texture.
      * ``PARTICLES`` Particles, Particle.
      * ``PHYSICS`` Physics, Physics.

      :type: enum in ['SCENE', 'RENDER', 'RENDER_LAYER', 'WORLD', 'OBJECT', 'CONSTRAINT', 'MODIFIER', 'DATA', 'BONE', 'BONE_CONSTRAINT', 'MATERIAL', 'TEXTURE', 'PARTICLES', 'PHYSICS'], default 'RENDER'

   .. attribute:: pin_id

      :type: :class:`ID`

   .. attribute:: texture_context

      Type of texture data to display and edit

      * ``MATERIAL`` Show material textures.
      * ``WORLD`` Show world textures.
      * ``LAMP`` Show lamp textures.
      * ``PARTICLES`` Show particles textures.
      * ``LINESTYLE`` Show linestyle textures.
      * ``OTHER`` Show other data textures.

      :type: enum in ['MATERIAL', 'WORLD', 'LAMP', 'PARTICLES', 'LINESTYLE', 'OTHER'], default 'MATERIAL'

   .. attribute:: use_limited_texture_context

      Use the limited version of texture user (for 'old shading' mode)

      :type: boolean, default False

   .. attribute:: use_pin_id

      Use the pinned context

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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

