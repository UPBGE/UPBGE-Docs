ID(bpy_struct)
==============

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`Action`, :class:`Armature`, :class:`Brush`, :class:`CacheFile`, :class:`Camera`, :class:`Curve`, :class:`FreestyleLineStyle`, :class:`GreasePencil`, :class:`Group`, :class:`Image`, :class:`Key`, :class:`Lamp`, :class:`Lattice`, :class:`Library`, :class:`Mask`, :class:`Material`, :class:`Mesh`, :class:`MetaBall`, :class:`MovieClip`, :class:`NodeTree`, :class:`Object`, :class:`PaintCurve`, :class:`Palette`, :class:`ParticleSettings`, :class:`Scene`, :class:`Screen`, :class:`Sound`, :class:`Speaker`, :class:`Text`, :class:`Texture`, :class:`VectorFont`, :class:`WindowManager`, :class:`World`

.. class:: ID(bpy_struct)

   Base type for data-blocks, defining a unique name, linking from other libraries and garbage collection

   .. data:: is_library_indirect

      Is this ID block linked indirectly

      :type: boolean, default False, (readonly)

   .. data:: is_updated

      Data-block is tagged for recalculation

      :type: boolean, default False, (readonly)

   .. data:: is_updated_data

      Data-block data is tagged for recalculation

      :type: boolean, default False, (readonly)

   .. data:: library

      Library file the data-block is linked from

      :type: :class:`Library`, (readonly)

   .. attribute:: name

      Unique data-block ID name

      :type: string, default "", (never None)

   .. data:: preview

      Preview image and icon of this data-block (None if not supported for this type of data)

      :type: :class:`ImagePreview`, (readonly)

   .. attribute:: tag

      Tools can use this to tag data for their own purposes (initial state is undefined)

      :type: boolean, default False

   .. attribute:: use_fake_user

      Save this data-block even if it has no users

      :type: boolean, default False

   .. data:: users

      Number of times this data-block is referenced

      :type: int in [0, inf], default 0, (readonly)

   .. method:: copy()

      Create a copy of this data-block (not supported for all data-blocks)

      :return:

         New copy of the ID

      :rtype: :class:`ID`

   .. method:: user_clear()

      Clear the user count of a data-block so its not saved, on reload the data will be removed

      This function is for advanced use only, misuse can crash blender since the user
      count is used to prevent data being removed when it is used.

      .. literalinclude:: ..\examples\bpy.types.ID.user_clear.1.py
         :lines: 5-


   .. method:: user_remap(new_id)

      Replace all usage in the .blend file of this ID by new given one

      :arg new_id:

         New ID to use

      :type new_id: :class:`ID`, (never None)

   .. method:: make_local(clear_proxy=True)

      Make this datablock local, return local one (may be a copy of the original, in case it is also indirectly used)

      :arg clear_proxy:

         Whether to clear proxies (the default behavior, note that if object has to be duplicated to be made local, proxies are always cleared)

      :type clear_proxy: boolean, (optional)
      :return:

         This ID, or the new ID if it was copied

      :rtype: :class:`ID`

   .. method:: user_of_id(id)

      Count the number of times that ID uses/references given one

      :arg id:

         ID to count usages

      :type id: :class:`ID`, (never None)
      :return:

         Number of usages/references of given id by current data-block

      :rtype: int in [0, inf]

   .. method:: animation_data_create()

      Create animation data to this ID, note that not all ID types support this

      :return:

         New animation data or NULL

      :rtype: :class:`AnimData`

   .. method:: animation_data_clear()

      Clear animation on this this ID


   .. method:: update_tag(refresh={})

      Tag the ID to update its display data, e.g. when calling :class:`bpy.types.Scene.update`

      :arg refresh:

         Type of updates to perform

      :type refresh: enum set in {'OBJECT', 'DATA', 'TIME'}, (optional)

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

   * :mod:`bpy.context.gpencil_data_owner`
   * :mod:`bpy.context.texture_user`
   * :class:`BlendDataObjects.new`
   * :class:`DopeSheet.source`
   * :class:`DriverTarget.id`
   * :class:`ID.copy`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.user_remap`
   * :class:`Key.user`
   * :class:`KeyingSetPath.id`
   * :class:`KeyingSetPaths.add`
   * :class:`MaskParent.id`
   * :class:`NodeTree.get_from_context`
   * :class:`NodeTree.get_from_context`
   * :class:`Object.data`
   * :class:`PropertyGroupItem.id`
   * :class:`SpaceNodeEditor.id`
   * :class:`SpaceNodeEditor.id_from`
   * :class:`SpaceProperties.pin_id`
   * :class:`UILayout.template_path_builder`
   * :class:`UILayout.template_preview`
   * :class:`UILayout.template_preview`

