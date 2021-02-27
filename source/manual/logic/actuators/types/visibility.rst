.. _bpy.types.VisibilityActuator:

*******************
Visibility Actuator
*******************

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_VisibilityActuator`.

The *Visibility Actuator* allows the user to change the visibility of objects during run-time.

.. note::

   Using the visibility actuator will save on Rasterizer usage, however, not Physics,
   and so is limited in terms of Level of Detail (LOD). For LOD look at replace mesh,
   but be aware that the logic required can negate the effect of the LOD.

.. figure:: /images/Logic/Actuators/logic-actuators-types-visibility-visibility.png

   Visibility Actuator.


Properties
==========

Visible
   Toggle checkbox to toggle visibility.
Occlusion
   Toggle checkbox to toggle occlusion. Must be initialized from the *Physics* tab.
Children
   Toggle checkbox to toggle recursive setting -- will set visibility / occlusion state
   to all child objects, children of children (recursively).


Example
=======
