CompositorNodeTree(NodeTree)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`NodeTree`

.. class:: CompositorNodeTree(NodeTree)

   Node tree consisting of linked nodes used for compositing

   .. attribute:: chunk_size

      Max size of a tile (smaller values gives better distribution of multiple threads, but more overhead)

      * ``32`` 32x32, Chunksize of 32x32.
      * ``64`` 64x64, Chunksize of 64x64.
      * ``128`` 128x128, Chunksize of 128x128.
      * ``256`` 256x256, Chunksize of 256x256.
      * ``512`` 512x512, Chunksize of 512x512.
      * ``1024`` 1024x1024, Chunksize of 1024x1024.

      :type: enum in ['32', '64', '128', '256', '512', '1024'], default '32'

   .. attribute:: edit_quality

      Quality when editing

      * ``HIGH`` High, High quality.
      * ``MEDIUM`` Medium, Medium quality.
      * ``LOW`` Low, Low quality.

      :type: enum in ['HIGH', 'MEDIUM', 'LOW'], default 'HIGH'

   .. attribute:: render_quality

      Quality when rendering

      * ``HIGH`` High, High quality.
      * ``MEDIUM`` Medium, Medium quality.
      * ``LOW`` Low, Low quality.

      :type: enum in ['HIGH', 'MEDIUM', 'LOW'], default 'HIGH'

   .. attribute:: use_groupnode_buffer

      Enable buffering of group nodes

      :type: boolean, default False

   .. attribute:: use_opencl

      Enable GPU calculations

      :type: boolean, default False

   .. attribute:: use_two_pass

      Use two pass execution during editing: first calculate fast nodes, second pass calculate all nodes

      :type: boolean, default False

   .. attribute:: use_viewer_border

      Use boundaries for viewer nodes and composite backdrop

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`
   * :class:`NodeTree.view_center`
   * :class:`NodeTree.animation_data`
   * :class:`NodeTree.nodes`
   * :class:`NodeTree.links`
   * :class:`NodeTree.grease_pencil`
   * :class:`NodeTree.type`
   * :class:`NodeTree.inputs`
   * :class:`NodeTree.active_input`
   * :class:`NodeTree.outputs`
   * :class:`NodeTree.active_output`
   * :class:`NodeTree.bl_idname`
   * :class:`NodeTree.bl_label`
   * :class:`NodeTree.bl_description`
   * :class:`NodeTree.bl_icon`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`NodeTree.interface_update`
   * :class:`NodeTree.poll`
   * :class:`NodeTree.update`
   * :class:`NodeTree.get_from_context`

