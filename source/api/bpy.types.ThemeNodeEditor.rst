ThemeNodeEditor(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeNodeEditor(bpy_struct)

   Theme settings for the Node Editor

   .. attribute:: color_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: converter_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: distor_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: filter_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: frame_node

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: gp_vertex

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_size

      :type: int in [1, 10], default 0

   .. attribute:: group_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: group_socket_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: input_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: layout_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: matte_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: node_active

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: node_backdrop

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: node_selected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: noodle_curving

      Curving of the noodle

      :type: int in [0, 10], default 5

   .. attribute:: output_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: pattern_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: script_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: selected_text

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: shader_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGeneric`, (readonly, never None)

   .. data:: space_list

      Settings for space list

      :type: :class:`ThemeSpaceListGeneric`, (readonly, never None)

   .. attribute:: texture_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vector_node

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire_inner

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

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

   * :class:`Theme.node_editor`

