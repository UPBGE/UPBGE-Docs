TexMapping(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: TexMapping(bpy_struct)

   Texture coordinate mapping settings

   .. attribute:: mapping

      * ``FLAT`` Flat, Map X and Y coordinates directly.
      * ``CUBE`` Cube, Map using the normal vector.
      * ``TUBE`` Tube, Map with Z as central axis.
      * ``SPHERE`` Sphere, Map with Z as central axis.

      :type: enum in ['FLAT', 'CUBE', 'TUBE', 'SPHERE'], default 'FLAT'

   .. attribute:: mapping_x

      :type: enum in ['NONE', 'X', 'Y', 'Z'], default 'NONE'

   .. attribute:: mapping_y

      :type: enum in ['NONE', 'X', 'Y', 'Z'], default 'NONE'

   .. attribute:: mapping_z

      :type: enum in ['NONE', 'X', 'Y', 'Z'], default 'NONE'

   .. attribute:: max

      Maximum value for clipping

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: min

      Minimum value for clipping

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: scale

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: translation

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: use_max

      Whether to use maximum clipping value

      :type: boolean, default False

   .. attribute:: use_min

      Whether to use minimum clipping value

      :type: boolean, default False

   .. attribute:: vector_type

      Type of vector that the mapping transforms

      * ``TEXTURE`` Texture, Transform a texture by inverse mapping the texture coordinate.
      * ``POINT`` Point, Transform a point.
      * ``VECTOR`` Vector, Transform a direction vector.
      * ``NORMAL`` Normal, Transform a normal vector with unit length.

      :type: enum in ['TEXTURE', 'POINT', 'VECTOR', 'NORMAL'], default 'POINT'

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

   * :class:`ShaderNodeTexBrick.texture_mapping`
   * :class:`ShaderNodeTexChecker.texture_mapping`
   * :class:`ShaderNodeTexEnvironment.texture_mapping`
   * :class:`ShaderNodeTexGradient.texture_mapping`
   * :class:`ShaderNodeTexImage.texture_mapping`
   * :class:`ShaderNodeTexMagic.texture_mapping`
   * :class:`ShaderNodeTexMusgrave.texture_mapping`
   * :class:`ShaderNodeTexNoise.texture_mapping`
   * :class:`ShaderNodeTexSky.texture_mapping`
   * :class:`ShaderNodeTexVoronoi.texture_mapping`
   * :class:`ShaderNodeTexWave.texture_mapping`

