KeyingSets(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyingSets(bpy_struct)

   Scene keying sets

   .. attribute:: active

      Active Keying Set used to insert/delete keyframes

      :type: :class:`KeyingSet`

   .. attribute:: active_index

      Current Keying Set index (negative for 'builtin' and positive for 'absolute')

      :type: int in [-inf, inf], default 0

   .. method:: new(idname="KeyingSet", name="KeyingSet")

      Add a new Keying Set to Scene

      :arg idname:

         IDName, Internal identifier of Keying Set

      :type idname: string, (optional, never None)
      :arg name:

         Name, User visible name of Keying Set

      :type name: string, (optional, never None)
      :return:

         Newly created Keying Set

      :rtype: :class:`KeyingSet`

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

   * :class:`Scene.keying_sets`

