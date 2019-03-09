ParticleEdit(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleEdit(bpy_struct)

   Properties of particle editing mode

   .. data:: brush

      :type: :class:`ParticleBrush`, (readonly)

   .. attribute:: default_key_count

      How many keys to make new particles with

      :type: int in [2, 32767], default 0

   .. attribute:: draw_step

      How many steps to draw the path with

      :type: int in [1, 10], default 0

   .. attribute:: emitter_distance

      Distance to keep particles away from the emitter

      :type: float in [0, inf], default 0.0

   .. attribute:: fade_frames

      How many frames to fade

      :type: int in [1, 100], default 0

   .. data:: is_editable

      A valid edit mode exists

      :type: boolean, default False, (readonly)

   .. data:: is_hair

      Editing hair

      :type: boolean, default False, (readonly)

   .. data:: object

      The edited object

      :type: :class:`Object`, (readonly)

   .. attribute:: select_mode

      Particle select and display mode

      * ``PATH`` Path, Path edit mode.
      * ``POINT`` Point, Point select mode.
      * ``TIP`` Tip, Tip select mode.

      :type: enum in ['PATH', 'POINT', 'TIP'], default 'PATH'

   .. attribute:: shape_object

      Outer shape to use for tools

      :type: :class:`Object`

   .. attribute:: show_particles

      Draw actual particles

      :type: boolean, default False

   .. attribute:: tool

      * ``NONE`` None, Don't use any brush.
      * ``COMB`` Comb, Comb hairs.
      * ``SMOOTH`` Smooth, Smooth hairs.
      * ``ADD`` Add, Add hairs.
      * ``LENGTH`` Length, Make hairs longer or shorter.
      * ``PUFF`` Puff, Make hairs stand up.
      * ``CUT`` Cut, Cut hairs.
      * ``WEIGHT`` Weight, Weight hair particles.

      :type: enum in ['NONE', 'COMB', 'SMOOTH', 'ADD', 'LENGTH', 'PUFF', 'CUT', 'WEIGHT'], default 'COMB'

   .. attribute:: type

      :type: enum in ['PARTICLES', 'SOFT_BODY', 'CLOTH'], default 'PARTICLES'

   .. attribute:: use_auto_velocity

      Calculate point velocities automatically

      :type: boolean, default False

   .. attribute:: use_default_interpolate

      Interpolate new particles from the existing ones

      :type: boolean, default False

   .. attribute:: use_emitter_deflect

      Keep paths from intersecting the emitter

      :type: boolean, default False

   .. attribute:: use_fade_time

      Fade paths and keys further away from current frame

      :type: boolean, default False

   .. attribute:: use_preserve_length

      Keep path lengths constant

      :type: boolean, default False

   .. attribute:: use_preserve_root

      Keep root keys unmodified

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

   * :class:`ToolSettings.particle_edit`

