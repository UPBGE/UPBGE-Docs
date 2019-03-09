RenderSettings(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderSettings(bpy_struct)

   Rendering settings for a Scene data-block

   .. attribute:: alpha_mode

      Representation of alpha information in the RGBA pixels

      * ``SKY`` Sky, Transparent pixels are filled with sky color.
      * ``TRANSPARENT`` Transparent, World background is transparent with premultiplied alpha.

      :type: enum in ['SKY', 'TRANSPARENT'], default 'SKY'

   .. attribute:: antialiasing_samples

      Amount of anti-aliasing samples per pixel

      :type: enum in ['5', '8', '11', '16'], default '5'

   .. data:: bake

      :type: :class:`BakeSettings`, (readonly, never None)

   .. attribute:: bake_aa_mode

      :type: enum in ['5', '8', '11', '16'], default '5'

   .. attribute:: bake_bias

      Bias towards faces further away from the object (in blender units)

      :type: float in [0, 1000], default 0.0

   .. attribute:: bake_distance

      Maximum distance from active object to other object (in blender units)

      :type: float in [0, 1000], default 0.0

   .. attribute:: bake_margin

      Extends the baked result as a post process filter

      :type: int in [0, 64], default 0

   .. attribute:: bake_normal_space

      Choose normal space for baking

      * ``CAMERA`` Camera, Bake the normals in camera space.
      * ``WORLD`` World, Bake the normals in world space.
      * ``OBJECT`` Object, Bake the normals in object space.
      * ``TANGENT`` Tangent, Bake the normals in tangent space.

      :type: enum in ['CAMERA', 'WORLD', 'OBJECT', 'TANGENT'], default 'CAMERA'

   .. attribute:: bake_quad_split

      Choose the method used to split a quad into 2 triangles for baking

      * ``AUTO`` Automatic, Split quads to give the least distortion while baking.
      * ``FIXED`` Fixed, Split quads predictably (0,1,2) (0,2,3).
      * ``FIXED_ALT`` Fixed Alternate, Split quads predictably (1,2,3) (1,3,0).

      :type: enum in ['AUTO', 'FIXED', 'FIXED_ALT'], default 'AUTO'

   .. attribute:: bake_samples

      Number of samples used for ambient occlusion baking from multires

      :type: int in [64, 1024], default 256

   .. attribute:: bake_type

      Choose shading information to bake into the image

      * ``FULL`` Full Render, Bake everything.
      * ``AO`` Ambient Occlusion, Bake ambient occlusion.
      * ``SHADOW`` Shadow, Bake shadows.
      * ``NORMALS`` Normals, Bake normals.
      * ``TEXTURE`` Textures, Bake textures.
      * ``DISPLACEMENT`` Displacement, Bake displacement.
      * ``DERIVATIVE`` Derivative, Bake derivative map.
      * ``VERTEX_COLORS`` Vertex Colors, Bake vertex colors.
      * ``EMIT`` Emission, Bake Emit values (glow).
      * ``ALPHA`` Alpha, Bake Alpha values (transparency).
      * ``MIRROR_INTENSITY`` Mirror Intensity, Bake Mirror values.
      * ``MIRROR_COLOR`` Mirror Colors, Bake Mirror colors.
      * ``SPEC_INTENSITY`` Specular Intensity, Bake Specular values.
      * ``SPEC_COLOR`` Specular Colors, Bake Specular colors.

      :type: enum in ['FULL', 'AO', 'SHADOW', 'NORMALS', 'TEXTURE', 'DISPLACEMENT', 'DERIVATIVE', 'VERTEX_COLORS', 'EMIT', 'ALPHA', 'MIRROR_INTENSITY', 'MIRROR_COLOR', 'SPEC_INTENSITY', 'SPEC_COLOR'], default 'FULL'

   .. attribute:: bake_user_scale

      Instead of automatically normalizing to 0..1, apply a user scale to the derivative map

      :type: float in [0, 1000], default 0.0

   .. attribute:: border_max_x

      Maximum X value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: border_max_y

      Maximum Y value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: border_min_x

      Minimum X value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: border_min_y

      Minimum Y value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: display_mode

      Select where rendered images will be displayed

      * ``SCREEN`` Full Screen, Images are rendered in full Screen.
      * ``AREA`` Image Editor, Images are rendered in Image Editor.
      * ``WINDOW`` New Window, Images are rendered in new Window.
      * ``NONE`` Keep UI, Images are rendered without forcing UI changes.

      :type: enum in ['SCREEN', 'AREA', 'WINDOW', 'NONE'], default 'SCREEN'

   .. attribute:: dither_intensity

      Amount of dithering noise added to the rendered image to break up banding

      :type: float in [0, 2], default 0.0

   .. attribute:: edge_color

      Edge color

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: edge_threshold

      Threshold for drawing outlines on geometry edges

      :type: int in [0, 255], default 0

   .. attribute:: engine

      Engine to use for rendering

      * ``BLENDER_RENDER`` Blender Render, Use the Blender internal rendering engine for rendering.

      :type: enum in ['BLENDER_RENDER'], default 'BLENDER_RENDER'

   .. data:: ffmpeg

      FFmpeg related settings for the scene

      :type: :class:`FFmpegSettings`, (readonly)

   .. attribute:: field_order

      Order of video fields (select which lines get rendered first, to create smooth motion for TV output)

      * ``EVEN_FIRST`` Upper First, Upper field first.
      * ``ODD_FIRST`` Lower First, Lower field first.

      :type: enum in ['EVEN_FIRST', 'ODD_FIRST'], default 'EVEN_FIRST'

   .. data:: file_extension

      The file extension used for saving renders

      :type: string, default "", (readonly, never None)

   .. attribute:: filepath

      Directory/name to save animations, # characters defines the position and length of frame numbers

      :type: string, default "", (never None)

   .. attribute:: filter_size

      Width over which the reconstruction filter combines samples

      :type: float in [0.5, 1.5], default 0.0

   .. attribute:: fps

      Framerate, expressed in frames per second

      :type: int in [1, 120], default 0

   .. attribute:: fps_base

      Framerate base

      :type: float in [0.1, 120], default 0.0

   .. attribute:: frame_map_new

      How many frames the Map Old will last

      :type: int in [1, 900], default 0

   .. attribute:: frame_map_old

      Old mapping value in frames

      :type: int in [1, 900], default 0

   .. data:: has_multiple_engines

      More than one rendering engine is available

      :type: boolean, default False, (readonly)

   .. data:: image_settings

      :type: :class:`ImageFormatSettings`, (readonly, never None)

   .. data:: is_movie_format

      When true the format is a movie

      :type: boolean, default False, (readonly)

   .. data:: layers

      :type: :class:`RenderLayers` :class:`bpy_prop_collection` of :class:`SceneRenderLayer`, (readonly)

   .. attribute:: line_thickness

      Line thickness in pixels

      :type: float in [0, 10000], default 0.0

   .. attribute:: line_thickness_mode

      Line thickness mode for Freestyle line drawing

      * ``ABSOLUTE`` Absolute, Specify unit line thickness in pixels.
      * ``RELATIVE`` Relative, Unit line thickness is scaled by the proportion of the present vertical image resolution to 480 pixels.

      :type: enum in ['ABSOLUTE', 'RELATIVE'], default 'ABSOLUTE'

   .. attribute:: motion_blur_samples

      Number of scene samples to take with motion blur

      :type: int in [1, 32], default 0

   .. attribute:: motion_blur_shutter

      Time taken in frames between shutter open and close (NOTE: Blender Internal does not support animated shutter)

      :type: float in [0, inf], default 0.0

   .. data:: motion_blur_shutter_curve

      Curve defining the shutter's openness over time

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: octree_resolution

      Resolution of raytrace accelerator, use higher resolutions for larger scenes

      :type: enum in ['64', '128', '256', '512'], default '64'

   .. attribute:: pixel_aspect_x

      Horizontal aspect ratio - for anamorphic or non-square pixel output

      :type: float in [1, 200], default 0.0

   .. attribute:: pixel_aspect_y

      Vertical aspect ratio - for anamorphic or non-square pixel output

      :type: float in [1, 200], default 0.0

   .. attribute:: pixel_filter_type

      Reconstruction filter used for combining anti-aliasing samples

      * ``BOX`` Box, Use a box filter for anti-aliasing.
      * ``TENT`` Tent, Use a tent filter for anti-aliasing.
      * ``QUADRATIC`` Quadratic, Use a quadratic filter for anti-aliasing.
      * ``CUBIC`` Cubic, Use a cubic filter for anti-aliasing.
      * ``CATMULLROM`` Catmull-Rom, Use a Catmull-Rom filter for anti-aliasing.
      * ``GAUSSIAN`` Gaussian, Use a Gaussian filter for anti-aliasing.
      * ``MITCHELL`` Mitchell-Netravali, Use a Mitchell-Netravali filter for anti-aliasing.

      :type: enum in ['BOX', 'TENT', 'QUADRATIC', 'CUBIC', 'CATMULLROM', 'GAUSSIAN', 'MITCHELL'], default 'BOX'

   .. attribute:: preview_pixel_size

      Pixel size for viewport rendering

      * ``AUTO`` Automatic, Automatic pixel size, depends on the UI scale.
      * ``1`` 1x, Render at full resolution.
      * ``2`` 2x, Render at 50% resolution.
      * ``4`` 4x, Render at 25% resolution.
      * ``8`` 8x, Render at 12.5% resolution.

      :type: enum in ['AUTO', '1', '2', '4', '8'], default 'AUTO'

   .. attribute:: preview_start_resolution

      Resolution to start rendering preview at, progressively increasing it to the full viewport size

      :type: int in [8, 16384], default 64

   .. attribute:: raytrace_method

      Type of raytrace accelerator structure

      * ``AUTO`` Auto, Automatically select acceleration structure.
      * ``OCTREE`` Octree, Use old Octree structure.
      * ``VBVH`` vBVH, Use vBVH.
      * ``SIMD_SVBVH`` SIMD SVBVH, Use SIMD SVBVH.
      * ``SIMD_QBVH`` SIMD QBVH, Use SIMD QBVH.

      :type: enum in ['AUTO', 'OCTREE', 'VBVH', 'SIMD_SVBVH', 'SIMD_QBVH'], default 'AUTO'

   .. attribute:: resolution_percentage

      Percentage scale for render resolution

      :type: int in [1, 32767], default 0

   .. attribute:: resolution_x

      Number of horizontal pixels in the rendered image

      :type: int in [4, 65536], default 0

   .. attribute:: resolution_y

      Number of vertical pixels in the rendered image

      :type: int in [4, 65536], default 0

   .. attribute:: sequencer_gl_preview

      Method to draw in the sequencer view

      * ``BOUNDBOX`` Bounding Box, Display the object's local bounding boxes only.
      * ``WIREFRAME`` Wireframe, Display the object as wire edges.
      * ``SOLID`` Solid, Display the object solid, lit with default OpenGL lights.
      * ``TEXTURED`` Texture, Display the object solid, with a texture.
      * ``MATERIAL`` Material, Display objects solid, with GLSL material.
      * ``RENDERED`` Rendered, Display render preview.

      :type: enum in ['BOUNDBOX', 'WIREFRAME', 'SOLID', 'TEXTURED', 'MATERIAL', 'RENDERED'], default 'BOUNDBOX'

   .. attribute:: simplify_ao_sss

      Global approximate AO and SSS quality factor

      :type: float in [0, 1], default 0.0

   .. attribute:: simplify_child_particles

      Global child particles percentage

      :type: float in [0, 1], default 0.0

   .. attribute:: simplify_child_particles_render

      Global child particles percentage during rendering

      :type: float in [0, 1], default 0.0

   .. attribute:: simplify_shadow_samples

      Global maximum shadow samples

      :type: int in [0, 32767], default 0

   .. attribute:: simplify_subdivision

      Global maximum subdivision level

      :type: int in [0, 32767], default 0

   .. attribute:: simplify_subdivision_render

      Global maximum subdivision level during rendering

      :type: int in [0, 32767], default 0

   .. attribute:: stamp_background

      Color to use behind stamp text

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: stamp_font_size

      Size of the font used when rendering stamp text

      :type: int in [8, 64], default 0

   .. attribute:: stamp_foreground

      Color to use for stamp text

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: stamp_note_text

      Custom text to appear in the stamp note

      :type: string, default "", (never None)

   .. data:: stereo_views

      :type: :class:`bpy_prop_collection` of :class:`SceneRenderView`, (readonly)

   .. attribute:: threads

      Number of CPU threads to use simultaneously while rendering (for multi-core/CPU systems)

      :type: int in [1, 1024], default 0

   .. attribute:: threads_mode

      Determine the amount of render threads used

      * ``AUTO`` Auto-detect, Automatically determine the number of threads, based on CPUs.
      * ``FIXED`` Fixed, Manually determine the number of threads.

      :type: enum in ['AUTO', 'FIXED'], default 'AUTO'

   .. attribute:: tile_x

      Horizontal tile size to use while rendering

      :type: int in [8, 65536], default 0

   .. attribute:: tile_y

      Vertical tile size to use while rendering

      :type: int in [8, 65536], default 0

   .. attribute:: use_antialiasing

      Render and combine multiple samples per pixel to prevent jagged edges

      :type: boolean, default False

   .. attribute:: use_bake_antialiasing

      Enables Anti-aliasing

      :type: boolean, default False

   .. attribute:: use_bake_clear

      Clear Images before baking

      :type: boolean, default False

   .. attribute:: use_bake_lores_mesh

      Calculate heights against unsubdivided low resolution mesh

      :type: boolean, default False

   .. attribute:: use_bake_multires

      Bake directly from multires object

      :type: boolean, default False

   .. attribute:: use_bake_normalize

      With displacement normalize to the distance, with ambient occlusion normalize without using material settings

      :type: boolean, default False

   .. attribute:: use_bake_selected_to_active

      Bake shading on the surface of selected objects to the active object

      :type: boolean, default False

   .. attribute:: use_bake_to_vertex_color

      Bake to vertex colors instead of to a UV-mapped image

      :type: boolean, default False

   .. attribute:: use_bake_user_scale

      Use a user scale for the derivative map

      :type: boolean, default False

   .. attribute:: use_border

      Render a user-defined border region, within the frame size (note that this disables save_buffers and full_sample)

      :type: boolean, default False

   .. attribute:: use_compositing

      Process the render result through the compositing pipeline, if compositing nodes are enabled

      :type: boolean, default False

   .. attribute:: use_crop_to_border

      Crop the rendered frame to the defined border size

      :type: boolean, default False

   .. attribute:: use_edge_enhance

      Create a toon outline around the edges of geometry

      :type: boolean, default False

   .. attribute:: use_envmaps

      Calculate environment maps while rendering

      :type: boolean, default False

   .. attribute:: use_fields

      Render image to two fields per frame, for interlaced TV output

      :type: boolean, default False

   .. attribute:: use_fields_still

      Disable the time difference between fields

      :type: boolean, default False

   .. attribute:: use_file_extension

      Add the file format extensions to the rendered file name (eg: filename + .jpg)

      :type: boolean, default False

   .. attribute:: use_free_image_textures

      Free all image textures from memory after render, to save memory before compositing

      :type: boolean, default False

   .. attribute:: use_freestyle

      Draw stylized strokes using Freestyle

      :type: boolean, default False

   .. attribute:: use_full_sample

      Save for every anti-aliasing sample the entire RenderLayer results (this solves anti-aliasing issues with compositing)

      :type: boolean, default False

   .. data:: use_game_engine

      Current rendering engine is a game engine

      :type: boolean, default False, (readonly)

   .. attribute:: use_instances

      Instance support leads to effective memory reduction when using duplicates

      :type: boolean, default False

   .. attribute:: use_local_coords

      Vertex coordinates are stored locally on each primitive (increases memory usage, but may have impact on speed)

      :type: boolean, default False

   .. attribute:: use_lock_interface

      Lock interface during rendering in favor of giving more memory to the renderer

      :type: boolean, default False

   .. attribute:: use_motion_blur

      Use multi-sampled 3D scene motion blur

      :type: boolean, default False

   .. attribute:: use_multiview

      Use multiple views in the scene

      :type: boolean, default False

   .. attribute:: use_overwrite

      Overwrite existing files while rendering

      :type: boolean, default False

   .. attribute:: use_persistent_data

      Keep render data around for faster re-renders

      :type: boolean, default False

   .. attribute:: use_placeholder

      Create empty placeholder files while rendering frames (similar to Unix 'touch')

      :type: boolean, default False

   .. attribute:: use_raytrace

      Pre-calculate the raytrace accelerator and render raytracing effects

      :type: boolean, default False

   .. attribute:: use_render_cache

      Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes)

      :type: boolean, default False

   .. attribute:: use_save_buffers

      Save tiles for all RenderLayers and SceneNodes to files in the temp directory (saves memory, required for Full Sample)

      :type: boolean, default False

   .. attribute:: use_sequencer

      Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist

      :type: boolean, default False

   .. attribute:: use_sequencer_gl_dof

      Use depth of field using the values from scene strip active camera

      :type: boolean, default False

   .. attribute:: use_sequencer_gl_textured_solid

      Draw face-assigned textures in solid draw method

      :type: boolean, default False

   .. data:: use_shading_nodes

      Active render engine uses new shading nodes system

      :type: boolean, default False, (readonly)

   .. attribute:: use_shadows

      Calculate shadows while rendering

      :type: boolean, default False

   .. attribute:: use_simplify

      Enable simplification of scene for quicker preview renders

      :type: boolean, default False

   .. attribute:: use_simplify_triangulate

      Disable non-planar quads being triangulated

      :type: boolean, default False

   .. attribute:: use_single_layer

      Only render the active layer

      :type: boolean, default False

   .. data:: use_spherical_stereo

      Active render engine supports spherical stereo rendering

      :type: boolean, default False, (readonly)

   .. attribute:: use_sss

      Calculate sub-surface scattering in materials rendering

      :type: boolean, default False

   .. attribute:: use_stamp

      Render the stamp info text in the rendered image

      :type: boolean, default False

   .. attribute:: use_stamp_camera

      Include the name of the active camera in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_date

      Include the current date in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_filename

      Include the .blend filename in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_frame

      Include the frame number in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_labels

      Draw stamp labels ("Camera" in front of camera name, etc.)

      :type: boolean, default False

   .. attribute:: use_stamp_lens

      Include the active camera's lens in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_marker

      Include the name of the last marker in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_memory

      Include the peak memory usage in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_note

      Include a custom note in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_render_time

      Include the render time in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_scene

      Include the name of the active scene in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_sequencer_strip

      Include the name of the foreground sequence strip in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_strip_meta

      Use metadata from the strips in the sequencer

      :type: boolean, default False

   .. attribute:: use_stamp_time

      Include the rendered frame timecode as HH:MM:SS.FF in image metadata

      :type: boolean, default False

   .. attribute:: use_textures

      Use textures to affect material properties

      :type: boolean, default False

   .. attribute:: use_world_space_shading

      Use world space interpretation of lighting data for node materials

      :type: boolean, default False

   .. data:: views

      :type: :class:`RenderViews` :class:`bpy_prop_collection` of :class:`SceneRenderView`, (readonly)

   .. attribute:: views_format

      * ``STEREO_3D`` Stereo 3D, Single stereo camera system, adjust the stereo settings in the camera panel.
      * ``MULTIVIEW`` Multi-View, Multi camera system, adjust the cameras individually.

      :type: enum in ['STEREO_3D', 'MULTIVIEW'], default 'STEREO_3D'

   .. method:: frame_path(frame=-2147483648, preview=False, view="")

      Return the absolute path to the filename to be written for a given frame

      :arg frame:

         Frame number to use, if unset the current frame will be used

      :type frame: int in [-inf, inf], (optional)
      :arg preview:

         Preview, Use preview range

      :type preview: boolean, (optional)
      :arg view:

         View, The name of the view to use to replace the "%" chars

      :type view: string, (optional, never None)
      :return:

         File Path, The resulting filepath from the scenes render settings

      :rtype: string, (never None)

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

   * :class:`RenderEngine.render`
   * :class:`Scene.render`

