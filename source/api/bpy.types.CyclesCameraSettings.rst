CyclesCameraSettings(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesCameraSettings(bpy_struct)

   

   .. attribute:: aperture_blades

      Number of blades in aperture for polygonal bokeh (at least 3)

      :type: int in [0, 100], default 0

   .. attribute:: aperture_fstop

      F-stop ratio (lower numbers give more defocus, higher numbers give a sharper image)

      :type: float in [0, inf], default 5.6

   .. attribute:: aperture_ratio

      Distortion to simulate anamorphic lens bokeh

      :type: float in [0.01, inf], default 1.0

   .. attribute:: aperture_rotation

      Rotation of blades in aperture

      :type: float in [-inf, inf], default 0.0

   .. attribute:: aperture_size

      Radius of the aperture for depth of field (higher values give more defocus)

      :type: float in [0, inf], default 0.0

   .. attribute:: aperture_type

      Use f-stop number or aperture radius

      * ``RADIUS`` Radius, Directly change the size of the aperture.
      * ``FSTOP`` F-stop, Change the size of the aperture by f-stop.

      :type: enum in ['RADIUS', 'FSTOP'], default 'RADIUS'

   .. attribute:: fisheye_fov

      Field of view for the fisheye lens

      :type: float in [0.1745, 31.4159], default 3.14159

   .. attribute:: fisheye_lens

      Lens focal length (mm)

      :type: float in [0.01, 100], default 10.5

   .. attribute:: latitude_max

      Maximum latitude (vertical angle) for the equirectangular lens

      :type: float in [-1.5708, 1.5708], default 1.5708

   .. attribute:: latitude_min

      Minimum latitude (vertical angle) for the equirectangular lens

      :type: float in [-1.5708, 1.5708], default -1.5708

   .. attribute:: longitude_max

      Maximum longitude (horizontal angle) for the equirectangular lens

      :type: float in [-3.14159, 3.14159], default 3.14159

   .. attribute:: longitude_min

      Minimum longitude (horizontal angle) for the equirectangular lens

      :type: float in [-3.14159, 3.14159], default -3.14159

   .. attribute:: panorama_type

      Distortion to use for the calculation

      * ``EQUIRECTANGULAR`` Equirectangular, Render the scene with a spherical camera, also known as Lat Long panorama.
      * ``FISHEYE_EQUIDISTANT`` Fisheye Equidistant, Ideal for fulldomes, ignore the sensor dimensions.
      * ``FISHEYE_EQUISOLID`` Fisheye Equisolid, Similar to most fisheye modern lens, takes sensor dimensions into consideration.
      * ``MIRRORBALL`` Mirror Ball, Uses the mirror ball mapping.

      :type: enum in ['EQUIRECTANGULAR', 'FISHEYE_EQUIDISTANT', 'FISHEYE_EQUISOLID', 'MIRRORBALL'], default 'FISHEYE_EQUISOLID'

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

