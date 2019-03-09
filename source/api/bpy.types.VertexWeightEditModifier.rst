VertexWeightEditModifier(Modifier)
==================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: VertexWeightEditModifier(Modifier)

   Edit the weights of vertices in a group

   .. attribute:: add_threshold

      Lower bound for a vertex's weight to be added to the vgroup

      :type: float in [0, 1], default 0.0

   .. attribute:: default_weight

      Default weight a vertex will have if it is not in the vgroup

      :type: float in [0, 1], default 0.0

   .. attribute:: falloff_type

      How weights are mapped to their new values

      * ``LINEAR`` Linear, Null action.
      * ``CURVE`` Custom Curve.
      * ``SHARP`` Sharp.
      * ``SMOOTH`` Smooth.
      * ``ROOT`` Root.
      * ``ICON_SPHERECURVE`` Sphere.
      * ``RANDOM`` Random.
      * ``STEP`` Median Step, Map all values below 0.5 to 0.0, and all others to 1.0.

      :type: enum in ['LINEAR', 'CURVE', 'SHARP', 'SMOOTH', 'ROOT', 'ICON_SPHERECURVE', 'RANDOM', 'STEP'], default 'LINEAR'

   .. data:: map_curve

      Custom mapping curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: mask_constant

      Global influence of current modifications on vgroup

      :type: float in [-inf, inf], default 0.0

   .. attribute:: mask_tex_map_object

      Which object to take texture coordinates from

      :type: :class:`Object`

   .. attribute:: mask_tex_mapping

      Which texture coordinates to use for mapping

      * ``LOCAL`` Local, Use local generated coordinates.
      * ``GLOBAL`` Global, Use global coordinates.
      * ``OBJECT`` Object, Use local generated coordinates of another object.
      * ``UV`` UV, Use coordinates from an UV layer.

      :type: enum in ['LOCAL', 'GLOBAL', 'OBJECT', 'UV'], default 'LOCAL'

   .. attribute:: mask_tex_use_channel

      Which texture channel to use for masking

      :type: enum in ['INT', 'RED', 'GREEN', 'BLUE', 'HUE', 'SAT', 'VAL', 'ALPHA'], default 'INT'

   .. attribute:: mask_tex_uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: mask_texture

      Masking texture

      :type: :class:`Texture`

   .. attribute:: mask_vertex_group

      Masking vertex group name

      :type: string, default "", (never None)

   .. attribute:: remove_threshold

      Upper bound for a vertex's weight to be removed from the vgroup

      :type: float in [0, 1], default 0.0

   .. attribute:: use_add

      Add vertices with weight over threshold to vgroup

      :type: boolean, default False

   .. attribute:: use_remove

      Remove vertices with weight below threshold from vgroup

      :type: boolean, default False

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

