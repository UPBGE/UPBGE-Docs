ThemeDopeSheet(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeDopeSheet(bpy_struct)

   Theme settings for the Dope Sheet

   .. attribute:: active_channels_group

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: channel_group

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: channels

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: channels_selected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: dopesheet_channel

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: dopesheet_subchannel

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: frame_current

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: grid

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe

      Color of Keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_border

      Color of keyframe border

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: keyframe_border_selected

      Color of selected keyframe border

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: keyframe_breakdown

      Color of breakdown keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_breakdown_selected

      Color of selected breakdown keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_extreme

      Color of extreme keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_extreme_selected

      Color of selected extreme keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_jitter

      Color of jitter keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_jitter_selected

      Color of selected jitter keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_scale_factor

      Scale factor for adjusting the height of keyframes

      :type: float in [0.8, 5], default 1.0

   .. attribute:: keyframe_selected

      Color of selected keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: long_key

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: long_key_selected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGeneric`, (readonly, never None)

   .. data:: space_list

      Settings for space list

      :type: :class:`ThemeSpaceListGeneric`, (readonly, never None)

   .. attribute:: summary

      Color of summary channel

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: value_sliders

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: view_sliders

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

   * :class:`Theme.dopesheet_editor`

