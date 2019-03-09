MetaElement(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MetaElement(bpy_struct)

   Blobby element in a Metaball data-block

   .. attribute:: co

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: hide

      Hide element

      :type: boolean, default False

   .. attribute:: radius

      :type: float in [0, inf], default 0.0

   .. attribute:: rotation

      Normalized quaternion rotation

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: size_x

      Size of element, use of components depends on element type

      :type: float in [0, 20], default 0.0

   .. attribute:: size_y

      Size of element, use of components depends on element type

      :type: float in [0, 20], default 0.0

   .. attribute:: size_z

      Size of element, use of components depends on element type

      :type: float in [0, 20], default 0.0

   .. attribute:: stiffness

      Stiffness defines how much of the element to fill

      :type: float in [0, 10], default 0.0

   .. attribute:: type

      Metaball types

      :type: enum in ['BALL', 'CAPSULE', 'PLANE', 'ELLIPSOID', 'CUBE'], default 'BALL'

   .. attribute:: use_negative

      Set metaball as negative one

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

   * :class:`MetaBall.elements`
   * :class:`MetaBallElements.active`
   * :class:`MetaBallElements.new`
   * :class:`MetaBallElements.remove`

