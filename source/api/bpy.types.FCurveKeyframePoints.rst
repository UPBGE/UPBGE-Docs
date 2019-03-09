FCurveKeyframePoints(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FCurveKeyframePoints(bpy_struct)

   Collection of keyframe points

   .. method:: insert(frame, value, options={}, keyframe_type='KEYFRAME')

      Add a keyframe point to a F-Curve

      :arg frame:

         X Value of this keyframe point

      :type frame: float in [-inf, inf]
      :arg value:

         Y Value of this keyframe point

      :type value: float in [-inf, inf]
      :arg options:

         Keyframe options

         * ``REPLACE`` Replace, Don't add any new keyframes, but just replace existing ones.
         * ``NEEDED`` Needed, Only adds keyframes that are needed.
         * ``FAST`` Fast, Fast keyframe insertion to avoid recalculating the curve each time.

      :type options: enum set in {'REPLACE', 'NEEDED', 'FAST'}, (optional)
      :arg keyframe_type:

         Type of keyframe to insert

         * ``KEYFRAME`` Keyframe, Normal keyframe - e.g. for key poses.
         * ``BREAKDOWN`` Breakdown, A breakdown pose - e.g. for transitions between key poses.
         * ``MOVING_HOLD`` Moving Hold, A keyframe that is part of a moving hold.
         * ``EXTREME`` Extreme, An 'extreme' pose, or some other purpose as needed.
         * ``JITTER`` Jitter, A filler or baked keyframe for keying on ones, or some other purpose as needed.

      :type keyframe_type: enum in ['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER'], (optional)
      :return:

         Newly created keyframe

      :rtype: :class:`Keyframe`

   .. method:: add(count=1)

      Add a keyframe point to a F-Curve

      :arg count:

         Number, Number of points to add to the spline

      :type count: int in [0, inf], (optional)

   .. method:: remove(keyframe, fast=False)

      Remove keyframe from an F-Curve

      :arg keyframe:

         Keyframe to remove

      :type keyframe: :class:`Keyframe`, (never None)
      :arg fast:

         Fast, Fast keyframe removal to avoid recalculating the curve each time

      :type fast: boolean, (optional)

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

