ExplodeModifier(Modifier)
=========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ExplodeModifier(Modifier)

   Explosion effect modifier based on a particle system

   .. attribute:: particle_uv

      UV map to change with particle age

      :type: string, default "", (never None)

   .. attribute:: protect

      Clean vertex group edges

      :type: float in [0, 1], default 0.0

   .. attribute:: show_alive

      Show mesh when particles are alive

      :type: boolean, default False

   .. attribute:: show_dead

      Show mesh when particles are dead

      :type: boolean, default False

   .. attribute:: show_unborn

      Show mesh when particles are unborn

      :type: boolean, default False

   .. attribute:: use_edge_cut

      Cut face edges for nicer shrapnel

      :type: boolean, default False

   .. attribute:: use_size

      Use particle size for the shrapnel

      :type: boolean, default False

   .. attribute:: vertex_group

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

