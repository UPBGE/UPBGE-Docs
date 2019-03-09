SteeringActuator(Actuator)
==========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: SteeringActuator(Actuator)

   

   .. attribute:: acceleration

      Max acceleration

      :type: float in [0, 1000], default 0.0

   .. attribute:: distance

      Relax distance

      :type: float in [0, 1000], default 0.0

   .. attribute:: facing

      Enable automatic facing

      :type: boolean, default False

   .. attribute:: facing_axis

      Axis for automatic facing

      :type: enum in ['X', 'Y', 'Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'X'

   .. attribute:: lock_z_velocity

      Disable simulation of linear motion along Z axis

      :type: boolean, default False

   .. attribute:: mode

      :type: enum in ['SEEK', 'FLEE', 'PATHFOLLOWING'], default 'SEEK'

   .. attribute:: navmesh

      Navigation mesh

      :type: :class:`Object`

   .. attribute:: normal_up

      Use normal of the navmesh to set "UP" vector

      :type: boolean, default False

   .. attribute:: self_terminated

      Terminate when target is reached

      :type: boolean, default False

   .. attribute:: show_visualization

      Enable debug visualization for 'Path following'

      :type: boolean, default False

   .. attribute:: target

      Target object

      :type: :class:`Object`

   .. attribute:: turn_speed

      Max turn speed

      :type: float in [0, 720], default 0.0

   .. attribute:: update_period

      Path update period

      :type: int in [-inf, inf], default 0

   .. attribute:: velocity

      Velocity magnitude

      :type: float in [0, 1000], default 0.0

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

