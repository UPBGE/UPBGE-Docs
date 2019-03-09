TimelineMarker(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: TimelineMarker(bpy_struct)

   Marker for noting points in the timeline

   .. attribute:: camera

      Camera this timeline sets to active

      :type: :class:`Object`

   .. attribute:: frame

      The frame on which the timeline marker appears

      :type: int in [-inf, inf], default 0

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: select

      Marker selection state

      :type: boolean, default False

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

   * :class:`Action.pose_markers`
   * :class:`ActionPoseMarkers.active`
   * :class:`ActionPoseMarkers.new`
   * :class:`ActionPoseMarkers.remove`
   * :class:`Scene.timeline_markers`
   * :class:`TimelineMarkers.new`
   * :class:`TimelineMarkers.remove`

