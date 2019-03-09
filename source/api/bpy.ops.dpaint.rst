Dpaint Operators
================

.. module:: bpy.ops.dpaint

.. function:: bake()

   Bake dynamic paint image sequence surface

.. function:: output_toggle(output='A')

   Add or remove Dynamic Paint output data layer

   :arg output:

      Output Toggle

   :type output: enum in ['A', 'B'], (optional)

.. function:: surface_slot_add()

   Add a new Dynamic Paint surface slot

.. function:: surface_slot_remove()

   Remove the selected surface slot

.. function:: type_toggle(type='CANVAS')

   Toggle whether given type is active or not

   :arg type:

      Type

   :type type: enum in ['CANVAS', 'BRUSH'], (optional)

