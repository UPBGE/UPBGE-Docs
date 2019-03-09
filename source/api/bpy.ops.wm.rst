Wm Operators
============

.. module:: bpy.ops.wm

.. function:: addon_disable(module="")

   Disable an add-on

   :arg module:

      Module, Module name of the add-on to disable

   :type module: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1860 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1860>`_

.. function:: addon_enable(module="")

   Enable an add-on

   :arg module:

      Module, Module name of the add-on to enable

   :type module: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1816 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1816>`_

.. function:: addon_expand(module="")

   Display information and preferences for this add-on

   :arg module:

      Module, Module name of the add-on to expand

   :type module: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:2180 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$2180>`_

.. function:: addon_install(overwrite=True, target='DEFAULT', filepath="", filter_folder=True, filter_python=True, filter_glob="*.py;*.zip")

   Install an add-on

   :arg overwrite:

      Overwrite, Remove existing add-ons with the same ID

   :type overwrite: boolean, (optional)
   :arg target:

      Target Path

   :type target: enum in ['DEFAULT', 'PREFS'], (optional)
   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_python:

      Filter python

   :type filter_python: boolean, (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1990 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1990>`_

.. function:: addon_refresh()

   Scan add-on directories for new modules

   :file: `startup\bl_operators\wm.py\:1946 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1946>`_

.. function:: addon_remove(module="")

   Delete the add-on from the file system

   :arg module:

      Module, Module name of the add-on to remove

   :type module: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:2135 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$2135>`_

.. function:: addon_userpref_show(module="")

   Show add-on user preferences

   :arg module:

      Module, Module name of the add-on to expand

   :type module: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:2204 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$2204>`_

.. function:: alembic_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', start=-2147483648, end=-2147483648, xsamples=1, gsamples=1, sh_open=0.0, sh_close=1.0, selected=False, renderable_only=True, visible_layers_only=False, flatten=False, uvs=True, packuv=True, normals=True, vcolors=False, face_sets=False, subdiv_schema=False, apply_subdiv=False, compression_type='OGAWA', global_scale=1.0, triangulate=False, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY', export_hair=True, export_particles=True, as_background_job=True, init_scene_frame_range=False)

   Export current scene in an Alembic archive

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg start:

      Start Frame, Start frame of the export, use the default value to take the start frame of the current scene

   :type start: int in [-inf, inf], (optional)
   :arg end:

      End Frame, End frame of the export, use the default value to take the end frame of the current scene

   :type end: int in [-inf, inf], (optional)
   :arg xsamples:

      Transform Samples, Number of times per frame transformations are sampled

   :type xsamples: int in [1, 128], (optional)
   :arg gsamples:

      Geometry Samples, Number of times per frame object data are sampled

   :type gsamples: int in [1, 128], (optional)
   :arg sh_open:

      Shutter Open, Time at which the shutter is open

   :type sh_open: float in [-1, 1], (optional)
   :arg sh_close:

      Shutter Close, Time at which the shutter is closed

   :type sh_close: float in [-1, 1], (optional)
   :arg selected:

      Selected Objects Only, Export only selected objects

   :type selected: boolean, (optional)
   :arg renderable_only:

      Renderable Objects Only, Export only objects marked renderable in the outliner

   :type renderable_only: boolean, (optional)
   :arg visible_layers_only:

      Visible Layers Only, Export only objects in visible layers

   :type visible_layers_only: boolean, (optional)
   :arg flatten:

      Flatten Hierarchy, Do not preserve objects' parent/children relationship

   :type flatten: boolean, (optional)
   :arg uvs:

      UVs, Export UVs

   :type uvs: boolean, (optional)
   :arg packuv:

      Pack UV Islands, Export UVs with packed island

   :type packuv: boolean, (optional)
   :arg normals:

      Normals, Export normals

   :type normals: boolean, (optional)
   :arg vcolors:

      Vertex Colors, Export vertex colors

   :type vcolors: boolean, (optional)
   :arg face_sets:

      Face Sets, Export per face shading group assignments

   :type face_sets: boolean, (optional)
   :arg subdiv_schema:

      Use Subdivision Schema, Export meshes using Alembic's subdivision schema

   :type subdiv_schema: boolean, (optional)
   :arg apply_subdiv:

      Apply Subsurf, Export subdivision surfaces as meshes

   :type apply_subdiv: boolean, (optional)
   :arg compression_type:

      Compression

   :type compression_type: enum in ['OGAWA', 'HDF5'], (optional)
   :arg global_scale:

      Scale, Value by which to enlarge or shrink the objects with respect to the world's origin

   :type global_scale: float in [0.0001, 1000], (optional)
   :arg triangulate:

      Triangulate, Export Polygons (Quads & NGons) as Triangles

   :type triangulate: boolean, (optional)
   :arg quad_method:

      Quad Method, Method for splitting the quads into triangles

      * ``BEAUTY`` Beauty , Split the quads in nice triangles, slower method.
      * ``FIXED`` Fixed, Split the quads on the first and third vertices.
      * ``FIXED_ALTERNATE`` Fixed Alternate, Split the quads on the 2nd and 4th vertices.
      * ``SHORTEST_DIAGONAL`` Shortest Diagonal, Split the quads based on the distance between the vertices.

   :type quad_method: enum in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], (optional)
   :arg ngon_method:

      Polygon Method, Method for splitting the polygons into triangles

      * ``BEAUTY`` Beauty , Split the quads in nice triangles, slower method.
      * ``FIXED`` Fixed, Split the quads on the first and third vertices.
      * ``FIXED_ALTERNATE`` Fixed Alternate, Split the quads on the 2nd and 4th vertices.
      * ``SHORTEST_DIAGONAL`` Shortest Diagonal, Split the quads based on the distance between the vertices.

   :type ngon_method: enum in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], (optional)
   :arg export_hair:

      Export Hair, Exports hair particle systems as animated curves

   :type export_hair: boolean, (optional)
   :arg export_particles:

      Export Particles, Exports non-hair particle systems

   :type export_particles: boolean, (optional)
   :arg as_background_job:

      Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing

   :type as_background_job: boolean, (optional)
   :type init_scene_frame_range: boolean, (optional)

.. function:: alembic_import(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', scale=1.0, set_frame_range=True, validate_meshes=False, is_sequence=False, as_background_job=True)

   Load an Alembic archive

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg scale:

      Scale, Value by which to enlarge or shrink the objects with respect to the world's origin

   :type scale: float in [0.0001, 1000], (optional)
   :arg set_frame_range:

      Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive

   :type set_frame_range: boolean, (optional)
   :arg validate_meshes:

      Validate Meshes, Check imported mesh objects for invalid data (slow)

   :type validate_meshes: boolean, (optional)
   :arg is_sequence:

      Is Sequence, Set to true if the cache is split into separate files

   :type is_sequence: boolean, (optional)
   :arg as_background_job:

      Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting

   :type as_background_job: boolean, (optional)

.. function:: app_template_install(overwrite=True, filepath="", filter_folder=True, filter_glob="*.zip")

   Install an application-template

   :arg overwrite:

      Overwrite, Remove existing template with the same ID

   :type overwrite: boolean, (optional)
   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:2249 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$2249>`_

.. function:: appconfig_activate(filepath="")

   Undocumented

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1409 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1409>`_

.. function:: appconfig_default()

   Undocumented

   :file: `startup\bl_operators\wm.py\:1385 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1385>`_

.. function:: append(filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=True, filemode=1, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', link=False, autoselect=True, active_layer=True, instance_groups=False, set_fake=False, use_recursive=True)

   Append from a Library .blend file

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg directory:

      Directory, Directory of the file

   :type directory: string, (optional, never None)
   :arg filename:

      File Name, Name of the file

   :type filename: string, (optional, never None)
   :arg files:

      Files

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg link:

      Link, Link the objects or data-blocks rather than appending

   :type link: boolean, (optional)
   :arg autoselect:

      Select, Select new objects

   :type autoselect: boolean, (optional)
   :arg active_layer:

      Active Layer, Put new objects on the active layer

   :type active_layer: boolean, (optional)
   :arg instance_groups:

      Instance Groups, Create Dupli-Group instances for each group

   :type instance_groups: boolean, (optional)
   :arg set_fake:

      Fake User, Set Fake User for appended items (except Objects and Groups)

   :type set_fake: boolean, (optional)
   :arg use_recursive:

      Localize All, Localize all appended data, including those indirectly linked from other libraries

   :type use_recursive: boolean, (optional)

.. function:: blenderplayer_start()

   Launch the blender-player with the current blend-file

   :file: `startup\bl_operators\wm.py\:1491 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1491>`_

.. function:: call_menu(name="")

   Call (draw) a pre-defined menu

   :arg name:

      Name, Name of the menu

   :type name: string, (optional, never None)

.. function:: call_menu_pie(name="")

   Call (draw) a pre-defined pie menu

   :arg name:

      Name, Name of the pie menu

   :type name: string, (optional, never None)

.. function:: collada_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', apply_modifiers=False, export_mesh_type=0, export_mesh_type_selection='view', selected=False, include_children=False, include_armatures=False, include_shapekeys=True, deform_bones_only=False, active_uv_only=False, use_texture_copies=True, triangulate=True, use_object_instantiation=True, use_blender_profile=True, sort_by_name=False, export_transformation_type=0, export_transformation_type_selection='matrix', export_texture_type=0, export_texture_type_selection='mat', open_sim=False, limit_precision=False, keep_bind_info=False)

   Save a Collada file

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg apply_modifiers:

      Apply Modifiers, Apply modifiers to exported mesh (non destructive))

   :type apply_modifiers: boolean, (optional)
   :arg export_mesh_type:

      Resolution, Modifier resolution for export

   :type export_mesh_type: int in [-inf, inf], (optional)
   :arg export_mesh_type_selection:

      Resolution, Modifier resolution for export

      * ``view`` View, Apply modifier's view settings.
      * ``render`` Render, Apply modifier's render settings.

   :type export_mesh_type_selection: enum in ['view', 'render'], (optional)
   :arg selected:

      Selection Only, Export only selected elements

   :type selected: boolean, (optional)
   :arg include_children:

      Include Children, Export all children of selected objects (even if not selected)

   :type include_children: boolean, (optional)
   :arg include_armatures:

      Include Armatures, Export related armatures (even if not selected)

   :type include_armatures: boolean, (optional)
   :arg include_shapekeys:

      Include Shape Keys, Export all Shape Keys from Mesh Objects

   :type include_shapekeys: boolean, (optional)
   :arg deform_bones_only:

      Deform Bones only, Only export deforming bones with armatures

   :type deform_bones_only: boolean, (optional)
   :arg active_uv_only:

      Only Selected UV Map, Export only the selected UV Map

   :type active_uv_only: boolean, (optional)
   :arg use_texture_copies:

      Copy, Copy textures to same folder where the .dae file is exported

   :type use_texture_copies: boolean, (optional)
   :arg triangulate:

      Triangulate, Export Polygons (Quads & NGons) as Triangles

   :type triangulate: boolean, (optional)
   :arg use_object_instantiation:

      Use Object Instances, Instantiate multiple Objects from same Data

   :type use_object_instantiation: boolean, (optional)
   :arg use_blender_profile:

      Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)

   :type use_blender_profile: boolean, (optional)
   :arg sort_by_name:

      Sort by Object name, Sort exported data by Object name

   :type sort_by_name: boolean, (optional)
   :arg export_transformation_type:

      Transform, Transformation type for translation, scale and rotation

   :type export_transformation_type: int in [-inf, inf], (optional)
   :arg export_transformation_type_selection:

      Transform, Transformation type for translation, scale and rotation

      * ``matrix`` Matrix, Use <matrix> to specify transformations.
      * ``transrotloc`` TransRotLoc, Use <translate>, <rotate>, <scale> to specify transformations.

   :type export_transformation_type_selection: enum in ['matrix', 'transrotloc'], (optional)
   :arg export_texture_type:

      Texture Type, Type for exported Textures (UV or MAT)

   :type export_texture_type: int in [-inf, inf], (optional)
   :arg export_texture_type_selection:

      Texture Type, Type for exported Textures (UV or MAT)

      * ``mat`` Materials, Export Materials.
      * ``uv`` UV Textures, Export UV Textures (Face textures) as materials.

   :type export_texture_type_selection: enum in ['mat', 'uv'], (optional)
   :arg open_sim:

      Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds

   :type open_sim: boolean, (optional)
   :arg limit_precision:

      Limit Precision, Reduce the precision of the exported data to 6 digits

   :type limit_precision: boolean, (optional)
   :arg keep_bind_info:

      Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export

   :type keep_bind_info: boolean, (optional)

.. function:: collada_import(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', import_units=False, fix_orientation=False, find_chains=False, auto_connect=False, min_chain_length=0, keep_bind_info=False)

   Load a Collada file

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg import_units:

      Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene

   :type import_units: boolean, (optional)
   :arg fix_orientation:

      Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)

   :type fix_orientation: boolean, (optional)
   :arg find_chains:

      Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected

   :type find_chains: boolean, (optional)
   :arg auto_connect:

      Auto Connect, Set use_connect for parent bones which have exactly one child bone

   :type auto_connect: boolean, (optional)
   :arg min_chain_length:

      Minimum Chain Length, When searching Bone Chains disregard chains of length below this value

   :type min_chain_length: int in [0, inf], (optional)
   :arg keep_bind_info:

      Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export

   :type keep_bind_info: boolean, (optional)

.. function:: console_toggle()

   Toggle System Console

.. function:: context_collection_boolean_set(data_path_iter="", data_path_item="", type='TOGGLE')

   Set boolean values for a collection of items

   :arg data_path_iter:

      data_path_iter, The data path relative to the context, must point to an iterable

   :type data_path_iter: string, (optional, never None)
   :arg data_path_item:

      data_path_item, The data path from each iterable to the value (int or float)

   :type data_path_item: string, (optional, never None)
   :arg type:

      Type

   :type type: enum in ['TOGGLE', 'ENABLE', 'DISABLE'], (optional)

   :file: `startup\bl_operators\wm.py\:697 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$697>`_

.. function:: context_cycle_array(data_path="", reverse=False)

   Set a context array value (useful for cycling the active mesh edit mode)

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg reverse:

      Reverse, Cycle backwards

   :type reverse: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:516 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$516>`_

.. function:: context_cycle_enum(data_path="", reverse=False, wrap=False)

   Toggle a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg reverse:

      Reverse, Cycle backwards

   :type reverse: boolean, (optional)
   :arg wrap:

      Wrap, Wrap back to the first/last values

   :type wrap: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:460 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$460>`_

.. function:: context_cycle_int(data_path="", reverse=False, wrap=False)

   Set a context value (useful for cycling active material, vertex keys, groups, etc.)

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg reverse:

      Reverse, Cycle backwards

   :type reverse: boolean, (optional)
   :arg wrap:

      Wrap, Wrap back to the first/last values

   :type wrap: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:424 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$424>`_

.. function:: context_menu_enum(data_path="")

   Undocumented

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:540 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$540>`_

.. function:: context_modal_mouse(data_path_iter="", data_path_item="", header_text="", input_scale=0.01, invert=False, initial_x=0)

   Adjust arbitrary values with mouse input

   :arg data_path_iter:

      data_path_iter, The data path relative to the context, must point to an iterable

   :type data_path_iter: string, (optional, never None)
   :arg data_path_item:

      data_path_item, The data path from each iterable to the value (int or float)

   :type data_path_item: string, (optional, never None)
   :arg header_text:

      Header Text, Text to display in header during scale

   :type header_text: string, (optional, never None)
   :arg input_scale:

      input_scale, Scale the mouse movement by this value before applying the delta

   :type input_scale: float in [-inf, inf], (optional)
   :arg invert:

      invert, Invert the mouse input

   :type invert: boolean, (optional)
   :arg initial_x:

      initial_x

   :type initial_x: int in [-inf, inf], (optional)

   :file: `startup\bl_operators\wm.py\:832 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$832>`_

.. function:: context_pie_enum(data_path="")

   Undocumented

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:566 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$566>`_

.. function:: context_scale_float(data_path="", value=1.0)

   Scale a float context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assign value

   :type value: float in [-inf, inf], (optional)

   :file: `startup\bl_operators\wm.py\:228 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$228>`_

.. function:: context_scale_int(data_path="", value=1.0, always_step=True)

   Scale an int context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assign value

   :type value: float in [-inf, inf], (optional)
   :arg always_step:

      Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0

   :type always_step: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:261 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$261>`_

.. function:: context_set_boolean(data_path="", value=True)

   Set a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assignment value

   :type value: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:120 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$120>`_

.. function:: context_set_enum(data_path="", value="")

   Set a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assignment value (as a string)

   :type value: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:120 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$120>`_

.. function:: context_set_float(data_path="", value=0.0, relative=False)

   Set a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assignment value

   :type value: float in [-inf, inf], (optional)
   :arg relative:

      Relative, Apply relative to the current value (delta)

   :type relative: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:120 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$120>`_

.. function:: context_set_id(data_path="", value="")

   Set a context value to an ID data-block

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assign value

   :type value: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:642 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$642>`_

.. function:: context_set_int(data_path="", value=0, relative=False)

   Set a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assign value

   :type value: int in [-inf, inf], (optional)
   :arg relative:

      Relative, Apply relative to the current value (delta)

   :type relative: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:120 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$120>`_

.. function:: context_set_string(data_path="", value="")

   Set a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assign value

   :type value: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:120 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$120>`_

.. function:: context_set_value(data_path="", value="")

   Set a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value:

      Value, Assignment value (as a string)

   :type value: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:348 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$348>`_

.. function:: context_toggle(data_path="")

   Toggle a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:364 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$364>`_

.. function:: context_toggle_enum(data_path="", value_1="", value_2="")

   Toggle a context value

   :arg data_path:

      Context Attributes, RNA context string

   :type data_path: string, (optional, never None)
   :arg value_1:

      Value, Toggle enum

   :type value_1: string, (optional, never None)
   :arg value_2:

      Value, Toggle enum

   :type value_2: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:393 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$393>`_

.. function:: copy_prev_settings()

   Copy settings from previous version

   :file: `startup\bl_operators\wm.py\:1457 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1457>`_

.. function:: debug_menu(debug_value=0)

   Open a popup to set the debug level

   :arg debug_value:

      Debug Value

   :type debug_value: int in [-32768, 32767], (optional)

.. function:: dependency_relations()

   Print dependency graph relations to the console

.. function:: doc_view(doc_id="")

   Load online reference docs

   :arg doc_id:

      Doc ID

   :type doc_id: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1038 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1038>`_

.. function:: doc_view_manual(doc_id="")

   Load online manual

   :arg doc_id:

      Doc ID

   :type doc_id: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1006 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1006>`_

.. function:: doc_view_manual_ui_context()

   View a context based online manual in a web browser

.. function:: interaction_preset_add(name="", remove_active=False)

   Add or remove an Application Interaction Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: interface_theme_preset_add(name="", remove_active=False)

   Add or remove a theme preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: keyconfig_activate(filepath="")

   Undocumented

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1374 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1374>`_

.. function:: keyconfig_export(filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True)

   Export key configuration to a python script

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_text:

      Filter text

   :type filter_text: boolean, (optional)
   :arg filter_python:

      Filter python

   :type filter_python: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:1643 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1643>`_

.. function:: keyconfig_import(filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True, keep_original=True)

   Import key configuration from a python script

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_text:

      Filter text

   :type filter_text: boolean, (optional)
   :arg filter_python:

      Filter python

   :type filter_python: boolean, (optional)
   :arg keep_original:

      Keep original, Keep original file after copying to configuration folder

   :type keep_original: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:1581 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1581>`_

.. function:: keyconfig_preset_add(name="", remove_active=False)

   Add or remove a Key-config Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: keyconfig_remove()

   Remove key config

   :file: `startup\bl_operators\wm.py\:1770 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1770>`_

.. function:: keyconfig_test()

   Test key-config for conflicts

   :file: `startup\bl_operators\wm.py\:1539 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1539>`_

.. function:: keyitem_add()

   Add key map item

   :file: `startup\bl_operators\wm.py\:1721 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1721>`_

.. function:: keyitem_remove(item_id=0)

   Remove key map item

   :arg item_id:

      Item Identifier, Identifier of the item to remove

   :type item_id: int in [-inf, inf], (optional)

   :file: `startup\bl_operators\wm.py\:1752 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1752>`_

.. function:: keyitem_restore(item_id=0)

   Restore key map item

   :arg item_id:

      Item Identifier, Identifier of the item to remove

   :type item_id: int in [-inf, inf], (optional)

   :file: `startup\bl_operators\wm.py\:1706 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1706>`_

.. function:: keymap_restore(all=False)

   Restore key map(s)

   :arg all:

      All Keymaps, Restore all keymaps to default

   :type all: boolean, (optional)

   :file: `startup\bl_operators\wm.py\:1678 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1678>`_

.. function:: lib_reload(library="", filepath="", directory="", filename="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Reload the given library

   :arg library:

      Library, Library to reload

   :type library: string, (optional, never None)
   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg directory:

      Directory, Directory of the file

   :type directory: string, (optional, never None)
   :arg filename:

      File Name, Name of the file

   :type filename: string, (optional, never None)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

.. function:: lib_relocate(library="", filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Relocate the given library to one or several others

   :arg library:

      Library, Library to relocate

   :type library: string, (optional, never None)
   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg directory:

      Directory, Directory of the file

   :type directory: string, (optional, never None)
   :arg filename:

      File Name, Name of the file

   :type filename: string, (optional, never None)
   :arg files:

      Files

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

.. function:: link(filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=True, filemode=1, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', link=True, autoselect=True, active_layer=True, instance_groups=True)

   Link from a Library .blend file

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg directory:

      Directory, Directory of the file

   :type directory: string, (optional, never None)
   :arg filename:

      File Name, Name of the file

   :type filename: string, (optional, never None)
   :arg files:

      Files

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg link:

      Link, Link the objects or data-blocks rather than appending

   :type link: boolean, (optional)
   :arg autoselect:

      Select, Select new objects

   :type autoselect: boolean, (optional)
   :arg active_layer:

      Active Layer, Put new objects on the active layer

   :type active_layer: boolean, (optional)
   :arg instance_groups:

      Instance Groups, Create Dupli-Group instances for each group

   :type instance_groups: boolean, (optional)

.. function:: memory_statistics()

   Print memory statistics to the console

.. function:: open_mainfile(filepath="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', load_ui=True, use_scripts=True)

   Open a Blender file

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg load_ui:

      Load UI, Load user interface setup in the .blend file

   :type load_ui: boolean, (optional)
   :arg use_scripts:

      Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences

   :type use_scripts: boolean, (optional)

.. function:: operator_cheat_sheet()

   List all the Operators in a text-block, useful for scripting

   :file: `startup\bl_operators\wm.py\:1782 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1782>`_

.. function:: operator_defaults()

   Set the active operator to its default values

.. function:: operator_pie_enum(data_path="", prop_string="")

   Undocumented

   :arg data_path:

      Operator, Operator name (in python as string)

   :type data_path: string, (optional, never None)
   :arg prop_string:

      Property, Property name (as a string)

   :type prop_string: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:602 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$602>`_

.. function:: operator_preset_add(name="", remove_active=False, operator="")

   Add or remove an Operator Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)
   :arg operator:

      Operator

   :type operator: string, (optional, never None)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: path_open(filepath="")

   Open a path in a file browser

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:875 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$875>`_

.. function:: previews_batch_clear(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_groups=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True)

   Clear selected .blend file's previews

   :arg files:

      files

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory:

      directory

   :type directory: string, (optional, never None)
   :arg filter_blender:

      filter_blender

   :type filter_blender: boolean, (optional)
   :arg filter_folder:

      filter_folder

   :type filter_folder: boolean, (optional)
   :arg use_scenes:

      Scenes, Clear scenes' previews

   :type use_scenes: boolean, (optional)
   :arg use_groups:

      Groups, Clear groups' previews

   :type use_groups: boolean, (optional)
   :arg use_objects:

      Objects, Clear objects' previews

   :type use_objects: boolean, (optional)
   :arg use_intern_data:

      Mat/Tex/..., Clear 'internal' previews (materials, textures, images, etc.)

   :type use_intern_data: boolean, (optional)
   :arg use_trusted:

      Trusted Blend Files, Enable python evaluation for selected files

   :type use_trusted: boolean, (optional)
   :arg use_backups:

      Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews

   :type use_backups: boolean, (optional)

   :file: `startup\bl_operators\file.py\:208 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\file.py$208>`_

.. function:: previews_batch_generate(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_groups=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True)

   Generate selected .blend file's previews

   :arg files:

      files

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory:

      directory

   :type directory: string, (optional, never None)
   :arg filter_blender:

      filter_blender

   :type filter_blender: boolean, (optional)
   :arg filter_folder:

      filter_folder

   :type filter_folder: boolean, (optional)
   :arg use_scenes:

      Scenes, Generate scenes' previews

   :type use_scenes: boolean, (optional)
   :arg use_groups:

      Groups, Generate groups' previews

   :type use_groups: boolean, (optional)
   :arg use_objects:

      Objects, Generate objects' previews

   :type use_objects: boolean, (optional)
   :arg use_intern_data:

      Mat/Tex/..., Generate 'internal' previews (materials, textures, images, etc.)

   :type use_intern_data: boolean, (optional)
   :arg use_trusted:

      Trusted Blend Files, Enable python evaluation for selected files

   :type use_trusted: boolean, (optional)
   :arg use_backups:

      Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews

   :type use_backups: boolean, (optional)

   :file: `startup\bl_operators\file.py\:99 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\file.py$99>`_

.. function:: previews_clear(id_type={'GROUP', 'IMAGE', 'LAMP', 'MATERIAL', 'OBJECT', 'SCENE', 'TEXTURE', 'WORLD'})

   Clear data-block previews (only for some types like objects, materials, textures, etc.)

   :arg id_type:

      Data-Block Type, Which data-block previews to clear

   :type id_type: enum set in {'SCENE', 'GROUP', 'OBJECT', 'MATERIAL', 'LAMP', 'WORLD', 'TEXTURE', 'IMAGE'}, (optional)

.. function:: previews_ensure()

   Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

.. function:: properties_add(data_path="")

   Undocumented

   :arg data_path:

      Property Edit, Property data_path edit

   :type data_path: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1291 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1291>`_

.. function:: properties_context_change(context="")

   Jump to a different tab inside the properties editor

   :arg context:

      Context

   :type context: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1337 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1337>`_

.. function:: properties_edit(data_path="", property="", value="", min=-10000, max=10000.0, use_soft_limits=False, soft_min=-10000, soft_max=10000.0, description="")

   Undocumented

   :arg data_path:

      Property Edit, Property data_path edit

   :type data_path: string, (optional, never None)
   :arg property:

      Property Name, Property name edit

   :type property: string, (optional, never None)
   :arg value:

      Property Value, Property value edit

   :type value: string, (optional, never None)
   :arg min:

      Min

   :type min: float in [-inf, inf], (optional)
   :arg max:

      Max

   :type max: float in [-inf, inf], (optional)
   :arg use_soft_limits:

      Use Soft Limits

   :type use_soft_limits: boolean, (optional)
   :arg soft_min:

      Min

   :type soft_min: float in [-inf, inf], (optional)
   :arg soft_max:

      Max

   :type soft_max: float in [-inf, inf], (optional)
   :arg description:

      Tooltip

   :type description: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1111 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1111>`_

.. function:: properties_remove(data_path="", property="")

   Internal use (edit a property data_path)

   :arg data_path:

      Property Edit, Property data_path edit

   :type data_path: string, (optional, never None)
   :arg property:

      Property Name, Property name edit

   :type property: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1351 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1351>`_

.. function:: quit_blender()

   Quit Blender

.. function:: radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)

   Set some size property (like e.g. brush size) with mouse wheel

   :arg data_path_primary:

      Primary Data Path, Primary path of property to be set by the radial control

   :type data_path_primary: string, (optional, never None)
   :arg data_path_secondary:

      Secondary Data Path, Secondary path of property to be set by the radial control

   :type data_path_secondary: string, (optional, never None)
   :arg use_secondary:

      Use Secondary, Path of property to select between the primary and secondary data paths

   :type use_secondary: string, (optional, never None)
   :arg rotation_path:

      Rotation Path, Path of property used to rotate the texture display

   :type rotation_path: string, (optional, never None)
   :arg color_path:

      Color Path, Path of property used to set the color of the control

   :type color_path: string, (optional, never None)
   :arg fill_color_path:

      Fill Color Path, Path of property used to set the fill color of the control

   :type fill_color_path: string, (optional, never None)
   :arg fill_color_override_path:

      Fill Color Override Path

   :type fill_color_override_path: string, (optional, never None)
   :arg fill_color_override_test_path:

      Fill Color Override Test

   :type fill_color_override_test_path: string, (optional, never None)
   :arg zoom_path:

      Zoom Path, Path of property used to set the zoom level for the control

   :type zoom_path: string, (optional, never None)
   :arg image_id:

      Image ID, Path of ID that is used to generate an image for the control

   :type image_id: string, (optional, never None)
   :arg secondary_tex:

      Secondary Texture, Tweak brush secondary/mask texture

   :type secondary_tex: boolean, (optional)

.. function:: read_factory_settings(app_template="Template", use_empty=False)

   Load default file and user preferences

   :type app_template: string, (optional, never None)
   :arg use_empty:

      Empty

   :type use_empty: boolean, (optional)

.. function:: read_history()

   Reloads history and bookmarks

.. function:: read_homefile(filepath="", load_ui=True, use_empty=False, use_splash=False, app_template="Template")

   Open the default file (doesn't save the current file)

   :arg filepath:

      File Path, Path to an alternative start-up file

   :type filepath: string, (optional, never None)
   :arg load_ui:

      Load UI, Load user interface setup from the .blend file

   :type load_ui: boolean, (optional)
   :arg use_empty:

      Empty

   :type use_empty: boolean, (optional)
   :arg use_splash:

      Splash

   :type use_splash: boolean, (optional)
   :type app_template: string, (optional, never None)

.. function:: recover_auto_save(filepath="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=False, filter_blenlib=False, filemode=8, display_type='LIST_LONG', sort_method='FILE_SORT_TIME')

   Open an automatically saved file to recover it

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

.. function:: recover_last_session()

   Open the last closed file ("quit.blend")

.. function:: redraw_timer(type='DRAW', iterations=10, time_limit=0.0)

   Simple redraw timer to test the speed of updating the interface

   :arg type:

      Type

      * ``DRAW`` Draw Region, Draw Region.
      * ``DRAW_SWAP`` Draw Region + Swap, Draw Region and Swap.
      * ``DRAW_WIN`` Draw Window, Draw Window.
      * ``DRAW_WIN_SWAP`` Draw Window + Swap, Draw Window and Swap.
      * ``ANIM_STEP`` Anim Step, Animation Steps.
      * ``ANIM_PLAY`` Anim Play, Animation Playback.
      * ``UNDO`` Undo/Redo, Undo/Redo.

   :type type: enum in ['DRAW', 'DRAW_SWAP', 'DRAW_WIN', 'DRAW_WIN_SWAP', 'ANIM_STEP', 'ANIM_PLAY', 'UNDO'], (optional)
   :arg iterations:

      Iterations, Number of times to redraw

   :type iterations: int in [1, inf], (optional)
   :arg time_limit:

      Time Limit, Seconds to run the test for (override iterations)

   :type time_limit: float in [0, inf], (optional)

.. function:: revert_mainfile(use_scripts=True)

   Reload the saved file

   :arg use_scripts:

      Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences

   :type use_scripts: boolean, (optional)

.. function:: save_as_mainfile(filepath="", check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=True, copy=False, use_mesh_compat=False)

   Save the current file in the desired location

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg compress:

      Compress, Write compressed .blend file

   :type compress: boolean, (optional)
   :arg relative_remap:

      Remap Relative, Remap relative paths when saving in a different directory

   :type relative_remap: boolean, (optional)
   :arg copy:

      Save Copy, Save a copy of the actual working state but does not make saved file active

   :type copy: boolean, (optional)
   :arg use_mesh_compat:

      Legacy Mesh Format, Save using legacy mesh format (no ngons) - WARNING: only saves tris and quads, other ngons will be lost (no implicit triangulation)

   :type use_mesh_compat: boolean, (optional)

.. function:: save_homefile()

   Make the current file the default .blend file, includes preferences

.. function:: save_mainfile(filepath="", check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=False)

   Save the current Blender file

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg compress:

      Compress, Write compressed .blend file

   :type compress: boolean, (optional)
   :arg relative_remap:

      Remap Relative, Remap relative paths when saving in a different directory

   :type relative_remap: boolean, (optional)

.. function:: save_userpref()

   Save user preferences separately, overrides startup file preferences

.. function:: search_menu()

   Pop-up a search menu over all available operators in current context

.. function:: set_stereo_3d(display_mode='ANAGLYPH', anaglyph_type='RED_CYAN', interlace_type='ROW_INTERLEAVED', use_interlace_swap=False, use_sidebyside_crosseyed=False)

   Toggle 3D stereo support for current window (or change the display mode)

   :arg display_mode:

      Display Mode

      * ``ANAGLYPH`` Anaglyph, Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).
      * ``INTERLACE`` Interlace, Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).
      * ``TIMESEQUENTIAL`` Time Sequential, Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required).
      * ``SIDEBYSIDE`` Side-by-Side, Render views for left and right eyes side-by-side.
      * ``TOPBOTTOM`` Top-Bottom, Render views for left and right eyes one above another.

   :type display_mode: enum in ['ANAGLYPH', 'INTERLACE', 'TIMESEQUENTIAL', 'SIDEBYSIDE', 'TOPBOTTOM'], (optional)
   :arg anaglyph_type:

      Anaglyph Type

   :type anaglyph_type: enum in ['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE'], (optional)
   :arg interlace_type:

      Interlace Type

   :type interlace_type: enum in ['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED'], (optional)
   :arg use_interlace_swap:

      Swap Left/Right, Swap left and right stereo channels

   :type use_interlace_swap: boolean, (optional)
   :arg use_sidebyside_crosseyed:

      Cross-Eyed, Right eye should see left image and vice-versa

   :type use_sidebyside_crosseyed: boolean, (optional)

.. function:: splash()

   Open the splash screen with release info

.. function:: sysinfo(filepath="")

   Generate system information, saved into a text file

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1435 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1435>`_

.. function:: theme_install(overwrite=True, filepath="", filter_folder=True, filter_glob="*.xml")

   Load and apply a Blender XML theme file

   :arg overwrite:

      Overwrite, Remove existing theme file if exists

   :type overwrite: boolean, (optional)
   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:1902 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$1902>`_

.. function:: url_open(url="")

   Open a website in the web-browser

   :arg url:

      URL, URL to open

   :type url: string, (optional, never None)

   :file: `startup\bl_operators\wm.py\:858 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$858>`_

.. function:: userpref_autoexec_path_add()

   Add path to exclude from autoexecution

.. function:: userpref_autoexec_path_remove(index=0)

   Remove path to exclude from autoexecution

   :arg index:

      Index

   :type index: int in [0, inf], (optional)

.. function:: window_close()

   Close the current Blender window

.. function:: window_duplicate()

   Duplicate the current Blender window

.. function:: window_fullscreen_toggle()

   Toggle the current window fullscreen

