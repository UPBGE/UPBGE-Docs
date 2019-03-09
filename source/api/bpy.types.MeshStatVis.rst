MeshStatVis(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshStatVis(bpy_struct)

   

   .. attribute:: distort_max

      Maximum angle to display

      :type: float in [0, 3.14159], default 0.5

   .. attribute:: distort_min

      Minimum angle to display

      :type: float in [0, 3.14159], default 0.5

   .. attribute:: overhang_axis

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

   .. attribute:: overhang_max

      Maximum angle to display

      :type: float in [0, 3.14159], default 0.5

   .. attribute:: overhang_min

      Minimum angle to display

      :type: float in [0, 3.14159], default 0.5

   .. attribute:: sharp_max

      Maximum angle to display

      :type: float in [-3.14159, 3.14159], default 0.5

   .. attribute:: sharp_min

      Minimum angle to display

      :type: float in [-3.14159, 3.14159], default 0.5

   .. attribute:: thickness_max

      Maximum for measuring thickness

      :type: float in [0, 1000], default 0.5

   .. attribute:: thickness_min

      Minimum for measuring thickness

      :type: float in [0, 1000], default 0.5

   .. attribute:: thickness_samples

      Number of samples to test per face

      :type: int in [1, 32], default 0

   .. attribute:: type

      Type of data to visualize/check

      :type: enum in ['OVERHANG', 'THICKNESS', 'INTERSECT', 'DISTORT', 'SHARP'], default 'OVERHANG'

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

   * :class:`ToolSettings.statvis`

