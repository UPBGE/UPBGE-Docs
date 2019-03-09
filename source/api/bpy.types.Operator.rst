Operator(bpy_struct)
====================

.. module:: bpy.types

Basic Operator Example
++++++++++++++++++++++

This script shows simple operator which prints a message.

Since the operator only has an :class:`Operator.execute` function it takes no
user input.

.. note::

   Operator subclasses must be registered before accessing them from blender.

.. literalinclude:: ..\examples\bpy.types.Operator.py
   :lines: 14-

Invoke Function
+++++++++++++++

:class:`Operator.invoke` is used to initialize the operator from the context
at the moment the operator is called.
invoke() is typically used to assign properties which are then used by
execute().
Some operators don't have an execute() function, removing the ability to be
repeated from a script or macro.

This example shows how to define an operator which gets mouse input to
execute a function and that this operator can be invoked or executed from
the python api.

Also notice this operator defines its own properties, these are different
to typical class properties because blender registers them with the
operator, to use as arguments when called, saved for operator undo/redo and
automatically added into the user interface.

.. literalinclude:: ..\examples\bpy.types.Operator.1.py
   :lines: 21-

Calling a File Selector
+++++++++++++++++++++++
This example shows how an operator can use the file selector.

Notice the invoke function calls a window manager method and returns
``{'RUNNING_MODAL'}``, this means the file selector stays open and the operator does not
exit immediately after invoke finishes.

The file selector runs the operator, calling :class:`Operator.execute` when the
user confirms.

The :class:`Operator.poll` function is optional, used to check if the operator
can run.

.. literalinclude:: ..\examples\bpy.types.Operator.2.py
   :lines: 16-

Dialog Box
++++++++++

This operator uses its :class:`Operator.invoke` function to call a popup.

.. literalinclude:: ..\examples\bpy.types.Operator.3.py
   :lines: 7-

Custom Drawing
++++++++++++++

By default operator properties use an automatic user interface layout.
If you need more control you can create your own layout with a
:class:`Operator.draw` function.

This works like the :class:`Panel` and :class:`Menu` draw functions, its used
for dialogs and file selectors.

.. literalinclude:: ..\examples\bpy.types.Operator.4.py
   :lines: 12-

Modal Execution
+++++++++++++++

This operator defines a :class:`Operator.modal` function that will keep being
run to handle events until it returns ``{'FINISHED'}`` or ``{'CANCELLED'}``.

Modal operators run every time a new event is detected, such as a mouse click
or key press. Conversely, when no new events are detected, the modal operator
will not run. Modal operators are especially useful for interactive tools, an
operator can have its own state where keys toggle options as the operator runs.
Grab, Rotate, Scale, and Fly-Mode are examples of modal operators.

:class:`Operator.invoke` is used to initialize the operator as being by
returning ``{'RUNNING_MODAL'}``, initializing the modal loop.

Notice ``__init__()`` and ``__del__()`` are declared.
For other operator types they are not useful but for modal operators they will
be called before the :class:`Operator.invoke` and after the operator finishes.

.. literalinclude:: ..\examples\bpy.types.Operator.5.py
   :lines: 21-

base class --- :class:`bpy_struct`

.. class:: Operator(bpy_struct)

   Storage of an operator being executed, or registered after execution

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

   .. data:: has_reports

      Operator has a set of reports (warnings and errors) from last execution

      :type: boolean, default False, (readonly)

   .. data:: layout

      :type: :class:`UILayout`, (readonly)

   .. data:: macros

      :type: :class:`bpy_prop_collection` of :class:`Macro`, (readonly)

   .. data:: name

      :type: string, default "", (readonly, never None)

   .. data:: options

      Runtime options

      :type: :class:`OperatorOptions`, (readonly, never None)

   .. data:: properties

      :type: :class:`OperatorProperties`, (readonly, never None)

   .. attribute:: bl_property

      The name of a property to use as this operators primary property.
      Currently this is only used to select the default property when
      expanding an operator into a menu.
      :type: string

   .. method:: report(type, message)

      report

      :arg type:

         Type

      :type type: enum set in {'DEBUG', 'INFO', 'OPERATOR', 'PROPERTY', 'WARNING', 'ERROR', 'ERROR_INVALID_INPUT', 'ERROR_INVALID_CONTEXT', 'ERROR_OUT_OF_MEMORY'}
      :arg message:

         Report Message

      :type message: string, (never None)

   .. method:: is_repeat()

      is_repeat

      :return:

         result

      :rtype: boolean

   .. classmethod:: poll(context)

      Test if the operator can be called or not

      :type context: :class:`Context`, (never None)
      :rtype: boolean

   .. method:: execute(context)

      Execute the operator

      :type context: :class:`Context`, (never None)
      :return:

         result

         * ``RUNNING_MODAL`` Running Modal, Keep the operator running with blender.
         * ``CANCELLED`` Cancelled, When no action has been taken, operator exits.
         * ``FINISHED`` Finished, When the operator is complete, operator exits.
         * ``PASS_THROUGH`` Pass Through, Do nothing and pass the event on.
         * ``INTERFACE`` Interface, Handled but not executed (popup menus).

      :rtype: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH', 'INTERFACE'}

   .. method:: check(context)

      Check the operator settings, return True to signal a change to redraw

      :type context: :class:`Context`, (never None)
      :return:

         result

      :rtype: boolean

   .. method:: invoke(context, event)

      Invoke the operator

      :type context: :class:`Context`, (never None)
      :type event: :class:`Event`, (never None)
      :return:

         result

         * ``RUNNING_MODAL`` Running Modal, Keep the operator running with blender.
         * ``CANCELLED`` Cancelled, When no action has been taken, operator exits.
         * ``FINISHED`` Finished, When the operator is complete, operator exits.
         * ``PASS_THROUGH`` Pass Through, Do nothing and pass the event on.
         * ``INTERFACE`` Interface, Handled but not executed (popup menus).

      :rtype: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH', 'INTERFACE'}

   .. method:: modal(context, event)

      Modal operator function

      :type context: :class:`Context`, (never None)
      :type event: :class:`Event`, (never None)
      :return:

         result

         * ``RUNNING_MODAL`` Running Modal, Keep the operator running with blender.
         * ``CANCELLED`` Cancelled, When no action has been taken, operator exits.
         * ``FINISHED`` Finished, When the operator is complete, operator exits.
         * ``PASS_THROUGH`` Pass Through, Do nothing and pass the event on.
         * ``INTERFACE`` Interface, Handled but not executed (popup menus).

      :rtype: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH', 'INTERFACE'}

   .. method:: draw(context)

      Draw function for the operator

      :type context: :class:`Context`, (never None)

   .. method:: cancel(context)

      Called when the operator is canceled

      :type context: :class:`Context`, (never None)

   .. method:: as_keywords(ignore=())

      Return a copy of the properties as a dictionary

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

   * :mod:`bpy.context.active_operator`
   * :class:`SpaceFileBrowser.active_operator`
   * :class:`SpaceFileBrowser.operator`
   * :class:`WindowManager.fileselect_add`
   * :class:`WindowManager.invoke_confirm`
   * :class:`WindowManager.invoke_popup`
   * :class:`WindowManager.invoke_props_dialog`
   * :class:`WindowManager.invoke_props_popup`
   * :class:`WindowManager.invoke_search_popup`
   * :class:`WindowManager.modal_handler_add`
   * :class:`WindowManager.operators`

