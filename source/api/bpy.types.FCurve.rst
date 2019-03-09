FCurve(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FCurve(bpy_struct)

   F-Curve defining values of a period of time

   .. attribute:: array_index

      Index to the specific property affected by F-Curve if applicable

      :type: int in [-inf, inf], default 0

   .. attribute:: auto_smoothing

      Algorithm used to compute automatic handles

      * ``NONE`` None, Auto handles only take adjacent keys into account (legacy mode).
      * ``CONT_ACCEL`` Continuous Acceleration, Auto handles are placed to avoid jumps in acceleration.

      :type: enum in ['NONE', 'CONT_ACCEL'], default 'NONE'

   .. attribute:: color

      Color of the F-Curve in the Graph Editor

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: color_mode

      Method used to determine color of F-Curve in Graph Editor

      * ``AUTO_RAINBOW`` Auto Rainbow, Cycle through the rainbow, trying to give each curve a unique color.
      * ``AUTO_RGB`` Auto XYZ to RGB, Use axis colors for transform and color properties, and auto-rainbow for the rest.
      * ``AUTO_YRGB`` Auto WXYZ to YRGB, Use axis colors for XYZ parts of transform, and yellow for the 'W' channel.
      * ``CUSTOM`` User Defined, Use custom hand-picked color for F-Curve.

      :type: enum in ['AUTO_RAINBOW', 'AUTO_RGB', 'AUTO_YRGB', 'CUSTOM'], default 'AUTO_RAINBOW'

   .. attribute:: data_path

      RNA Path to property affected by F-Curve

      :type: string, default "", (never None)

   .. data:: driver

      Channel Driver (only set for Driver F-Curves)

      :type: :class:`Driver`, (readonly)

   .. attribute:: extrapolation

      Method used for evaluating value of F-Curve outside first and last keyframes

      * ``CONSTANT`` Constant, Hold values of endpoint keyframes.
      * ``LINEAR`` Linear, Use slope of curve leading in/out of endpoint keyframes.

      :type: enum in ['CONSTANT', 'LINEAR'], default 'CONSTANT'

   .. attribute:: group

      Action Group that this F-Curve belongs to

      :type: :class:`ActionGroup`

   .. attribute:: hide

      F-Curve and its keyframes are hidden in the Graph Editor graphs

      :type: boolean, default False

   .. attribute:: is_valid

      False when F-Curve could not be evaluated in past, so should be skipped when evaluating

      :type: boolean, default False

   .. data:: keyframe_points

      User-editable keyframes

      :type: :class:`FCurveKeyframePoints` :class:`bpy_prop_collection` of :class:`Keyframe`, (readonly)

   .. attribute:: lock

      F-Curve's settings cannot be edited

      :type: boolean, default False

   .. data:: modifiers

      Modifiers affecting the shape of the F-Curve

      :type: :class:`FCurveModifiers` :class:`bpy_prop_collection` of :class:`FModifier`, (readonly)

   .. attribute:: mute

      F-Curve is not evaluated

      :type: boolean, default False

   .. data:: sampled_points

      Sampled animation data

      :type: :class:`bpy_prop_collection` of :class:`FCurveSample`, (readonly)

   .. attribute:: select

      F-Curve is selected for editing

      :type: boolean, default False

   .. method:: evaluate(frame)

      Evaluate F-Curve

      :arg frame:

         Frame, Evaluate F-Curve at given frame

      :type frame: float in [-inf, inf]
      :return:

         Value, Value of F-Curve specific frame

      :rtype: float in [-inf, inf]

   .. method:: update()

      Ensure keyframes are sorted in chronological order and handles are set correctly


   .. method:: range()

      Get the time extents for F-Curve

      :return:

         Range, Min/Max values

      :rtype: float array of 2 items in [-inf, inf]

   .. method:: update_autoflags(data)

      Update FCurve flags set automatically from affected property (currently, integer/discrete flags set when the property is not a float)

      :arg data:

         Data, Data containing the property controlled by given FCurve

      :type data: :class:`AnyType`, (never None)

   .. method:: convert_to_samples(start, end)

      Convert current FCurve from keyframes to sample points, if necessary

      :arg start:

         Start Frame

      :type start: int in [-1048574, 1048574]
      :arg end:

         End Frame

      :type end: int in [-1048574, 1048574]

   .. method:: convert_to_keyframes(start, end)

      Convert current FCurve from sample points to keyframes (linear interpolation), if necessary

      :arg start:

         Start Frame

      :type start: int in [-1048574, 1048574]
      :arg end:

         End Frame

      :type end: int in [-1048574, 1048574]

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

   * :class:`Action.fcurves`
   * :class:`ActionFCurves.find`
   * :class:`ActionFCurves.new`
   * :class:`ActionFCurves.remove`
   * :class:`ActionGroup.channels`
   * :class:`AnimData.drivers`
   * :class:`AnimDataDrivers.find`
   * :class:`AnimDataDrivers.from_existing`
   * :class:`AnimDataDrivers.from_existing`
   * :class:`NlaStrip.fcurves`
   * :class:`NlaStripFCurves.find`

