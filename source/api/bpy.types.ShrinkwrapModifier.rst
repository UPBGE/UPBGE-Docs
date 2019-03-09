ShrinkwrapModifier(Modifier)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ShrinkwrapModifier(Modifier)

   Shrink wrapping modifier to shrink wrap and object to a target

   .. attribute:: auxiliary_target

      Additional mesh target to shrink to

      :type: :class:`Object`

   .. attribute:: cull_face

      Stop vertices from projecting to a face on the target when facing towards/away

      * ``OFF`` Off, No culling.
      * ``FRONT`` Front, No projection when in front of the face.
      * ``BACK`` Back, No projection when behind the face.

      :type: enum in ['OFF', 'FRONT', 'BACK'], default 'OFF'

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: offset

      Distance to keep from the target

      :type: float in [-inf, inf], default 0.0

   .. attribute:: project_limit

      Limit the distance used for projection (zero disables)

      :type: float in [0, inf], default 0.0

   .. attribute:: subsurf_levels

      Number of subdivisions that must be performed before extracting vertices' positions and normals

      :type: int in [0, 6], default 0

   .. attribute:: target

      Mesh target to shrink to

      :type: :class:`Object`

   .. attribute:: use_keep_above_surface

      :type: boolean, default False

   .. attribute:: use_negative_direction

      Allow vertices to move in the negative direction of axis

      :type: boolean, default False

   .. attribute:: use_positive_direction

      Allow vertices to move in the positive direction of axis

      :type: boolean, default False

   .. attribute:: use_project_x

      :type: boolean, default False

   .. attribute:: use_project_y

      :type: boolean, default False

   .. attribute:: use_project_z

      :type: boolean, default False

   .. attribute:: vertex_group

      Vertex group name

      :type: string, default "", (never None)

   .. attribute:: wrap_method

      * ``NEAREST_SURFACEPOINT`` Nearest Surface Point, Shrink the mesh to the nearest target surface.
      * ``PROJECT`` Project, Shrink the mesh to the nearest target surface along a given axis.
      * ``NEAREST_VERTEX`` Nearest Vertex, Shrink the mesh to the nearest target vertex.

      :type: enum in ['NEAREST_SURFACEPOINT', 'PROJECT', 'NEAREST_VERTEX'], default 'NEAREST_SURFACEPOINT'

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

