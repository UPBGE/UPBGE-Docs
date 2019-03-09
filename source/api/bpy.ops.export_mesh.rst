Export Mesh Operators
=====================

.. module:: bpy.ops.export_mesh

.. function:: ply(filepath="", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.ply", use_mesh_modifiers=True, use_normals=True, use_uv_coords=True, use_colors=True, global_scale=1.0)

   Export a single object as a Stanford PLY with normals, colors and texture coordinates

   :arg filepath:

      File Path, Filepath used for exporting the file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg axis_forward:

      Forward

   :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg axis_up:

      Up

   :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)
   :arg use_mesh_modifiers:

      Apply Modifiers, Apply Modifiers to the exported mesh

   :type use_mesh_modifiers: boolean, (optional)
   :arg use_normals:

      Normals, Export Normals for smooth and hard shaded faces (hard shaded faces will be exported as individual faces)

   :type use_normals: boolean, (optional)
   :arg use_uv_coords:

      UVs, Export the active UV layer

   :type use_uv_coords: boolean, (optional)
   :arg use_colors:

      Vertex Colors, Export the active vertex color layer

   :type use_colors: boolean, (optional)
   :arg global_scale:

      Scale

   :type global_scale: float in [0.01, 1000], (optional)

   :file: `addons\io_mesh_ply\__init__.py\:139 <https://developer.blender.org/diffusion/BA/addons\io_mesh_ply\__init__.py$139>`_

.. function:: stl(filepath="", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.stl", use_selection=False, global_scale=1.0, use_scene_unit=False, ascii=False, use_mesh_modifiers=True, batch_mode='OFF')

   Save STL triangle mesh data from the active object

   :arg filepath:

      File Path, Filepath used for exporting the file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg axis_forward:

      Forward

   :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg axis_up:

      Up

   :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)
   :arg use_selection:

      Selection Only, Export selected objects only

   :type use_selection: boolean, (optional)
   :arg global_scale:

      Scale

   :type global_scale: float in [0.01, 1000], (optional)
   :arg use_scene_unit:

      Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data

   :type use_scene_unit: boolean, (optional)
   :arg ascii:

      Ascii, Save the file in ASCII file format

   :type ascii: boolean, (optional)
   :arg use_mesh_modifiers:

      Apply Modifiers, Apply the modifiers before saving

   :type use_mesh_modifiers: boolean, (optional)
   :arg batch_mode:

      Batch Mode

      * ``OFF`` Off, All data in one file.
      * ``OBJECT`` Object, Each object as a file.

   :type batch_mode: enum in ['OFF', 'OBJECT'], (optional)

   :file: `addons\io_mesh_stl\__init__.py\:202 <https://developer.blender.org/diffusion/BA/addons\io_mesh_stl\__init__.py$202>`_

