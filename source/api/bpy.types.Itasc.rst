Itasc(IKParam)
==============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`IKParam`

.. class:: Itasc(IKParam)

   Parameters for the iTaSC IK solver

   .. attribute:: damping_epsilon

      Singular value under which damping is progressively applied (higher values=more stability, less reactivity - default=0.1)

      :type: float in [0, 1], default 0.0

   .. attribute:: damping_max

      Maximum damping coefficient when singular value is nearly 0 (higher values=more stability, less reactivity - default=0.5)

      :type: float in [0, 1], default 0.0

   .. attribute:: feedback

      Feedback coefficient for error correction, average response time is 1/feedback (default=20)

      :type: float in [0, 100], default 0.0

   .. attribute:: iterations

      Maximum number of iterations for convergence in case of reiteration

      :type: int in [0, 1000], default 0

   .. attribute:: mode

      * ``ANIMATION`` Animation, Stateless solver computing pose starting from current action and non-IK constraints.
      * ``SIMULATION`` Simulation, State-full solver running in real-time context and ignoring actions and non-IK constraints.

      :type: enum in ['ANIMATION', 'SIMULATION'], default 'ANIMATION'

   .. attribute:: precision

      Precision of convergence in case of reiteration

      :type: float in [0, 0.1], default 0.0

   .. attribute:: reiteration_method

      Defines if the solver is allowed to reiterate (converge until precision is met) on none, first or all frames

      * ``NEVER`` Never, The solver does not reiterate, not even on first frame (starts from rest pose).
      * ``INITIAL`` Initial, The solver reiterates (converges) on the first frame but not on subsequent frame.
      * ``ALWAYS`` Always, The solver reiterates (converges) on all frames.

      :type: enum in ['NEVER', 'INITIAL', 'ALWAYS'], default 'NEVER'

   .. attribute:: solver

      Solving method selection: automatic damping or manual damping

      * ``SDLS`` SDLS, Selective Damped Least Square.
      * ``DLS`` DLS, Damped Least Square with Numerical Filtering.

      :type: enum in ['SDLS', 'DLS'], default 'SDLS'

   .. attribute:: step_count

      Divide the frame interval into this many steps

      :type: int in [1, 50], default 0

   .. attribute:: step_max

      Higher bound for timestep in second in case of automatic substeps

      :type: float in [0, 1], default 0.0

   .. attribute:: step_min

      Lower bound for timestep in second in case of automatic substeps

      :type: float in [0, 0.1], default 0.0

   .. attribute:: use_auto_step

      Automatically determine the optimal number of steps for best performance/accuracy trade off

      :type: boolean, default False

   .. attribute:: velocity_max

      Maximum joint velocity in rad/s (default=50)

      :type: float in [0, 100], default 0.0

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
   * :class:`IKParam.ik_solver`

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

