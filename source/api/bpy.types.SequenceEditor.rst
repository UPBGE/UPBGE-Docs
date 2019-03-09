SequenceEditor(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequenceEditor(bpy_struct)

   Sequence editing data for a Scene data-block

   .. attribute:: active_strip

      Sequencer's active strip

      :type: :class:`Sequence`

   .. data:: meta_stack

      Meta strip stack, last is currently edited meta strip

      :type: :class:`bpy_prop_collection` of :class:`Sequence`, (readonly)

   .. attribute:: overlay_frame

      :type: int in [-inf, inf], default 0

   .. attribute:: proxy_dir

      :type: string, default "", (never None)

   .. attribute:: proxy_storage

      How to store proxies for this project

      * ``PER_STRIP`` Per Strip, Store proxies using per strip settings.
      * ``PROJECT`` Project, Store proxies using project directory.

      :type: enum in ['PER_STRIP', 'PROJECT'], default 'PER_STRIP'

   .. data:: sequences

      Top-level strips only

      :type: :class:`Sequences` :class:`bpy_prop_collection` of :class:`Sequence`, (readonly)

   .. data:: sequences_all

      All strips, recursively including those inside metastrips

      :type: :class:`bpy_prop_collection` of :class:`Sequence`, (readonly)

   .. attribute:: show_overlay

      Partial overlay on top of the sequencer

      :type: boolean, default False

   .. attribute:: use_overlay_lock

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

   * :class:`Scene.sequence_editor`
   * :class:`Scene.sequence_editor_create`

