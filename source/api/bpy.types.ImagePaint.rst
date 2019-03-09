ImagePaint(Paint)
=================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Paint`

.. class:: ImagePaint(Paint)

   Properties of image and texture painting mode

   .. attribute:: canvas

      Image used as canvas

      :type: :class:`Image`

   .. attribute:: clone_image

      Image used as clone source

      :type: :class:`Image`

   .. attribute:: dither

      Amount of dithering when painting on byte images

      :type: float in [0, 2], default 0.0

   .. attribute:: invert_stencil

      Invert the stencil layer

      :type: boolean, default False

   .. data:: missing_materials

      The mesh is missing materials

      :type: boolean, default False, (readonly)

   .. data:: missing_stencil

      Image Painting does not have a stencil

      :type: boolean, default False, (readonly)

   .. data:: missing_texture

      Image Painting does not have a texture to paint on

      :type: boolean, default False, (readonly)

   .. data:: missing_uvs

      A UV layer is missing on the mesh

      :type: boolean, default False, (readonly)

   .. attribute:: mode

      Mode of operation for projection painting

      * ``MATERIAL`` Material, Detect image slots from the material.
      * ``IMAGE`` Image, Set image for texture painting directly.

      :type: enum in ['MATERIAL', 'IMAGE'], default 'MATERIAL'

   .. attribute:: normal_angle

      Paint most on faces pointing towards the view according to this angle

      :type: int in [0, 90], default 0

   .. attribute:: screen_grab_size

      Size to capture the image for re-projecting

      :type: int array of 2 items in [512, 16384], default (0, 0)

   .. attribute:: seam_bleed

      Extend paint beyond the faces UVs to reduce seams (in pixels, slower)

      :type: int in [-32768, 32767], default 0

   .. attribute:: stencil_color

      Stencil color in the viewport

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: stencil_image

      Image used as stencil

      :type: :class:`Image`

   .. attribute:: use_backface_culling

      Ignore faces pointing away from the view (faster)

      :type: boolean, default False

   .. attribute:: use_clone_layer

      Use another UV map as clone source, otherwise use the 3D cursor as the source

      :type: boolean, default False

   .. attribute:: use_normal_falloff

      Paint most on faces pointing towards the view

      :type: boolean, default False

   .. attribute:: use_occlude

      Only paint onto the faces directly under the brush (slower)

      :type: boolean, default False

   .. attribute:: use_stencil_layer

      Set the mask layer from the UV map buttons

      :type: boolean, default False

   .. method:: detect_data()

      Check if required texpaint data exist

      :rtype: boolean

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
   * :class:`Paint.brush`
   * :class:`Paint.palette`
   * :class:`Paint.show_brush`
   * :class:`Paint.show_brush_on_surface`
   * :class:`Paint.show_low_resolution`
   * :class:`Paint.input_samples`
   * :class:`Paint.use_symmetry_x`
   * :class:`Paint.use_symmetry_y`
   * :class:`Paint.use_symmetry_z`
   * :class:`Paint.use_symmetry_feather`
   * :class:`Paint.cavity_curve`
   * :class:`Paint.use_cavity`
   * :class:`Paint.tile_offset`
   * :class:`Paint.tile_x`
   * :class:`Paint.tile_y`
   * :class:`Paint.tile_z`

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

   * :class:`ToolSettings.image_paint`

