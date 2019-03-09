ShapeKey(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ShapeKey(bpy_struct)

   Shape key in a shape keys data-block

   .. data:: data

      :type: :class:`bpy_prop_collection` of :class:`UnknownType`, (readonly)

   .. data:: frame

      Frame for absolute keys

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: interpolation

      Interpolation type for absolute shape keys

      :type: enum in ['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE'], default 'KEY_LINEAR'

   .. attribute:: mute

      Mute this shape key

      :type: boolean, default False

   .. attribute:: name

      Name of Shape Key

      :type: string, default "", (never None)

   .. attribute:: relative_key

      Shape used as a relative key

      :type: :class:`ShapeKey`, (never None)

   .. attribute:: slider_max

      Maximum for slider

      :type: float in [-10, 10], default 1.0

   .. attribute:: slider_min

      Minimum for slider

      :type: float in [-10, 10], default 0.0

   .. attribute:: value

      Value of shape key at the current frame

      :type: float in [0, 1], default 0.0

   .. attribute:: vertex_group

      Vertex weight group, to blend with basis shape

      :type: string, default "", (never None)

   .. method:: normals_vertex_get()

      Compute local space vertices' normals for this shape key

      :return:

         normals

      :rtype: float in [-1, 1]

   .. method:: normals_polygon_get()

      Compute local space faces' normals for this shape key

      :return:

         normals

      :rtype: float in [-1, 1]

   .. method:: normals_split_get()

      Compute local space face corners' normals for this shape key

      :return:

         normals

      :rtype: float in [-1, 1]

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

   * :class:`ClothSettings.rest_shape_key`
   * :class:`Key.key_blocks`
   * :class:`Key.reference_key`
   * :class:`Object.active_shape_key`
   * :class:`Object.shape_key_add`
   * :class:`Object.shape_key_remove`
   * :class:`ShapeKey.relative_key`

