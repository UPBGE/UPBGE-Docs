View2D(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: View2D(bpy_struct)

   Scroll and zoom for a 2D region

   .. method:: region_to_view(x, y)

      Transform region coordinates to 2D view

      :arg x:

         x, Region x coordinate

      :type x: int in [-inf, inf]
      :arg y:

         y, Region y coordinate

      :type y: int in [-inf, inf]
      :return:

         Result, View coordinates

      :rtype: float array of 2 items in [-inf, inf]

   .. method:: view_to_region(x, y, clip=True)

      Transform 2D view coordinates to region

      :arg x:

         x, 2D View x coordinate

      :type x: float in [-inf, inf]
      :arg y:

         y, 2D View y coordinate

      :type y: float in [-inf, inf]
      :arg clip:

         Clip, Clip coordinates to the visible region

      :type clip: boolean, (optional)
      :return:

         Result, Region coordinates

      :rtype: int array of 2 items in [-inf, inf]

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

   * :class:`Region.view2d`

