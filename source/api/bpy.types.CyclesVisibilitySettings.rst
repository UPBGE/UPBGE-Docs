CyclesVisibilitySettings(bpy_struct)
====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesVisibilitySettings(bpy_struct)

   

   .. attribute:: camera

      Object visibility for camera rays

      :type: boolean, default True

   .. attribute:: diffuse

      Object visibility for diffuse reflection rays

      :type: boolean, default True

   .. attribute:: glossy

      Object visibility for glossy reflection rays

      :type: boolean, default True

   .. attribute:: scatter

      Object visibility for volume scatter rays

      :type: boolean, default True

   .. attribute:: shadow

      Object visibility for shadow rays

      :type: boolean, default True

   .. attribute:: transmission

      Object visibility for transmission rays

      :type: boolean, default True

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

