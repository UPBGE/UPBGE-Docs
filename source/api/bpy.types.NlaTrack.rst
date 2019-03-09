NlaTrack(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NlaTrack(bpy_struct)

   A animation layer containing Actions referenced as NLA strips

   .. data:: active

      NLA Track is active

      :type: boolean, default False, (readonly)

   .. attribute:: is_solo

      NLA Track is evaluated itself (i.e. active Action and all other NLA Tracks in the same AnimData block are disabled)

      :type: boolean, default False

   .. attribute:: lock

      NLA Track is locked

      :type: boolean, default False

   .. attribute:: mute

      NLA Track is not evaluated

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: select

      NLA Track is selected

      :type: boolean, default False

   .. data:: strips

      NLA Strips on this NLA-track

      :type: :class:`NlaStrips` :class:`bpy_prop_collection` of :class:`NlaStrip`, (readonly)

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

   * :class:`AnimData.nla_tracks`
   * :class:`NlaTracks.active`
   * :class:`NlaTracks.new`
   * :class:`NlaTracks.new`
   * :class:`NlaTracks.remove`

