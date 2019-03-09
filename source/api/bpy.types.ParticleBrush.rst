ParticleBrush(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleBrush(bpy_struct)

   Particle editing brush

   .. attribute:: count

      Particle count

      :type: int in [1, 1000], default 0

   .. data:: curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: length_mode

      * ``GROW`` Grow, Make hairs longer.
      * ``SHRINK`` Shrink, Make hairs shorter.

      :type: enum in ['GROW', 'SHRINK'], default 'GROW'

   .. attribute:: puff_mode

      * ``ADD`` Add, Make hairs more puffy.
      * ``SUB`` Sub, Make hairs less puffy.

      :type: enum in ['ADD', 'SUB'], default 'ADD'

   .. attribute:: size

      Radius of the brush in pixels

      :type: int in [1, 32767], default 0

   .. attribute:: steps

      Brush steps

      :type: int in [1, 32767], default 0

   .. attribute:: strength

      Brush strength

      :type: float in [0.001, 1], default 0.0

   .. attribute:: use_puff_volume

      Apply puff to unselected end-points (helps maintain hair volume when puffing root)

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

   * :class:`ParticleEdit.brush`

