ScrewModifier(Modifier)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ScrewModifier(Modifier)

   Revolve edges

   .. attribute:: angle

      Angle of revolution

      :type: float in [-inf, inf], default 0.0

   .. attribute:: axis

      Screw axis

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: iterations

      Number of times to apply the screw operation

      :type: int in [1, 10000], default 0

   .. attribute:: merge_threshold

      Limit below which to merge vertices

      :type: float in [0, inf], default 0.0

   .. attribute:: object

      Object to define the screw axis

      :type: :class:`Object`

   .. attribute:: render_steps

      Number of steps in the revolution

      :type: int in [2, 10000], default 0

   .. attribute:: screw_offset

      Offset the revolution along its axis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: steps

      Number of steps in the revolution

      :type: int in [2, 10000], default 0

   .. attribute:: use_merge_vertices

      Merge adjacent vertices (screw offset must be zero)

      :type: boolean, default False

   .. attribute:: use_normal_calculate

      Calculate the order of edges (needed for meshes, but not curves)

      :type: boolean, default False

   .. attribute:: use_normal_flip

      Flip normals of lathed faces

      :type: boolean, default False

   .. attribute:: use_object_screw_offset

      Use the distance between the objects to make a screw

      :type: boolean, default False

   .. attribute:: use_smooth_shade

      Output faces with smooth shading rather than flat shaded

      :type: boolean, default False

   .. attribute:: use_stretch_u

      Stretch the U coordinates between 0-1 when UV's are present

      :type: boolean, default False

   .. attribute:: use_stretch_v

      Stretch the V coordinates between 0-1 when UV's are present

      :type: boolean, default False

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

