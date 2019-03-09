Macro(bpy_struct)
=================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Macro(bpy_struct)

   Storage of a macro operator being executed, or registered after execution

   .. attribute:: bl_description

      :type: string, default ""

   .. attribute:: bl_idname

      :type: string, default "", (never None)

   .. attribute:: bl_label

      :type: string, default "", (never None)

   .. attribute:: bl_options

      Options for this operator type

      * ``REGISTER`` Register, Display in the info window and support the redo toolbar panel.
      * ``UNDO`` Undo, Push an undo event (needed for operator redo).
      * ``UNDO_GROUPED`` Grouped Undo, Push a single undo event for repetead instances of this operator.
      * ``BLOCKING`` Blocking, Block anything else from using the cursor.
      * ``MACRO`` Macro, Use to check if an operator is a macro.
      * ``GRAB_CURSOR`` Grab Pointer, Use so the operator grabs the mouse focus, enables wrapping when continuous grab is enabled.
      * ``PRESET`` Preset, Display a preset button with the operators settings.
      * ``INTERNAL`` Internal, Removes the operator from search results.

      :type: enum set in {'REGISTER', 'UNDO', 'UNDO_GROUPED', 'BLOCKING', 'MACRO', 'GRAB_CURSOR', 'PRESET', 'INTERNAL'}, default {'REGISTER'}

   .. attribute:: bl_translation_context

      :type: string, default "Operator"

   .. attribute:: bl_undo_group

      :type: string, default ""

   .. data:: name

      :type: string, default "", (readonly, never None)

   .. data:: properties

      :type: :class:`OperatorProperties`, (readonly, never None)

   .. method:: report(type, message)

      report

      :arg type:

         Type

      :type type: enum set in {'DEBUG', 'INFO', 'OPERATOR', 'PROPERTY', 'WARNING', 'ERROR', 'ERROR_INVALID_INPUT', 'ERROR_INVALID_CONTEXT', 'ERROR_OUT_OF_MEMORY'}
      :arg message:

         Report Message

      :type message: string, (never None)

   .. classmethod:: poll(context)

      Test if the operator can be called or not

      :type context: :class:`Context`, (never None)
      :rtype: boolean

   .. method:: draw(context)

      Draw function for the operator

      :type context: :class:`Context`, (never None)

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

   * :class:`Operator.macros`

