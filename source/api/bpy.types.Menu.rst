Menu(bpy_struct)
================

.. module:: bpy.types

Basic Menu Example
++++++++++++++++++

Here is an example of a simple menu. Menus differ from panels in that they must
reference from a header, panel or another menu.

Notice the 'CATEGORY_MT_name' in  :class:`Menu.bl_idname`, this is a naming
convention for menus.

.. note::

   Menu subclasses must be registered before referencing them from blender.

.. note::

   Menus have their :class:`Layout.operator_context` initialized as
   'EXEC_REGION_WIN' rather than 'INVOKE_DEFAULT' (see :ref:`Execution Context <operator-execution_context>`).
   If the operator context needs to initialize inputs from the
   :class:`Operator.invoke` function, then this needs to be explicitly set.

.. literalinclude:: ..\examples\bpy.types.Menu.py
   :lines: 22-

Submenus
++++++++

This menu demonstrates some different functions.

.. literalinclude:: ..\examples\bpy.types.Menu.1.py
   :lines: 7-

Extending Menus
+++++++++++++++

When creating menus for add-ons you can't reference menus
in Blender's default scripts.
Instead, the add-on can add menu items to existing menus.

The function menu_draw acts like :class:`Menu.draw`.

.. literalinclude:: ..\examples\bpy.types.Menu.2.py
   :lines: 11-

Preset Menus
++++++++++++

Preset menus are simply a convention that uses a menu sub-class
to perform the common task of managing presets.

This example shows how you can add a preset menu.

This example uses the object draw options,
however you can use properties defined by your own scripts too.

.. literalinclude:: ..\examples\bpy.types.Menu.3.py
   :lines: 13-

Extending the Button Context Menu
+++++++++++++++++++++++++++++++++

This example enables you to insert your own menu entry into the common
right click menu that you get while hovering over a value field,
color, string, etc.

To make the example work, you have to first select an object
then right click on an user interface element (maybe a color in the
material properties) and choose *Execute Custom Action*.

Executing the operator will then print all values.

.. literalinclude:: ..\examples\bpy.types.Menu.4.py
   :lines: 15-

base class --- :class:`bpy_struct`

.. class:: Menu(bpy_struct)

   Editor menu containing buttons

   .. attribute:: bl_description

      :type: string, default ""

   .. attribute:: bl_idname

      If this is set, the menu gets a custom ID, otherwise it takes the name of the class used to define the menu (for example, if the class name is "OBJECT_MT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_MT_hello")

      :type: string, default "", (never None)

   .. attribute:: bl_label

      The menu label

      :type: string, default "", (never None)

   .. attribute:: bl_translation_context

      :type: string, default "*", (never None)

   .. data:: layout

      Defines the structure of the menu in the UI

      :type: :class:`UILayout`, (readonly)

   .. classmethod:: poll(context)

      If this method returns a non-null output, then the menu can be drawn

      :type context: :class:`Context`
      :rtype: boolean

   .. method:: draw(context)

      Draw UI elements into the menu UI layout

      :type context: :class:`Context`

   .. method:: draw_preset(context)

      Define these on the subclass:
      - preset_operator (string)
      - preset_subdir (string)
      
      Optionally:
      - preset_extensions (set of strings)
      - preset_operator_defaults (dict of keyword args)

   .. method:: path_menu(searchpaths, operator, *, props_default=None, prop_filepath='filepath', filter_ext=None, filter_path=None, display_name=None)

      Populate a menu from a list of paths.
      
      :arg searchpaths: Paths to scan.
      :type searchpaths: sequence of strings.
      :arg operator: The operator id to use with each file.
      :type operator: string
      :arg prop_filepath: Optional operator filepath property (defaults to "filepath").
      :type prop_filepath: string
      :arg props_default: Properties to assign to each operator.
      :type props_default: dict
      :arg filter_ext: Optional callback that takes the file extensions.
      
         Returning false excludes the file from the list.
      
      :type filter_ext: Callable that takes a string and returns a bool.
      :arg display_name: Optional callback that takes the full path, returns the name to display.
      :type display_name: Callable that takes a string and returns a string.

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

