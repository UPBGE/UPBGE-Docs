NodeInternal(Node)
==================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`

subclasses --- 
:class:`CompositorNode`, :class:`NodeFrame`, :class:`NodeGroup`, :class:`NodeGroupInput`, :class:`NodeGroupOutput`, :class:`NodeReroute`, :class:`ShaderNode`, :class:`TextureNode`

.. class:: NodeInternal(Node)

   

   .. classmethod:: poll(node_tree)

      If non-null output is returned, the node type can be added to the tree

      :arg node_tree:

         Node Tree

      :type node_tree: :class:`NodeTree`
      :rtype: boolean

   .. method:: poll_instance(node_tree)

      If non-null output is returned, the node can be added to the tree

      :arg node_tree:

         Node Tree

      :type node_tree: :class:`NodeTree`
      :rtype: boolean

   .. method:: update()

      Update on editor changes


   .. method:: draw_buttons(context, layout)

      Draw node buttons

      :type context: :class:`Context`, (never None)
      :arg layout:

         Layout, Layout in the UI

      :type layout: :class:`UILayout`, (never None)

   .. method:: draw_buttons_ext(context, layout)

      Draw node buttons in the sidebar

      :type context: :class:`Context`, (never None)
      :arg layout:

         Layout, Layout in the UI

      :type layout: :class:`UILayout`, (never None)

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

