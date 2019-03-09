KeyingSetInfo(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyingSetInfo(bpy_struct)

   Callback function defines for builtin Keying Sets

   .. attribute:: bl_description

      A short description of the keying set

      :type: string, default "", (never None)

   .. attribute:: bl_idname

      If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is "BUILTIN_KSI_location", and bl_idname is not set by the script, then bl_idname = "BUILTIN_KSI_location")

      :type: string, default "", (never None)

   .. attribute:: bl_label

      :type: string, default "", (never None)

   .. attribute:: bl_options

      Keying Set options to use when inserting keyframes

      * ``INSERTKEY_NEEDED`` Only Needed, Only insert keyframes where they're needed in the relevant F-Curves.
      * ``INSERTKEY_VISUAL`` Visual Keying, Insert keyframes based on 'visual transforms'.
      * ``INSERTKEY_XYZ_TO_RGB`` XYZ=RGB Colors, Color for newly added transformation F-Curves (Location, Rotation, Scale) and also Color is based on the transform axis.

      :type: enum set in {'INSERTKEY_NEEDED', 'INSERTKEY_VISUAL', 'INSERTKEY_XYZ_TO_RGB'}, default {'INSERTKEY_NEEDED'}

   .. method:: poll(context)

      Test if Keying Set can be used or not

      :type context: :class:`Context`
      :rtype: boolean

   .. method:: iterator(context, ks)

      Call generate() on the structs which have properties to be keyframed

      :type context: :class:`Context`
      :type ks: :class:`KeyingSet`

   .. method:: generate(context, ks, data)

      Add Paths to the Keying Set to keyframe the properties of the given data

      :type context: :class:`Context`
      :type ks: :class:`KeyingSet`
      :type data: :class:`AnyType`, (never None)

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

   * :class:`KeyingSet.type_info`

