SceneGameRecastData(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SceneGameRecastData(bpy_struct)

   Recast data for a Game data-block

   .. attribute:: agent_height

      Minimum height where the agent can still walk

      :type: float in [-inf, inf], default 2.0

   .. attribute:: agent_radius

      Radius of the agent

      :type: float in [-inf, inf], default 0.6

   .. attribute:: cell_height

      Rasterized cell height

      :type: float in [-inf, inf], default 0.2

   .. attribute:: cell_size

      Rasterized cell size

      :type: float in [-inf, inf], default 0.3

   .. attribute:: climb_max

      Maximum height between grid cells the agent can climb

      :type: float in [-inf, inf], default 0.9

   .. attribute:: edge_max_error

      Maximum distance error from contour to cells

      :type: float in [-inf, inf], default 1.3

   .. attribute:: edge_max_len

      Maximum contour edge length

      :type: float in [-inf, inf], default 12.0

   .. attribute:: partitioning

      Choose partitioning method

      * ``WATERSHED`` Watershed, Classic Recast partitioning method generating the nicest tessellation.
      * ``MONOTONE`` Monotone, Fastest navmesh generation method, may create long thin polygons.
      * ``LAYERS`` Layers, Reasonably fast method that produces better triangles than monotone partitioning.

      :type: enum in ['WATERSHED', 'MONOTONE', 'LAYERS'], default 'WATERSHED'

   .. attribute:: region_merge_size

      Minimum regions size (smaller regions will be merged)

      :type: float in [-inf, inf], default 20.0

   .. attribute:: region_min_size

      Minimum regions size (smaller regions will be deleted)

      :type: float in [-inf, inf], default 8.0

   .. attribute:: sample_dist

      Detail mesh sample spacing

      :type: float in [-inf, inf], default 6.0

   .. attribute:: sample_max_error

      Detail mesh simplification max sample error

      :type: float in [-inf, inf], default 1.0

   .. attribute:: slope_max

      Maximum walkable slope angle

      :type: float in [0, 1.5708], default 0.785398

   .. attribute:: verts_per_poly

      Max number of vertices per polygon

      :type: int in [-inf, inf], default 6

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

   * :class:`SceneGameData.recast_data`

