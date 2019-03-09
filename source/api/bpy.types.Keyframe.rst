Keyframe(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Keyframe(bpy_struct)

   Bezier curve point with two handles defining a Keyframe on an F-Curve

   .. attribute:: amplitude

      Amount to boost elastic bounces for 'elastic' easing

      :type: float in [0, inf], default 0.0

   .. attribute:: back

      Amount of overshoot for 'back' easing

      :type: float in [-inf, inf], default 0.0

   .. attribute:: co

      Coordinates of the control point

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: easing

      Which ends of the segment between this and the next keyframe easing interpolation is applied to

      * ``AUTO`` Automatic Easing, Easing type is chosen automatically based on what the type of interpolation used (e.g. 'Ease In' for transitional types, and 'Ease Out' for dynamic effects).
      * ``EASE_IN`` Ease In, Only on the end closest to the next keyframe.
      * ``EASE_OUT`` Ease Out, Only on the end closest to the first keyframe.
      * ``EASE_IN_OUT`` Ease In and Out, Segment between both keyframes.

      :type: enum in ['AUTO', 'EASE_IN', 'EASE_OUT', 'EASE_IN_OUT'], default 'AUTO'

   .. attribute:: handle_left

      Coordinates of the left handle (before the control point)

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: handle_left_type

      Handle types

      * ``FREE`` Free.
      * ``VECTOR`` Vector.
      * ``ALIGNED`` Aligned.
      * ``AUTO`` Automatic.
      * ``AUTO_CLAMPED`` Auto Clamped, Auto handles clamped to not overshoot.

      :type: enum in ['FREE', 'VECTOR', 'ALIGNED', 'AUTO', 'AUTO_CLAMPED'], default 'FREE'

   .. attribute:: handle_right

      Coordinates of the right handle (after the control point)

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: handle_right_type

      Handle types

      * ``FREE`` Free.
      * ``VECTOR`` Vector.
      * ``ALIGNED`` Aligned.
      * ``AUTO`` Automatic.
      * ``AUTO_CLAMPED`` Auto Clamped, Auto handles clamped to not overshoot.

      :type: enum in ['FREE', 'VECTOR', 'ALIGNED', 'AUTO', 'AUTO_CLAMPED'], default 'FREE'

   .. attribute:: interpolation

      Interpolation method to use for segment of the F-Curve from this Keyframe until the next Keyframe

      * ``CONSTANT`` Constant, No interpolation, value of A gets held until B is encountered.
      * ``LINEAR`` Linear, Straight-line interpolation between A and B (i.e. no ease in/out).
      * ``BEZIER`` Bezier, Smooth interpolation between A and B, with some control over curve shape.
      * ``SINE`` Sinusoidal, Sinusoidal easing (weakest, almost linear but with a slight curvature).
      * ``QUAD`` Quadratic, Quadratic easing.
      * ``CUBIC`` Cubic, Cubic easing.
      * ``QUART`` Quartic, Quartic easing.
      * ``QUINT`` Quintic, Quintic easing.
      * ``EXPO`` Exponential, Exponential easing (dramatic).
      * ``CIRC`` Circular, Circular easing (strongest and most dynamic).
      * ``BACK`` Back, Cubic easing with overshoot and settle.
      * ``BOUNCE`` Bounce, Exponentially decaying parabolic bounce, like when objects collide.
      * ``ELASTIC`` Elastic, Exponentially decaying sine wave, like an elastic band.

      :type: enum in ['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC'], default 'CONSTANT'

   .. attribute:: period

      Time between bounces for elastic easing

      :type: float in [-inf, inf], default 0.0

   .. attribute:: select_control_point

      Control point selection status

      :type: boolean, default False

   .. attribute:: select_left_handle

      Left handle selection status

      :type: boolean, default False

   .. attribute:: select_right_handle

      Right handle selection status

      :type: boolean, default False

   .. attribute:: type

      Type of keyframe (for visual purposes only)

      * ``KEYFRAME`` Keyframe, Normal keyframe - e.g. for key poses.
      * ``BREAKDOWN`` Breakdown, A breakdown pose - e.g. for transitions between key poses.
      * ``MOVING_HOLD`` Moving Hold, A keyframe that is part of a moving hold.
      * ``EXTREME`` Extreme, An 'extreme' pose, or some other purpose as needed.
      * ``JITTER`` Jitter, A filler or baked keyframe for keying on ones, or some other purpose as needed.

      :type: enum in ['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER'], default 'KEYFRAME'

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

   * :class:`FCurve.keyframe_points`
   * :class:`FCurveKeyframePoints.insert`
   * :class:`FCurveKeyframePoints.remove`

