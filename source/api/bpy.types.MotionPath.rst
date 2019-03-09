MotionPath(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MotionPath(bpy_struct)

   Cache of the worldspace positions of an element over a frame range

   .. attribute:: color

      Custom color for motion path

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: frame_end

      End frame of the stored range

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: frame_start

      Starting frame of the stored range

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: is_modified

      Path is being edited

      :type: boolean, default False

   .. data:: length

      Number of frames cached

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: line_thickness

      Line thickness for drawing path

      :type: int in [1, 6], default 0

   .. attribute:: lines

      Draw straight lines between keyframe points

      :type: boolean, default False

   .. data:: points

      Cached positions per frame

      :type: :class:`bpy_prop_collection` of :class:`MotionPathVert`, (readonly)

   .. data:: use_bone_head

      For PoseBone paths, use the bone head location when calculating this path

      :type: boolean, default False, (readonly)

   .. attribute:: use_custom_color

      Use custom color for this motion path

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

   * :class:`Object.motion_path`
   * :class:`PoseBone.motion_path`

