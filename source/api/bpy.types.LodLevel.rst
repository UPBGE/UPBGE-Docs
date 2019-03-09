LodLevel(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: LodLevel(bpy_struct)

   

   .. attribute:: distance

      Distance to begin using this level of detail

      :type: float in [0, inf], default 0.0

   .. attribute:: object

      Object to use for this level of detail

      :type: :class:`Object`

   .. attribute:: object_hysteresis_percentage

      Minimum distance change required to transition to the previous level of detail

      :type: int in [0, 100], default 0

   .. attribute:: use_material

      Use the material from this object at this level of detail

      :type: boolean, default False

   .. attribute:: use_mesh

      Use the mesh from this object at this level of detail

      :type: boolean, default False

   .. attribute:: use_object_hysteresis

      Override LoD Hysteresis scene setting for this LoD level

      :type: boolean, default False

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

   * :class:`Object.lod_levels`

