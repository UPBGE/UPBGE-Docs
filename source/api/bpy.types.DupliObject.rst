DupliObject(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DupliObject(bpy_struct)

   An object duplicate

   .. data:: hide

      Don't show dupli object in viewport or render

      :type: boolean, default False, (readonly)

   .. data:: index

      Index in the lowest-level dupli list

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: matrix

      Object duplicate transformation matrix

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. data:: object

      Object being duplicated

      :type: :class:`Object`, (readonly)

   .. data:: orco

      Generated coordinates in parent object space

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: particle_system

      Particle system that this dupli object was instanced from

      :type: :class:`ParticleSystem`, (readonly)

   .. data:: persistent_id

      Persistent identifier for inter-frame matching of objects with motion blur

      :type: int array of 16 items in [-inf, inf], default (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (readonly)

   .. data:: random_id

      Random id for this dupli object

      :type: int in [0, inf], default 0, (readonly)

   .. data:: type

      Duplicator type that generated this dupli object

      * ``NONE`` None.
      * ``FRAMES`` Frames, Make copy of object for every frame.
      * ``VERTS`` Verts, Duplicate child objects on all vertices.
      * ``FACES`` Faces, Duplicate child objects on all faces.
      * ``GROUP`` Group, Enable group instancing.

      :type: enum in ['NONE', 'FRAMES', 'VERTS', 'FACES', 'GROUP'], default 'NONE', (readonly)

   .. data:: uv

      UV coordinates in parent object space

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0), (readonly)

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

   * :class:`Object.dupli_list`

