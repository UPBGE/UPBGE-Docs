BlendDataBrushes(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataBrushes(bpy_struct)

   Collection of brushes

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: new(name, mode='TEXTURE_PAINT')

      Add a new brush to the main database

      :arg name:

         New name for the data-block

      :type name: string, (never None)
      :arg mode:

         Paint Mode for the new brush

         * ``OBJECT`` Object Mode.
         * ``EDIT`` Edit Mode.
         * ``POSE`` Pose Mode.
         * ``SCULPT`` Sculpt Mode.
         * ``VERTEX_PAINT`` Vertex Paint.
         * ``WEIGHT_PAINT`` Weight Paint.
         * ``TEXTURE_PAINT`` Texture Paint.
         * ``PARTICLE_EDIT`` Particle Edit.
         * ``GPENCIL_EDIT`` Edit Strokes, Edit Grease Pencil Strokes.

      :type mode: enum in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'GPENCIL_EDIT'], (optional)
      :return:

         New brush data-block

      :rtype: :class:`Brush`

   .. method:: remove(brush, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a brush from the current blendfile

      :arg brush:

         Brush to remove

      :type brush: :class:`Brush`, (never None)
      :arg do_unlink:

         Unlink all usages of this brush before deleting it

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this brush

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this brush

      :type do_ui_user: boolean, (optional)

   .. method:: tag(value)

      tag

      :arg value:

         Value

      :type value: boolean

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

   * :class:`BlendData.brushes`

