Curve(ID)
=========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

subclasses --- 
:class:`SurfaceCurve`, :class:`TextCurve`

.. class:: Curve(ID)

   Curve data-block storing curves, splines and NURBS

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: bevel_depth

      Bevel depth when not using a bevel object

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bevel_factor_end

      Factor that defines to where beveling of spline happens (0=to the very beginning, 1=to the very end)

      :type: float in [0, 1], default 0.0

   .. attribute:: bevel_factor_mapping_end

      Determines how the end bevel factor is mapped to a spline

      * ``RESOLUTION`` Resolution, Map the bevel factor to the number of subdivisions of a spline (U resolution).
      * ``SEGMENTS`` Segments, Map the bevel factor to the length of a segment and to the number of subdivisions of a segment.
      * ``SPLINE`` Spline, Map the bevel factor to the length of a spline.

      :type: enum in ['RESOLUTION', 'SEGMENTS', 'SPLINE'], default 'RESOLUTION'

   .. attribute:: bevel_factor_mapping_start

      Determines how the start bevel factor is mapped to a spline

      * ``RESOLUTION`` Resolution, Map the bevel factor to the number of subdivisions of a spline (U resolution).
      * ``SEGMENTS`` Segments, Map the bevel factor to the length of a segment and to the number of subdivisions of a segment.
      * ``SPLINE`` Spline, Map the bevel factor to the length of a spline.

      :type: enum in ['RESOLUTION', 'SEGMENTS', 'SPLINE'], default 'RESOLUTION'

   .. attribute:: bevel_factor_start

      Factor that defines from where beveling of spline happens (0=from the very beginning, 1=from the very end)

      :type: float in [0, 1], default 0.0

   .. attribute:: bevel_object

      Curve object name that defines the bevel shape

      :type: :class:`Object`

   .. attribute:: bevel_resolution

      Bevel resolution when depth is non-zero and no specific bevel object has been defined

      :type: int in [0, 32], default 0

   .. data:: cycles

      Cycles mesh settings

      :type: :class:`CyclesMeshSettings`, (readonly)

   .. attribute:: dimensions

      Select 2D or 3D curve type

      * ``2D`` 2D, Clamp the Z axis of the curve.
      * ``3D`` 3D, Allow editing on the Z axis of this curve, also allows tilt and curve radius to be used.

      :type: enum in ['2D', '3D'], default '2D'

   .. attribute:: eval_time

      Parametric position along the length of the curve that Objects 'following' it should be at (position is evaluated by dividing by the 'Path Length' value)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: extrude

      Amount of curve extrusion when not using a bevel object

      :type: float in [0, inf], default 0.0

   .. attribute:: fill_mode

      Mode of filling curve

      :type: enum in ['FULL', 'BACK', 'FRONT', 'HALF'], default 'FULL'

   .. data:: is_editmode

      True when used in editmode

      :type: boolean, default False, (readonly)

   .. data:: materials

      :type: :class:`IDMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. attribute:: offset

      Offset the curve to adjust the width of a text

      :type: float in [-inf, inf], default 0.0

   .. attribute:: path_duration

      The number of frames that are needed to traverse the path, defining the maximum value for the 'Evaluation Time' setting

      :type: int in [1, 1048574], default 0

   .. attribute:: render_resolution_u

      Surface resolution in U direction used while rendering (zero uses preview resolution)

      :type: int in [0, 1024], default 0

   .. attribute:: render_resolution_v

      Surface resolution in V direction used while rendering (zero uses preview resolution)

      :type: int in [0, 1024], default 0

   .. attribute:: resolution_u

      Surface resolution in U direction

      :type: int in [1, 1024], default 0

   .. attribute:: resolution_v

      Surface resolution in V direction

      :type: int in [1, 1024], default 0

   .. data:: shape_keys

      :type: :class:`Key`, (readonly)

   .. attribute:: show_handles

      Display Bezier handles in editmode

      :type: boolean, default False

   .. attribute:: show_normal_face

      Display 3D curve normals in editmode

      :type: boolean, default False

   .. data:: splines

      Collection of splines in this curve data object

      :type: :class:`CurveSplines` :class:`bpy_prop_collection` of :class:`Spline`, (readonly)

   .. attribute:: taper_object

      Curve object name that defines the taper (width)

      :type: :class:`Object`

   .. attribute:: texspace_location

      Texture space location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: texspace_size

      Texture space size

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: twist_mode

      The type of tilt calculation for 3D Curves

      * ``Z_UP`` Z-Up, Use Z-Up axis to calculate the curve twist at each point.
      * ``MINIMUM`` Minimum, Use the least twist over the entire curve.
      * ``TANGENT`` Tangent, Use the tangent to calculate twist.

      :type: enum in ['Z_UP', 'MINIMUM', 'TANGENT'], default 'Z_UP'

   .. attribute:: twist_smooth

      Smoothing iteration for tangents

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use_auto_texspace

      Adjust active object's texture space automatically when transforming object

      :type: boolean, default False

   .. attribute:: use_deform_bounds

      Option for curve-deform: Use the mesh bounds to clamp the deformation

      :type: boolean, default False

   .. attribute:: use_fill_caps

      Fill caps for beveled curves

      :type: boolean, default False

   .. attribute:: use_fill_deform

      Fill curve after applying shape keys and all modifiers

      :type: boolean, default False

   .. attribute:: use_map_taper

      Map effect of taper object on actually beveled curve

      :type: boolean, default False

   .. attribute:: use_path

      Enable the curve to become a translation path

      :type: boolean, default False

   .. attribute:: use_path_follow

      Make curve path children to rotate along the path

      :type: boolean, default False

   .. attribute:: use_radius

      Option for paths and curve-deform: apply the curve radius with path following it and deforming

      :type: boolean, default False

   .. attribute:: use_stretch

      Option for curve-deform: make deformed child to stretch along entire path

      :type: boolean, default False

   .. attribute:: use_uv_as_generated

      Uses the UV values as Generated textured coordinates

      :type: boolean, default False

   .. method:: transform(matrix, shape_keys=False)

      Transform curve by a matrix

      :arg matrix:

         Matrix

      :type matrix: float multi-dimensional array of 4 * 4 items in [-inf, inf]
      :arg shape_keys:

         Transform Shape Keys

      :type shape_keys: boolean, (optional)

   .. method:: validate_material_indices()

      Validate material indices of splines or letters, return True when the curve has had invalid indices corrected (to default 0)

      :return:

         Result

      :rtype: boolean

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

   * :mod:`bpy.context.curve`
   * :class:`BlendData.curves`
   * :class:`BlendDataCurves.new`
   * :class:`BlendDataCurves.remove`

