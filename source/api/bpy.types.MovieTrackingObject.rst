MovieTrackingObject(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingObject(bpy_struct)

   Match-moving object tracking and reconstruction data

   .. data:: is_camera

      Object is used for camera tracking

      :type: boolean, default False, (readonly)

   .. attribute:: keyframe_a

      First keyframe used for reconstruction initialization

      :type: int in [-inf, inf], default 0

   .. attribute:: keyframe_b

      Second keyframe used for reconstruction initialization

      :type: int in [-inf, inf], default 0

   .. attribute:: name

      Unique name of object

      :type: string, default "", (never None)

   .. data:: plane_tracks

      Collection of plane tracks in this tracking data object

      :type: :class:`MovieTrackingObjectPlaneTracks` :class:`bpy_prop_collection` of :class:`MovieTrackingPlaneTrack`, (readonly)

   .. data:: reconstruction

      :type: :class:`MovieTrackingReconstruction`, (readonly)

   .. attribute:: scale

      Scale of object solution in camera space

      :type: float in [0.0001, 10000], default 1.0

   .. data:: tracks

      Collection of tracks in this tracking data object

      :type: :class:`MovieTrackingObjectTracks` :class:`bpy_prop_collection` of :class:`MovieTrackingTrack`, (readonly)

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

   * :class:`MovieTracking.objects`
   * :class:`MovieTrackingObjects.active`
   * :class:`MovieTrackingObjects.new`
   * :class:`MovieTrackingObjects.remove`

