MovieTracking(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTracking(bpy_struct)

   Match-moving data for tracking

   .. attribute:: active_object_index

      Index of active object

      :type: int in [-inf, inf], default 0

   .. data:: camera

      :type: :class:`MovieTrackingCamera`, (readonly)

   .. data:: dopesheet

      :type: :class:`MovieTrackingDopesheet`, (readonly)

   .. data:: objects

      Collection of objects in this tracking data object

      :type: :class:`MovieTrackingObjects` :class:`bpy_prop_collection` of :class:`MovieTrackingObject`, (readonly)

   .. data:: plane_tracks

      Collection of plane tracks in this tracking data object

      :type: :class:`MovieTrackingPlaneTracks` :class:`bpy_prop_collection` of :class:`MovieTrackingPlaneTrack`, (readonly)

   .. data:: reconstruction

      :type: :class:`MovieTrackingReconstruction`, (readonly)

   .. data:: settings

      :type: :class:`MovieTrackingSettings`, (readonly)

   .. data:: stabilization

      :type: :class:`MovieTrackingStabilization`, (readonly)

   .. data:: tracks

      Collection of tracks in this tracking data object

      :type: :class:`MovieTrackingTracks` :class:`bpy_prop_collection` of :class:`MovieTrackingTrack`, (readonly)

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

   * :class:`MovieClip.tracking`

