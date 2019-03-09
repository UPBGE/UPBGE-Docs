SpaceView3D(Space)
==================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceView3D(Space)

   3D View space data

   .. data:: active_layer

      Active 3D view layer index

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: background_images

      List of background images

      :type: :class:`BackgroundImages` :class:`bpy_prop_collection` of :class:`BackgroundImage`, (readonly)

   .. attribute:: camera

      Active camera used in this view (when unlocked from the scene's active camera)

      :type: :class:`Object`

   .. attribute:: clip_end

      3D View far clipping distance

      :type: float in [1e-06, inf], default 1000.0

   .. attribute:: clip_start

      3D View near clipping distance (perspective view only)

      :type: float in [1e-06, inf], default 0.1

   .. data:: current_orientation

      Current transformation orientation

      :type: :class:`TransformOrientation`, (readonly)

   .. attribute:: cursor_location

      3D cursor location for this view (dependent on local view setting)

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: fx_settings

      Options used for real time compositing

      :type: :class:`GPUFXSettings`, (readonly)

   .. attribute:: grid_lines

      Number of grid lines to display in perspective view

      :type: int in [0, 1024], default 16

   .. attribute:: grid_scale

      Distance between 3D View grid lines

      :type: float in [0, inf], default 1.0

   .. data:: grid_scale_unit

      Grid cell size scaled by scene unit system settings

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: grid_subdivisions

      Number of subdivisions between grid lines

      :type: int in [1, 1024], default 10

   .. attribute:: layers

      Layers visible in this 3D View

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. data:: layers_local_view

      Local view layers visible in this 3D View

      :type: boolean array of 8 items, default (False, False, False, False, False, False, False, False), (readonly)

   .. data:: layers_used

      Layers that contain something

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), (readonly)

   .. attribute:: lens

      Viewport lens angle

      :type: float in [1, 250], default 0.0

   .. data:: local_view

      Display an isolated sub-set of objects, apart from the scene visibility

      :type: :class:`SpaceView3D`, (readonly)

   .. attribute:: lock_bone

      3D View center is locked to this bone's position

      :type: string, default "", (never None)

   .. attribute:: lock_camera

      Enable view navigation within the camera view

      :type: boolean, default False

   .. attribute:: lock_camera_and_layers

      Use the scene's active camera and layers in this view, rather than local layers

      :type: boolean, default False

   .. attribute:: lock_cursor

      3D View center is locked to the cursor's position

      :type: boolean, default False

   .. attribute:: lock_object

      3D View center is locked to this object's position

      :type: :class:`Object`

   .. attribute:: matcap_icon

      Image to use for Material Capture, active objects only

      :type: enum in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'], default '01'

   .. attribute:: pivot_point

      Pivot center for rotation/scaling

      * ``BOUNDING_BOX_CENTER`` Bounding Box Center, Pivot around bounding box center of selected object(s).
      * ``CURSOR`` 3D Cursor, Pivot around the 3D cursor.
      * ``INDIVIDUAL_ORIGINS`` Individual Origins, Pivot around each object's own origin.
      * ``MEDIAN_POINT`` Median Point, Pivot around the median point of selected objects.
      * ``ACTIVE_ELEMENT`` Active Element, Pivot around active object.

      :type: enum in ['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT'], default 'BOUNDING_BOX_CENTER'

   .. data:: region_3d

      3D region in this space, in case of quad view the camera region

      :type: :class:`RegionView3D`, (readonly)

   .. data:: region_quadviews

      3D regions (the third one defines quad view settings, the fourth one is same as 'region_3d')

      :type: :class:`bpy_prop_collection` of :class:`RegionView3D`, (readonly)

   .. attribute:: render_border_max_x

      Maximum X value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: render_border_max_y

      Maximum Y value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: render_border_min_x

      Minimum X value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: render_border_min_y

      Minimum Y value for the render border

      :type: float in [0, 1], default 0.0

   .. attribute:: show_all_objects_origin

      Show the object origin center dot for all (selected and unselected) objects

      :type: boolean, default False

   .. attribute:: show_axis_x

      Show the X axis line in perspective view

      :type: boolean, default False

   .. attribute:: show_axis_y

      Show the Y axis line in perspective view

      :type: boolean, default False

   .. attribute:: show_axis_z

      Show the Z axis line in perspective view

      :type: boolean, default False

   .. attribute:: show_backface_culling

      Use back face culling to hide the back side of faces

      :type: boolean, default False

   .. attribute:: show_background_images

      Display reference images behind objects in the 3D View

      :type: boolean, default False

   .. attribute:: show_bundle_names

      Show names for reconstructed tracks objects

      :type: boolean, default False

   .. attribute:: show_camera_path

      Show reconstructed camera path

      :type: boolean, default False

   .. attribute:: show_floor

      Show the ground plane grid in perspective view

      :type: boolean, default False

   .. attribute:: show_grease_pencil

      Show grease pencil for this view

      :type: boolean, default False

   .. attribute:: show_manipulator

      Use a 3D manipulator widget for controlling transforms

      :type: boolean, default False

   .. attribute:: show_mist

      Display world mist

      :type: boolean, default False

   .. attribute:: show_occlude_wire

      Use hidden wireframe display

      :type: boolean, default False

   .. attribute:: show_only_render

      Display only objects which will be rendered

      :type: boolean, default False

   .. attribute:: show_outline_selected

      Show an outline highlight around selected objects in non-wireframe views

      :type: boolean, default False

   .. attribute:: show_reconstruction

      Display reconstruction data from active movie clip

      :type: boolean, default False

   .. attribute:: show_relationship_lines

      Show dashed lines indicating parent or constraint relationships

      :type: boolean, default False

   .. attribute:: show_stereo_3d_cameras

      Show the left and right cameras

      :type: boolean, default False

   .. attribute:: show_stereo_3d_convergence_plane

      Show the stereo 3d convergence plane

      :type: boolean, default False

   .. attribute:: show_stereo_3d_volume

      Show the stereo 3d frustum volume

      :type: boolean, default False

   .. attribute:: show_textured_shadeless

      Show shadeless texture without lighting in textured draw mode

      :type: boolean, default False

   .. attribute:: show_textured_solid

      Display face-assigned textures in solid view

      :type: boolean, default False

   .. attribute:: show_world

      Display world colors in the background

      :type: boolean, default False

   .. attribute:: stereo_3d_camera

      :type: enum in ['LEFT', 'RIGHT', 'S3D'], default 'LEFT'

   .. attribute:: stereo_3d_convergence_plane_alpha

      Opacity (alpha) of the convergence plane

      :type: float in [0, 1], default 0.0

   .. data:: stereo_3d_eye

      Current stereo eye being drawn

      :type: enum in ['LEFT_EYE', 'RIGHT_EYE'], default 'LEFT_EYE', (readonly)

   .. attribute:: stereo_3d_volume_alpha

      Opacity (alpha) of the cameras' frustum volume

      :type: float in [0, 1], default 0.0

   .. attribute:: tracks_draw_size

      Display size of tracks from reconstructed data

      :type: float in [0, inf], default 0.0

   .. attribute:: tracks_draw_type

      Viewport display style for tracks

      :type: enum in ['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE'], default 'PLAIN_AXES'

   .. attribute:: transform_manipulators

      Transformation manipulators

      * ``TRANSLATE`` Translate, Use the manipulator for movement transformations.
      * ``ROTATE`` Rotate, Use the manipulator for rotation transformations.
      * ``SCALE`` Scale, Use the manipulator for scale transformations.

      :type: enum set in {'TRANSLATE', 'ROTATE', 'SCALE'}, default {'TRANSLATE'}

   .. attribute:: transform_orientation

      Transformation orientation

      * ``GLOBAL`` Global, Align the transformation axes to world space.
      * ``LOCAL`` Local, Align the transformation axes to the selected objects' local space.
      * ``NORMAL`` Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).
      * ``GIMBAL`` Gimbal, Align each axis to the Euler rotation axis as used for input.
      * ``VIEW`` View, Align the transformation axes to the window.

      :type: enum in ['GLOBAL', 'LOCAL', 'NORMAL', 'GIMBAL', 'VIEW'], default 'GLOBAL'

   .. attribute:: use_matcap

      Active Objects draw images mapped on normals, enhancing Solid Draw Mode

      :type: boolean, default False

   .. attribute:: use_occlude_geometry

      Limit selection to visible (clipped with depth buffer)

      :type: boolean, default False

   .. attribute:: use_pivot_point_align

      Manipulate center points (object, pose and weight paint mode only)

      :type: boolean, default False

   .. attribute:: use_render_border

      Use a region within the frame size for rendered viewport (when not viewing through the camera)

      :type: boolean, default False

   .. attribute:: viewport_shade

      Method to display/shade objects in the 3D View

      * ``BOUNDBOX`` Bounding Box, Display the object's local bounding boxes only.
      * ``WIREFRAME`` Wireframe, Display the object as wire edges.
      * ``SOLID`` Solid, Display the object solid, lit with default OpenGL lights.
      * ``TEXTURED`` Texture, Display the object solid, with a texture.
      * ``MATERIAL`` Material, Display objects solid, with GLSL material.
      * ``RENDERED`` Rendered, Display render preview.

      :type: enum in ['BOUNDBOX', 'WIREFRAME', 'SOLID', 'TEXTURED', 'MATERIAL', 'RENDERED'], default 'BOUNDBOX'

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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

   * :class:`ObjectBase.layers_from_view`
   * :class:`SpaceView3D.local_view`

