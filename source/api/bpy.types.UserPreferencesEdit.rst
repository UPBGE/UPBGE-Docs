UserPreferencesEdit(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserPreferencesEdit(bpy_struct)

   Settings for interacting with Blender data

   .. attribute:: auto_keying_mode

      Mode of automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)

      :type: enum in ['ADD_REPLACE_KEYS', 'REPLACE_KEYS'], default 'ADD_REPLACE_KEYS'

   .. attribute:: fcurve_unselected_alpha

      Amount that unselected F-Curves stand out from the background (Graph Editor)

      :type: float in [0.001, 1], default 0.0

   .. attribute:: grease_pencil_default_color

      Color of new Grease Pencil layers

      :type: float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: grease_pencil_eraser_radius

      Radius of eraser 'brush'

      :type: int in [1, 500], default 0

   .. attribute:: grease_pencil_euclidean_distance

      Distance moved by mouse when drawing stroke to include

      :type: int in [0, 100], default 0

   .. attribute:: grease_pencil_manhattan_distance

      Pixels moved by mouse per axis when drawing stroke

      :type: int in [0, 100], default 0

   .. attribute:: keyframe_new_handle_type

      Handle type for handles of new keyframes

      * ``FREE`` Free.
      * ``VECTOR`` Vector.
      * ``ALIGNED`` Aligned.
      * ``AUTO`` Automatic.
      * ``AUTO_CLAMPED`` Auto Clamped, Auto handles clamped to not overshoot.

      :type: enum in ['FREE', 'VECTOR', 'ALIGNED', 'AUTO', 'AUTO_CLAMPED'], default 'FREE'

   .. attribute:: keyframe_new_interpolation_type

      Interpolation mode used for first keyframe on newly added F-Curves (subsequent keyframes take interpolation from preceding keyframe)

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

   .. attribute:: material_link

      Toggle whether the material is linked to object data or the object block

      * ``OBDATA`` ObData, Toggle whether the material is linked to object data or the object block.
      * ``OBJECT`` Object, Toggle whether the material is linked to object data or the object block.

      :type: enum in ['OBDATA', 'OBJECT'], default 'OBDATA'

   .. attribute:: node_margin

      Minimum distance between nodes for Auto-offsetting nodes

      :type: int in [0, 255], default 0

   .. attribute:: object_align

      When adding objects from a 3D View menu, either align them with that view or with the world

      * ``WORLD`` World, Align newly added objects to the world coordinate system.
      * ``VIEW`` View, Align newly added objects facing the active 3D View direction.

      :type: enum in ['WORLD', 'VIEW'], default 'WORLD'

   .. attribute:: sculpt_paint_overlay_color

      Color of texture overlay

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: undo_memory_limit

      Maximum memory usage in megabytes (0 means unlimited)

      :type: int in [0, 32767], default 0

   .. attribute:: undo_steps

      Number of undo steps available (smaller values conserve memory)

      :type: int in [0, 256], default 0

   .. attribute:: use_auto_keying

      Automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)

      :type: boolean, default False

   .. attribute:: use_auto_keying_warning

      Show warning indicators when transforming objects and bones if auto keying is enabled

      :type: boolean, default False

   .. attribute:: use_drag_immediately

      Moving things with a mouse drag confirms when releasing the button

      :type: boolean, default False

   .. attribute:: use_duplicate_action

      Causes actions to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_armature

      Causes armature data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_curve

      Causes curve data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_fcurve

      Causes F-curve data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_lamp

      Causes lamp data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_material

      Causes material data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_mesh

      Causes mesh data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_metaball

      Causes metaball data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_particle

      Causes particle systems to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_surface

      Causes surface data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_text

      Causes text data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_duplicate_texture

      Causes texture data to be duplicated with the object

      :type: boolean, default False

   .. attribute:: use_enter_edit_mode

      Enter Edit Mode automatically after adding a new object

      :type: boolean, default False

   .. attribute:: use_global_undo

      Global undo works by keeping a full copy of the file itself in memory, so takes extra memory

      :type: boolean, default False

   .. attribute:: use_grease_pencil_simplify_stroke

      Simplify the final stroke

      :type: boolean, default False

   .. attribute:: use_insertkey_xyz_to_rgb

      Color for newly added transformation F-Curves (Location, Rotation, Scale) and also Color is based on the transform axis

      :type: boolean, default False

   .. attribute:: use_keyframe_insert_available

      Automatic keyframe insertion in available F-Curves

      :type: boolean, default False

   .. attribute:: use_keyframe_insert_needed

      Keyframe insertion only when keyframe needed

      :type: boolean, default False

   .. attribute:: use_negative_frames

      Current frame number can be manually set to a negative value

      :type: boolean, default False

   .. attribute:: use_visual_keying

      Use Visual keying automatically for constrained objects

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

   * :class:`UserPreferences.edit`

