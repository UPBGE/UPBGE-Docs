ColorManagedViewSettings(bpy_struct)
====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorManagedViewSettings(bpy_struct)

   Color management settings used for displaying images on the display

   .. data:: curve_mapping

      Color curve mapping applied before display transform

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: exposure

      Exposure (stops) applied before display transform

      :type: float in [-10, 10], default 0.0

   .. attribute:: gamma

      Amount of gamma modification applied after display transform

      :type: float in [0, 5], default 1.0

   .. attribute:: look

      Additional transform applied before view transform for an artistic needs

      * ``NONE`` None, Do not modify image in an artistic manner.

      :type: enum in ['NONE'], default 'NONE'

   .. attribute:: use_curve_mapping

      Use RGB curved for pre-display transformation

      :type: boolean, default False

   .. attribute:: view_transform

      View used when converting image to a display space

      * ``NONE`` None, Do not perform any color transform on display, use old non-color managed technique for display.

      :type: enum in ['NONE'], default 'NONE'

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

   * :class:`ImageFormatSettings.view_settings`
   * :class:`Scene.view_settings`

