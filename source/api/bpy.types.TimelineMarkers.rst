TimelineMarkers(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: TimelineMarkers(bpy_struct)

   Collection of timeline markers

   .. method:: new(name, frame=1)

      Add a keyframe to the curve

      :arg name:

         New name for the marker (not unique)

      :type name: string, (never None)
      :arg frame:

         The frame for the new marker

      :type frame: int in [-1048574, 1048574], (optional)
      :return:

         Newly created timeline marker

      :rtype: :class:`TimelineMarker`

   .. method:: remove(marker)

      Remove a timeline marker

      :arg marker:

         Timeline marker to remove

      :type marker: :class:`TimelineMarker`, (never None)

   .. method:: clear()

      Remove all timeline markers


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

   * :class:`Scene.timeline_markers`

