Node Operators
==============

.. module:: bpy.ops.node

.. function:: add_and_link_node(type="", use_transform=False, settings=None, link_socket_index=0)

   Add a node to the active tree and link to an existing socket

   :arg type:

      Node Type, Node type

   :type type: string, (optional, never None)
   :arg use_transform:

      Use Transform, Start transform operator after inserting the node

   :type use_transform: boolean, (optional)
   :arg settings:

      Settings, Settings to be applied on the newly created node

   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :arg link_socket_index:

      Link Socket Index, Index of the socket to link

   :type link_socket_index: int in [-inf, inf], (optional)

   :file: `startup\bl_operators\node.py\:160 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\node.py$160>`_

.. function:: add_file(filepath="", filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', name="Image")

   Add a file node to the current node editor

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
   :arg show_multiview:

      Enable Multi-View

   :type show_multiview: boolean, (optional)
   :arg use_multiview:

      Use Multi-View

   :type use_multiview: boolean, (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
   :arg name:

      Name, Data-block name to assign

   :type name: string, (optional, never None)

.. function:: add_mask(name="Mask")

   Add a mask node to the current node editor

   :arg name:

      Name, Data-block name to assign

   :type name: string, (optional, never None)

.. function:: add_node(type="", use_transform=False, settings=None)

   Add a node to the active tree

   :arg type:

      Node Type, Node type

   :type type: string, (optional, never None)
   :arg use_transform:

      Use Transform, Start transform operator after inserting the node

   :type use_transform: boolean, (optional)
   :arg settings:

      Settings, Settings to be applied on the newly created node

   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)

   :file: `startup\bl_operators\node.py\:120 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\node.py$120>`_

.. function:: add_reroute(path=None, cursor=6)

   Add a reroute node

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg cursor:

      Cursor

   :type cursor: int in [0, inf], (optional)

.. function:: add_search(type="", use_transform=False, settings=None, node_item='')

   Add a node to the active tree

   :arg type:

      Node Type, Node type

   :type type: string, (optional, never None)
   :arg use_transform:

      Use Transform, Start transform operator after inserting the node

   :type use_transform: boolean, (optional)
   :arg settings:

      Settings, Settings to be applied on the newly created node

   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :arg node_item:

      Node Type, Node type

   :type node_item: enum in [], (optional)

   :file: `startup\bl_operators\node.py\:219 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\node.py$219>`_

.. function:: attach()

   Attach active node to a frame

.. function:: backimage_fit()

   Fit the background image to the view

.. function:: backimage_move()

   Move Node backdrop

.. function:: backimage_sample()

   Use mouse to sample background image

.. function:: backimage_zoom(factor=1.2)

   Zoom in/out the background image

   :arg factor:

      Factor

   :type factor: float in [0, 10], (optional)

.. function:: clear_viewer_border()

   Clear the boundaries for viewer operations

.. function:: clipboard_copy()

   Copies selected nodes to the clipboard

.. function:: clipboard_paste()

   Pastes nodes from the clipboard to the active node tree

.. function:: collapse_hide_unused_toggle()

   Toggle collapsed nodes and hide unused sockets

   :file: `startup\bl_operators\node.py\:262 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\node.py$262>`_

.. function:: delete()

   Delete selected nodes

.. function:: delete_reconnect()

   Delete nodes; will reconnect nodes as if deletion was muted

.. function:: detach()

   Detach selected nodes from parents

.. function:: detach_translate_attach(NODE_OT_detach=None, TRANSFORM_OT_translate=None, NODE_OT_attach=None)

   Detach nodes, move and attach to frame

   :arg NODE_OT_detach:

      Detach Nodes, Detach selected nodes from parents

   :type NODE_OT_detach: :class:`NODE_OT_detach`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)
   :arg NODE_OT_attach:

      Attach Nodes, Attach active node to a frame

   :type NODE_OT_attach: :class:`NODE_OT_attach`, (optional)

.. function:: duplicate(keep_inputs=False)

   Duplicate selected nodes

   :arg keep_inputs:

      Keep Inputs, Keep the input links to duplicated nodes

   :type keep_inputs: boolean, (optional)

.. function:: duplicate_move(NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

   Duplicate selected nodes and move them

   :arg NODE_OT_duplicate:

      Duplicate Nodes, Duplicate selected nodes

   :type NODE_OT_duplicate: :class:`NODE_OT_duplicate`, (optional)
   :arg NODE_OT_translate_attach:

      Move and Attach, Move nodes and attach to frame

   :type NODE_OT_translate_attach: :class:`NODE_OT_translate_attach`, (optional)

.. function:: duplicate_move_keep_inputs(NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

   Duplicate selected nodes keeping input links and move them

   :arg NODE_OT_duplicate:

      Duplicate Nodes, Duplicate selected nodes

   :type NODE_OT_duplicate: :class:`NODE_OT_duplicate`, (optional)
   :arg NODE_OT_translate_attach:

      Move and Attach, Move nodes and attach to frame

   :type NODE_OT_translate_attach: :class:`NODE_OT_translate_attach`, (optional)

.. function:: find_node(prev=False)

   Search for named node and allow to select and activate it

   :arg prev:

      Previous

   :type prev: boolean, (optional)

.. function:: group_edit(exit=False)

   Edit node group

   :arg exit:

      Exit

   :type exit: boolean, (optional)

.. function:: group_insert()

   Insert selected nodes into a node group

.. function:: group_make()

   Make group from selected nodes

.. function:: group_separate(type='COPY')

   Separate selected nodes from the node group

   :arg type:

      Type

      * ``COPY`` Copy, Copy to parent node tree, keep group intact.
      * ``MOVE`` Move, Move to parent node tree, remove from group.

   :type type: enum in ['COPY', 'MOVE'], (optional)

.. function:: group_ungroup()

   Ungroup selected nodes

.. function:: hide_socket_toggle()

   Toggle unused node socket display

.. function:: hide_toggle()

   Toggle hiding of selected nodes

.. function:: insert_offset()

   Automatically offset nodes on insertion

.. function:: join()

   Attach selected nodes to a new common frame

.. function:: link(detach=False)

   Use the mouse to create a link between two nodes

   :arg detach:

      Detach, Detach and redirect existing links

   :type detach: boolean, (optional)

.. function:: link_make(replace=False)

   Makes a link between selected output in input sockets

   :arg replace:

      Replace, Replace socket connections with the new links

   :type replace: boolean, (optional)

.. function:: link_viewer()

   Link to viewer node

.. function:: links_cut(path=None, cursor=9)

   Use the mouse to cut (remove) some links

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg cursor:

      Cursor

   :type cursor: int in [0, inf], (optional)

.. function:: links_detach()

   Remove all links to selected nodes, and try to connect neighbor nodes together

.. function:: move_detach_links(NODE_OT_links_detach=None, TRANSFORM_OT_translate=None, NODE_OT_insert_offset=None)

   Move a node to detach links

   :arg NODE_OT_links_detach:

      Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together

   :type NODE_OT_links_detach: :class:`NODE_OT_links_detach`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)
   :arg NODE_OT_insert_offset:

      Insert Offset, Automatically offset nodes on insertion

   :type NODE_OT_insert_offset: :class:`NODE_OT_insert_offset`, (optional)

.. function:: move_detach_links_release(NODE_OT_links_detach=None, NODE_OT_translate_attach=None)

   Move a node to detach links

   :arg NODE_OT_links_detach:

      Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together

   :type NODE_OT_links_detach: :class:`NODE_OT_links_detach`, (optional)
   :arg NODE_OT_translate_attach:

      Move and Attach, Move nodes and attach to frame

   :type NODE_OT_translate_attach: :class:`NODE_OT_translate_attach`, (optional)

.. function:: mute_toggle()

   Toggle muting of the nodes

.. function:: new_node_tree(type='', name="NodeTree")

   Create a new node tree

   :arg type:

      Tree Type

   :type type: enum in [], (optional)
   :arg name:

      Name

   :type name: string, (optional, never None)

.. function:: node_color_preset_add(name="", remove_active=False)

   Add or remove a Node Color Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: node_copy_color()

   Copy color to all selected nodes

.. function:: options_toggle()

   Toggle option buttons display for selected nodes

.. function:: output_file_add_socket(file_path="Image")

   Add a new input to a file output node

   :arg file_path:

      File Path, Sub-path of the output file

   :type file_path: string, (optional, never None)

.. function:: output_file_move_active_socket(direction='DOWN')

   Move the active input of a file output node up or down the list

   :arg direction:

      Direction

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: output_file_remove_active_socket()

   Remove active input from a file output node

.. function:: parent_set()

   Attach selected nodes

.. function:: preview_toggle()

   Toggle preview display for selected nodes

.. function:: properties()

   Toggle the properties region visibility

.. function:: read_fullsamplelayers()

   Read all render layers of current scene, in full sample

.. function:: read_renderlayers()

   Read all render layers of all used scenes

.. function:: render_changed()

   Render current scene, when input node's layer has been changed

.. function:: resize()

   Resize a node

.. function:: select(mouse_x=0, mouse_y=0, extend=False)

   Select the node under the cursor

   :arg mouse_x:

      Mouse X

   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y:

      Mouse Y

   :type mouse_y: int in [-inf, inf], (optional)
   :arg extend:

      Extend

   :type extend: boolean, (optional)

.. function:: select_all(action='TOGGLE')

   (De)select all nodes

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True, tweak=False)

   Use box selection to select nodes

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg tweak:

      Tweak, Only activate when mouse is not over a node - useful for tweak gesture

   :type tweak: boolean, (optional)

.. function:: select_circle(x=0, y=0, radius=25, deselect=False)

   Use circle selection to select nodes

   :arg x:

      X

   :type x: int in [-inf, inf], (optional)
   :arg y:

      Y

   :type y: int in [-inf, inf], (optional)
   :arg radius:

      Radius

   :type radius: int in [1, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)

.. function:: select_grouped(extend=False, type='TYPE')

   Select nodes with similar properties

   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg type:

      Type

   :type type: enum in ['TYPE', 'COLOR', 'PREFIX', 'SUFFIX'], (optional)

.. function:: select_lasso(path=None, deselect=False, extend=True)

   Select nodes using lasso selection

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_link_viewer(NODE_OT_select=None, NODE_OT_link_viewer=None)

   Select node and link it to a viewer node

   :arg NODE_OT_select:

      Select, Select the node under the cursor

   :type NODE_OT_select: :class:`NODE_OT_select`, (optional)
   :arg NODE_OT_link_viewer:

      Link to Viewer Node, Link to viewer node

   :type NODE_OT_link_viewer: :class:`NODE_OT_link_viewer`, (optional)

.. function:: select_linked_from()

   Select nodes linked from the selected ones

.. function:: select_linked_to()

   Select nodes linked to the selected ones

.. function:: select_same_type_step(prev=False)

   Activate and view same node type, step by step

   :arg prev:

      Previous

   :type prev: boolean, (optional)

.. function:: shader_script_update()

   Update shader script node with new sockets and options from the script

.. function:: switch_view_update()

   Update views of selected node

.. function:: toolbar()

   Toggles tool shelf display

.. function:: translate_attach(TRANSFORM_OT_translate=None, NODE_OT_attach=None, NODE_OT_insert_offset=None)

   Move nodes and attach to frame

   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)
   :arg NODE_OT_attach:

      Attach Nodes, Attach active node to a frame

   :type NODE_OT_attach: :class:`NODE_OT_attach`, (optional)
   :arg NODE_OT_insert_offset:

      Insert Offset, Automatically offset nodes on insertion

   :type NODE_OT_insert_offset: :class:`NODE_OT_insert_offset`, (optional)

.. function:: translate_attach_remove_on_cancel(TRANSFORM_OT_translate=None, NODE_OT_attach=None, NODE_OT_insert_offset=None)

   Move nodes and attach to frame

   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)
   :arg NODE_OT_attach:

      Attach Nodes, Attach active node to a frame

   :type NODE_OT_attach: :class:`NODE_OT_attach`, (optional)
   :arg NODE_OT_insert_offset:

      Insert Offset, Automatically offset nodes on insertion

   :type NODE_OT_insert_offset: :class:`NODE_OT_insert_offset`, (optional)

.. function:: tree_path_parent()

   Go to parent node tree

   :file: `startup\bl_operators\node.py\:292 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\node.py$292>`_

.. function:: tree_socket_add(in_out='IN')

   Add an input or output socket to the current node tree

   :arg in_out:

      Socket Type

   :type in_out: enum in ['IN', 'OUT'], (optional)

.. function:: tree_socket_move(direction='UP')

   Move a socket up or down in the current node tree's sockets stack

   :arg direction:

      Direction

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: tree_socket_remove()

   Remove an input or output socket to the current node tree

.. function:: view_all()

   Resize view so you can see all nodes

.. function:: view_selected()

   Resize view so you can see selected nodes

.. function:: viewer_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Set the boundaries for viewer operations

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

