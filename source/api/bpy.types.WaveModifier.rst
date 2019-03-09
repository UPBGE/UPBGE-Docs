WaveModifier(Modifier)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: WaveModifier(Modifier)

   Wave effect modifier

   .. attribute:: damping_time

      Number of frames in which the wave damps out after it dies

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: falloff_radius

      Distance after which it fades out

      :type: float in [0, inf], default 0.0

   .. attribute:: height

      Height of the wave

      :type: float in [-inf, inf], default 0.0

   .. attribute:: lifetime

      Lifetime of the wave in frames, zero means infinite

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: narrowness

      Distance between the top and the base of a wave, the higher the value, the more narrow the wave

      :type: float in [0, inf], default 0.0

   .. attribute:: speed

      Speed of the wave, towards the starting point when negative

      :type: float in [-inf, inf], default 0.0

   .. attribute:: start_position_object

      Object which defines the wave center

      :type: :class:`Object`

   .. attribute:: start_position_x

      X coordinate of the start position

      :type: float in [-inf, inf], default 0.0

   .. attribute:: start_position_y

      Y coordinate of the start position

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture

      :type: :class:`Texture`

   .. attribute:: texture_coords

      * ``LOCAL`` Local, Use the local coordinate system for the texture coordinates.
      * ``GLOBAL`` Global, Use the global coordinate system for the texture coordinates.
      * ``OBJECT`` Object, Use the linked object's local coordinate system for the texture coordinates.
      * ``UV`` UV, Use UV coordinates for the texture coordinates.

      :type: enum in ['LOCAL', 'GLOBAL', 'OBJECT', 'UV'], default 'LOCAL'

   .. attribute:: texture_coords_object

      Object to set the texture coordinates

      :type: :class:`Object`

   .. attribute:: time_offset

      Either the starting frame (for positive speed) or ending frame (for negative speed.)

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: use_cyclic

      Cyclic wave effect

      :type: boolean, default False

   .. attribute:: use_normal

      Displace along normals

      :type: boolean, default False

   .. attribute:: use_normal_x

      Enable displacement along the X normal

      :type: boolean, default False

   .. attribute:: use_normal_y

      Enable displacement along the Y normal

      :type: boolean, default False

   .. attribute:: use_normal_z

      Enable displacement along the Z normal

      :type: boolean, default False

   .. attribute:: use_x

      X axis motion

      :type: boolean, default False

   .. attribute:: use_y

      Y axis motion

      :type: boolean, default False

   .. attribute:: uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: vertex_group

      Vertex group name for modulating the wave

      :type: string, default "", (never None)

   .. attribute:: width

      Distance between the waves

      :type: float in [0, inf], default 0.0

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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

