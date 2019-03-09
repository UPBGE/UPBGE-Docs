MovieTrackingPlaneTrack(bpy_struct)
===================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingPlaneTrack(bpy_struct)

   Match-moving plane track data for tracking

   .. attribute:: image

      Image displayed in the track during editing in clip editor

      :type: :class:`Image`

   .. attribute:: image_opacity

      Opacity of the image

      :type: float in [0, 1], default 0.0

   .. data:: markers

      Collection of markers in track

      :type: :class:`MovieTrackingPlaneMarkers` :class:`bpy_prop_collection` of :class:`MovieTrackingPlaneMarker`, (readonly)

   .. attribute:: name

      Unique name of track

      :type: string, default "", (never None)

   .. attribute:: select

      Plane track is selected

      :type: boolean, default False

   .. attribute:: use_auto_keying

      Automatic keyframe insertion when moving plane corners

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

   * :class:`MovieTracking.plane_tracks`
   * :class:`MovieTrackingObject.plane_tracks`
   * :class:`MovieTrackingPlaneTracks.active`

