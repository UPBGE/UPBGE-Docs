GPencilLayer(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilLayer(bpy_struct)

   Collection of related sketches

   .. data:: active_frame

      Frame currently being displayed for this layer

      :type: :class:`GPencilFrame`, (readonly)

   .. attribute:: after_color

      Base color for ghosts after the active frame

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: before_color

      Base color for ghosts before the active frame

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: frames

      Sketches for this layer on different frames

      :type: :class:`GPencilFrames` :class:`bpy_prop_collection` of :class:`GPencilFrame`, (readonly)

   .. attribute:: ghost_after_range

      Maximum number of frames to show after current frame (0 = show only the next sketch, -1 = don't show any frames after current)

      :type: int in [-1, 120], default 0

   .. attribute:: ghost_before_range

      Maximum number of frames to show before current frame (0 = show only the previous sketch, -1 = don't show any frames before current)

      :type: int in [-1, 120], default 0

   .. attribute:: hide

      Set layer Visibility

      :type: boolean, default False

   .. attribute:: info

      Layer name

      :type: string, default "", (never None)

   .. data:: is_parented

      True when the layer parent object is set

      :type: boolean, default False, (readonly)

   .. attribute:: line_change

      Thickness change to apply to current strokes (in pixels)

      :type: int in [-32768, 32767], default 0

   .. attribute:: lock

      Protect layer from further editing and/or frame changes

      :type: boolean, default False

   .. attribute:: lock_frame

      Lock current frame displayed by layer

      :type: boolean, default False

   .. attribute:: matrix_inverse

      Parent inverse transformation matrix

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: opacity

      Layer Opacity

      :type: float in [0, 1], default 0.0

   .. attribute:: parent

      Parent Object

      :type: :class:`Object`

   .. attribute:: parent_bone

      Name of parent bone in case of a bone parenting relation

      :type: string, default "", (never None)

   .. attribute:: parent_type

      Type of parent relation

      * ``OBJECT`` Object, The layer is parented to an object.
      * ``ARMATURE`` Armature.
      * ``BONE`` Bone, The layer is parented to a bone.

      :type: enum in ['OBJECT', 'ARMATURE', 'BONE'], default 'OBJECT'

   .. attribute:: select

      Layer is selected for editing in the Dope Sheet

      :type: boolean, default False

   .. attribute:: show_points

      Draw the points which make up the strokes (for debugging purposes)

      :type: boolean, default False

   .. attribute:: show_x_ray

      Make the layer draw in front of objects

      :type: boolean, default False

   .. attribute:: tint_color

      Color for tinting stroke colors

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tint_factor

      Factor of tinting color

      :type: float in [0, 1], default 0.0

   .. attribute:: unlock_color

      Unprotect selected colors from further editing and/or frame changes

      :type: boolean, default False

   .. attribute:: use_ghost_custom_colors

      Use custom colors for ghost frames

      :type: boolean, default False

   .. attribute:: use_ghosts_always

      Ghosts are shown in renders and animation playback. Useful for special effects (e.g. motion blur)

      :type: boolean, default False

   .. attribute:: use_onion_skinning

      Ghost frames on either side of frame

      :type: boolean, default False

   .. attribute:: use_volumetric_strokes

      Draw strokes as a series of circular blobs, resulting in a volumetric effect

      :type: boolean, default False

   .. method:: clear()

      Remove all the grease pencil layer data


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

   * :mod:`bpy.context.active_gpencil_layer`
   * :mod:`bpy.context.editable_gpencil_layers`
   * :mod:`bpy.context.visible_gpencil_layers`
   * :class:`GreasePencil.layers`
   * :class:`GreasePencilLayers.active`
   * :class:`GreasePencilLayers.new`
   * :class:`GreasePencilLayers.remove`

