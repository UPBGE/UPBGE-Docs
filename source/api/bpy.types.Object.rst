Object(ID)
==========

.. module:: bpy.types

Basic Object Operations Example
+++++++++++++++++++++++++++++++

This script demonstrates basic operations on object like creating new
object, placing it into scene, selecting it and making it active.

.. literalinclude:: ..\examples\bpy.types.Object.py
   :lines: 8-

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Object(ID)

   Object data-block defining an object in a scene

   .. attribute:: active_material

      Active material being displayed

      :type: :class:`Material`

   .. attribute:: active_material_index

      Index of active material slot

      :type: int in [0, inf], default 0

   .. data:: active_shape_key

      Current shape key

      :type: :class:`ShapeKey`, (readonly)

   .. attribute:: active_shape_key_index

      Current shape key index

      :type: int in [-32768, 32767], default 0

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: animation_visualization

      Animation data for this data-block

      :type: :class:`AnimViz`, (readonly, never None)

   .. data:: bound_box

      Object's bounding box in object-space coordinates, all values are -1.0 when not available

      :type: float multi-dimensional array of 8 * 3 items in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), (readonly)

   .. data:: collision

      Settings for using the object as a collider in physics simulation

      :type: :class:`CollisionSettings`, (readonly)

   .. attribute:: color

      Object color and alpha, used when faces have the ObColor mode enabled

      :type: float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

   .. data:: constraints

      Constraints affecting the transformation of the object

      :type: :class:`ObjectConstraints` :class:`bpy_prop_collection` of :class:`Constraint`, (readonly)

   .. data:: cycles

      Cycles object settings

      :type: :class:`CyclesObjectSettings`, (readonly)

   .. data:: cycles_visibility

      Cycles visibility settings

      :type: :class:`CyclesVisibilitySettings`, (readonly)

   .. attribute:: data

      Object data

      :type: :class:`ID`

   .. attribute:: delta_location

      Extra translation added to the location of the object

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: delta_rotation_euler

      Extra rotation added to the rotation of the object (when using Euler rotations)

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: delta_rotation_quaternion

      Extra rotation added to the rotation of the object (when using Quaternion rotations)

      :type: float array of 4 items in [-inf, inf], default (1.0, 0.0, 0.0, 0.0)

   .. attribute:: delta_scale

      Extra scaling added to the scale of the object

      :type: float array of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. attribute:: dimensions

      Absolute bounding box dimensions of the object

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: draw_bounds_type

      Object boundary display type

      * ``BOX`` Box, Draw bounds as box.
      * ``SPHERE`` Sphere, Draw bounds as sphere.
      * ``CYLINDER`` Cylinder, Draw bounds as cylinder.
      * ``CONE`` Cone, Draw bounds as cone.
      * ``CAPSULE`` Capsule, Draw bounds as capsule.

      :type: enum in ['BOX', 'SPHERE', 'CYLINDER', 'CONE', 'CAPSULE'], default 'BOX'

   .. attribute:: draw_type

      Maximum draw type to display object with in viewport

      * ``BOUNDS`` Bounds, Draw the bounds of the object.
      * ``WIRE`` Wire, Draw the object as a wireframe.
      * ``SOLID`` Solid, Draw the object as a solid (if solid drawing is enabled in the viewport).
      * ``TEXTURED`` Textured, Draw the object with textures (if textures are enabled in the viewport).

      :type: enum in ['BOUNDS', 'WIRE', 'SOLID', 'TEXTURED'], default 'BOUNDS'

   .. attribute:: dupli_faces_scale

      Scale the DupliFace objects

      :type: float in [0.001, 10000], default 0.0

   .. attribute:: dupli_frames_end

      End frame for DupliFrames

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: dupli_frames_off

      Recurring frames to exclude from the Dupliframes

      :type: int in [0, 1048574], default 0

   .. attribute:: dupli_frames_on

      Number of frames to use between DupOff frames

      :type: int in [0, 1048574], default 0

   .. attribute:: dupli_frames_start

      Start frame for DupliFrames

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: dupli_group

      Instance an existing group

      :type: :class:`Group`

   .. data:: dupli_list

      Object duplis

      :type: :class:`bpy_prop_collection` of :class:`DupliObject`, (readonly)

   .. attribute:: dupli_type

      If not None, object duplication method to use

      * ``NONE`` None.
      * ``FRAMES`` Frames, Make copy of object for every frame.
      * ``VERTS`` Verts, Duplicate child objects on all vertices.
      * ``FACES`` Faces, Duplicate child objects on all faces.
      * ``GROUP`` Group, Enable group instancing.

      :type: enum in ['NONE', 'FRAMES', 'VERTS', 'FACES', 'GROUP'], default 'NONE'

   .. attribute:: empty_draw_size

      Size of display for empties in the viewport

      :type: float in [0.0001, 1000], default 0.0

   .. attribute:: empty_draw_type

      Viewport display style for empties

      :type: enum in ['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE', 'IMAGE'], default 'PLAIN_AXES'

   .. attribute:: empty_image_offset

      Origin offset distance

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. data:: field

      Settings for using the object as a field in physics simulation

      :type: :class:`FieldSettings`, (readonly)

   .. data:: game

      Game engine related settings for the object

      :type: :class:`GameObjectSettings`, (readonly, never None)

   .. attribute:: grease_pencil

      Grease Pencil data-block

      :type: :class:`GreasePencil`

   .. attribute:: hide

      Restrict visibility in the viewport

      :type: boolean, default False

   .. attribute:: hide_render

      Restrict renderability

      :type: boolean, default False

   .. attribute:: hide_select

      Restrict selection in the viewport

      :type: boolean, default False

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly, never None)

   .. data:: is_duplicator

      :type: boolean, default False, (readonly)

   .. attribute:: layers

      Layers the object is on

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. data:: layers_local_view

      3D local view layers the object is on

      :type: boolean array of 8 items, default (False, False, False, False, False, False, False, False), (readonly)

   .. attribute:: location

      Location of the object

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: lock_location

      Lock editing of location in the interface

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation

      Lock editing of rotation in the interface

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation_w

      Lock editing of 'angle' component of four-component rotations in the interface

      :type: boolean, default False

   .. attribute:: lock_rotations_4d

      Lock editing of four component rotations by components (instead of as Eulers)

      :type: boolean, default False

   .. attribute:: lock_scale

      Lock editing of scale in the interface

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lod_factor

      The factor applied to distance computed in Lod

      :type: float in [0, inf], default 1.0

   .. data:: lod_levels

      A collection of detail levels to automatically switch between

      :type: :class:`bpy_prop_collection` of :class:`LodLevel`, (readonly)

   .. data:: material_slots

      Material slots in the object

      :type: :class:`bpy_prop_collection` of :class:`MaterialSlot`, (readonly)

   .. attribute:: matrix_basis

      Matrix access to location, rotation and scale (including deltas), before constraints and parenting are applied

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_local

      Parent relative transformation matrix - WARNING: Only takes into account 'Object' parenting, so e.g. in case of bone parenting you get a matrix relative to the Armature object, not to the actual parent bone

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_parent_inverse

      Inverse of object's parent matrix at time of parenting

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_world

      Worldspace transformation matrix

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. data:: mode

      Object interaction mode

      * ``OBJECT`` Object Mode.
      * ``EDIT`` Edit Mode.
      * ``POSE`` Pose Mode.
      * ``SCULPT`` Sculpt Mode.
      * ``VERTEX_PAINT`` Vertex Paint.
      * ``WEIGHT_PAINT`` Weight Paint.
      * ``TEXTURE_PAINT`` Texture Paint.
      * ``PARTICLE_EDIT`` Particle Edit.
      * ``GPENCIL_EDIT`` Edit Strokes, Edit Grease Pencil Strokes.

      :type: enum in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'GPENCIL_EDIT'], default 'OBJECT', (readonly)

   .. data:: modifiers

      Modifiers affecting the geometric data of the object

      :type: :class:`ObjectModifiers` :class:`bpy_prop_collection` of :class:`Modifier`, (readonly)

   .. data:: motion_path

      Motion Path for this element

      :type: :class:`MotionPath`, (readonly)

   .. attribute:: parent

      Parent Object

      :type: :class:`Object`

   .. attribute:: parent_bone

      Name of parent bone in case of a bone parenting relation

      :type: string, default "", (never None)

   .. attribute:: parent_type

      Type of parent relation

      * ``OBJECT`` Object, The object is parented to an object.
      * ``ARMATURE`` Armature.
      * ``LATTICE`` Lattice, The object is parented to a lattice.
      * ``VERTEX`` Vertex, The object is parented to a vertex.
      * ``VERTEX_3`` 3 Vertices.
      * ``BONE`` Bone, The object is parented to a bone.

      :type: enum in ['OBJECT', 'ARMATURE', 'LATTICE', 'VERTEX', 'VERTEX_3', 'BONE'], default 'OBJECT'

   .. attribute:: parent_vertices

      Indices of vertices in case of a vertex parenting relation

      :type: int array of 3 items in [0, inf], default (0, 0, 0)

   .. data:: particle_systems

      Particle systems emitted from the object

      :type: :class:`ParticleSystems` :class:`bpy_prop_collection` of :class:`ParticleSystem`, (readonly)

   .. attribute:: pass_index

      Index number for the "Object Index" render pass

      :type: int in [0, 32767], default 0

   .. data:: pose

      Current pose for armatures

      :type: :class:`Pose`, (readonly)

   .. attribute:: pose_library

      Action used as a pose library for armatures

      :type: :class:`Action`

   .. data:: proxy

      Library object this proxy object controls

      :type: :class:`Object`, (readonly)

   .. data:: proxy_group

      Library group duplicator object this proxy object controls

      :type: :class:`Object`, (readonly)

   .. data:: rigid_body

      Settings for rigid body simulation

      :type: :class:`RigidBodyObject`, (readonly)

   .. data:: rigid_body_constraint

      Constraint constraining rigid bodies

      :type: :class:`RigidBodyConstraint`, (readonly)

   .. attribute:: rotation_axis_angle

      Angle of Rotation for Axis-Angle rotation representation

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 1.0, 0.0)

   .. attribute:: rotation_euler

      Rotation in Eulers

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation_mode

      * ``QUATERNION`` Quaternion (WXYZ), No Gimbal Lock.
      * ``XYZ`` XYZ Euler, XYZ Rotation Order - prone to Gimbal Lock (default).
      * ``XZY`` XZY Euler, XZY Rotation Order - prone to Gimbal Lock.
      * ``YXZ`` YXZ Euler, YXZ Rotation Order - prone to Gimbal Lock.
      * ``YZX`` YZX Euler, YZX Rotation Order - prone to Gimbal Lock.
      * ``ZXY`` ZXY Euler, ZXY Rotation Order - prone to Gimbal Lock.
      * ``ZYX`` ZYX Euler, ZYX Rotation Order - prone to Gimbal Lock.
      * ``AXIS_ANGLE`` Axis Angle, Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.

      :type: enum in ['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE'], default 'QUATERNION'

   .. attribute:: rotation_quaternion

      Rotation in Quaternions

      :type: float array of 4 items in [-inf, inf], default (1.0, 0.0, 0.0, 0.0)

   .. attribute:: scale

      Scaling of the object

      :type: float array of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. attribute:: select

      Object selection state

      :type: boolean, default False

   .. attribute:: show_all_edges

      Display all edges for mesh objects

      :type: boolean, default False

   .. attribute:: show_axis

      Display the object's origin and axes

      :type: boolean, default False

   .. attribute:: show_bounds

      Display the object's bounds

      :type: boolean, default False

   .. attribute:: show_name

      Display the object's name

      :type: boolean, default False

   .. attribute:: show_only_shape_key

      Always show the current Shape for this Object

      :type: boolean, default False

   .. attribute:: show_texture_space

      Display the object's texture space

      :type: boolean, default False

   .. attribute:: show_transparent

      Display material transparency in the object (unsupported for duplicator drawing)

      :type: boolean, default False

   .. attribute:: show_wire

      Add the object's wireframe over solid drawing

      :type: boolean, default False

   .. attribute:: show_x_ray

      Make the object draw in front of others (unsupported for duplicator drawing)

      :type: boolean, default False

   .. attribute:: slow_parent_offset

      Delay in the parent relationship

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. data:: soft_body

      Settings for soft body simulation

      :type: :class:`SoftBodySettings`, (readonly)

   .. attribute:: track_axis

      Axis that points in 'forward' direction (applies to DupliFrame when parent 'Follow' is enabled)

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

   .. data:: type

      Type of Object

      :type: enum in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER'], default 'EMPTY', (readonly)

   .. attribute:: up_axis

      Axis that points in the upward direction (applies to DupliFrame when parent 'Follow' is enabled)

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: use_dupli_faces_scale

      Scale dupli based on face size

      :type: boolean, default False

   .. attribute:: use_dupli_frames_speed

      Set dupliframes to use the current frame instead of parent curve's evaluation time

      :type: boolean, default False

   .. attribute:: use_dupli_vertices_rotation

      Rotate dupli according to vertex normal

      :type: boolean, default False

   .. data:: use_dynamic_topology_sculpting

      :type: boolean, default False, (readonly)

   .. attribute:: use_extra_recalc_data

      Refresh this object's data again on frame changes, dependency graph hack

      :type: boolean, default False

   .. attribute:: use_extra_recalc_object

      Refresh this object again on frame changes, dependency graph hack

      :type: boolean, default False

   .. attribute:: use_shape_key_edit_mode

      Apply shape keys in edit mode (for Meshes only)

      :type: boolean, default False

   .. attribute:: use_slow_parent

      Create a delay in the parent relationship (beware: this isn't renderfarm safe and may be invalid after jumping around the timeline)

      :type: boolean, default False

   .. data:: vertex_groups

      Vertex groups of the object

      :type: :class:`VertexGroups` :class:`bpy_prop_collection` of :class:`VertexGroup`, (readonly)

   .. data:: children

      All the children of this object
      (readonly)

   .. data:: users_group

      The groups this object is in
      (readonly)

   .. data:: users_scene

      The scenes this object is in
      (readonly)

   .. method:: convert_space(pose_bone=None, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), from_space='WORLD', to_space='WORLD')

      Convert (transform) the given matrix from one space to another

      :arg pose_bone:

         Bone to use to define spaces (may be None, in which case only the two 'WORLD' and 'LOCAL' spaces are usable)

      :type pose_bone: :class:`PoseBone`, (optional)
      :arg matrix:

         The matrix to transform

      :type matrix: float multi-dimensional array of 4 * 4 items in [-inf, inf], (optional)
      :arg from_space:

         The space in which 'matrix' is currently

         * ``WORLD`` World Space, The most gobal space in Blender.
         * ``POSE`` Pose Space, The pose space of a bone (its armature's object space).
         * ``LOCAL_WITH_PARENT`` Local With Parent, The local space of a bone's parent bone.
         * ``LOCAL`` Local Space, The local space of an object/bone.

      :type from_space: enum in ['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'], (optional)
      :arg to_space:

         The space to which you want to transform 'matrix'

         * ``WORLD`` World Space, The most gobal space in Blender.
         * ``POSE`` Pose Space, The pose space of a bone (its armature's object space).
         * ``LOCAL_WITH_PARENT`` Local With Parent, The local space of a bone's parent bone.
         * ``LOCAL`` Local Space, The local space of an object/bone.

      :type to_space: enum in ['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'], (optional)
      :return:

         The transformed matrix

      :rtype: float multi-dimensional array of 4 * 4 items in [-inf, inf]

   .. method:: calc_matrix_camera(x=1, y=1, scale_x=1.0, scale_y=1.0)

      Generate the camera projection matrix of this object (mostly useful for Camera and Lamp types)

      :arg x:

         Width of the render area

      :type x: int in [0, inf], (optional)
      :arg y:

         Height of the render area

      :type y: int in [0, inf], (optional)
      :arg scale_x:

         Width scaling factor

      :type scale_x: float in [1e-06, inf], (optional)
      :arg scale_y:

         height scaling factor

      :type scale_y: float in [1e-06, inf], (optional)
      :return:

         The camera projection matrix

      :rtype: float multi-dimensional array of 4 * 4 items in [-inf, inf]

   .. method:: camera_fit_coords(scene, coordinates)

      Compute the coordinate (and scale for ortho cameras) given object should be to 'see' all given coordinates

      :arg scene:

         Scene to get render size information from, if available

      :type scene: :class:`Scene`
      :arg coordinates:

         Coordinates to fit in

      :type coordinates: float array of 1 items in [-inf, inf], (never None)
      :return (co_return, scale_return):
         `co_return`, The location to aim to be able to see all given points, float array of 3 items in [-inf, inf]

         `scale_return`, The ortho scale to aim to be able to see all given points (if relevant), float in [-inf, inf]


   .. method:: to_mesh(scene, apply_modifiers, settings, calc_tessface=True, calc_undeformed=False)

      Create a Mesh data-block with modifiers applied

      :arg scene:

         Scene within which to evaluate modifiers

      :type scene: :class:`Scene`, (never None)
      :arg apply_modifiers:

         Apply modifiers

      :type apply_modifiers: boolean
      :arg settings:

         Modifier settings to apply

         * ``PREVIEW`` Preview, Apply modifier preview settings.
         * ``RENDER`` Render, Apply modifier render settings.

      :type settings: enum in ['PREVIEW', 'RENDER']
      :arg calc_tessface:

         Calculate Tessellation, Calculate tessellation faces

      :type calc_tessface: boolean, (optional)
      :arg calc_undeformed:

         Calculate Undeformed, Calculate undeformed vertex coordinates

      :type calc_undeformed: boolean, (optional)
      :return:

         Mesh created from object, remove it if it is only used for export

      :rtype: :class:`Mesh`

   .. method:: dupli_list_create(scene, settings='VIEWPORT')

      Create a list of dupli objects for this object, needs to be freed manually with free_dupli_list to restore the objects real matrix and layers

      :arg scene:

         Scene within which to evaluate duplis

      :type scene: :class:`Scene`, (never None)
      :arg settings:

         Generate texture coordinates for rendering

         * ``VIEWPORT`` Viewport, Generate duplis using viewport settings.
         * ``PREVIEW`` Preview, Generate duplis using preview settings.
         * ``RENDER`` Render, Generate duplis using render settings.

      :type settings: enum in ['VIEWPORT', 'PREVIEW', 'RENDER'], (optional)

   .. method:: dupli_list_clear()

      Free the list of dupli objects


   .. method:: find_armature()

      Find armature influencing this object as a parent or via a modifier

      :return:

         Armature object influencing this object or NULL

      :rtype: :class:`Object`

   .. method:: shape_key_add(name="Key", from_mix=True)

      Add shape key to this object

      :arg name:

         Unique name for the new keyblock

      :type name: string, (optional, never None)
      :arg from_mix:

         Create new shape from existing mix of shapes

      :type from_mix: boolean, (optional)
      :return:

         New shape keyblock

      :rtype: :class:`ShapeKey`

   .. method:: shape_key_remove(key)

      Remove a Shape Key from this object

      :arg key:

         Keyblock to be removed

      :type key: :class:`ShapeKey`, (never None)

   .. method:: ray_cast(origin, direction, distance=1.70141e+38)

      Cast a ray onto in object space

      :type origin: float array of 3 items in [-inf, inf]
      :type direction: float array of 3 items in [-inf, inf]
      :arg distance:

         Maximum distance

      :type distance: float in [0, inf], (optional)
      :return (result, location, normal, index):
         `result`, boolean

         `location`, The hit location of this ray cast, float array of 3 items in [-inf, inf]

         `normal`, The face normal at the ray cast hit location, float array of 3 items in [-inf, inf]

         `index`, The face index, -1 when original data isn't available, int in [-inf, inf]


   .. method:: closest_point_on_mesh(origin, distance=1.84467e+19)

      Find the nearest point in object space

      :type origin: float array of 3 items in [-inf, inf]
      :arg distance:

         Maximum distance

      :type distance: float in [0, inf], (optional)
      :return (result, location, normal, index):
         `result`, boolean

         `location`, The location on the object closest to the point, float array of 3 items in [-inf, inf]

         `normal`, The face normal at the closest point, float array of 3 items in [-inf, inf]

         `index`, The face index, -1 when original data isn't available, int in [-inf, inf]


   .. method:: is_visible(scene)

      Determine if object is visible in a given scene

      :type scene: :class:`Scene`, (never None)
      :return:

         Object visibility

      :rtype: boolean

   .. method:: is_modified(scene, settings)

      Determine if this object is modified from the base mesh data

      :type scene: :class:`Scene`, (never None)
      :arg settings:

         Modifier settings to apply

         * ``PREVIEW`` Preview, Apply modifier preview settings.
         * ``RENDER`` Render, Apply modifier render settings.

      :type settings: enum in ['PREVIEW', 'RENDER']
      :return:

         Object visibility

      :rtype: boolean

   .. method:: is_deform_modified(scene, settings)

      Determine if this object is modified by a deformation from the base mesh data

      :type scene: :class:`Scene`, (never None)
      :arg settings:

         Modifier settings to apply

         * ``PREVIEW`` Preview, Apply modifier preview settings.
         * ``RENDER`` Render, Apply modifier render settings.

      :type settings: enum in ['PREVIEW', 'RENDER']
      :return:

         Object visibility

      :rtype: boolean

   .. method:: update_from_editmode()

      Load the objects edit-mode data into the object data

      :return:

         Success

      :rtype: boolean

   .. method:: cache_release()

      Release memory used by caches associated with this object. Intended to be used by render engines only


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

   * :mod:`bpy.context.active_object`
   * :mod:`bpy.context.edit_object`
   * :mod:`bpy.context.editable_objects`
   * :mod:`bpy.context.image_paint_object`
   * :mod:`bpy.context.object`
   * :mod:`bpy.context.particle_edit_object`
   * :mod:`bpy.context.sculpt_object`
   * :mod:`bpy.context.selectable_objects`
   * :mod:`bpy.context.selected_editable_objects`
   * :mod:`bpy.context.selected_objects`
   * :mod:`bpy.context.vertex_paint_object`
   * :mod:`bpy.context.visible_objects`
   * :mod:`bpy.context.weight_paint_object`
   * :class:`ActionConstraint.target`
   * :class:`ArmatureActuator.secondary_target`
   * :class:`ArmatureActuator.target`
   * :class:`ArmatureModifier.object`
   * :class:`ArrayModifier.curve`
   * :class:`ArrayModifier.end_cap`
   * :class:`ArrayModifier.offset_object`
   * :class:`ArrayModifier.start_cap`
   * :class:`BlendData.objects`
   * :class:`BlendDataMeshes.new_from_object`
   * :class:`BlendDataObjects.new`
   * :class:`BlendDataObjects.remove`
   * :class:`BoidRuleAvoid.object`
   * :class:`BoidRuleFollowLeader.object`
   * :class:`BoidRuleGoal.object`
   * :class:`BooleanModifier.object`
   * :class:`Camera.dof_object`
   * :class:`CameraActuator.object`
   * :class:`CastModifier.object`
   * :class:`ChildOfConstraint.target`
   * :class:`ClampToConstraint.target`
   * :class:`ConstraintTarget.target`
   * :class:`CopyLocationConstraint.target`
   * :class:`CopyRotationConstraint.target`
   * :class:`CopyScaleConstraint.target`
   * :class:`CopyTransformsConstraint.target`
   * :class:`Curve.bevel_object`
   * :class:`Curve.taper_object`
   * :class:`CurveModifier.object`
   * :class:`DampedTrackConstraint.target`
   * :class:`DataTransferModifier.object`
   * :class:`DisplaceModifier.texture_coords_object`
   * :class:`DupliObject.object`
   * :class:`DynamicPaintSurface.output_exists`
   * :class:`EditObjectActuator.object`
   * :class:`EditObjectActuator.track_object`
   * :class:`EnvironmentMap.viewpoint_object`
   * :class:`FieldSettings.source_object`
   * :class:`FloorConstraint.target`
   * :class:`FollowPathConstraint.target`
   * :class:`FollowTrackConstraint.camera`
   * :class:`FollowTrackConstraint.depth_object`
   * :class:`GPencilLayer.parent`
   * :class:`Group.objects`
   * :class:`GroupObjects.link`
   * :class:`GroupObjects.unlink`
   * :class:`HookModifier.object`
   * :class:`KinematicConstraint.pole_target`
   * :class:`KinematicConstraint.target`
   * :class:`LampTextureSlot.object`
   * :class:`LatticeModifier.object`
   * :class:`LimitDistanceConstraint.target`
   * :class:`LineStyleAlphaModifier_DistanceFromObject.target`
   * :class:`LineStyleColorModifier_DistanceFromObject.target`
   * :class:`LineStyleThicknessModifier_DistanceFromObject.target`
   * :class:`LockedTrackConstraint.target`
   * :class:`LodLevel.object`
   * :class:`MaskModifier.armature`
   * :class:`MaterialTextureSlot.object`
   * :class:`MeshDeformModifier.object`
   * :class:`MirrorModifier.mirror_object`
   * :class:`NormalEditModifier.target`
   * :class:`Object.find_armature`
   * :class:`Object.parent`
   * :class:`Object.proxy`
   * :class:`Object.proxy_group`
   * :class:`ObjectActuator.reference_object`
   * :class:`ObjectBase.object`
   * :class:`ObjectSolverConstraint.camera`
   * :class:`OceanTexData.ocean_object`
   * :class:`ParentActuator.object`
   * :class:`ParticleEdit.object`
   * :class:`ParticleEdit.shape_object`
   * :class:`ParticleHairKey.co_object`
   * :class:`ParticleInstanceModifier.object`
   * :class:`ParticleSettings.billboard_object`
   * :class:`ParticleSettings.dupli_object`
   * :class:`ParticleSettingsTextureSlot.object`
   * :class:`ParticleSystem.co_hair`
   * :class:`ParticleSystem.parent`
   * :class:`ParticleSystem.reactor_target_object`
   * :class:`ParticleSystem.set_resolution`
   * :class:`ParticleTarget.object`
   * :class:`PivotConstraint.target`
   * :class:`PointDensity.object`
   * :class:`PoseBone.custom_shape`
   * :class:`PropertyActuator.object`
   * :class:`RenderEngine.bake`
   * :class:`RenderEngine.camera_model_matrix`
   * :class:`RenderEngine.camera_override`
   * :class:`RenderEngine.camera_shift_x`
   * :class:`RenderEngine.use_spherical_stereo`
   * :class:`RigidBodyConstraint.object1`
   * :class:`RigidBodyConstraint.object2`
   * :class:`RigidBodyJointConstraint.child`
   * :class:`RigidBodyJointConstraint.target`
   * :class:`RigidBodyWorld.convex_sweep_test`
   * :class:`Scene.camera`
   * :class:`Scene.objects`
   * :class:`Scene.ray_cast`
   * :class:`Scene.uvedit_aspect`
   * :class:`SceneActuator.camera`
   * :class:`SceneObjects.active`
   * :class:`SceneObjects.link`
   * :class:`SceneObjects.unlink`
   * :class:`SceneSequence.scene_camera`
   * :class:`ScrewModifier.object`
   * :class:`Sculpt.gravity_object`
   * :class:`ShaderNodeLampData.lamp_object`
   * :class:`ShaderNodeTexCoord.object`
   * :class:`ShaderNodeTexPointDensity.object`
   * :class:`ShrinkwrapConstraint.target`
   * :class:`ShrinkwrapModifier.auxiliary_target`
   * :class:`ShrinkwrapModifier.target`
   * :class:`SimpleDeformModifier.origin`
   * :class:`SpaceView3D.camera`
   * :class:`SpaceView3D.lock_object`
   * :class:`SplineIKConstraint.target`
   * :class:`SteeringActuator.navmesh`
   * :class:`SteeringActuator.target`
   * :class:`StretchToConstraint.target`
   * :class:`SurfaceDeformModifier.target`
   * :class:`TextCurve.follow_curve`
   * :class:`TimelineMarker.camera`
   * :class:`ToolSettings.etch_template`
   * :class:`TrackToConstraint.target`
   * :class:`TransformConstraint.target`
   * :class:`UVProjector.object`
   * :class:`UVWarpModifier.object_from`
   * :class:`UVWarpModifier.object_to`
   * :class:`VertexWeightEditModifier.mask_tex_map_object`
   * :class:`VertexWeightMixModifier.mask_tex_map_object`
   * :class:`VertexWeightProximityModifier.mask_tex_map_object`
   * :class:`VertexWeightProximityModifier.target`
   * :class:`VoxelData.domain_object`
   * :class:`WarpModifier.object_from`
   * :class:`WarpModifier.object_to`
   * :class:`WarpModifier.texture_coords_object`
   * :class:`WaveModifier.start_position_object`
   * :class:`WaveModifier.texture_coords_object`
   * :class:`WorldTextureSlot.object`

