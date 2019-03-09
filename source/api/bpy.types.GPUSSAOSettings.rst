GPUSSAOSettings(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPUSSAOSettings(bpy_struct)

   Settings for GPU based screen space ambient occlusion

   .. attribute:: attenuation

      Attenuation constant

      :type: float in [1, 100000], default 0.0

   .. attribute:: color

      Color for screen space ambient occlusion effect

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: distance_max

      Distance of object that contribute to the SSAO effect

      :type: float in [0, 100000], default 0.0

   .. attribute:: factor

      Strength of the SSAO effect

      :type: float in [0, 250], default 0.0

   .. attribute:: samples

      Number of samples

      :type: int in [1, 500], default 0

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

   * :class:`GPUFXSettings.ssao`

