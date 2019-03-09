MovieTrackingReconstructedCameras(bpy_struct)
=============================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingReconstructedCameras(bpy_struct)

   Collection of solved cameras

   .. method:: find_frame(frame=1)

      Find a reconstructed camera for a give frame number

      :arg frame:

         Frame, Frame number to find camera for

      :type frame: int in [0, 1048574], (optional)
      :return:

         Camera for a given frame

      :rtype: :class:`MovieReconstructedCamera`

   .. method:: matrix_from_frame(frame=1)

      Return interpolated camera matrix for a given frame

      :arg frame:

         Frame, Frame number to find camera for

      :type frame: int in [0, 1048574], (optional)
      :return:

         Matrix, Interpolated camera matrix for a given frame

      :rtype: float multi-dimensional array of 4 * 4 items in [-inf, inf]

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

   * :class:`MovieTrackingReconstruction.cameras`

