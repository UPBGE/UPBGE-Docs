RandomActuator(Actuator)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: RandomActuator(Actuator)

   

   .. attribute:: chance

      Pick a number between 0 and 1, success if it's below this value

      :type: float in [0, 1], default 0.0

   .. attribute:: distribution

      Choose the type of distribution

      :type: enum in ['BOOL_CONSTANT', 'BOOL_UNIFORM', 'BOOL_BERNOUILLI', 'INT_CONSTANT', 'INT_UNIFORM', 'INT_POISSON', 'FLOAT_CONSTANT', 'FLOAT_UNIFORM', 'FLOAT_NORMAL', 'FLOAT_NEGATIVE_EXPONENTIAL'], default 'BOOL_CONSTANT'

   .. attribute:: float_max

      Choose a number from a range: upper boundary of the range

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: float_mean

      A normal distribution: mean of the distribution

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: float_min

      Choose a number from a range: lower boundary of the range

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: float_value

      Always return this number

      :type: float in [0, 1], default 0.0

   .. attribute:: half_life_time

      Negative exponential dropoff

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: int_max

      Choose a number from a range: upper boundary of the range

      :type: int in [-1000, 1000], default 0

   .. attribute:: int_mean

      Expected mean value of the distribution

      :type: float in [0.01, 100], default 0.0

   .. attribute:: int_min

      Choose a number from a range: lower boundary of the range

      :type: int in [-1000, 1000], default 0

   .. attribute:: int_value

      Always return this number

      :type: int in [-inf, inf], default 0

   .. attribute:: property

      Assign the random value to this property

      :type: string, default "", (never None)

   .. attribute:: seed

      Initial seed of the random generator, use Python for more freedom (choose 0 for not random)

      :type: int in [0, 1048574], default 0

   .. attribute:: standard_derivation

      A normal distribution: standard deviation of the distribution

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: use_always_true

      Always false or always true

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
   * :class:`Actuator.name`
   * :class:`Actuator.type`
   * :class:`Actuator.pin`
   * :class:`Actuator.show_expanded`
   * :class:`Actuator.active`

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
   * :class:`Actuator.link`
   * :class:`Actuator.unlink`

