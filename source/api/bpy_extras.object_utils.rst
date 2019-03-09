bpy_extras submodule (bpy_extras.object_utils)
==============================================

.. module:: bpy_extras.object_utils

.. function:: add_object_align_init(context, operator)

   Return a matrix using the operator settings and view context.
   
   :arg context: The context to use.
   :type context: :class:`bpy.types.Context`
   :arg operator: The operator, checked for location and rotation properties.
   :type operator: :class:`bpy.types.Operator`
   :return: the matrix from the context and settings.
   :rtype: :class:`mathutils.Matrix`

.. function:: object_data_add(context, obdata, operator=None, use_active_layer=True, name=None)

   Add an object using the view context and preference to to initialize the
   location, rotation and layer.
   
   :arg context: The context to use.
   :type context: :class:`bpy.types.Context`
   :arg obdata: the data used for the new object.
   :type obdata: valid object data type or None.
   :arg operator: The operator, checked for location and rotation properties.
   :type operator: :class:`bpy.types.Operator`
   :arg name: Optional name
   :type name: string
   :return: the newly created object in the scene.
   :rtype: :class:`bpy.types.ObjectBase`

.. function:: object_add_grid_scale(context)

   Return scale which should be applied on object
   data to align it to grid scale

.. function:: object_add_grid_scale_apply_operator(operator, context)

   Scale an operators distance values by the grid size.

.. function:: object_image_guess(obj, bm=None)

   Return a single image used by the object,
   first checking the texture-faces, then the material.

.. function:: world_to_camera_view(scene, obj, coord)

   Returns the camera space coords for a 3d point.
   (also known as: normalized device coordinates - NDC).
   
   Where (0, 0) is the bottom left and (1, 1)
   is the top right of the camera frame.
   values outside 0-1 are also supported.
   A negative 'z' value means the point is behind the camera.
   
   Takes shift-x/y, lens angle and sensor size into account
   as well as perspective/ortho projections.
   
   :arg scene: Scene to use for frame size.
   :type scene: :class:`bpy.types.Scene`
   :arg obj: Camera object.
   :type obj: :class:`bpy.types.Object`
   :arg coord: World space location.
   :type coord: :class:`mathutils.Vector`
   :return: a vector where X and Y map to the view plane and
      Z is the depth on the view axis.
   :rtype: :class:`mathutils.Vector`

.. class:: AddObjectHelper


   .. method:: view_align_update_callback(context)



