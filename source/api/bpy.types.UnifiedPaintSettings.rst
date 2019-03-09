UnifiedPaintSettings(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UnifiedPaintSettings(bpy_struct)

   Overrides for some of the active brush's settings

   .. attribute:: color

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: secondary_color

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: size

      Radius of the brush

      :type: int in [1, 5000], default 0

   .. attribute:: strength

      How powerful the effect of the brush is when applied

      :type: float in [0, 10], default 0.5

   .. attribute:: unprojected_radius

      Radius of brush in Blender units

      :type: float in [0.001, inf], default 0.0

   .. attribute:: use_locked_size

      When locked brush stays same size relative to object; when unlocked brush size is given in pixels

      :type: boolean, default False

   .. attribute:: use_pressure_size

      Enable tablet pressure sensitivity for size

      :type: boolean, default False

   .. attribute:: use_pressure_strength

      Enable tablet pressure sensitivity for strength

      :type: boolean, default False

   .. attribute:: use_unified_color

      Instead of per-brush color, the color is shared across brushes

      :type: boolean, default False

   .. attribute:: use_unified_size

      Instead of per-brush radius, the radius is shared across brushes

      :type: boolean, default False

   .. attribute:: use_unified_strength

      Instead of per-brush strength, the strength is shared across brushes

      :type: boolean, default False

   .. attribute:: use_unified_weight

      Instead of per-brush weight, the weight is shared across brushes

      :type: boolean, default False

   .. attribute:: weight

      Weight to assign in vertex groups

      :type: float in [0, 1], default 0.5

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

   * :class:`ToolSettings.unified_paint_settings`

