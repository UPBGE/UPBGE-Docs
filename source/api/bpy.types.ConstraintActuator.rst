ConstraintActuator(Actuator)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: ConstraintActuator(Actuator)

   Actuator to handle Constraints

   .. attribute:: angle_max

      Maximum angle allowed with target direction (no correction is done if angle with target direction is between min and max)

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: angle_min

      Minimum angle to maintain with target direction (no correction is done if angle with target direction is between min and max)

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: damping

      Damping factor: time constant (in frame) of low pass filter

      :type: int in [-32768, 32767], default 0

   .. attribute:: damping_rotation

      Use a different damping for orientation

      :type: int in [-32768, 32767], default 0

   .. attribute:: direction

      Direction of the ray

      :type: enum in ['NONE', 'DIRPX', 'DIRPY', 'DIRPZ', 'DIRNX', 'DIRNY', 'DIRNZ'], default 'NONE'

   .. attribute:: direction_axis

      Select the axis to be aligned along the reference direction

      :type: enum in ['NONE', 'DIRPX', 'DIRPY', 'DIRPZ', 'DIRNX', 'DIRNY', 'DIRNZ'], default 'NONE'

   .. attribute:: direction_axis_pos

      Select the axis to be aligned along the reference direction

      :type: enum in ['NONE', 'DIRPX', 'DIRPY', 'DIRPZ'], default 'NONE'

   .. attribute:: distance

      Keep this distance to target

      :type: float in [-inf, inf], default 0.0

   .. attribute:: fh_damping

      Damping factor of the force field spring

      :type: float in [-inf, inf], default 0.0

   .. attribute:: fh_force

      Spring force within the force field area

      :type: float in [-inf, inf], default 0.0

   .. attribute:: fh_height

      Height of the force field area

      :type: float in [-inf, inf], default 0.0

   .. attribute:: limit

      :type: enum in ['NONE', 'LOCX', 'LOCY', 'LOCZ'], default 'NONE'

   .. attribute:: limit_max

      :type: float in [-inf, inf], default 0.0

   .. attribute:: limit_min

      :type: float in [-inf, inf], default 0.0

   .. attribute:: material

      Ray detects only Objects with this material

      :type: string, default "", (never None)

   .. attribute:: mode

      The type of the constraint

      :type: enum in ['LOC', 'DIST', 'ORI', 'FH'], default 'LOC'

   .. attribute:: property

      Ray detects only Objects with this property

      :type: string, default "", (never None)

   .. attribute:: range

      Maximum length of ray

      :type: float in [-inf, inf], default 0.0

   .. attribute:: rotation_max

      Reference Direction

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: time

      Maximum activation time in frame, 0 for unlimited

      :type: int in [-32768, 32767], default 0

   .. attribute:: use_fh_normal

      Add a horizontal spring force on slopes

      :type: boolean, default False

   .. attribute:: use_fh_paralel_axis

      Keep object axis parallel to normal

      :type: boolean, default False

   .. attribute:: use_force_distance

      Force distance of object to point of impact of ray

      :type: boolean, default False

   .. attribute:: use_local

      Set ray along object's axis or global axis

      :type: boolean, default False

   .. attribute:: use_material_detect

      Detect material instead of property

      :type: boolean, default False

   .. attribute:: use_normal

      Set object axis along (local axis) or parallel (global axis) to the normal at hit position

      :type: boolean, default False

   .. attribute:: use_persistent

      Persistent actuator: stays active even if ray does not reach target

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

