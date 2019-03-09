Import Mesh Operators
=====================

.. module:: bpy.ops.import_mesh

.. function:: ply(filepath="", files=None, directory="", filter_glob="*.ply")

   Load a PLY geometry file

   :arg filepath:

      File Path, Filepath used for importing the file

   :type filepath: string, (optional, never None)
   :arg files:

      File Path, File path used for importing the PLY file

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory:

      directory

   :type directory: string, (optional, never None)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)

   :file: `addons\io_mesh_ply\__init__.py\:82 <https://developer.blender.org/diffusion/BA/addons\io_mesh_ply\__init__.py$82>`_

.. function:: stl(filepath="", axis_forward='Y', axis_up='Z', filter_glob="*.stl", files=None, directory="", global_scale=1.0, use_scene_unit=False, use_facet_normal=False)

   Load STL triangle mesh data

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
   :arg files:

      File Path

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory:

      directory

   :type directory: string, (optional, never None)
   :arg global_scale:

      Scale

   :type global_scale: float in [1e-06, 1e+06], (optional)
   :arg use_scene_unit:

      Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data

   :type use_scene_unit: boolean, (optional)
   :arg use_facet_normal:

      Facet Normals, Use (import) facet normals (note that this will still give flat shading)

   :type use_facet_normal: boolean, (optional)

   :file: `addons\io_mesh_stl\__init__.py\:121 <https://developer.blender.org/diffusion/BA/addons\io_mesh_stl\__init__.py$121>`_

