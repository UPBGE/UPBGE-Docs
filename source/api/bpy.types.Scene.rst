Scene(ID)
=========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Scene(ID)

   Scene data-block, consisting in objects and defining time and render related settings

   .. attribute:: active_clip

      Active movie clip used for constraints and viewport drawing

      :type: :class:`MovieClip`

   .. data:: active_layer

      Active scene layer index

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: audio_distance_model

      Distance model for distance attenuation calculation

      * ``NONE`` None, No distance attenuation.
      * ``INVERSE`` Inverse, Inverse distance model.
      * ``INVERSE_CLAMPED`` Inverse Clamped, Inverse distance model with clamping.
      * ``LINEAR`` Linear, Linear distance model.
      * ``LINEAR_CLAMPED`` Linear Clamped, Linear distance model with clamping.
      * ``EXPONENT`` Exponent, Exponent distance model.
      * ``EXPONENT_CLAMPED`` Exponent Clamped, Exponent distance model with clamping.

      :type: enum in ['NONE', 'INVERSE', 'INVERSE_CLAMPED', 'LINEAR', 'LINEAR_CLAMPED', 'EXPONENT', 'EXPONENT_CLAMPED'], default 'NONE'

   .. attribute:: audio_doppler_factor

      Pitch factor for Doppler effect calculation

      :type: float in [0, inf], default 0.0

   .. attribute:: audio_doppler_speed

      Speed of sound for Doppler effect calculation

      :type: float in [0.01, inf], default 0.0

   .. attribute:: audio_volume

      Audio volume

      :type: float in [0, 100], default 0.0

   .. attribute:: background_set

      Background set scene

      :type: :class:`Scene`

   .. attribute:: camera

      Active camera, used for rendering the scene

      :type: :class:`Object`

   .. attribute:: cursor_location

      3D cursor location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: cycles

      Cycles render settings

      :type: :class:`CyclesRenderSettings`, (readonly)

   .. data:: cycles_curves

      Cycles hair rendering settings

      :type: :class:`CyclesCurveRenderSettings`, (readonly)

   .. data:: depsgraph

      Dependencies in the scene data

      :type: :class:`Depsgraph`, (readonly)

   .. data:: display_settings

      Settings of device saved image would be displayed on

      :type: :class:`ColorManagedDisplaySettings`, (readonly)

   .. attribute:: frame_current

      Current Frame, to update animation data from python frame_set() instead

      :type: int in [-1048574, 1048574], default 0

   .. data:: frame_current_final

      Current frame with subframe and time remapping applied

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0, (readonly)

   .. attribute:: frame_end

      Final frame of the playback/rendering range

      :type: int in [0, 1048574], default 0

   .. attribute:: frame_float

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: frame_preview_end

      Alternative end frame for UI playback

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_preview_start

      Alternative start frame for UI playback

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      First frame of the playback/rendering range

      :type: int in [0, 1048574], default 0

   .. attribute:: frame_step

      Number of frames to skip forward while rendering/playing back each frame

      :type: int in [0, 1048574], default 0

   .. attribute:: frame_subframe

      :type: float in [0, 1], default 0.0

   .. data:: game_settings

      :type: :class:`SceneGameData`, (readonly, never None)

   .. attribute:: gravity

      Constant acceleration in a given direction

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: grease_pencil

      Grease Pencil data-block

      :type: :class:`GreasePencil`

   .. data:: is_nla_tweakmode

      Whether there is any action referenced by NLA being edited (strictly read-only)

      :type: boolean, default False, (readonly)

   .. data:: keying_sets

      Absolute Keying Sets for this Scene

      :type: :class:`KeyingSets` :class:`bpy_prop_collection` of :class:`KeyingSet`, (readonly)

   .. data:: keying_sets_all

      All Keying Sets available for use (Builtins and Absolute Keying Sets for this Scene)

      :type: :class:`KeyingSetsAll` :class:`bpy_prop_collection` of :class:`KeyingSet`, (readonly)

   .. attribute:: layers

      Visible layers - Shift-Click/Drag to select multiple layers

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: lock_frame_selection_to_range

      Don't allow frame to be selected with mouse outside of frame range

      :type: boolean, default False

   .. data:: node_tree

      Compositing node tree

      :type: :class:`NodeTree`, (readonly)

   .. data:: object_bases

      :type: :class:`SceneBases` :class:`bpy_prop_collection` of :class:`ObjectBase`, (readonly)

   .. data:: objects

      :type: :class:`SceneObjects` :class:`bpy_prop_collection` of :class:`Object`, (readonly)

   .. data:: orientations

      :type: :class:`bpy_prop_collection` of :class:`TransformOrientation`, (readonly)

   .. data:: render

      :type: :class:`RenderSettings`, (readonly, never None)

   .. data:: rigidbody_world

      :type: :class:`RigidBodyWorld`, (readonly)

   .. data:: safe_areas

      :type: :class:`DisplaySafeAreas`, (readonly, never None)

   .. data:: sequence_editor

      :type: :class:`SequenceEditor`, (readonly)

   .. data:: sequencer_colorspace_settings

      Settings of color space sequencer is working in

      :type: :class:`ColorManagedSequencerColorspaceSettings`, (readonly)

   .. attribute:: show_keys_from_selected_only

      Consider keyframes for active Object and/or its selected bones only (in timeline and when jumping between keyframes)

      :type: boolean, default False

   .. attribute:: show_subframe

      Show current scene subframe and allow set it using interface tools

      :type: boolean, default False

   .. attribute:: sync_mode

      How to sync playback

      * ``NONE`` No Sync, Do not sync, play every frame.
      * ``FRAME_DROP`` Frame Dropping, Drop frames if playback is too slow.
      * ``AUDIO_SYNC`` AV-sync, Sync to audio playback, dropping frames.

      :type: enum in ['NONE', 'FRAME_DROP', 'AUDIO_SYNC'], default 'NONE'

   .. data:: timeline_markers

      Markers used in all timelines for the current scene

      :type: :class:`TimelineMarkers` :class:`bpy_prop_collection` of :class:`TimelineMarker`, (readonly)

   .. data:: tool_settings

      :type: :class:`ToolSettings`, (readonly, never None)

   .. data:: unit_settings

      Unit editing settings

      :type: :class:`UnitSettings`, (readonly, never None)

   .. attribute:: use_audio

      Play back of audio from Sequence Editor will be muted

      :type: boolean, default False

   .. attribute:: use_audio_scrub

      Play audio from Sequence Editor while scrubbing

      :type: boolean, default False

   .. attribute:: use_audio_sync

      Play back and sync with audio clock, dropping frames if frame display is too slow

      :type: boolean, default False

   .. attribute:: use_frame_drop

      Play back dropping frames if frame display is too slow

      :type: boolean, default False

   .. attribute:: use_gravity

      Use global gravity for all dynamics

      :type: boolean, default False

   .. attribute:: use_nodes

      Enable the compositing node tree

      :type: boolean, default False

   .. attribute:: use_preview_range

      Use an alternative start/end frame range for animation playback and OpenGL renders instead of the Render properties start/end frame range

      :type: boolean, default False

   .. attribute:: use_stamp_note

      User defined note for the render stamping

      :type: string, default "", (never None)

   .. data:: view_settings

      Color management settings applied on image before saving

      :type: :class:`ColorManagedViewSettings`, (readonly)

   .. attribute:: world

      World used for rendering the scene

      :type: :class:`World`

   .. method:: sequence_editor_create()

      Ensure sequence editor is valid in this scene

      :return:

         New sequence editor data or NULL

      :rtype: :class:`SequenceEditor`

   .. method:: sequence_editor_clear()

      Clear sequence editor in this scene


   .. method:: statistics()

      statistics

      :return:

         Statistics

      :rtype: string, (never None)

   .. method:: frame_set(frame, subframe=0.0)

      Set scene frame updating all objects immediately

      :arg frame:

         Frame number to set

      :type frame: int in [-1048574, 1048574]
      :arg subframe:

         Sub-frame time, between 0.0 and 1.0

      :type subframe: float in [0, 1], (optional)

   .. method:: update()

      Update data tagged to be updated from previous access to data or operators


   .. method:: uvedit_aspect(object)

      Get uv aspect for current object

      :arg object:

         Object

      :type object: :class:`Object`, (never None)
      :return:

         aspect

      :rtype: float array of 2 items in [0, inf]

   .. method:: ray_cast(origin, direction, distance=1.70141e+38)

      Cast a ray onto in object space

      :type origin: float array of 3 items in [-inf, inf]
      :type direction: float array of 3 items in [-inf, inf]
      :arg distance:

         Maximum distance

      :type distance: float in [0, inf], (optional)
      :return (result, location, normal, index, object, matrix):
         `result`, boolean

         `location`, The hit location of this ray cast, float array of 3 items in [-inf, inf]

         `normal`, The face normal at the ray cast hit location, float array of 3 items in [-inf, inf]

         `index`, The face index, -1 when original data isn't available, int in [-inf, inf]

         `object`, Ray cast object, :class:`Object`

         `matrix`, Matrix, float multi-dimensional array of 4 * 4 items in [-inf, inf]


   .. method:: collada_export(filepath, apply_modifiers=False, export_mesh_type=0, selected=False, include_children=False, include_armatures=False, include_shapekeys=True, deform_bones_only=False, active_uv_only=False, export_texture_type=0, use_texture_copies=True, triangulate=True, use_object_instantiation=True, use_blender_profile=True, sort_by_name=False, export_transformation_type=0, open_sim=False, limit_precision=False, keep_bind_info=False)

      collada_export

      :arg filepath:

         File Path, File path to write Collada file

      :type filepath: string, (never None)
      :arg apply_modifiers:

         Apply Modifiers, Apply modifiers to exported mesh (non destructive))

      :type apply_modifiers: boolean, (optional)
      :arg export_mesh_type:

         Resolution, Modifier resolution for export

      :type export_mesh_type: int in [-inf, inf], (optional)
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
      :arg export_texture_type:

         Texture Type, Type for exported Textures (UV or MAT)

      :type export_texture_type: int in [-inf, inf], (optional)
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
      :arg open_sim:

         Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds

      :type open_sim: boolean, (optional)
      :arg limit_precision:

         Limit Precision, Reduce the precision of the exported data to 6 digits

      :type limit_precision: boolean, (optional)
      :arg keep_bind_info:

         Keep Bind Info, Store bind pose information in custom bone properties for later use during Collada export

      :type keep_bind_info: boolean, (optional)

   .. method:: alembic_export(filepath, frame_start=1, frame_end=1, xform_samples=1, geom_samples=1, shutter_open=0.0, shutter_close=1.0, selected_only=False, uvs=True, normals=True, vcolors=False, apply_subdiv=True, flatten=False, visible_layers_only=False, renderable_only=False, face_sets=False, subdiv_schema=False, export_hair=True, export_particles=True, compression_type='OGAWA', packuv=False, scale=1.0, triangulate=False, quad_method='BEAUTY', ngon_method='BEAUTY')

      Export to Alembic file (deprecated, use the Alembic export operator)

      :arg filepath:

         File Path, File path to write Alembic file

      :type filepath: string, (never None)
      :arg frame_start:

         Start, Start Frame

      :type frame_start: int in [-inf, inf], (optional)
      :arg frame_end:

         End, End Frame

      :type frame_end: int in [-inf, inf], (optional)
      :arg xform_samples:

         Xform samples, Transform samples per frame

      :type xform_samples: int in [1, 128], (optional)
      :arg geom_samples:

         Geom samples, Geometry samples per frame

      :type geom_samples: int in [1, 128], (optional)
      :arg shutter_open:

         Shutter open

      :type shutter_open: float in [-1, 1], (optional)
      :arg shutter_close:

         Shutter close

      :type shutter_close: float in [-1, 1], (optional)
      :arg selected_only:

         Selected only, Export only selected objects

      :type selected_only: boolean, (optional)
      :arg uvs:

         UVs, Export UVs

      :type uvs: boolean, (optional)
      :arg normals:

         Normals, Export cormals

      :type normals: boolean, (optional)
      :arg vcolors:

         Vertex colors, Export vertex colors

      :type vcolors: boolean, (optional)
      :arg apply_subdiv:

         Subsurfs as meshes, Export subdivision surfaces as meshes

      :type apply_subdiv: boolean, (optional)
      :arg flatten:

         Flatten hierarchy, Flatten hierarchy

      :type flatten: boolean, (optional)
      :arg visible_layers_only:

         Visible layers only, Export only objects in visible layers

      :type visible_layers_only: boolean, (optional)
      :arg renderable_only:

         Renderable objects only, Export only objects marked renderable in the outliner

      :type renderable_only: boolean, (optional)
      :arg face_sets:

         Facesets, Export face sets

      :type face_sets: boolean, (optional)
      :arg subdiv_schema:

         Use Alembic subdivision Schema, Use Alembic subdivision Schema

      :type subdiv_schema: boolean, (optional)
      :arg export_hair:

         Export Hair, Exports hair particle systems as animated curves

      :type export_hair: boolean, (optional)
      :arg export_particles:

         Export Particles, Exports non-hair particle systems

      :type export_particles: boolean, (optional)
      :arg compression_type:

         Compression

      :type compression_type: enum in ['OGAWA', 'HDF5'], (optional)
      :arg packuv:

         Export with packed UV islands, Export with packed UV islands

      :type packuv: boolean, (optional)
      :arg scale:

         Scale, Value by which to enlarge or shrink the objects with respect to the world's origin

      :type scale: float in [0.0001, 1000], (optional)
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

   * :mod:`bpy.context.scene`
   * :class:`BlendData.scenes`
   * :class:`BlendDataMeshes.new_from_object`
   * :class:`BlendDataScenes.new`
   * :class:`BlendDataScenes.remove`
   * :class:`Camera.view_frame`
   * :class:`CompositorNodeDefocus.scene`
   * :class:`CompositorNodeRLayers.scene`
   * :class:`Context.scene`
   * :class:`EnvironmentMap.save`
   * :class:`Image.save_render`
   * :class:`Object.camera_fit_coords`
   * :class:`Object.dupli_list_create`
   * :class:`Object.is_deform_modified`
   * :class:`Object.is_modified`
   * :class:`Object.is_visible`
   * :class:`Object.to_mesh`
   * :class:`ParticleSystem.set_resolution`
   * :class:`RenderEngine.bake`
   * :class:`RenderEngine.bind_display_space_shader`
   * :class:`RenderEngine.get_preview_pixel_size`
   * :class:`RenderEngine.register_pass`
   * :class:`RenderEngine.render`
   * :class:`RenderEngine.support_display_space_shader`
   * :class:`RenderEngine.update`
   * :class:`RenderEngine.update_render_passes`
   * :class:`Scene.background_set`
   * :class:`SceneActuator.scene`
   * :class:`SceneSequence.scene`
   * :class:`Screen.scene`
   * :class:`Sequences.new_scene`
   * :class:`ShaderNodeTexPointDensity.cache_point_density`
   * :class:`ShaderNodeTexPointDensity.calc_point_density`
   * :class:`ShaderNodeTexPointDensity.calc_point_density_minmax`

