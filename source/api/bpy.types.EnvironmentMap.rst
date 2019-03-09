EnvironmentMap(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: EnvironmentMap(bpy_struct)

   Environment map created by the renderer and cached for subsequent renders

   .. attribute:: auto_update

      True if the cube map is updated every frame

      :type: boolean, default False

   .. attribute:: clip_end

      Objects further than this are not visible to map

      :type: float in [0.01, inf], default 0.0

   .. attribute:: clip_start

      Objects nearer than this are not visible to map

      :type: float in [0.001, inf], default 0.0

   .. attribute:: depth

      Number of times a map will be rendered recursively (mirror effects)

      :type: int in [0, 5], default 0

   .. attribute:: filtering

      Texture filtering method

      * ``NONE`` None, None texture filtering.
      * ``LINEAR`` Linear Filtering, Linear texture filtering.
      * ``MIPMAP`` Mipmap Filtering, Mipmap texture filtering.

      :type: enum in ['NONE', 'LINEAR', 'MIPMAP'], default 'NONE'

   .. data:: is_valid

      True if this map is ready for use, False if it needs rendering

      :type: boolean, default False, (readonly)

   .. attribute:: layers_ignore

      Hide objects on these layers when generating the Environment Map

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: lod_factor

      The factor applied to distance computed in Lod

      :type: float in [0, inf], default 1.0

   .. attribute:: mapping

      * ``CUBE`` Cube, Use environment map with six cube sides.
      * ``PLANE`` Plane, Only one side is rendered, with Z axis pointing in direction of image.

      :type: enum in ['CUBE', 'PLANE'], default 'CUBE'

   .. attribute:: mode

      Texture rendering method

      * ``REFLECTION`` Reflection, Reflection rendering.
      * ``REFRACTION`` Refraction, Refraction rendering.

      :type: enum in ['REFLECTION', 'REFRACTION'], default 'REFLECTION'

   .. attribute:: resolution

      Pixel resolution of the rendered environment map

      :type: int in [50, 4096], default 0

   .. attribute:: source

      * ``STATIC`` Static, Calculate environment map only once.
      * ``ANIMATED`` Animated, Calculate environment map at each rendering.
      * ``IMAGE_FILE`` Image File, Load a saved environment map image from disk.
      * ``REALTIME`` Realtime, Image generated for realtime reflections in the game engine.

      :type: enum in ['STATIC', 'ANIMATED', 'IMAGE_FILE', 'REALTIME'], default 'STATIC'

   .. attribute:: viewpoint_object

      Object to use as the environment map's viewpoint location

      :type: :class:`Object`

   .. attribute:: zoom

      :type: float in [0.1, 5], default 0.0

   .. method:: clear()

      Discard the environment map and free it from memory


   .. method:: save(filepath, scene=None, layout=(0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 1.0))

      Save the environment map to disc using the scene render settings

      :arg filepath:

         File path, Location of the output file

      :type filepath: string, (never None)
      :arg scene:

         Overrides the scene from which image parameters are taken

      :type scene: :class:`Scene`, (optional)
      :arg layout:

         File layout, Flat array describing the X,Y position of each cube face in the output image, where 1 is the size of a face - order is [+Z -Z +Y -X -Y +X] (use -1 to skip a face)

      :type layout: float array of 12 items in [0, 1000], (optional)

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

   * :class:`EnvironmentMapTexture.environment_map`

