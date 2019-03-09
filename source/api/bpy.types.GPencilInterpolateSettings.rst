GPencilInterpolateSettings(bpy_struct)
======================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilInterpolateSettings(bpy_struct)

   Settings for Grease Pencil interpolation tools

   .. attribute:: amplitude

      Amount to boost elastic bounces for 'elastic' easing

      :type: float in [0, inf], default 0.0

   .. attribute:: back

      Amount of overshoot for 'back' easing

      :type: float in [-inf, inf], default 0.0

   .. attribute:: easing

      Which ends of the segment between the preceding and following grease pencil frames easing interpolation is applied to

      * ``AUTO`` Automatic Easing, Easing type is chosen automatically based on what the type of interpolation used (e.g. 'Ease In' for transitional types, and 'Ease Out' for dynamic effects).
      * ``EASE_IN`` Ease In, Only on the end closest to the next keyframe.
      * ``EASE_OUT`` Ease Out, Only on the end closest to the first keyframe.
      * ``EASE_IN_OUT`` Ease In and Out, Segment between both keyframes.

      :type: enum in ['AUTO', 'EASE_IN', 'EASE_OUT', 'EASE_IN_OUT'], default 'AUTO'

   .. attribute:: interpolate_all_layers

      Interpolate all layers, not only active

      :type: boolean, default False

   .. attribute:: interpolate_selected_only

      Interpolate only selected strokes in the original frame

      :type: boolean, default False

   .. data:: interpolation_curve

      Custom curve to control 'sequence' interpolation between Grease Pencil frames

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: period

      Time between bounces for elastic easing

      :type: float in [-inf, inf], default 0.0

   .. attribute:: type

      Interpolation method to use the next time 'Interpolate Sequence' is run

      * ``LINEAR`` Linear, Straight-line interpolation between A and B (i.e. no ease in/out).
      * ``CUSTOM`` Custom, Custom interpolation defined using a curve map.
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

      :type: enum in ['LINEAR', 'CUSTOM', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC'], default 'LINEAR'

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

   * :class:`ToolSettings.gpencil_interpolate`

