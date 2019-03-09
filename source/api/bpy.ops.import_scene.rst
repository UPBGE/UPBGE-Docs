Import Scene Operators
======================

.. module:: bpy.ops.import_scene

.. function:: autodesk_3ds(filepath="", axis_forward='Y', axis_up='Z', filter_glob="*.3ds", constrain_size=10.0, use_image_search=True, use_apply_transform=True)

   Import from 3DS file format (.3ds)

   :arg filepath:

      File Path, Filepath used for importing the file

   :type filepath: string, (optional, never None)
   :arg axis_forward:

      Forward

   :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg axis_up:

      Up

   :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)
   :arg constrain_size:

      Size Constraint, Scale the model by 10 until it reaches the size constraint (0 to disable)

   :type constrain_size: float in [0, 1000], (optional)
   :arg use_image_search:

      Image Search, Search subdirectories for any associated images (Warning, may be slow)

   :type use_image_search: boolean, (optional)
   :arg use_apply_transform:

      Apply Transform, Workaround for object transformations importing incorrectly

   :type use_apply_transform: boolean, (optional)

   :file: `addons\io_scene_3ds\__init__.py\:90 <https://developer.blender.org/diffusion/BA/addons\io_scene_3ds\__init__.py$90>`_

.. function:: fbx(filepath="", axis_forward='-Z', axis_up='Y', directory="", filter_glob="*.fbx", ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True)

   Load a FBX file

   :arg filepath:

      File Path, Filepath used for importing the file

   :type filepath: string, (optional, never None)
   :arg axis_forward:

      Forward

   :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg axis_up:

      Up

   :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg directory:

      directory

   :type directory: string, (optional, never None)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)
   :arg ui_tab:

      ui_tab, Import options categories

      * ``MAIN`` Main, Main basic settings.
      * ``ARMATURE`` Armatures, Armature-related settings.

   :type ui_tab: enum in ['MAIN', 'ARMATURE'], (optional)
   :arg use_manual_orientation:

      Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file

   :type use_manual_orientation: boolean, (optional)
   :arg global_scale:

      Scale

   :type global_scale: float in [0.001, 1000], (optional)
   :arg bake_space_transform:

      !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)

   :type bake_space_transform: boolean, (optional)
   :arg use_custom_normals:

      Import Normals, Import custom normals, if available (otherwise Blender will recompute them)

   :type use_custom_normals: boolean, (optional)
   :arg use_image_search:

      Image Search, Search subdirs for any associated images (WARNING: may be slow)

   :type use_image_search: boolean, (optional)
   :arg use_alpha_decals:

      Alpha Decals, Treat materials with alpha as decals (no shadow casting)

   :type use_alpha_decals: boolean, (optional)
   :arg decal_offset:

      Decal Offset, Displace geometry of alpha meshes

   :type decal_offset: float in [0, 1], (optional)
   :arg use_anim:

      Import Animation, Import FBX animation

   :type use_anim: boolean, (optional)
   :arg anim_offset:

      Animation Offset, Offset to apply to animation during import, in frames

   :type anim_offset: float in [-inf, inf], (optional)
   :arg use_custom_props:

      Import User Properties, Import user properties as custom properties

   :type use_custom_props: boolean, (optional)
   :arg use_custom_props_enum_as_string:

      Import Enums As Strings, Store enumeration values as strings

   :type use_custom_props_enum_as_string: boolean, (optional)
   :arg ignore_leaf_bones:

      Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)

   :type ignore_leaf_bones: boolean, (optional)
   :arg force_connect_children:

      Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)

   :type force_connect_children: boolean, (optional)
   :arg automatic_bone_orientation:

      Automatic Bone Orientation, Try to align the major bone axis with the bone children

   :type automatic_bone_orientation: boolean, (optional)
   :arg primary_bone_axis:

      Primary Bone Axis

   :type primary_bone_axis: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg secondary_bone_axis:

      Secondary Bone Axis

   :type secondary_bone_axis: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg use_prepost_rot:

      Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)

   :type use_prepost_rot: boolean, (optional)

   :file: `addons\io_scene_fbx\__init__.py\:229 <https://developer.blender.org/diffusion/BA/addons\io_scene_fbx\__init__.py$229>`_

.. function:: obj(filepath="", axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True, use_groups_as_vgroups=False, use_image_search=True, split_mode='ON', global_clamp_size=0.0)

   Load a Wavefront OBJ File

   :arg filepath:

      File Path, Filepath used for importing the file

   :type filepath: string, (optional, never None)
   :arg axis_forward:

      Forward

   :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg axis_up:

      Up

   :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)
   :arg use_edges:

      Lines, Import lines and faces with 2 verts as edge

   :type use_edges: boolean, (optional)
   :arg use_smooth_groups:

      Smooth Groups, Surround smooth groups by sharp edges

   :type use_smooth_groups: boolean, (optional)
   :arg use_split_objects:

      Object, Import OBJ Objects into Blender Objects

   :type use_split_objects: boolean, (optional)
   :arg use_split_groups:

      Group, Import OBJ Groups into Blender Objects

   :type use_split_groups: boolean, (optional)
   :arg use_groups_as_vgroups:

      Poly Groups, Import OBJ groups as vertex groups

   :type use_groups_as_vgroups: boolean, (optional)
   :arg use_image_search:

      Image Search, Search subdirs for any associated images (Warning, may be slow)

   :type use_image_search: boolean, (optional)
   :arg split_mode:

      Split

      * ``ON`` Split, Split geometry, omits unused verts.
      * ``OFF`` Keep Vert Order, Keep vertex order from file.

   :type split_mode: enum in ['ON', 'OFF'], (optional)
   :arg global_clamp_size:

      Clamp Size, Clamp bounds under this value (zero to disable)

   :type global_clamp_size: float in [0, 1000], (optional)

   :file: `addons\io_scene_obj\__init__.py\:122 <https://developer.blender.org/diffusion/BA/addons\io_scene_obj\__init__.py$122>`_

.. function:: x3d(filepath="", axis_forward='Z', axis_up='Y', filter_glob="*.x3d;*.wrl")

   Import an X3D or VRML2 file

   :arg filepath:

      File Path, Filepath used for importing the file

   :type filepath: string, (optional, never None)
   :arg axis_forward:

      Forward

   :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg axis_up:

      Up

   :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)

   :file: `addons\io_scene_x3d\__init__.py\:69 <https://developer.blender.org/diffusion/BA/addons\io_scene_x3d\__init__.py$69>`_

