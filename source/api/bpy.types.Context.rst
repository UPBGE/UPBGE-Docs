Context(bpy_struct)
===================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Context(bpy_struct)

   Current windowmanager and data context

   .. data:: area

      :type: :class:`Area`, (readonly)

   .. data:: blend_data

      :type: :class:`BlendData`, (readonly)

   .. data:: mode

      :type: enum in ['EDIT_MESH', 'EDIT_CURVE', 'EDIT_SURFACE', 'EDIT_TEXT', 'EDIT_ARMATURE', 'EDIT_METABALL', 'EDIT_LATTICE', 'POSE', 'SCULPT', 'PAINT_WEIGHT', 'PAINT_VERTEX', 'PAINT_TEXTURE', 'PARTICLE', 'OBJECT'], default 'EDIT_MESH', (readonly)

   .. data:: region

      :type: :class:`Region`, (readonly)

   .. data:: region_data

      :type: :class:`RegionView3D`, (readonly)

   .. data:: scene

      :type: :class:`Scene`, (readonly)

   .. data:: screen

      :type: :class:`Screen`, (readonly)

   .. data:: space_data

      :type: :class:`Space`, (readonly)

   .. data:: tool_settings

      :type: :class:`ToolSettings`, (readonly)

   .. data:: user_preferences

      :type: :class:`UserPreferences`, (readonly)

   .. data:: window

      :type: :class:`Window`, (readonly)

   .. data:: window_manager

      :type: :class:`WindowManager`, (readonly)

   .. method:: copy()

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

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`Header.draw`
   * :class:`KeyingSetInfo.generate`
   * :class:`KeyingSetInfo.iterator`
   * :class:`KeyingSetInfo.poll`
   * :class:`Macro.draw`
   * :class:`Macro.poll`
   * :class:`Menu.draw`
   * :class:`Menu.poll`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`Node.init`
   * :class:`Node.socket_value_update`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`
   * :class:`NodeSocket.draw`
   * :class:`NodeSocket.draw_color`
   * :class:`NodeSocketInterface.draw`
   * :class:`NodeSocketInterface.draw_color`
   * :class:`NodeSocketInterfaceStandard.draw`
   * :class:`NodeSocketInterfaceStandard.draw_color`
   * :class:`NodeSocketStandard.draw`
   * :class:`NodeSocketStandard.draw_color`
   * :class:`NodeTree.get_from_context`
   * :class:`NodeTree.interface_update`
   * :class:`NodeTree.poll`
   * :class:`Operator.cancel`
   * :class:`Operator.check`
   * :class:`Operator.draw`
   * :class:`Operator.execute`
   * :class:`Operator.invoke`
   * :class:`Operator.modal`
   * :class:`Operator.poll`
   * :class:`Panel.draw`
   * :class:`Panel.draw_header`
   * :class:`Panel.poll`
   * :class:`RenderEngine.view_draw`
   * :class:`RenderEngine.view_update`
   * :class:`UIList.draw_filter`
   * :class:`UIList.draw_item`
   * :class:`UIList.filter_items`

