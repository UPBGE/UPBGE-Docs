UnitSettings(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UnitSettings(bpy_struct)

   

   .. attribute:: scale_length

      Scale to use when converting between blender units and dimensions

      :type: float in [1e-05, 100000], default 0.0

   .. attribute:: system

      The unit system to use for button display

      :type: enum in ['NONE', 'METRIC', 'IMPERIAL'], default 'NONE'

   .. attribute:: system_rotation

      Unit to use for displaying/editing rotation values

      * ``DEGREES`` Degrees, Use degrees for measuring angles and rotations.
      * ``RADIANS`` Radians.

      :type: enum in ['DEGREES', 'RADIANS'], default 'DEGREES'

   .. attribute:: use_separate

      Display units in pairs (e.g. 1m 0cm)

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

   * :class:`Scene.unit_settings`

