Action(ID)
==========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Action(ID)

   A collection of F-Curves for animation

   .. data:: fcurves

      The individual F-Curves that make up the action

      :type: :class:`ActionFCurves` :class:`bpy_prop_collection` of :class:`FCurve`, (readonly)

   .. data:: frame_range

      The final frame range of all F-Curves within this action

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0), (readonly)

   .. data:: groups

      Convenient groupings of F-Curves

      :type: :class:`ActionGroups` :class:`bpy_prop_collection` of :class:`ActionGroup`, (readonly)

   .. attribute:: id_root

      Type of ID block that action can be used on - DO NOT CHANGE UNLESS YOU KNOW WHAT YOU ARE DOING

      :type: enum in ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'GROUP', 'IMAGE', 'KEY', 'LAMP', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD'], default 'ACTION'

   .. data:: pose_markers

      Markers specific to this action, for labeling poses

      :type: :class:`ActionPoseMarkers` :class:`bpy_prop_collection` of :class:`TimelineMarker`, (readonly)

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`ActionActuator.action`
   * :class:`ActionConstraint.action`
   * :class:`AnimData.action`
   * :class:`BlendData.actions`
   * :class:`BlendDataActions.new`
   * :class:`BlendDataActions.remove`
   * :class:`NlaStrip.action`
   * :class:`NlaStrips.new`
   * :class:`Object.pose_library`
   * :class:`SpaceDopeSheetEditor.action`

