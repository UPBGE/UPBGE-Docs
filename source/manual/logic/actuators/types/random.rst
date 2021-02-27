.. _bpy.types.RandomActuator:

***************
Random Actuator
***************

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_RandomActuator`.

The *Random Actuator* creates a random value which can be stored in a property of the object.

.. figure:: /images/Logic/Actuators/logic-actuators-types-random-random.png

   Random Actuator.


Properties
==========

Seed
   Starting seed for random generator.
Property
   Property where to store the random value.


Distribution
------------

Distributions from which to select the random value. The default entry of *Boolean Constant*
gives either True or False, which is useful for test purposes.

Each distribution has one common property called: *Property*.
This can be either a float, integer, or a boolean depending on the distribution type.

Float Neg. Exp.
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-float_neg_exp.png

      Distribution: Float Neg. Exp.

   Values drop off exponentially with the specified half-life time.

   Half-Life Time
      Half-life time.

Float Normal
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-float_normal.png

      Distribution: Float Normal.

   Random numbers from a normal distribution.

   Mean
      Mean of normal distribution.
   SD
      Standard deviation of normal distribution.

Float Uniform
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-float_uniform.png

      Distribution: Float Uniform.

   Random values selected uniformly between a minimum (*Min*) and maximum (*Max*) values.

Float Constant
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-float_constant.png

      Distribution: Float Constant.

   Returns a constant value specified in the *Value* field.

Int Poisson
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-int_poisson.png

      Distribution: Int Poisson.

   Random numbers from a `Poisson distribution <https://en.wikipedia.org/wiki/Poisson_distribution>`__.
   The mean of the equation is defined by the *Mean* value.

Int Uniform
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-int_uniform.png

      Distribution: Int Uniform.

   Random values selected uniformly between a minimum (*Min*) and maximum (*Max*) values.

Int Constant
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-int_constant.png

      Distribution: Int Constant.

   Returns a constant value specified by the *Value* field.

Bool Bernoulli
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-bool_bernoulli.png

      Distribution: Bool Bernoulli.

   Returns a random distribution using
   the `Bernoulli distribution <https://en.wikipedia.org/wiki/Bernoulli_distribution>`__
   with specified ratio of ``TRUE`` pulses. This ratio is calculated by the *Chance* value.

Bool Uniform
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-bool_uniform.png

      Distribution: Bool Uniform.

   A 50/50 chance of obtaining True/False.

Bool Constant
   .. figure:: /images/Logic/Actuators/logic-actuators-types-random-bool_constant.png

      Distribution: Bool Constant.

   Returns a constant value specified in the *Value* field, must be either ``True`` or ``False``.


Example
=======
