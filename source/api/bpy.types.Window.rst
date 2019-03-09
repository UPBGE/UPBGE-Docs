Window(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Window(bpy_struct)

   Open window

   .. data:: height

      Window height

      :type: int in [0, 32767], default 0, (readonly)

   .. attribute:: screen

      Active screen showing in the window

      :type: :class:`Screen`, (never None)

   .. data:: stereo_3d_display

      Settings for stereo 3d display

      :type: :class:`Stereo3dDisplay`, (readonly, never None)

   .. data:: width

      Window width

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: x

      Horizontal location of the window

      :type: int in [-32768, 32767], default 0, (readonly)

   .. data:: y

      Vertical location of the window

      :type: int in [-32768, 32767], default 0, (readonly)

   .. method:: cursor_warp(x, y)

      Set the cursor position

      :type x: int in [-inf, inf]
      :type y: int in [-inf, inf]

   .. method:: cursor_set(cursor)

      Set the cursor

      :arg cursor:

         cursor

      :type cursor: enum in ['DEFAULT', 'NONE', 'WAIT', 'CROSSHAIR', 'MOVE_X', 'MOVE_Y', 'KNIFE', 'TEXT', 'PAINT_BRUSH', 'HAND', 'SCROLL_X', 'SCROLL_Y', 'SCROLL_XY', 'EYEDROPPER']

   .. method:: cursor_modal_set(cursor)

      Restore the previous cursor after calling ``cursor_modal_set``

      :arg cursor:

         cursor

      :type cursor: enum in ['DEFAULT', 'NONE', 'WAIT', 'CROSSHAIR', 'MOVE_X', 'MOVE_Y', 'KNIFE', 'TEXT', 'PAINT_BRUSH', 'HAND', 'SCROLL_X', 'SCROLL_Y', 'SCROLL_XY', 'EYEDROPPER']

   .. method:: cursor_modal_restore()

      cursor_modal_restore


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

   * :class:`Context.window`
   * :class:`WindowManager.event_timer_add`
   * :class:`WindowManager.windows`

