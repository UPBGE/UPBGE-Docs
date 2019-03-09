Armature(ID)
============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Armature(ID)

   Armature data-block containing a hierarchy of bones, usually used for rigging characters

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: bones

      :type: :class:`ArmatureBones` :class:`bpy_prop_collection` of :class:`Bone`, (readonly)

   .. attribute:: deform_method

      Vertex Deformer Method (Game Engine only)

      * ``BLENDER`` Blender, Use Blender's armature vertex deformation.
      * ``BGE_CPU`` BGE, Use vertex deformation code optimized for the BGE.

      :type: enum in ['BLENDER', 'BGE_CPU'], default 'BLENDER'

   .. attribute:: draw_type

      * ``OCTAHEDRAL`` Octahedral, Display bones as octahedral shape (default).
      * ``STICK`` Stick, Display bones as simple 2D lines with dots.
      * ``BBONE`` B-Bone, Display bones as boxes, showing subdivision and B-Splines.
      * ``ENVELOPE`` Envelope, Display bones as extruded spheres, showing deformation influence volume.
      * ``WIRE`` Wire, Display bones as thin wires, showing subdivision and B-Splines.

      :type: enum in ['OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE'], default 'OCTAHEDRAL'

   .. data:: edit_bones

      :type: :class:`ArmatureEditBones` :class:`bpy_prop_collection` of :class:`EditBone`, (readonly)

   .. attribute:: ghost_frame_end

      End frame of range of Ghosts to display (not for 'Around Current Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: ghost_frame_start

      Starting frame of range of Ghosts to display (not for 'Around Current Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: ghost_size

      Frame step for Ghosts (not for 'On Keyframes' Onion-skinning method)

      :type: int in [1, 20], default 0

   .. attribute:: ghost_step

      Number of frame steps on either side of current frame to show as ghosts (only for 'Around Current Frame' Onion-skinning method)

      :type: int in [0, 30], default 0

   .. attribute:: ghost_type

      Method of Onion-skinning for active Action

      * ``CURRENT_FRAME`` Around Frame, Display Ghosts of poses within a fixed number of frames around the current frame.
      * ``RANGE`` In Range, Display Ghosts of poses within specified range.
      * ``KEYS`` On Keyframes, Display Ghosts of poses on Keyframes.

      :type: enum in ['CURRENT_FRAME', 'RANGE', 'KEYS'], default 'CURRENT_FRAME'

   .. data:: is_editmode

      True when used in editmode

      :type: boolean, default False, (readonly)

   .. attribute:: layers

      Armature layer visibility

      :type: boolean array of 32 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: layers_protected

      Protected layers in Proxy Instances are restored to Proxy settings on file reload and undo

      :type: boolean array of 32 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: pose_position

      Show armature in binding pose or final posed state

      * ``POSE`` Pose Position, Show armature in posed state.
      * ``REST`` Rest Position, Show Armature in binding pose state (no posing possible).

      :type: enum in ['POSE', 'REST'], default 'POSE'

   .. attribute:: show_axes

      Draw bone axes

      :type: boolean, default False

   .. attribute:: show_bone_custom_shapes

      Draw bones with their custom shapes

      :type: boolean, default False

   .. attribute:: show_group_colors

      Draw bone group colors

      :type: boolean, default False

   .. attribute:: show_names

      Draw bone names

      :type: boolean, default False

   .. attribute:: show_only_ghost_selected

      :type: boolean, default False

   .. attribute:: use_auto_ik

      Add temporary IK constraints while grabbing bones in Pose Mode

      :type: boolean, default False

   .. attribute:: use_deform_delay

      Don't deform children when manipulating bones in Pose Mode

      :type: boolean, default False

   .. attribute:: use_mirror_x

      Apply changes to matching bone on opposite side of X-Axis

      :type: boolean, default False

   .. method:: transform(matrix)

      Transform armature bones by a matrix

      :arg matrix:

         Matrix

      :type matrix: float multi-dimensional array of 4 * 4 items in [-inf, inf]

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

   * :mod:`bpy.context.armature`
   * :class:`BlendData.armatures`
   * :class:`BlendDataArmatures.new`
   * :class:`BlendDataArmatures.remove`

