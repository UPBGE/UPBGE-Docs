VertexWeightMixModifier(Modifier)
=================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: VertexWeightMixModifier(Modifier)

   Mix the weights of two vertex groups

   .. attribute:: default_weight_a

      Default weight a vertex will have if it is not in the first A vgroup

      :type: float in [0, 1], default 0.0

   .. attribute:: default_weight_b

      Default weight a vertex will have if it is not in the second B vgroup

      :type: float in [0, 1], default 0.0

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

   .. attribute:: mix_mode

      How weights from vgroup B affect weights of vgroup A

      * ``SET`` Replace, Replace VGroup A's weights by VGroup B's ones.
      * ``ADD`` Add, Add VGroup B's weights to VGroup A's ones.
      * ``SUB`` Subtract, Subtract VGroup B's weights from VGroup A's ones.
      * ``MUL`` Multiply, Multiply VGroup A's weights by VGroup B's ones.
      * ``DIV`` Divide, Divide VGroup A's weights by VGroup B's ones.
      * ``DIF`` Difference, Difference between VGroup A's and VGroup B's weights.
      * ``AVG`` Average, Average value of VGroup A's and VGroup B's weights.

      :type: enum in ['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'DIF', 'AVG'], default 'SET'

   .. attribute:: mix_set

      Which vertices should be affected

      * ``ALL`` All, Affect all vertices (might add some to VGroup A).
      * ``A`` VGroup A, Affect vertices in VGroup A.
      * ``B`` VGroup B, Affect vertices in VGroup B (might add some to VGroup A).
      * ``OR`` VGroup A or B, Affect vertices in at least one of both VGroups (might add some to VGroup A).
      * ``AND`` VGroup A and B, Affect vertices in both groups.

      :type: enum in ['ALL', 'A', 'B', 'OR', 'AND'], default 'ALL'

   .. attribute:: vertex_group_a

      First vertex group name

      :type: string, default "", (never None)

   .. attribute:: vertex_group_b

      Second vertex group name

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

