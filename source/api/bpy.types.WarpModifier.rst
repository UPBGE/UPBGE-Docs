WarpModifier(Modifier)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: WarpModifier(Modifier)

   Warp modifier

   .. data:: falloff_curve

      Custom Lamp Falloff Curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: falloff_radius

      Radius to apply

      :type: float in [-inf, inf], default 0.0

   .. attribute:: falloff_type

      :type: enum in ['NONE', 'CURVE', 'SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT'], default 'NONE'

   .. attribute:: object_from

      Object to transform from

      :type: :class:`Object`

   .. attribute:: object_to

      Object to transform to

      :type: :class:`Object`

   .. attribute:: strength

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

   .. attribute:: use_volume_preserve

      Preserve volume when rotations are used

      :type: boolean, default False

   .. attribute:: uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: vertex_group

      Vertex group name for modulating the deform

      :type: string, default "", (never None)

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

