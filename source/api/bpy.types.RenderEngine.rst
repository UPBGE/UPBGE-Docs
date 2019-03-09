RenderEngine(bpy_struct)
========================

.. module:: bpy.types

Simple Render Engine
++++++++++++++++++++

.. literalinclude:: ..\examples\bpy.types.RenderEngine.py
   :lines: 5-

base class --- :class:`bpy_struct`

.. class:: RenderEngine(bpy_struct)

   Render engine

   .. attribute:: bl_idname

      :type: string, default "", (never None)

   .. attribute:: bl_label

      :type: string, default "", (never None)

   .. attribute:: bl_use_exclude_layers

      :type: boolean, default False

   .. attribute:: bl_use_postprocess

      :type: boolean, default False

   .. attribute:: bl_use_preview

      :type: boolean, default False

   .. attribute:: bl_use_save_buffers

      :type: boolean, default False

   .. attribute:: bl_use_shading_nodes

      :type: boolean, default False

   .. attribute:: bl_use_shading_nodes_custom

      :type: boolean, default True

   .. attribute:: bl_use_spherical_stereo

      :type: boolean, default False

   .. attribute:: bl_use_texture_preview

      :type: boolean, default False

   .. data:: camera_override

      :type: :class:`Object`, (readonly)

   .. attribute:: is_animation

      :type: boolean, default False

   .. attribute:: is_preview

      :type: boolean, default False

   .. attribute:: layer_override

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. data:: render

      :type: :class:`RenderSettings`, (readonly)

   .. data:: resolution_x

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: resolution_y

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: tile_x

      :type: int in [0, inf], default 0

   .. attribute:: tile_y

      :type: int in [0, inf], default 0

   .. attribute:: use_highlight_tiles

      :type: boolean, default False

   .. method:: update(data=None, scene=None)

      Export scene data for render

      :type data: :class:`BlendData`, (optional)
      :type scene: :class:`Scene`, (optional)

   .. method:: render(scene=None)

      Render scene into an image

      :type scene: :class:`Scene`, (optional)

   .. method:: bake(scene, object, pass_type, pass_filter, object_id, pixel_array, num_pixels, depth, result)

      Bake passes

      :type scene: :class:`Scene`
      :type object: :class:`Object`
      :arg pass_type:

         Pass, Pass to bake

      :type pass_type: enum in ['COMBINED', 'AO', 'SHADOW', 'NORMAL', 'UV', 'EMIT', 'ENVIRONMENT', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE']
      :arg pass_filter:

         Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes

      :type pass_filter: int in [0, inf]
      :arg object_id:

         Object Id, Id of the current object being baked in relation to the others

      :type object_id: int in [0, inf]
      :type pixel_array: :class:`BakePixel`
      :arg num_pixels:

         Number of Pixels, Size of the baking batch

      :type num_pixels: int in [0, inf]
      :arg depth:

         Pixels depth, Number of channels

      :type depth: int in [0, inf]
      :type result: :class:`AnyType`

   .. method:: view_update(context=None)

      Update on data changes for viewport render

      :type context: :class:`Context`, (optional)

   .. method:: view_draw(context=None)

      Draw viewport render

      :type context: :class:`Context`, (optional)

   .. method:: update_script_node(node=None)

      Compile shader script node

      :type node: :class:`Node`, (optional)

   .. method:: tag_redraw()

      Request redraw for viewport rendering


   .. method:: tag_update()

      Request update call for viewport rendering


   .. method:: update_render_passes(scene=None, renderlayer=None)

      Update the render passes that will be generated

      :type scene: :class:`Scene`, (optional)
      :type renderlayer: :class:`SceneRenderLayer`, (optional)

   .. method:: begin_result(x, y, w, h, layer="", view="")

      Create render result to write linear floating point render layers and passes

      :arg x:

         X

      :type x: int in [0, inf]
      :arg y:

         Y

      :type y: int in [0, inf]
      :arg w:

         Width

      :type w: int in [0, inf]
      :arg h:

         Height

      :type h: int in [0, inf]
      :arg layer:

         Layer, Single layer to get render result for

      :type layer: string, (optional, never None)
      :arg view:

         View, Single view to get render result for

      :type view: string, (optional, never None)
      :return:

         Result

      :rtype: :class:`RenderResult`

   .. method:: update_result(result)

      Signal that pixels have been updated and can be redrawn in the user interface

      :arg result:

         Result

      :type result: :class:`RenderResult`

   .. method:: end_result(result, cancel=False, highlight=False, do_merge_results=False)

      All pixels in the render result have been set and are final

      :arg result:

         Result

      :type result: :class:`RenderResult`
      :arg cancel:

         Cancel, Don't mark tile as done, don't merge results unless forced

      :type cancel: boolean, (optional)
      :arg highlight:

         Highlight, Don't mark tile as done yet

      :type highlight: boolean, (optional)
      :arg do_merge_results:

         Merge Results, Merge results even if cancel=true

      :type do_merge_results: boolean, (optional)

   .. method:: add_pass(name, channels, chan_id, layer="")

      Add a pass to the render layer

      :arg name:

         Name, Name of the Pass, without view or channel tag

      :type name: string, (never None)
      :arg channels:

         Channels

      :type channels: int in [0, inf]
      :arg chan_id:

         Channel IDs, Channel names, one character per channel

      :type chan_id: string, (never None)
      :arg layer:

         Layer, Single layer to add render pass to

      :type layer: string, (optional, never None)

   .. method:: get_result()

      Get final result for non-pixel operations

      :return:

         Result

      :rtype: :class:`RenderResult`

   .. method:: test_break()

      Test if the render operation should been canceled, this is a fast call that should be used regularly for responsiveness

      :return:

         Break

      :rtype: boolean

   .. method:: active_view_get()

      active_view_get

      :return:

         View, Single view active

      :rtype: string, (never None)

   .. method:: active_view_set(view)

      active_view_set

      :arg view:

         View, Single view to set as active

      :type view: string, (never None)

   .. method:: camera_shift_x(camera, use_spherical_stereo=False)

      camera_shift_x

      :type camera: :class:`Object`
      :arg use_spherical_stereo:

         Spherical Stereo

      :type use_spherical_stereo: boolean, (optional)
      :return:

         Shift X

      :rtype: float in [0, inf]

   .. method:: camera_model_matrix(camera, use_spherical_stereo=False, r_model_matrix)

      camera_model_matrix

      :type camera: :class:`Object`
      :arg use_spherical_stereo:

         Spherical Stereo

      :type use_spherical_stereo: boolean, (optional)
      :arg r_model_matrix:

         Model Matrix, Normalized camera model matrix

      :type r_model_matrix: float multi-dimensional array of 4 * 4 items in [-inf, inf]

   .. method:: use_spherical_stereo(camera)

      use_spherical_stereo

      :type camera: :class:`Object`
      :return:

         Spherical Stereo

      :rtype: boolean

   .. method:: update_stats(stats, info)

      Update and signal to redraw render status text

      :arg stats:

         Stats

      :type stats: string, (never None)
      :arg info:

         Info

      :type info: string, (never None)

   .. method:: frame_set(frame, subframe)

      Evaluate scene at a different frame (for motion blur)

      :arg frame:

         Frame

      :type frame: int in [-inf, inf]
      :arg subframe:

         Subframe

      :type subframe: float in [0, 1]

   .. method:: update_progress(progress)

      Update progress percentage of render

      :arg progress:

         Percentage of render that's done

      :type progress: float in [0, 1]

   .. method:: update_memory_stats(memory_used=0.0, memory_peak=0.0)

      Update memory usage statistics

      :arg memory_used:

         Current memory usage in megabytes

      :type memory_used: float in [0, inf], (optional)
      :arg memory_peak:

         Peak memory usage in megabytes

      :type memory_peak: float in [0, inf], (optional)

   .. method:: report(type, message)

      Report info, warning or error messages

      :arg type:

         Type

      :type type: enum set in {'DEBUG', 'INFO', 'OPERATOR', 'PROPERTY', 'WARNING', 'ERROR', 'ERROR_INVALID_INPUT', 'ERROR_INVALID_CONTEXT', 'ERROR_OUT_OF_MEMORY'}
      :arg message:

         Report Message

      :type message: string, (never None)

   .. method:: error_set(message)

      Set error message displaying after the render is finished

      :arg message:

         Report Message

      :type message: string, (never None)

   .. method:: bind_display_space_shader(scene)

      Bind GLSL fragment shader that converts linear colors to display space colors using scene color management settings

      :type scene: :class:`Scene`

   .. method:: unbind_display_space_shader()

      Unbind GLSL display space shader, must always be called after binding the shader


   .. method:: support_display_space_shader(scene)

      Test if GLSL display space shader is supported for the combination of graphics card and scene settings

      :type scene: :class:`Scene`
      :return:

         Supported

      :rtype: boolean

   .. method:: get_preview_pixel_size(scene)

      Get the pixel size that should be used for preview rendering

      :type scene: :class:`Scene`
      :return:

         Pixel Size

      :rtype: int in [1, 8]

   .. method:: register_pass(scene=None, srl=None, name="", channels=1, chanid="", type='VALUE')

      Register a render pass that will be part of the render with the current settings

      :type scene: :class:`Scene`, (optional)
      :type srl: :class:`SceneRenderLayer`, (optional)
      :arg name:

         Name

      :type name: string, (optional, never None)
      :arg channels:

         Channels

      :type channels: int in [1, 8], (optional)
      :arg chanid:

         Channel IDs

      :type chanid: string, (optional, never None)
      :arg type:

         Type

      :type type: enum in ['VALUE', 'VECTOR', 'COLOR'], (optional)

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

