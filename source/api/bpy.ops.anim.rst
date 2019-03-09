Anim Operators
==============

.. module:: bpy.ops.anim

.. function:: change_frame(frame=0.0, snap=False)

   Interactively change the current frame number

   :arg frame:

      Frame

   :type frame: float in [-1.04857e+06, 1.04857e+06], (optional)
   :arg snap:

      Snap

   :type snap: boolean, (optional)

.. function:: channel_select_keys(extend=False)

   Select all keyframes of channel under mouse

   :arg extend:

      Extend, Extend selection

   :type extend: boolean, (optional)

.. function:: channels_clean_empty()

   Delete all empty animation data containers from visible data-blocks

.. function:: channels_click(extend=False, children_only=False)

   Handle mouse-clicks over animation channels

   :arg extend:

      Extend Select

   :type extend: boolean, (optional)
   :arg children_only:

      Select Children Only

   :type children_only: boolean, (optional)

.. function:: channels_collapse(all=True)

   Collapse (i.e. close) all selected expandable animation channels

   :arg all:

      All, Collapse all channels (not just selected ones)

   :type all: boolean, (optional)

.. function:: channels_delete()

   Delete all selected animation channels

.. function:: channels_editable_toggle(mode='TOGGLE', type='PROTECT')

   Toggle editability of selected channels

   :arg mode:

      Mode

   :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
   :arg type:

      Type

   :type type: enum in ['PROTECT', 'MUTE'], (optional)

.. function:: channels_expand(all=True)

   Expand (i.e. open) all selected expandable animation channels

   :arg all:

      All, Expand all channels (not just selected ones)

   :type all: boolean, (optional)

.. function:: channels_fcurves_enable()

   Clears 'disabled' tag from all F-Curves to get broken F-Curves working again

.. function:: channels_find(query="Query")

   Filter the set of channels shown to only include those with matching names

   :arg query:

      Text to search for in channel names

   :type query: string, (optional, never None)

.. function:: channels_group(name="New Group")

   Add selected F-Curves to a new group

   :arg name:

      Name, Name of newly created group

   :type name: string, (optional, never None)

.. function:: channels_move(direction='DOWN')

   Rearrange selected animation channels

   :arg direction:

      Direction

   :type direction: enum in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)

.. function:: channels_rename()

   Rename animation channel under mouse

.. function:: channels_select_all_toggle(invert=False)

   Toggle selection of all animation channels

   :arg invert:

      Invert

   :type invert: boolean, (optional)

.. function:: channels_select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select all animation channels within the specified region

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

.. function:: channels_setting_disable(mode='DISABLE', type='PROTECT')

   Disable specified setting on all selected animation channels

   :arg mode:

      Mode

   :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
   :arg type:

      Type

   :type type: enum in ['PROTECT', 'MUTE'], (optional)

.. function:: channels_setting_enable(mode='ENABLE', type='PROTECT')

   Enable specified setting on all selected animation channels

   :arg mode:

      Mode

   :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
   :arg type:

      Type

   :type type: enum in ['PROTECT', 'MUTE'], (optional)

.. function:: channels_setting_toggle(mode='TOGGLE', type='PROTECT')

   Toggle specified setting on all selected animation channels

   :arg mode:

      Mode

   :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
   :arg type:

      Type

   :type type: enum in ['PROTECT', 'MUTE'], (optional)

.. function:: channels_ungroup()

   Remove selected F-Curves from their current groups

.. function:: clear_useless_actions(only_unused=True)

   Mark actions with no F-Curves for deletion after save & reload of file preserving "action libraries"

   :arg only_unused:

      Only Unused, Only unused (Fake User only) actions get considered

   :type only_unused: boolean, (optional)

   :file: `startup\bl_operators\anim.py\:314 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\anim.py$314>`_

.. function:: copy_driver_button()

   Copy the driver for the highlighted button

.. function:: driver_button_add(mapping_type='SINGLE_MANY')

   Add driver(s) for the property(s) represented by the highlighted button

   :arg mapping_type:

      Mapping Type, Method used to match target and driven properties

      * ``SINGLE_MANY`` All from Target, Drive all components of this property using the target picked.
      * ``DIRECT`` Single from Target, Drive this component of this property using the target picked.
      * ``MATCH`` Match Indices, Create drivers for each pair of corresponding elements.
      * ``NONE_ALL`` Manually Create Later, Create drivers for all properties without assigning any targets yet.
      * ``NONE_SINGLE`` Manually Create Later (Single), Create driver for this property only and without assigning any targets yet.

   :type mapping_type: enum in ['SINGLE_MANY', 'DIRECT', 'MATCH', 'NONE_ALL', 'NONE_SINGLE'], (optional)

.. function:: driver_button_remove(all=True)

   Remove the driver(s) for the property(s) connected represented by the highlighted button

   :arg all:

      All, Delete drivers for all elements of the array

   :type all: boolean, (optional)

.. function:: keyframe_clear_button(all=True)

   Clear all keyframes on the currently active property

   :arg all:

      All, Clear keyframes from all elements of the array

   :type all: boolean, (optional)

.. function:: keyframe_clear_v3d()

   Remove all keyframe animation for selected objects

.. function:: keyframe_delete(type='DEFAULT', confirm_success=True)

   Delete keyframes on the current frame for all properties in the specified Keying Set

   :arg type:

      Keying Set, The Keying Set to use

   :type type: enum in ['DEFAULT'], (optional)
   :arg confirm_success:

      Confirm Successful Delete, Show a popup when the keyframes get successfully removed

   :type confirm_success: boolean, (optional)

.. function:: keyframe_delete_button(all=True)

   Delete current keyframe of current UI-active property

   :arg all:

      All, Delete keyframes from all elements of the array

   :type all: boolean, (optional)

.. function:: keyframe_delete_v3d()

   Remove keyframes on current frame for selected objects and bones

.. function:: keyframe_insert(type='DEFAULT', confirm_success=True)

   Insert keyframes on the current frame for all properties in the specified Keying Set

   :arg type:

      Keying Set, The Keying Set to use

   :type type: enum in ['DEFAULT'], (optional)
   :arg confirm_success:

      Confirm Successful Insert, Show a popup when the keyframes get successfully added

   :type confirm_success: boolean, (optional)

.. function:: keyframe_insert_button(all=True)

   Insert a keyframe for current UI-active property

   :arg all:

      All, Insert a keyframe for all element of the array

   :type all: boolean, (optional)

.. function:: keyframe_insert_menu(type='DEFAULT', confirm_success=False, always_prompt=False)

   Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined

   :arg type:

      Keying Set, The Keying Set to use

   :type type: enum in ['DEFAULT'], (optional)
   :arg confirm_success:

      Confirm Successful Insert, Show a popup when the keyframes get successfully added

   :type confirm_success: boolean, (optional)
   :arg always_prompt:

      Always Show Menu

   :type always_prompt: boolean, (optional)

.. function:: keying_set_active_set(type='DEFAULT')

   Select a new keying set as the active one

   :arg type:

      Keying Set, The Keying Set to use

   :type type: enum in ['DEFAULT'], (optional)

.. function:: keying_set_add()

   Add a new (empty) Keying Set to the active Scene

.. function:: keying_set_export(filepath="", filter_folder=True, filter_text=True, filter_python=True)

   Export Keying Set to a python script

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_text:

      Filter text

   :type filter_text: boolean, (optional)
   :arg filter_python:

      Filter python

   :type filter_python: boolean, (optional)

   :file: `startup\bl_operators\anim.py\:62 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\anim.py$62>`_

.. function:: keying_set_path_add()

   Add empty path to active Keying Set

.. function:: keying_set_path_remove()

   Remove active Path from active Keying Set

.. function:: keying_set_remove()

   Remove the active Keying Set

.. function:: keyingset_button_add(all=True)

   Add current UI-active property to current keying set

   :arg all:

      All, Add all elements of the array to a Keying Set

   :type all: boolean, (optional)

.. function:: keyingset_button_remove()

   Remove current UI-active property from current keying set

.. function:: paste_driver_button()

   Paste the driver in the copy/paste buffer for the highlighted button

.. function:: previewrange_clear()

   Clear Preview Range

.. function:: previewrange_set(xmin=0, xmax=0, ymin=0, ymax=0)

   Interactively define frame range used for playback

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

.. function:: update_animated_transform_constraints(use_convert_to_radians=True)

   Update fcurves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)

   :arg use_convert_to_radians:

      Convert To Radians, Convert fcurves/drivers affecting rotations to radians (Warning: use this only once!)

   :type use_convert_to_radians: boolean, (optional)

   :file: `startup\bl_operators\anim.py\:347 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\anim.py$347>`_

