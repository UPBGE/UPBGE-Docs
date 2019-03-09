Outliner Operators
==================

.. module:: bpy.ops.outliner

.. function:: action_set(action='')

   Change the active action used

   :arg action:

      Action

   :type action: enum in [], (optional)

.. function:: animdata_operation(type='CLEAR_ANIMDATA')

   Undocumented

   :arg type:

      Animation Operation

      * ``CLEAR_ANIMDATA`` Clear Animation Data, Remove this animation data container.
      * ``SET_ACT`` Set Action.
      * ``CLEAR_ACT`` Unlink Action.
      * ``REFRESH_DRIVERS`` Refresh Drivers.
      * ``CLEAR_DRIVERS`` Clear Drivers.

   :type type: enum in ['CLEAR_ANIMDATA', 'SET_ACT', 'CLEAR_ACT', 'REFRESH_DRIVERS', 'CLEAR_DRIVERS'], (optional)

.. function:: constraint_operation(type='ENABLE')

   Undocumented

   :arg type:

      Constraint Operation

   :type type: enum in ['ENABLE', 'DISABLE', 'DELETE'], (optional)

.. function:: data_operation(type='SELECT')

   Undocumented

   :arg type:

      Data Operation

   :type type: enum in ['SELECT', 'DESELECT', 'HIDE', 'UNHIDE', 'SELECT_LINKED'], (optional)

.. function:: drivers_add_selected()

   Add drivers to selected items

.. function:: drivers_delete_selected()

   Delete drivers assigned to selected items

.. function:: expanded_toggle()

   Expand/Collapse all items

.. function:: group_link(object="Object")

   Link Object to Group in Outliner

   :arg object:

      Object, Target Object

   :type object: string, (optional, never None)

.. function:: group_operation(type='UNLINK')

   Undocumented

   :arg type:

      Group Operation

      * ``UNLINK`` Unlink Group.
      * ``LOCAL`` Make Local Group.
      * ``LINK`` Link Group Objects to Scene.
      * ``DELETE`` Delete Group.
      * ``REMAP`` Remap Users, Make all users of selected data-blocks to use instead current (clicked) one.
      * ``INSTANCE`` Instance Groups in Scene.
      * ``TOGVIS`` Toggle Visible Group.
      * ``TOGSEL`` Toggle Selectable.
      * ``TOGREN`` Toggle Renderable.
      * ``RENAME`` Rename.

   :type type: enum in ['UNLINK', 'LOCAL', 'LINK', 'DELETE', 'REMAP', 'INSTANCE', 'TOGVIS', 'TOGSEL', 'TOGREN', 'RENAME'], (optional)

.. function:: id_delete()

   Delete the ID under cursor

.. function:: id_operation(type='UNLINK')

   Undocumented

   :arg type:

      ID data Operation

      * ``UNLINK`` Unlink.
      * ``LOCAL`` Make Local.
      * ``SINGLE`` Make Single User.
      * ``DELETE`` Delete, WARNING: no undo.
      * ``REMAP`` Remap Users, Make all users of selected data-blocks to use instead current (clicked) one.
      * ``ADD_FAKE`` Add Fake User, Ensure data-block gets saved even if it isn't in use (e.g. for motion and material libraries).
      * ``CLEAR_FAKE`` Clear Fake User.
      * ``RENAME`` Rename.
      * ``SELECT_LINKED`` Select Linked.

   :type type: enum in ['UNLINK', 'LOCAL', 'SINGLE', 'DELETE', 'REMAP', 'ADD_FAKE', 'CLEAR_FAKE', 'RENAME', 'SELECT_LINKED'], (optional)

.. function:: id_remap(id_type='OBJECT', old_id='', new_id='')

   Undocumented

   :arg id_type:

      ID Type

   :type id_type: enum in ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'GROUP', 'IMAGE', 'KEY', 'LAMP', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD'], (optional)
   :arg old_id:

      Old ID, Old ID to replace

   :type old_id: enum in [], (optional)
   :arg new_id:

      New ID, New ID to remap all selected IDs' users to

   :type new_id: enum in [], (optional)

.. function:: item_activate(extend=True, recursive=False)

   Handle mouse clicks to activate/select items

   :arg extend:

      Extend, Extend selection for activation

   :type extend: boolean, (optional)
   :arg recursive:

      Recursive, Select Objects and their children

   :type recursive: boolean, (optional)

.. function:: item_openclose(all=True)

   Toggle whether item under cursor is enabled or closed

   :arg all:

      All, Close or open all items

   :type all: boolean, (optional)

.. function:: item_rename()

   Rename item under cursor

.. function:: keyingset_add_selected()

   Add selected items (blue-gray rows) to active Keying Set

.. function:: keyingset_remove_selected()

   Remove selected items (blue-gray rows) from active Keying Set

.. function:: lib_operation(type='RENAME')

   Undocumented

   :arg type:

      Library Operation

      * ``RENAME`` Rename.
      * ``DELETE`` Delete, Delete this library and all its item from Blender - WARNING: no undo.
      * ``RELOCATE`` Relocate, Select a new path for this library, and reload all its data.
      * ``RELOAD`` Reload, Reload all data from this library.

   :type type: enum in ['RENAME', 'DELETE', 'RELOCATE', 'RELOAD'], (optional)

.. function:: lib_relocate()

   Relocate the library under cursor

.. function:: material_drop(object="Object", material="Material")

   Drag material to object in Outliner

   :arg object:

      Object, Target Object

   :type object: string, (optional, never None)
   :arg material:

      Material, Target Material

   :type material: string, (optional, never None)

.. function:: modifier_operation(type='TOGVIS')

   Undocumented

   :arg type:

      Modifier Operation

   :type type: enum in ['TOGVIS', 'TOGREN', 'DELETE'], (optional)

.. function:: object_operation(type='SELECT')

   Undocumented

   :arg type:

      Object Operation

      * ``SELECT`` Select.
      * ``DESELECT`` Deselect.
      * ``SELECT_HIERARCHY`` Select Hierarchy.
      * ``DELETE`` Delete.
      * ``DELETE_HIERARCHY`` Delete Hierarchy.
      * ``REMAP`` Remap Users, Make all users of selected data-blocks to use instead a new chosen one.
      * ``TOGVIS`` Toggle Visible.
      * ``TOGSEL`` Toggle Selectable.
      * ``TOGREN`` Toggle Renderable.
      * ``RENAME`` Rename.

   :type type: enum in ['SELECT', 'DESELECT', 'SELECT_HIERARCHY', 'DELETE', 'DELETE_HIERARCHY', 'REMAP', 'TOGVIS', 'TOGSEL', 'TOGREN', 'RENAME'], (optional)

.. function:: operation()

   Context menu for item operations

.. function:: orphans_purge()

   Clear all orphaned data-blocks without any users from the file (cannot be undone, saves to current .blend file)

.. function:: parent_clear(dragged_obj="Object", type='CLEAR')

   Drag to clear parent in Outliner

   :arg dragged_obj:

      Child, Child Object

   :type dragged_obj: string, (optional, never None)
   :arg type:

      Type

      * ``CLEAR`` Clear Parent, Completely clear the parenting relationship, including involved modifiers if any.
      * ``CLEAR_KEEP_TRANSFORM`` Clear and Keep Transformation, As 'Clear Parent', but keep the current visual transformations of the object.
      * ``CLEAR_INVERSE`` Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.

   :type type: enum in ['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE'], (optional)

.. function:: parent_drop(child="Object", parent="Object", type='OBJECT')

   Drag to parent in Outliner

   :arg child:

      Child, Child Object

   :type child: string, (optional, never None)
   :arg parent:

      Parent, Parent Object

   :type parent: string, (optional, never None)
   :arg type:

      Type

   :type type: enum in ['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI'], (optional)

.. function:: renderability_toggle()

   Toggle the renderability of selected items

.. function:: scene_drop(object="Object", scene="Scene")

   Drag object to scene in Outliner

   :arg object:

      Object, Target Object

   :type object: string, (optional, never None)
   :arg scene:

      Scene, Target Scene

   :type scene: string, (optional, never None)

.. function:: scene_operation(type='DELETE')

   Context menu for scene operations

   :arg type:

      Scene Operation

   :type type: enum in ['DELETE'], (optional)

.. function:: scroll_page(up=False)

   Scroll page up or down

   :arg up:

      Up, Scroll up one page

   :type up: boolean, (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False)

   Use box selection to select tree elements

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

.. function:: selectability_toggle()

   Toggle the selectability

.. function:: selected_toggle()

   Toggle the Outliner selection of items

.. function:: show_active()

   Open up the tree and adjust the view so that the active Object is shown centered

.. function:: show_hierarchy()

   Open all object entries and close all others

.. function:: show_one_level(open=True)

   Expand/collapse all entries by one level

   :arg open:

      Open, Expand all entries one level deep

   :type open: boolean, (optional)

.. function:: visibility_toggle()

   Toggle the visibility of selected items

