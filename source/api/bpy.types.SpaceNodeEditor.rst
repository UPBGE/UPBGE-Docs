SpaceNodeEditor(Space)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceNodeEditor(Space)

   Node editor space data

   .. attribute:: backdrop_channels

      Channels of the image to draw

      * ``COLOR_ALPHA`` Color and Alpha, Draw image with RGB colors and alpha transparency.
      * ``COLOR`` Color, Draw image with RGB colors.
      * ``ALPHA`` Alpha, Draw alpha transparency channel.
      * ``RED`` Red.
      * ``GREEN`` Green.
      * ``BLUE`` Blue.

      :type: enum in ['COLOR_ALPHA', 'COLOR', 'ALPHA', 'RED', 'GREEN', 'BLUE'], default 'COLOR'

   .. attribute:: backdrop_x

      Backdrop X offset

      :type: float in [-inf, inf], default 0.0

   .. attribute:: backdrop_y

      Backdrop Y offset

      :type: float in [-inf, inf], default 0.0

   .. attribute:: backdrop_zoom

      Backdrop zoom factor

      :type: float in [0.01, inf], default 1.0

   .. attribute:: cursor_location

      Location for adding new nodes

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. data:: edit_tree

      Node tree being displayed and edited

      :type: :class:`NodeTree`, (readonly)

   .. data:: id

      Data-block whose nodes are being edited

      :type: :class:`ID`, (readonly)

   .. data:: id_from

      Data-block from which the edited data-block is linked

      :type: :class:`ID`, (readonly)

   .. attribute:: insert_offset_direction

      Direction to offset nodes on insertion

      :type: enum in ['RIGHT', 'LEFT'], default 'RIGHT'

   .. attribute:: node_tree

      Base node tree from context

      :type: :class:`NodeTree`

   .. data:: path

      Path from the data-block to the currently edited node tree

      :type: :class:`SpaceNodeEditorPath` :class:`bpy_prop_collection` of :class:`NodeTreePath`, (readonly)

   .. attribute:: pin

      Use the pinned node tree

      :type: boolean, default False

   .. attribute:: shader_type

      Type of data to take shader from

      * ``OBJECT`` Object, Edit shader nodes from Object.
      * ``WORLD`` World, Edit shader nodes from World.
      * ``LINESTYLE`` Line Style, Edit shader nodes from Line Style.

      :type: enum in ['OBJECT', 'WORLD', 'LINESTYLE'], default 'OBJECT'

   .. attribute:: show_backdrop

      Use active Viewer Node output as backdrop for compositing nodes

      :type: boolean, default False

   .. attribute:: show_grease_pencil

      Show grease pencil for this view

      :type: boolean, default False

   .. attribute:: texture_type

      Type of data to take texture from

      * ``OBJECT`` Object, Edit texture nodes from Object.
      * ``WORLD`` World, Edit texture nodes from World.
      * ``BRUSH`` Brush, Edit texture nodes from Brush.
      * ``LINESTYLE`` Line Style, Edit texture nodes from Line Style.

      :type: enum in ['OBJECT', 'WORLD', 'BRUSH', 'LINESTYLE'], default 'OBJECT'

   .. attribute:: tree_type

      Node tree type to display and edit

      :type: enum in ['DUMMY'], default 'DUMMY'

   .. attribute:: use_auto_render

      Re-render and composite changed layers on 3D edits

      :type: boolean, default False

   .. attribute:: use_insert_offset

      Automatically offset the following or previous nodes in a chain when inserting a new node

      :type: boolean, default False

   .. method:: cursor_location_from_region(x, y)

      Set the cursor location using region coordinates

      :arg x:

         x, Region x coordinate

      :type x: int in [-inf, inf]
      :arg y:

         y, Region y coordinate

      :type y: int in [-inf, inf]

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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

