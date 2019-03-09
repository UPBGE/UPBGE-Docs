MaskLayers(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaskLayers(bpy_struct)

   Collection of layers used by mask

   .. attribute:: active

      Active layer in this mask

      :type: :class:`MaskLayer`

   .. method:: new(name="")

      Add layer to this mask

      :arg name:

         Name, Name of new layer

      :type name: string, (optional, never None)
      :return:

         New mask layer

      :rtype: :class:`MaskLayer`

   .. method:: remove(layer)

      Remove layer from this mask

      :arg layer:

         Shape to be removed

      :type layer: :class:`MaskLayer`, (never None)

   .. method:: clear()

      Remove all mask layers


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

   * :class:`Mask.layers`

