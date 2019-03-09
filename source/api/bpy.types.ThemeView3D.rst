ThemeView3D(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeView3D(bpy_struct)

   Theme settings for the 3D View

   .. attribute:: act_spline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bone_pose

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bone_pose_active

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bone_solid

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bundle_solid

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: camera

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: camera_path

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: clipping_border_3d

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: edge_bevel

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_crease

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_facesel

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_seam

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_sharp

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: editmesh_active

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: empty

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_edge_angle

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_edge_len

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_face_angle

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_face_area

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: face

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: face_dot

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: face_select

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: facedot_size

      :type: int in [1, 10], default 0

   .. attribute:: frame_current

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: freestyle_edge_mark

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: freestyle_face_mark

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: gp_vertex

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_size

      :type: int in [1, 10], default 0

   .. attribute:: grid

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_align

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_auto

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_free

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_align

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_auto

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_free

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_vect

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_vect

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: lamp

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: lastsel_point

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: normal

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_sel_uline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_sel_vline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_uline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_vline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: object_active

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: object_grouped

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: object_grouped_active

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: object_selected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: outline_width

      :type: int in [1, 5], default 0

   .. attribute:: paint_curve_handle

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: paint_curve_pivot

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: skin_root

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGradient`, (readonly, never None)

   .. attribute:: speaker

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: split_normal

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_grease_pencil

      Color for indicating Grease Pencil keyframes

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_keyframe

      Color for indicating Object keyframes

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: transform

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_bevel

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_normal

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_size

      :type: int in [1, 10], default 0

   .. attribute:: vertex_unreferenced

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: view_overlay

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire_edit

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

   * :class:`Theme.view_3d`

