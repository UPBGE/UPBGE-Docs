GPUDOFSettings(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPUDOFSettings(bpy_struct)

   Settings for GPU based depth of field

   .. attribute:: blades

      Blades for dof effect

      :type: int in [0, 16], default 0

   .. attribute:: focal_length

      Focal length for dof effect

      :type: float in [1, inf], default 0.0

   .. attribute:: focus_distance

      Viewport depth of field focus distance

      :type: float in [0, inf], default 0.0

   .. attribute:: fstop

      F-stop for dof effect

      :type: float in [0, inf], default 0.0

   .. data:: is_hq_supported

      Use high quality depth of field

      :type: boolean, default False, (readonly)

   .. attribute:: sensor

      Size of sensor

      :type: float in [1, inf], default 0.0

   .. attribute:: use_high_quality

      Use high quality depth of field

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

   * :class:`Camera.gpu_dof`
   * :class:`GPUFXSettings.dof`

