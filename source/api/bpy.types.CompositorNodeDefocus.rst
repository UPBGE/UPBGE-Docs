CompositorNodeDefocus(CompositorNode)
=====================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`CompositorNode`

.. class:: CompositorNodeDefocus(CompositorNode)

   

   .. attribute:: angle

      Bokeh shape rotation offset

      :type: float in [0, 1.5708], default 0.0

   .. attribute:: blur_max

      Blur limit, maximum CoC radius

      :type: float in [0, 10000], default 0.0

   .. attribute:: bokeh

      * ``OCTAGON`` Octagonal, 8 sides.
      * ``HEPTAGON`` Heptagonal, 7 sides.
      * ``HEXAGON`` Hexagonal, 6 sides.
      * ``PENTAGON`` Pentagonal, 5 sides.
      * ``SQUARE`` Square, 4 sides.
      * ``TRIANGLE`` Triangular, 3 sides.
      * ``CIRCLE`` Circular.

      :type: enum in ['OCTAGON', 'HEPTAGON', 'HEXAGON', 'PENTAGON', 'SQUARE', 'TRIANGLE', 'CIRCLE'], default 'CIRCLE'

   .. attribute:: f_stop

      Amount of focal blur, 128=infinity=perfect focus, half the value doubles the blur radius

      :type: float in [0, 128], default 0.0

   .. attribute:: scene

      Scene from which to select the active camera (render scene if undefined)

      :type: :class:`Scene`

   .. attribute:: threshold

      CoC radius threshold, prevents background bleed on in-focus midground, 0=off

      :type: float in [0, 100], default 0.0

   .. attribute:: use_gamma_correction

      Enable gamma correction before and after main process

      :type: boolean, default False

   .. attribute:: use_preview

      Enable low quality mode, useful for preview

      :type: boolean, default False

   .. attribute:: use_zbuffer

      Disable when using an image as input instead of actual z-buffer (auto enabled if node not image based, eg. time node)

      :type: boolean, default False

   .. attribute:: z_scale

      Scale the Z input when not using a z-buffer, controls maximum blur designated by the color white or input value 1

      :type: float in [0, 1000], default 0.0

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

