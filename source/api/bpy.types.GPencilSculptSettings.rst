GPencilSculptSettings(bpy_struct)
=================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilSculptSettings(bpy_struct)

   Properties for Grease Pencil stroke sculpting tool

   .. attribute:: affect_position

      The brush affects the position of the point

      :type: boolean, default False

   .. attribute:: affect_strength

      The brush affects the color strength of the point

      :type: boolean, default False

   .. attribute:: affect_thickness

      The brush affects the thickness of the point

      :type: boolean, default False

   .. data:: brush

      :type: :class:`GPencilSculptBrush`, (readonly)

   .. attribute:: lockaxis

      * ``GP_LOCKAXIS_NONE`` None.
      * ``GP_LOCKAXIS_X`` X, Project strokes to plane locked to X.
      * ``GP_LOCKAXIS_Y`` Y, Project strokes to plane locked to Y.
      * ``GP_LOCKAXIS_Z`` Z, Project strokes to plane locked to Z.

      :type: enum in ['GP_LOCKAXIS_NONE', 'GP_LOCKAXIS_X', 'GP_LOCKAXIS_Y', 'GP_LOCKAXIS_Z'], default 'GP_LOCKAXIS_NONE'

   .. attribute:: selection_alpha

      Alpha value for selected vertices

      :type: float in [0, 1], default 0.0

   .. attribute:: tool

      * ``SMOOTH`` Smooth, Smooth stroke points.
      * ``THICKNESS`` Thickness, Adjust thickness of strokes.
      * ``STRENGTH`` Strength, Adjust color strength of strokes.
      * ``GRAB`` Grab, Translate the set of points initially within the brush circle.
      * ``PUSH`` Push, Move points out of the way, as if combing them.
      * ``TWIST`` Twist, Rotate points around the midpoint of the brush.
      * ``PINCH`` Pinch, Pull points towards the midpoint of the brush.
      * ``RANDOMIZE`` Randomize, Introduce jitter/randomness into strokes.
      * ``CLONE`` Clone, Paste copies of the strokes stored on the clipboard.

      :type: enum in ['SMOOTH', 'THICKNESS', 'STRENGTH', 'GRAB', 'PUSH', 'TWIST', 'PINCH', 'RANDOMIZE', 'CLONE'], default 'SMOOTH'

   .. attribute:: use_select_mask

      Only sculpt selected stroke points

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

   * :class:`ToolSettings.gpencil_sculpt`

