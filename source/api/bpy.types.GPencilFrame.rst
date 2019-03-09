GPencilFrame(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilFrame(bpy_struct)

   Collection of related sketches on a particular frame

   .. attribute:: frame_number

      The frame on which this sketch appears

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: is_edited

      Frame is being edited (painted on)

      :type: boolean, default False

   .. attribute:: select

      Frame is selected for editing in the Dope Sheet

      :type: boolean, default False

   .. data:: strokes

      Freehand curves defining the sketch on this frame

      :type: :class:`GPencilStrokes` :class:`bpy_prop_collection` of :class:`GPencilStroke`, (readonly)

   .. method:: clear()

      Remove all the grease pencil frame data


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

   * :class:`GPencilFrames.copy`
   * :class:`GPencilFrames.copy`
   * :class:`GPencilFrames.new`
   * :class:`GPencilFrames.remove`
   * :class:`GPencilLayer.active_frame`
   * :class:`GPencilLayer.frames`

