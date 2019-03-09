Camera(ID)
==========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Camera(ID)

   Camera data-block for storing camera settings

   .. attribute:: angle

      Camera lens field of view

      :type: float in [0.00640536, 3.01675], default 0.0

   .. attribute:: angle_x

      Camera lens horizontal field of view

      :type: float in [0.00640536, 3.01675], default 0.0

   .. attribute:: angle_y

      Camera lens vertical field of view

      :type: float in [0.00640536, 3.01675], default 0.0

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: clip_end

      Camera far clipping distance

      :type: float in [1e-06, inf], default 0.0

   .. attribute:: clip_start

      Camera near clipping distance

      :type: float in [1e-06, inf], default 0.0

   .. data:: cycles

      Cycles camera settings

      :type: :class:`CyclesCameraSettings`, (readonly)

   .. attribute:: dof_distance

      Distance to the focus point for depth of field

      :type: float in [0, inf], default 0.0

   .. attribute:: dof_object

      Use this object to define the depth of field focal point

      :type: :class:`Object`

   .. attribute:: draw_size

      Apparent size of the Camera object in the 3D View

      :type: float in [0.01, 1000], default 0.0

   .. data:: gpu_dof

      :type: :class:`GPUDOFSettings`, (readonly)

   .. attribute:: lens

      Perspective Camera lens value in millimeters

      :type: float in [1, inf], default 0.0

   .. attribute:: lens_unit

      Unit to edit lens in for the user interface

      * ``MILLIMETERS`` Millimeters, Specify the lens in millimeters.
      * ``FOV`` Field of View, Specify the lens as the field of view's angle.

      :type: enum in ['MILLIMETERS', 'FOV'], default 'MILLIMETERS'

   .. attribute:: lod_factor

      The factor applied to distance computed in Lod

      :type: float in [0, inf], default 1.0

   .. attribute:: ortho_scale

      Orthographic Camera scale (similar to zoom)

      :type: float in [0, inf], default 0.0

   .. attribute:: override_culling

      Use only this camera for scene culling in Game Engine

      :type: boolean, default False

   .. attribute:: passepartout_alpha

      Opacity (alpha) of the darkened overlay in Camera view

      :type: float in [0, 1], default 0.0

   .. attribute:: sensor_fit

      Method to fit image and field of view angle inside the sensor

      * ``AUTO`` Auto, Fit to the sensor width or height depending on image resolution.
      * ``HORIZONTAL`` Horizontal, Fit to the sensor width.
      * ``VERTICAL`` Vertical, Fit to the sensor height.

      :type: enum in ['AUTO', 'HORIZONTAL', 'VERTICAL'], default 'AUTO'

   .. attribute:: sensor_height

      Vertical size of the image sensor area in millimeters

      :type: float in [1, inf], default 0.0

   .. attribute:: sensor_width

      Horizontal size of the image sensor area in millimeters

      :type: float in [1, inf], default 0.0

   .. attribute:: shift_x

      Camera horizontal shift

      :type: float in [-10, 10], default 0.0

   .. attribute:: shift_y

      Camera vertical shift

      :type: float in [-10, 10], default 0.0

   .. attribute:: show_frustum

      Show a visualization of frustum in Game Engine

      :type: boolean, default False

   .. attribute:: show_guide

      Draw overlay

      :type: enum set in {'CENTER', 'CENTER_DIAGONAL', 'THIRDS', 'GOLDEN', 'GOLDEN_TRIANGLE_A', 'GOLDEN_TRIANGLE_B', 'HARMONY_TRIANGLE_A', 'HARMONY_TRIANGLE_B'}, default {'CENTER'}

   .. attribute:: show_limits

      Draw the clipping range and focus point on the camera

      :type: boolean, default False

   .. attribute:: show_mist

      Draw a line from the Camera to indicate the mist area

      :type: boolean, default False

   .. attribute:: show_name

      Show the active Camera's name in Camera view

      :type: boolean, default False

   .. attribute:: show_passepartout

      Show a darkened overlay outside the image area in Camera view

      :type: boolean, default False

   .. attribute:: show_safe_areas

      Show TV title safe and action safe areas in Camera view

      :type: boolean, default False

   .. attribute:: show_safe_center

      Show safe areas to fit content in a different aspect ratio

      :type: boolean, default False

   .. attribute:: show_sensor

      Show sensor size (film gate) in Camera view

      :type: boolean, default False

   .. data:: stereo

      :type: :class:`CameraStereoData`, (readonly, never None)

   .. attribute:: type

      Camera types

      :type: enum in ['PERSP', 'ORTHO', 'PANO'], default 'PERSP'

   .. attribute:: use_object_activity_culling

      Enable object activity culling with this camera

      :type: boolean, default False

   .. attribute:: use_viewport

      Show a visualization of frustum in Game Engine

      :type: boolean, default False

   .. data:: viewport

      :type: :class:`GameCameraViewportData`, (readonly, never None)

   .. method:: view_frame(scene=None)

      Return 4 points for the cameras frame (before object transformation)

      :arg scene:

         Scene to use for aspect calculation, when omitted 1:1 aspect is used

      :type scene: :class:`Scene`, (optional)
      :return (result_1, result_2, result_3, result_4):
         `result_1`, Result, float array of 3 items in [-inf, inf]

         `result_2`, Result, float array of 3 items in [-inf, inf]

         `result_3`, Result, float array of 3 items in [-inf, inf]

         `result_4`, Result, float array of 3 items in [-inf, inf]


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

   * :mod:`bpy.context.camera`
   * :class:`BlendData.cameras`
   * :class:`BlendDataCameras.new`
   * :class:`BlendDataCameras.remove`

