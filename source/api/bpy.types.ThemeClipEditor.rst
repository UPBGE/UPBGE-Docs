ThemeClipEditor(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeClipEditor(bpy_struct)

   Theme settings for the Movie Clip Editor

   .. attribute:: active_marker

      Color of active marker

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: disabled_marker

      Color of disabled marker

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: frame_current

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_size

      :type: int in [1, 10], default 0

   .. attribute:: handle_align

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_auto

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_auto_clamped

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_free

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_align

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_auto

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_auto_clamped

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_free

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_vertex

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_vertex_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_vertex_size

      :type: int in [0, 255], default 0

   .. attribute:: locked_marker

      Color of locked marker

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: marker

      Color of marker

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: marker_outline

      Color of marker's outline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: path_after

      Color of path after current frame

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: path_before

      Color of path before current frame

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: selected_marker

      Color of selected marker

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGeneric`, (readonly, never None)

   .. data:: space_list

      Settings for space list

      :type: :class:`ThemeSpaceListGeneric`, (readonly, never None)

   .. attribute:: strips

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: strips_selected

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

   * :class:`Theme.clip_editor`

