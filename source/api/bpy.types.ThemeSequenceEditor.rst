ThemeSequenceEditor(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeSequenceEditor(bpy_struct)

   Theme settings for the Sequence Editor

   .. attribute:: audio_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: draw_action

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: effect_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: frame_current

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_select

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_size

      :type: int in [1, 10], default 0

   .. attribute:: grid

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: image_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: meta_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: metadatabg

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: metadatatext

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: movie_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: movieclip_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: preview_back

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: scene_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGeneric`, (readonly, never None)

   .. attribute:: text_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: transition_strip

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: window_sliders

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

   * :class:`Theme.sequence_editor`

