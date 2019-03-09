ShaderNodeTexImage(ShaderNode)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`ShaderNode`

.. class:: ShaderNodeTexImage(ShaderNode)

   

   .. data:: color_mapping

      Color mapping settings

      :type: :class:`ColorMapping`, (readonly, never None)

   .. attribute:: color_space

      Image file color space

      * ``COLOR`` Color, Image contains color data, and will be converted to linear color for rendering.
      * ``NONE`` Non-Color Data, Image contains non-color data, for example a displacement or normal map, and will not be converted.

      :type: enum in ['COLOR', 'NONE'], default 'COLOR'

   .. attribute:: extension

      How the image is extrapolated past its original bounds

      * ``REPEAT`` Repeat, Cause the image to repeat horizontally and vertically.
      * ``EXTEND`` Extend, Extend by repeating edge pixels of the image.
      * ``CLIP`` Clip, Clip to image size and set exterior pixels as transparent.

      :type: enum in ['REPEAT', 'EXTEND', 'CLIP'], default 'REPEAT'

   .. attribute:: image

      :type: :class:`Image`

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly, never None)

   .. attribute:: interpolation

      Texture interpolation

      * ``Linear`` Linear, Linear interpolation.
      * ``Closest`` Closest, No interpolation (sample closest texel).
      * ``Cubic`` Cubic, Cubic interpolation.
      * ``Smart`` Smart, Bicubic when magnifying, else bilinear (OSL only).

      :type: enum in ['Linear', 'Closest', 'Cubic', 'Smart'], default 'Linear'

   .. attribute:: projection

      Method to project 2D image on object with a 3D texture vector

      * ``FLAT`` Flat, Image is projected flat using the X and Y coordinates of the texture vector.
      * ``BOX`` Box, Image is projected using different components for each side of the object space bounding box.
      * ``SPHERE`` Sphere, Image is projected spherically using the Z axis as central.
      * ``TUBE`` Tube, Image is projected from the tube using the Z axis as central.

      :type: enum in ['FLAT', 'BOX', 'SPHERE', 'TUBE'], default 'FLAT'

   .. attribute:: projection_blend

      For box projection, amount of blend to use between sides

      :type: float in [0, 1], default 0.0

   .. data:: texture_mapping

      Texture coordinate mapping settings

      :type: :class:`TexMapping`, (readonly, never None)

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

