MovieTrackingCamera(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingCamera(bpy_struct)

   Match-moving camera data for tracking

   .. attribute:: distortion_model

      Distortion model used for camera lenses

      * ``POLYNOMIAL`` Polynomial, Radial distortion model which fits common cameras.
      * ``DIVISION`` Divisions, Division distortion model which better represents wide-angle cameras.

      :type: enum in ['POLYNOMIAL', 'DIVISION'], default 'POLYNOMIAL'

   .. attribute:: division_k1

      First coefficient of second order division distortion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: division_k2

      First coefficient of second order division distortion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: focal_length

      Camera's focal length

      :type: float in [0.0001, inf], default 0.0

   .. attribute:: focal_length_pixels

      Camera's focal length

      :type: float in [0, inf], default 0.0

   .. attribute:: k1

      First coefficient of third order polynomial radial distortion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: k2

      Second coefficient of third order polynomial radial distortion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: k3

      Third coefficient of third order polynomial radial distortion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: pixel_aspect

      Pixel aspect ratio

      :type: float in [0.1, inf], default 1.0

   .. attribute:: principal

      Optical center of lens

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: sensor_width

      Width of CCD sensor in millimeters

      :type: float in [0, 500], default 0.0

   .. attribute:: units

      Units used for camera focal length

      * ``PIXELS`` px, Use pixels for units of focal length.
      * ``MILLIMETERS`` mm, Use millimeters for units of focal length.

      :type: enum in ['PIXELS', 'MILLIMETERS'], default 'PIXELS'

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

   * :class:`MovieTracking.camera`

