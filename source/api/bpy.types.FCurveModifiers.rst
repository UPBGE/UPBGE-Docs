FCurveModifiers(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FCurveModifiers(bpy_struct)

   Collection of F-Curve Modifiers

   .. attribute:: active

      Active F-Curve Modifier

      :type: :class:`FModifier`

   .. method:: new(type)

      Add a constraint to this object

      :arg type:

         Constraint type to add

         * ``NULL`` Invalid.
         * ``GENERATOR`` Generator, Generate a curve using a factorized or expanded polynomial.
         * ``FNGENERATOR`` Built-In Function, Generate a curve using standard math functions such as sin and cos.
         * ``ENVELOPE`` Envelope, Reshape F-Curve values - e.g. change amplitude of movements.
         * ``CYCLES`` Cycles, Cyclic extend/repeat keyframe sequence.
         * ``NOISE`` Noise, Add pseudo-random noise on top of F-Curves.
         * ``LIMITS`` Limits, Restrict maximum and minimum values of F-Curve.
         * ``STEPPED`` Stepped Interpolation, Snap values to nearest grid-step - e.g. for a stop-motion look.

      :type type: enum in ['NULL', 'GENERATOR', 'FNGENERATOR', 'ENVELOPE', 'CYCLES', 'NOISE', 'LIMITS', 'STEPPED']
      :return:

         New fmodifier

      :rtype: :class:`FModifier`

   .. method:: remove(modifier)

      Remove a modifier from this F-Curve

      :arg modifier:

         Removed modifier

      :type modifier: :class:`FModifier`, (never None)

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

   * :class:`FCurve.modifiers`

