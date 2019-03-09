bpy_extras submodule (bpy_extras.view3d_utils)
==============================================

.. module:: bpy_extras.view3d_utils

.. function:: region_2d_to_vector_3d(region, rv3d, coord)

   Return a direction vector from the viewport at the specific 2d region
   coordinate.
   
   :arg region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :arg rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :arg coord: 2d coordinates relative to the region:
      (event.mouse_region_x, event.mouse_region_y) for example.
   :type coord: 2d vector
   :return: normalized 3d vector.
   :rtype: :class:`mathutils.Vector`

.. function:: region_2d_to_origin_3d(region, rv3d, coord, clamp=None)

   Return the 3d view origin from the region relative 2d coords.
   
   .. note::
   
      Orthographic views have a less obvious origin,
      the far clip is used to define the viewport near/far extents.
      Since far clip can be a very large value,
      the result may give with numeric precision issues.
   
      To avoid this problem, you can optionally clamp the far clip to a
      smaller value based on the data you're operating on.
   
   :arg region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :arg rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :arg coord: 2d coordinates relative to the region;
      (event.mouse_region_x, event.mouse_region_y) for example.
   :type coord: 2d vector
   :arg clamp: Clamp the maximum far-clip value used.
      (negative value will move the offset away from the view_location)
   :type clamp: float or None
   :return: The origin of the viewpoint in 3d space.
   :rtype: :class:`mathutils.Vector`

.. function:: region_2d_to_location_3d(region, rv3d, coord, depth_location)

   Return a 3d location from the region relative 2d coords, aligned with
   *depth_location*.
   
   :arg region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :arg rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :arg coord: 2d coordinates relative to the region;
      (event.mouse_region_x, event.mouse_region_y) for example.
   :type coord: 2d vector
   :arg depth_location: the returned vectors depth is aligned with this since
      there is no defined depth with a 2d region input.
   :type depth_location: 3d vector
   :return: normalized 3d vector.
   :rtype: :class:`mathutils.Vector`

.. function:: location_3d_to_region_2d(region, rv3d, coord, default=None)

   Return the *region* relative 2d location of a 3d position.
   
   :arg region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :arg rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :arg coord: 3d worldspace location.
   :type coord: 3d vector
   :arg default: Return this value if ``coord``
      is behind the origin of a perspective view.
   :return: 2d location
   :rtype: :class:`mathutils.Vector` or ``default`` argument.

