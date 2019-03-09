GPencilFrames(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilFrames(bpy_struct)

   Collection of grease pencil frames

   .. method:: new(frame_number)

      Add a new grease pencil frame

      :arg frame_number:

         Frame Number, The frame on which this sketch appears

      :type frame_number: int in [-1048574, 1048574]
      :return:

         The newly created frame

      :rtype: :class:`GPencilFrame`

   .. method:: remove(frame)

      Remove a grease pencil frame

      :arg frame:

         Frame, The frame to remove

      :type frame: :class:`GPencilFrame`, (never None)

   .. method:: copy(source)

      Copy a grease pencil frame

      :arg source:

         Source, The source frame

      :type source: :class:`GPencilFrame`, (never None)
      :return:

         The newly copied frame

      :rtype: :class:`GPencilFrame`

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

   * :class:`GPencilLayer.frames`

