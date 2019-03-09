MovieTrackingMarker(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingMarker(bpy_struct)

   Match-moving marker data for tracking

   .. attribute:: co

      Marker position at frame in normalized coordinates

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: frame

      Frame number marker is keyframed on

      :type: int in [-inf, inf], default 0

   .. attribute:: is_keyed

      Whether the position of the marker is keyframed or tracked

      :type: boolean, default False

   .. attribute:: mute

      Is marker muted for current frame

      :type: boolean, default False

   .. data:: pattern_bound_box

      Pattern area bounding box in normalized coordinates

      :type: float multi-dimensional array of 2 * 2 items in [-inf, inf], default ((0.0, 0.0), (0.0, 0.0)), (readonly)

   .. attribute:: pattern_corners

      Array of coordinates which represents pattern's corners in normalized coordinates relative to marker position

      :type: float multi-dimensional array of 4 * 2 items in [-inf, inf], default ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0))

   .. attribute:: search_max

      Right-bottom corner of search area in normalized coordinates relative to marker position

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: search_min

      Left-bottom corner of search area in normalized coordinates relative to marker position

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

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

   * :class:`MovieTrackingMarkers.find_frame`
   * :class:`MovieTrackingMarkers.insert_frame`
   * :class:`MovieTrackingTrack.markers`

