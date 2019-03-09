Bone(bpy_struct)
================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Bone(bpy_struct)

   Bone in an Armature data-block

   .. attribute:: bbone_curveinx

      X-axis handle offset for start of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_curveiny

      Y-axis handle offset for start of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_curveoutx

      X-axis handle offset for end of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_curveouty

      Y-axis handle offset for end of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_easein

      Length of first Bezier Handle (for B-Bones only)

      :type: float in [-5, 5], default 1.0

   .. attribute:: bbone_easeout

      Length of second Bezier Handle (for B-Bones only)

      :type: float in [-5, 5], default 1.0

   .. attribute:: bbone_rollin

      Roll offset for the start of the B-Bone, adjusts twist

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: bbone_rollout

      Roll offset for the end of the B-Bone, adjusts twist

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: bbone_scalein

      Scale factor for start of the B-Bone, adjusts thickness (for tapering effects)

      :type: float in [0, 5], default 1.0

   .. attribute:: bbone_scaleout

      Scale factor for end of the B-Bone, adjusts thickness (for tapering effects)

      :type: float in [0, 5], default 1.0

   .. attribute:: bbone_segments

      Number of subdivisions of bone (for B-Bones only)

      :type: int in [1, 32], default 0

   .. attribute:: bbone_x

      B-Bone X size

      :type: float in [0, 1000], default 0.0

   .. attribute:: bbone_z

      B-Bone Z size

      :type: float in [0, 1000], default 0.0

   .. data:: children

      Bones which are children of this bone

      :type: :class:`bpy_prop_collection` of :class:`Bone`, (readonly)

   .. attribute:: envelope_distance

      Bone deformation distance (for Envelope deform only)

      :type: float in [0, 1000], default 0.0

   .. attribute:: envelope_weight

      Bone deformation weight (for Envelope deform only)

      :type: float in [0, 1000], default 0.0

   .. attribute:: head

      Location of head end of the bone relative to its parent

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: head_local

      Location of head end of the bone relative to armature

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: head_radius

      Radius of head of bone (for Envelope deform only)

      :type: float in [0, inf], default 0.0

   .. attribute:: hide

      Bone is not visible when it is not in Edit Mode (i.e. in Object or Pose Modes)

      :type: boolean, default False

   .. attribute:: hide_select

      Bone is able to be selected

      :type: boolean, default False

   .. attribute:: layers

      Layers bone exists in

      :type: boolean array of 32 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: matrix

      3x3 bone matrix

      :type: float multi-dimensional array of 3 * 3 items in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

   .. attribute:: matrix_local

      4x4 bone matrix relative to armature

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: name

      :type: string, default "", (never None)

   .. data:: parent

      Parent bone (in same Armature)

      :type: :class:`Bone`, (readonly)

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: select_head

      :type: boolean, default False

   .. attribute:: select_tail

      :type: boolean, default False

   .. attribute:: show_wire

      Bone is always drawn as Wireframe regardless of viewport draw mode (useful for non-obstructive custom bone shapes)

      :type: boolean, default False

   .. attribute:: tail

      Location of tail end of the bone

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: tail_local

      Location of tail end of the bone relative to armature

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: tail_radius

      Radius of tail of bone (for Envelope deform only)

      :type: float in [0, inf], default 0.0

   .. data:: use_connect

      When bone has a parent, bone's head is stuck to the parent's tail

      :type: boolean, default False, (readonly)

   .. attribute:: use_cyclic_offset

      When bone doesn't have a parent, it receives cyclic offset effects (Deprecated)

      :type: boolean, default False

   .. attribute:: use_deform

      Enable Bone to deform geometry

      :type: boolean, default False

   .. attribute:: use_endroll_as_inroll

      Use Roll Out of parent bone as Roll In of its children

      :type: boolean, default False

   .. attribute:: use_envelope_multiply

      When deforming bone, multiply effects of Vertex Group weights with Envelope influence

      :type: boolean, default False

   .. attribute:: use_inherit_rotation

      Bone inherits rotation or scale from parent bone

      :type: boolean, default False

   .. attribute:: use_inherit_scale

      Bone inherits scaling from parent bone

      :type: boolean, default False

   .. attribute:: use_local_location

      Bone location is set in local space

      :type: boolean, default False

   .. attribute:: use_relative_parent

      Object children will use relative transform, like deform

      :type: boolean, default False

   .. data:: basename

      The name of this bone before any '.' character
      (readonly)

   .. data:: center

      The midpoint between the head and the tail.
      (readonly)

   .. data:: children

      A list of all the bones children.
      (readonly)

   .. data:: children_recursive

      A list of all children from this bone.
      (readonly)

   .. data:: children_recursive_basename

      Returns a chain of children with the same base name as this bone.
      Only direct chains are supported, forks caused by multiple children
      with matching base names will terminate the function
      and not be returned.
      (readonly)

   .. attribute:: length

      The distance from head to tail,
      when set the head is moved to fit the length.

   .. data:: parent_recursive

      A list of parents, starting with the immediate parent
      (readonly)

   .. data:: vector

      The direction this bone is pointing.
      Utility function for (tail - head)
      (readonly)

   .. data:: x_axis

      Vector pointing down the x-axis of the bone.
      (readonly)

   .. data:: y_axis

      Vector pointing down the y-axis of the bone.
      (readonly)

   .. data:: z_axis

      Vector pointing down the z-axis of the bone.
      (readonly)

   .. method:: evaluate_envelope(point)

      Calculate bone envelope at given point

      :arg point:

         Point, Position in 3d space to evaluate

      :type point: float array of 3 items in [-inf, inf]
      :return:

         Factor, Envelope factor

      :rtype: float in [-inf, inf]

   .. method:: parent_index(parent_test)

      The same as 'bone in other_bone.parent_recursive'
      but saved generating a list.

   .. method:: translate(vec)

      Utility function to add *vec* to the head and tail of this bone

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

   * :mod:`bpy.context.bone`
   * :class:`Armature.bones`
   * :class:`ArmatureBones.active`
   * :class:`Bone.children`
   * :class:`Bone.parent`
   * :class:`PoseBone.bone`

