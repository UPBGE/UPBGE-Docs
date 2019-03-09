NlaStrips(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NlaStrips(bpy_struct)

   Collection of Nla Strips

   .. method:: new(name, start, action)

      Add a new Action-Clip strip to the track

      :arg name:

         Name for the NLA Strips

      :type name: string, (never None)
      :arg start:

         Start Frame, Start frame for this strip

      :type start: int in [-inf, inf]
      :arg action:

         Action to assign to this strip

      :type action: :class:`Action`, (never None)
      :return:

         New NLA Strip

      :rtype: :class:`NlaStrip`

   .. method:: remove(strip)

      Remove a NLA Strip

      :arg strip:

         NLA Strip to remove

      :type strip: :class:`NlaStrip`, (never None)

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

   * :class:`NlaTrack.strips`

