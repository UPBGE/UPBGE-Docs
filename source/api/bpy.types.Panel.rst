Panel(bpy_struct)
=================

.. module:: bpy.types

Basic Panel Example
+++++++++++++++++++

This script is a simple panel which will draw into the object properties
section.

Notice the 'CATEGORY_PT_name' :class:`Panel.bl_idname`, this is a naming
convention for panels.

.. note::

   Panel subclasses must be registered for blender to use them.

.. literalinclude:: ..\examples\bpy.types.Panel.py
   :lines: 15-

Simple Object Panel
+++++++++++++++++++

This panel has a :class:`Panel.poll` and :class:`Panel.draw_header` function,
even though the contents is basic this closely resembles blenders panels.

.. literalinclude:: ..\examples\bpy.types.Panel.1.py
   :lines: 8-

Mix-in Classes
++++++++++++++
A mix-in parent class can be used to share common properties and
:class:`Menu.poll` function.

.. literalinclude:: ..\examples\bpy.types.Panel.2.py
   :lines: 7-

base class --- :class:`bpy_struct`

.. class:: Panel(bpy_struct)

   Panel containing UI elements

   .. attribute:: bl_category

      :type: string, default "", (never None)

   .. attribute:: bl_context

      The context in which the panel belongs to. (TODO: explain the possible combinations bl_context/bl_region_type/bl_space_type)

      :type: string, default "", (never None)

   .. attribute:: bl_idname

      If this is set, the panel gets a custom ID, otherwise it takes the name of the class used to define the panel. For example, if the class name is "OBJECT_PT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_PT_hello"

      :type: string, default "", (never None)

   .. attribute:: bl_label

      The panel label, shows up in the panel header at the right of the triangle used to collapse the panel

      :type: string, default "", (never None)

   .. attribute:: bl_options

      Options for this panel type

      * ``DEFAULT_CLOSED`` Default Closed, Defines if the panel has to be open or collapsed at the time of its creation.
      * ``HIDE_HEADER`` Hide Header, If set to False, the panel shows a header, which contains a clickable arrow to collapse the panel and the label (see bl_label).

      :type: enum set in {'DEFAULT_CLOSED', 'HIDE_HEADER'}, default {'DEFAULT_CLOSED'}

   .. attribute:: bl_region_type

      The region where the panel is going to be used in

      :type: enum in ['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'PREVIEW'], default 'WINDOW'

   .. attribute:: bl_space_type

      The space where the panel is going to be used in

      * ``EMPTY`` Empty.
      * ``VIEW_3D`` 3D View, 3D viewport.
      * ``TIMELINE`` Timeline, Timeline and playback controls.
      * ``GRAPH_EDITOR`` Graph Editor, Edit drivers and keyframe interpolation.
      * ``DOPESHEET_EDITOR`` Dope Sheet, Adjust timing of keyframes.
      * ``NLA_EDITOR`` NLA Editor, Combine and layer Actions.
      * ``IMAGE_EDITOR`` UV/Image Editor, View and edit images and UV Maps.
      * ``CLIP_EDITOR`` Movie Clip Editor, Motion tracking tools.
      * ``SEQUENCE_EDITOR`` Video Sequence Editor, Video editing tools.
      * ``NODE_EDITOR`` Node Editor, Editor for node-based shading and compositing tools.
      * ``TEXT_EDITOR`` Text Editor, Edit scripts and in-file documentation.
      * ``LOGIC_EDITOR`` Logic Editor, Game logic editing.
      * ``PROPERTIES`` Properties, Edit properties of active object and related data-blocks.
      * ``OUTLINER`` Outliner, Overview of scene graph and all available data-blocks.
      * ``USER_PREFERENCES`` User Preferences, Edit persistent configuration settings.
      * ``INFO`` Info, Main menu bar and list of error messages (drag down to expand and display).
      * ``FILE_BROWSER`` File Browser, Browse for files and assets.
      * ``CONSOLE`` Python Console, Interactive programmatic console for advanced editing and script development.

      :type: enum in ['EMPTY', 'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR', 'IMAGE_EDITOR', 'CLIP_EDITOR', 'SEQUENCE_EDITOR', 'NODE_EDITOR', 'TEXT_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINER', 'USER_PREFERENCES', 'INFO', 'FILE_BROWSER', 'CONSOLE'], default 'EMPTY'

   .. attribute:: bl_translation_context

      :type: string, default "*", (never None)

   .. data:: layout

      Defines the structure of the panel in the UI

      :type: :class:`UILayout`, (readonly)

   .. attribute:: text

      XXX todo

      :type: string, default "", (never None)

   .. attribute:: use_pin

      :type: boolean, default False

   .. classmethod:: poll(context)

      If this method returns a non-null output, then the panel can be drawn

      :type context: :class:`Context`, (never None)
      :rtype: boolean

   .. method:: draw(context)

      Draw UI elements into the panel UI layout

      :type context: :class:`Context`, (never None)

   .. method:: draw_header(context)

      Draw UI elements into the panel's header UI layout

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

