Armature Operators
==================

.. module:: bpy.ops.armature

.. function:: align()

   Align selected bones to the active bone (or to their parent)

.. function:: armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

   Change the visible armature layers

   :arg layers:

      Layer, Armature layers to make visible

   :type layers: boolean array of 32 items, (optional)

.. function:: autoside_names(type='XAXIS')

   Automatically renames the selected bones according to which side of the target axis they fall on

   :arg type:

      Axis, Axis tag names with

      * ``XAXIS`` X-Axis, Left/Right.
      * ``YAXIS`` Y-Axis, Front/Back.
      * ``ZAXIS`` Z-Axis, Top/Bottom.

   :type type: enum in ['XAXIS', 'YAXIS', 'ZAXIS'], (optional)

.. function:: bone_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

   Change the layers that the selected bones belong to

   :arg layers:

      Layer, Armature layers that bone belongs to

   :type layers: boolean array of 32 items, (optional)

.. function:: bone_primitive_add(name="Bone")

   Add a new bone located at the 3D-Cursor

   :arg name:

      Name, Name of the newly created bone

   :type name: string, (optional, never None)

.. function:: calculate_roll(type='POS_X', axis_flip=False, axis_only=False)

   Automatically fix alignment of select bones' axes

   :arg type:

      Type

   :type type: enum in ['POS_X', 'POS_Z', 'GLOBAL_POS_X', 'GLOBAL_POS_Y', 'GLOBAL_POS_Z', 'NEG_X', 'NEG_Z', 'GLOBAL_NEG_X', 'GLOBAL_NEG_Y', 'GLOBAL_NEG_Z', 'ACTIVE', 'VIEW', 'CURSOR'], (optional)
   :arg axis_flip:

      Flip Axis, Negate the alignment axis

   :type axis_flip: boolean, (optional)
   :arg axis_only:

      Shortest Rotation, Ignore the axis direction, use the shortest rotation to align

   :type axis_only: boolean, (optional)

.. function:: click_extrude()

   Create a new bone going from the last selected joint to the mouse position

.. function:: delete()

   Remove selected bones from the armature

.. function:: dissolve()

   Dissolve selected bones from the armature

.. function:: duplicate()

   Make copies of the selected bones within the same armature

.. function:: duplicate_move(ARMATURE_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Make copies of the selected bones within the same armature and move them

   :arg ARMATURE_OT_duplicate:

      Duplicate Selected Bone(s), Make copies of the selected bones within the same armature

   :type ARMATURE_OT_duplicate: :class:`ARMATURE_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude(forked=False)

   Create new bones from the selected joints

   :arg forked:

      Forked

   :type forked: boolean, (optional)

.. function:: extrude_forked(ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None)

   Create new bones from the selected joints and move them

   :arg ARMATURE_OT_extrude:

      Extrude, Create new bones from the selected joints

   :type ARMATURE_OT_extrude: :class:`ARMATURE_OT_extrude`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude_move(ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None)

   Create new bones from the selected joints and move them

   :arg ARMATURE_OT_extrude:

      Extrude, Create new bones from the selected joints

   :type ARMATURE_OT_extrude: :class:`ARMATURE_OT_extrude`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: fill()

   Add bone between selected joint(s) and/or 3D-Cursor

.. function:: flip_names()

   Flips (and corrects) the axis suffixes of the names of selected bones

.. function:: hide(unselected=False)

   Tag selected bones to not be visible in Edit Mode

   :arg unselected:

      Unselected, Hide unselected rather than selected

   :type unselected: boolean, (optional)

.. function:: layers_show_all(all=True)

   Make all armature layers visible

   :arg all:

      All Layers, Enable all layers or just the first 16 (top row)

   :type all: boolean, (optional)

.. function:: merge(type='WITHIN_CHAIN')

   Merge continuous chains of selected bones

   :arg type:

      Type

   :type type: enum in ['WITHIN_CHAIN'], (optional)

.. function:: parent_clear(type='CLEAR')

   Remove the parent-child relationship between selected bones and their parents

   :arg type:

      ClearType, What way to clear parenting

   :type type: enum in ['CLEAR', 'DISCONNECT'], (optional)

.. function:: parent_set(type='CONNECTED')

   Set the active bone as the parent of the selected bones

   :arg type:

      ParentType, Type of parenting

   :type type: enum in ['CONNECTED', 'OFFSET'], (optional)

.. function:: reveal(select=True)

   Reveal all bones hidden in Edit Mode

   :arg select:

      Select

   :type select: boolean, (optional)

.. function:: roll_clear(roll=0.0)

   Clear roll for selected bones

   :arg roll:

      Roll

   :type roll: float in [-6.28319, 6.28319], (optional)

.. function:: select_all(action='TOGGLE')

   Toggle selection status of all bones

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_hierarchy(direction='PARENT', extend=False)

   Select immediate parent/children of selected bones

   :arg direction:

      Direction

   :type direction: enum in ['PARENT', 'CHILD'], (optional)
   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)

.. function:: select_less()

   Deselect those bones at the boundary of each selection region

.. function:: select_linked(extend=False)

   Select bones related to selected ones by parent/child relationships

   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_mirror(only_active=False, extend=False)

   Mirror the bone selection

   :arg only_active:

      Active Only, Only operate on the active bone

   :type only_active: boolean, (optional)
   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)

.. function:: select_more()

   Select those bones connected to the initial selection

.. function:: select_similar(type='LENGTH', threshold=0.1)

   Select similar bones by property types

   :arg type:

      Type

   :type type: enum in ['CHILDREN', 'CHILDREN_IMMEDIATE', 'SIBLINGS', 'LENGTH', 'DIRECTION', 'PREFIX', 'SUFFIX', 'LAYER', 'GROUP', 'SHAPE'], (optional)
   :arg threshold:

      Threshold

   :type threshold: float in [0, 1], (optional)

.. function:: separate()

   Isolate selected bones into a separate armature

.. function:: shortest_path_pick()

   Select shortest path between two bones

.. function:: split()

   Split off selected bones from connected unselected bones

.. function:: subdivide(number_cuts=1)

   Break selected bones into chains of smaller bones

   :arg number_cuts:

      Number of Cuts

   :type number_cuts: int in [1, 1000], (optional)

.. function:: switch_direction()

   Change the direction that a chain of bones points in (head <-> tail swap)

.. function:: symmetrize(direction='NEGATIVE_X')

   Enforce symmetry, make copies of the selection or use existing

   :arg direction:

      Direction, Which sides to copy from and to (when both are selected)

   :type direction: enum in ['NEGATIVE_X', 'POSITIVE_X'], (optional)

