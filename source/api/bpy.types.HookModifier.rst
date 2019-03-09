HookModifier(Modifier)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: HookModifier(Modifier)

   Hook modifier to modify the location of vertices

   .. attribute:: center

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: falloff_curve

      Custom Lamp Falloff Curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: falloff_radius

      If not zero, the distance from the hook where influence ends

      :type: float in [0, inf], default 0.0

   .. attribute:: falloff_type

      :type: enum in ['NONE', 'CURVE', 'SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT'], default 'NONE'

   .. attribute:: matrix_inverse

      Reverse the transformation between this object and its target

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: object

      Parent Object for hook, also recalculates and clears offset

      :type: :class:`Object`

   .. attribute:: strength

      Relative force of the hook

      :type: float in [0, 1], default 0.0

   .. attribute:: subtarget

      Name of Parent Bone for hook (if applicable), also recalculates and clears offset

      :type: string, default "", (never None)

   .. attribute:: use_falloff_uniform

      Compensate for non-uniform object scale

      :type: boolean, default False

   .. attribute:: vertex_group

      Name of Vertex Group which determines influence of modifier per point

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

