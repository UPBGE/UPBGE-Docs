ShaderNodeTexPointDensity(ShaderNode)
=====================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`ShaderNode`

.. class:: ShaderNodeTexPointDensity(ShaderNode)

   

   .. attribute:: interpolation

      Texture interpolation

      * ``Closest`` Closest, No interpolation (sample closest texel).
      * ``Linear`` Linear, Linear interpolation.
      * ``Cubic`` Cubic, Cubic interpolation.

      :type: enum in ['Closest', 'Linear', 'Cubic'], default 'Linear'

   .. attribute:: object

      Object to take point data from

      :type: :class:`Object`

   .. attribute:: particle_color_source

      Data to derive color results from

      * ``PARTICLE_AGE`` Particle Age, Lifetime mapped as 0.0 - 1.0 intensity.
      * ``PARTICLE_SPEED`` Particle Speed, Particle speed (absolute magnitude of velocity) mapped as 0.0-1.0 intensity.
      * ``PARTICLE_VELOCITY`` Particle Velocity, XYZ velocity mapped to RGB colors.

      :type: enum in ['PARTICLE_AGE', 'PARTICLE_SPEED', 'PARTICLE_VELOCITY'], default 'PARTICLE_AGE'

   .. attribute:: particle_system

      Particle System to render as points

      :type: :class:`ParticleSystem`

   .. attribute:: point_source

      Point data to use as renderable point density

      * ``PARTICLE_SYSTEM`` Particle System, Generate point density from a particle system.
      * ``OBJECT`` Object Vertices, Generate point density from an object's vertices.

      :type: enum in ['PARTICLE_SYSTEM', 'OBJECT'], default 'PARTICLE_SYSTEM'

   .. attribute:: radius

      Radius from the shaded sample to look for points within

      :type: float in [0.001, inf], default 0.0

   .. attribute:: resolution

      Resolution used by the texture holding the point density

      :type: int in [1, 32768], default 0

   .. attribute:: space

      Coordinate system to calculate voxels in

      :type: enum in ['OBJECT', 'WORLD'], default 'OBJECT'

   .. attribute:: vertex_attribute_name

      Vertex attribute to use for color

      :type: string, default "", (never None)

   .. attribute:: vertex_color_source

      Data to derive color results from

      * ``VERTEX_COLOR`` Vertex Color, Vertex color layer.
      * ``VERTEX_WEIGHT`` Vertex Weight, Vertex group weight.
      * ``VERTEX_NORMAL`` Vertex Normal, XYZ normal vector mapped to RGB colors.

      :type: enum in ['VERTEX_COLOR', 'VERTEX_WEIGHT', 'VERTEX_NORMAL'], default 'VERTEX_COLOR'

   .. classmethod:: is_registered_node_type()

      True if a registered node type

      :return:

         Result

      :rtype: boolean

   .. classmethod:: input_template(index)

      Input socket template

      :arg index:

         Index

      :type index: int in [0, inf]
      :return:

         result

      :rtype: :class:`NodeInternalSocketTemplate`

   .. classmethod:: output_template(index)

      Output socket template

      :arg index:

         Index

      :type index: int in [0, inf]
      :return:

         result

      :rtype: :class:`NodeInternalSocketTemplate`

   .. method:: cache_point_density(scene=None, settings='RENDER')

      Cache point density data for later calculation

      :type scene: :class:`Scene`, (optional)
      :arg settings:

         Calculate density for rendering

         * ``VIEWPORT`` Viewport, Canculate density using viewport settings.
         * ``RENDER`` Render, Canculate duplis using render settings.

      :type settings: enum in ['VIEWPORT', 'RENDER'], (optional)

   .. method:: calc_point_density(scene=None, settings='RENDER')

      Calculate point density

      :type scene: :class:`Scene`, (optional)
      :arg settings:

         Calculate density for rendering

         * ``VIEWPORT`` Viewport, Canculate density using viewport settings.
         * ``RENDER`` Render, Canculate duplis using render settings.

      :type settings: enum in ['VIEWPORT', 'RENDER'], (optional)
      :return:

         RGBA Values

      :rtype: float array of 1 items in [-inf, inf]

   .. method:: calc_point_density_minmax(scene=None, settings='RENDER')

      Calculate point density

      :type scene: :class:`Scene`, (optional)
      :arg settings:

         Calculate density for rendering

         * ``VIEWPORT`` Viewport, Canculate density using viewport settings.
         * ``RENDER`` Render, Canculate duplis using render settings.

      :type settings: enum in ['VIEWPORT', 'RENDER'], (optional)
      :return (min, max):
         `min`, min, float array of 3 items in [-inf, inf]

         `max`, max, float array of 3 items in [-inf, inf]


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
   * :class:`Node.type`
   * :class:`Node.location`
   * :class:`Node.width`
   * :class:`Node.width_hidden`
   * :class:`Node.height`
   * :class:`Node.dimensions`
   * :class:`Node.name`
   * :class:`Node.label`
   * :class:`Node.inputs`
   * :class:`Node.outputs`
   * :class:`Node.internal_links`
   * :class:`Node.parent`
   * :class:`Node.use_custom_color`
   * :class:`Node.color`
   * :class:`Node.select`
   * :class:`Node.show_options`
   * :class:`Node.show_preview`
   * :class:`Node.hide`
   * :class:`Node.mute`
   * :class:`Node.show_texture`
   * :class:`Node.shading_compatibility`
   * :class:`Node.bl_idname`
   * :class:`Node.bl_label`
   * :class:`Node.bl_description`
   * :class:`Node.bl_icon`
   * :class:`Node.bl_static_type`
   * :class:`Node.bl_width_default`
   * :class:`Node.bl_width_min`
   * :class:`Node.bl_width_max`
   * :class:`Node.bl_height_default`
   * :class:`Node.bl_height_min`
   * :class:`Node.bl_height_max`

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
   * :class:`Node.socket_value_update`
   * :class:`Node.is_registered_node_type`
   * :class:`Node.poll`
   * :class:`Node.poll_instance`
   * :class:`Node.update`
   * :class:`Node.insert_link`
   * :class:`Node.init`
   * :class:`Node.copy`
   * :class:`Node.free`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`Node.draw_label`
   * :class:`Node.poll`
   * :class:`NodeInternal.poll`
   * :class:`NodeInternal.poll_instance`
   * :class:`NodeInternal.update`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`
   * :class:`ShaderNode.poll`

