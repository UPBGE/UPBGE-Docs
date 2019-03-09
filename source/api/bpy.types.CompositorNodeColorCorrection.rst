CompositorNodeColorCorrection(CompositorNode)
=============================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`CompositorNode`

.. class:: CompositorNodeColorCorrection(CompositorNode)

   

   .. attribute:: blue

      Blue channel active

      :type: boolean, default True

   .. attribute:: green

      Green channel active

      :type: boolean, default True

   .. attribute:: highlights_contrast

      Highlights contrast

      :type: float in [0, 4], default 1.0

   .. attribute:: highlights_gain

      Highlights gain

      :type: float in [0, 4], default 1.0

   .. attribute:: highlights_gamma

      Highlights gamma

      :type: float in [0, 4], default 1.0

   .. attribute:: highlights_lift

      Highlights lift

      :type: float in [-1, 1], default 0.0

   .. attribute:: highlights_saturation

      Highlights saturation

      :type: float in [0, 4], default 1.0

   .. attribute:: master_contrast

      Master contrast

      :type: float in [0, 4], default 1.0

   .. attribute:: master_gain

      Master gain

      :type: float in [0, 4], default 1.0

   .. attribute:: master_gamma

      Master gamma

      :type: float in [0, 4], default 1.0

   .. attribute:: master_lift

      Master lift

      :type: float in [-1, 1], default 0.0

   .. attribute:: master_saturation

      Master saturation

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_contrast

      Midtones contrast

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_end

      End of midtones

      :type: float in [0, 1], default 0.7

   .. attribute:: midtones_gain

      Midtones gain

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_gamma

      Midtones gamma

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_lift

      Midtones lift

      :type: float in [-1, 1], default 0.0

   .. attribute:: midtones_saturation

      Midtones saturation

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_start

      Start of midtones

      :type: float in [0, 1], default 0.2

   .. attribute:: red

      Red channel active

      :type: boolean, default True

   .. attribute:: shadows_contrast

      Shadows contrast

      :type: float in [0, 4], default 1.0

   .. attribute:: shadows_gain

      Shadows gain

      :type: float in [0, 4], default 1.0

   .. attribute:: shadows_gamma

      Shadows gamma

      :type: float in [0, 4], default 1.0

   .. attribute:: shadows_lift

      Shadows lift

      :type: float in [-1, 1], default 0.0

   .. attribute:: shadows_saturation

      Shadows saturation

      :type: float in [0, 4], default 1.0

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

   .. method:: update()

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
   * :class:`CompositorNode.tag_need_exec`
   * :class:`CompositorNode.poll`
   * :class:`CompositorNode.update`

