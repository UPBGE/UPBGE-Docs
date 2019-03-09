ArmatureActuator(Actuator)
==========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: ArmatureActuator(Actuator)

   

   .. attribute:: bone

      Bone on which the constraint is defined

      :type: string, default "", (never None)

   .. attribute:: constraint

      Name of the constraint to control

      :type: string, default "", (never None)

   .. attribute:: influence

      Influence of this constraint

      :type: float in [0, 1], default 0.0

   .. attribute:: mode

      :type: enum in ['RUN', 'ENABLE', 'DISABLE', 'SETTARGET', 'SETWEIGHT', 'SETINFLUENCE'], default 'RUN'

   .. attribute:: secondary_target

      Set this object as the secondary target of the constraint (only IK polar target at the moment)

      :type: :class:`Object`

   .. attribute:: target

      Set this object as the target of the constraint

      :type: :class:`Object`

   .. attribute:: weight

      Weight of this constraint

      :type: float in [0, 1], default 0.0

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

