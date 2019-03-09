SimpleDeformModifier(Modifier)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SimpleDeformModifier(Modifier)

   Simple deformation modifier to apply effects such as twisting and bending

   .. attribute:: angle

      Angle of deformation

      :type: float in [-inf, inf], default 0.785398

   .. attribute:: deform_method

      * ``TWIST`` Twist, Rotate around the Z axis of the modifier space.
      * ``BEND`` Bend, Bend the mesh over the Z axis of the modifier space.
      * ``TAPER`` Taper, Linearly scale along Z axis of the modifier space.
      * ``STRETCH`` Stretch, Stretch the object along the Z axis of the modifier space.

      :type: enum in ['TWIST', 'BEND', 'TAPER', 'STRETCH'], default 'TWIST'

   .. attribute:: factor

      Amount to deform object

      :type: float in [-inf, inf], default 0.0

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: limits

      Lower/Upper limits for deform

      :type: float array of 2 items in [0, 1], default (0.0, 0.0)

   .. attribute:: lock_x

      Do not allow deformation along the X axis

      :type: boolean, default False

   .. attribute:: lock_y

      Do not allow deformation along the Y axis

      :type: boolean, default False

   .. attribute:: origin

      Offset the origin and orientation of the deformation

      :type: :class:`Object`

   .. attribute:: vertex_group

      Vertex group name

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

