EditObjectActuator(Actuator)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: EditObjectActuator(Actuator)

   Actuator used to edit objects

   .. attribute:: angular_velocity

      Angular velocity upon creation

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: dynamic_operation

      :type: enum in ['RESTOREDYN', 'SUSPENDDYN', 'ENABLERIGIDBODY', 'DISABLERIGIDBODY', 'SETMASS', 'RESTOREPHY', 'SUSPENDPHY'], default 'RESTOREDYN'

   .. attribute:: linear_velocity

      Velocity upon creation

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: mass

      The mass of the object

      :type: float in [-inf, inf], default 0.0

   .. attribute:: mesh

      Replace the existing, when left blank 'Phys' will remake the existing physics mesh

      :type: :class:`Mesh`

   .. attribute:: mode

      The mode of the actuator

      :type: enum in ['ADDOBJECT', 'ENDOBJECT', 'REPLACEMESH', 'TRACKTO', 'DYNAMICS'], default 'ADDOBJECT'

   .. attribute:: object

      Add this Object and all its children (can't be on a visible layer)

      :type: :class:`Object`

   .. attribute:: time

      Duration the new Object lives or the track takes

      :type: float in [-inf, inf], default 0.0

   .. attribute:: track_axis

      The axis that points to the target object

      :type: enum in ['TRACKAXISX', 'TRACKAXISY', 'TRACKAXISZ', 'TRACKAXISNEGX', 'TRACKAXISNEGY', 'TRACKAXISNEGZ'], default 'TRACKAXISX'

   .. attribute:: track_object

      Track to this Object

      :type: :class:`Object`

   .. attribute:: up_axis

      The axis that points upward

      :type: enum in ['UPAXISX', 'UPAXISY', 'UPAXISZ'], default 'UPAXISX'

   .. attribute:: use_3d_tracking

      Enable 3D tracking

      :type: boolean, default False

   .. attribute:: use_local_angular_velocity

      Apply the rotation locally

      :type: boolean, default False

   .. attribute:: use_local_linear_velocity

      Apply the transformation locally

      :type: boolean, default False

   .. attribute:: use_replace_display_mesh

      Replace the display mesh

      :type: boolean, default False

   .. attribute:: use_replace_physics_mesh

      Replace the physics mesh (triangle bounds only - compound shapes not supported)

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

