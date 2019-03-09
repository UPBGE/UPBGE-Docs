OperatorStrokeElement(PropertyGroup)
====================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`PropertyGroup`

.. class:: OperatorStrokeElement(PropertyGroup)

   

   .. attribute:: is_start

      :type: boolean, default False

   .. attribute:: location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: mouse

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: pen_flip

      :type: boolean, default False

   .. attribute:: pressure

      Tablet pressure

      :type: float in [0, 1], default 0.0

   .. attribute:: size

      Brush Size in screen space

      :type: float in [0, inf], default 0.0

   .. attribute:: time

      :type: float in [0, inf], default 0.0

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
   * :class:`PropertyGroup.name`

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

