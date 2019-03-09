ThemeNLAEditor(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeNLAEditor(bpy_struct)

   Theme settings for the NLA Editor

   .. attribute:: active_action

      Animation data-block has active action

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: active_action_unset

      Animation data-block doesn't have active action

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: frame_current

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: grid

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_border

      Color of keyframe border

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: keyframe_border_selected

      Color of selected keyframe border

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: meta_strips

      Meta Strip - Unselected (for grouping related strips)

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: meta_strips_selected

      Meta Strip - Selected (for grouping related strips)

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: sound_strips

      Sound Strip - Unselected (for timing speaker sounds)

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: sound_strips_selected

      Sound Strip - Selected (for timing speaker sounds)

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGeneric`, (readonly, never None)

   .. data:: space_list

      Settings for space list

      :type: :class:`ThemeSpaceListGeneric`, (readonly, never None)

   .. attribute:: strips

      Action-Clip Strip - Unselected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: strips_selected

      Action-Clip Strip - Selected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: transition_strips

      Transition Strip - Unselected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: transition_strips_selected

      Transition Strip - Selected

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tweak

      Color for strip/action being 'tweaked' or edited

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tweak_duplicate

      Warning/error indicator color for strips referencing the strip being tweaked

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

   * :class:`Theme.nla_editor`

