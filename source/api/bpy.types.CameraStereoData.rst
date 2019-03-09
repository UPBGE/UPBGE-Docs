CameraStereoData(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CameraStereoData(bpy_struct)

   Stereoscopy settings for a Camera data-block

   .. attribute:: convergence_distance

      The converge point for the stereo cameras (often the distance between a projector and the projection screen)

      :type: float in [1e-05, inf], default 0.0

   .. attribute:: convergence_mode

      * ``OFFAXIS`` Off-Axis, Off-axis frustums converging in a plane.
      * ``PARALLEL`` Parallel, Parallel cameras with no convergence.
      * ``TOE`` Toe-in, Rotated cameras, looking at the convergence distance.

      :type: enum in ['OFFAXIS', 'PARALLEL', 'TOE'], default 'OFFAXIS'

   .. attribute:: interocular_distance

      Set the distance between the eyes - the stereo plane distance / 30 should be fine

      :type: float in [0, inf], default 0.0

   .. attribute:: pivot

      :type: enum in ['LEFT', 'RIGHT', 'CENTER'], default 'LEFT'

   .. attribute:: pole_merge_angle_from

      Angle at which interocular distance starts to fade to 0

      :type: float in [0, 1.5708], default 0.0

   .. attribute:: pole_merge_angle_to

      Angle at which interocular distance is 0

      :type: float in [0, 1.5708], default 0.0

   .. attribute:: use_pole_merge

      Fade interocular distance to 0 after the given cutoff angle

      :type: boolean, default False

   .. attribute:: use_spherical_stereo

      Render every pixel rotating the camera around the middle of the interocular distance

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

   * :class:`Camera.stereo`

