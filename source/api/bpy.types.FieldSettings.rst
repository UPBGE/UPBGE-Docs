FieldSettings(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FieldSettings(bpy_struct)

   Field settings for an object in physics simulation

   .. attribute:: apply_to_location

      Effect particles' location

      :type: boolean, default False

   .. attribute:: apply_to_rotation

      Effect particles' dynamic rotation

      :type: boolean, default False

   .. attribute:: distance_max

      Maximum distance for the field to work

      :type: float in [0, 1000], default 0.0

   .. attribute:: distance_min

      Minimum distance for the field's fall-off

      :type: float in [0, 1000], default 0.0

   .. attribute:: falloff_power

      :type: float in [0, 10], default 0.0

   .. attribute:: falloff_type

      :type: enum in ['SPHERE', 'TUBE', 'CONE'], default 'SPHERE'

   .. attribute:: flow

      Convert effector force into air flow velocity

      :type: float in [0, 10], default 0.0

   .. attribute:: guide_clump_amount

      Amount of clumping

      :type: float in [-1, 1], default 0.0

   .. attribute:: guide_clump_shape

      Shape of clumping

      :type: float in [-0.999, 0.999], default 0.0

   .. attribute:: guide_free

      Guide-free time from particle life's end

      :type: float in [0, 0.99], default 0.0

   .. attribute:: guide_kink_amplitude

      The amplitude of the offset

      :type: float in [0, 10], default 0.0

   .. attribute:: guide_kink_axis

      Which axis to use for offset

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: guide_kink_frequency

      The frequency of the offset (1/total length)

      :type: float in [0, 10], default 0.0

   .. attribute:: guide_kink_shape

      Adjust the offset to the beginning/end

      :type: float in [-0.999, 0.999], default 0.0

   .. attribute:: guide_kink_type

      Type of periodic offset on the curve

      :type: enum in ['NONE', 'CURL', 'RADIAL', 'WAVE', 'BRAID', 'ROTATION', 'ROLL'], default 'NONE'

   .. attribute:: guide_minimum

      The distance from which particles are affected fully

      :type: float in [0, 1000], default 0.0

   .. attribute:: harmonic_damping

      Damping of the harmonic force

      :type: float in [0, 10], default 0.0

   .. attribute:: inflow

      Inwards component of the vortex force

      :type: float in [-10, 10], default 0.0

   .. attribute:: linear_drag

      Drag component proportional to velocity

      :type: float in [-2, 2], default 0.0

   .. attribute:: noise

      Amount of noise for the force strength

      :type: float in [0, 10], default 0.0

   .. attribute:: quadratic_drag

      Drag component proportional to the square of velocity

      :type: float in [-2, 2], default 0.0

   .. attribute:: radial_falloff

      Radial falloff power (real gravitational falloff = 2)

      :type: float in [0, 10], default 0.0

   .. attribute:: radial_max

      Maximum radial distance for the field to work

      :type: float in [0, 1000], default 0.0

   .. attribute:: radial_min

      Minimum radial distance for the field's fall-off

      :type: float in [0, 1000], default 0.0

   .. attribute:: rest_length

      Rest length of the harmonic force

      :type: float in [0, 1000], default 0.0

   .. attribute:: seed

      Seed of the noise

      :type: int in [1, 128], default 0

   .. attribute:: shape

      Which direction is used to calculate the effector force

      :type: enum in ['POINT', 'PLANE', 'SURFACE', 'POINTS'], default 'POINT'

   .. attribute:: size

      Size of the turbulence

      :type: float in [0, 10], default 0.0

   .. attribute:: source_object

      Select domain object of the smoke simulation

      :type: :class:`Object`

   .. attribute:: strength

      Strength of force field

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture

      Texture to use as force

      :type: :class:`Texture`

   .. attribute:: texture_mode

      How the texture effect is calculated (RGB & Curl need a RGB texture, else Gradient will be used instead)

      :type: enum in ['RGB', 'GRADIENT', 'CURL'], default 'RGB'

   .. attribute:: texture_nabla

      Defines size of derivative offset used for calculating gradient and curl

      :type: float in [0.0001, 1], default 0.0

   .. attribute:: type

      Type of field

      * ``NONE`` None.
      * ``FORCE`` Force, Radial field toward the center of object.
      * ``WIND`` Wind, Constant force along the force object's local Z axis.
      * ``VORTEX`` Vortex, Spiraling force that twists the force object's local Z axis.
      * ``MAGNET`` Magnetic, Forcefield depends on the speed of the particles.
      * ``HARMONIC`` Harmonic, The source of this force field is the zero point of a harmonic oscillator.
      * ``CHARGE`` Charge, Spherical forcefield based on the charge of particles, only influences other charge force fields.
      * ``LENNARDJ`` Lennard-Jones, Forcefield based on the Lennard-Jones potential.
      * ``TEXTURE`` Texture, Forcefield based on a texture.
      * ``GUIDE`` Curve Guide, Create a force along a curve object.
      * ``BOID`` Boid.
      * ``TURBULENCE`` Turbulence, Create turbulence with a noise field.
      * ``DRAG`` Drag, Create a force that dampens motion.
      * ``SMOKE_FLOW`` Smoke Flow, Create a force based on smoke simulation air flow.

      :type: enum in ['NONE', 'FORCE', 'WIND', 'VORTEX', 'MAGNET', 'HARMONIC', 'CHARGE', 'LENNARDJ', 'TEXTURE', 'GUIDE', 'BOID', 'TURBULENCE', 'DRAG', 'SMOKE_FLOW'], default 'NONE'

   .. attribute:: use_2d_force

      Apply force only in 2D

      :type: boolean, default False

   .. attribute:: use_absorption

      Force gets absorbed by collision objects

      :type: boolean, default False

   .. attribute:: use_global_coords

      Use effector/global coordinates for turbulence

      :type: boolean, default False

   .. attribute:: use_gravity_falloff

      Multiply force by 1/distance²

      :type: boolean, default False

   .. attribute:: use_guide_path_add

      Based on distance/falloff it adds a portion of the entire path

      :type: boolean, default False

   .. attribute:: use_guide_path_weight

      Use curve weights to influence the particle influence along the curve

      :type: boolean, default False

   .. attribute:: use_max_distance

      Use a maximum distance for the field to work

      :type: boolean, default False

   .. attribute:: use_min_distance

      Use a minimum distance for the field's fall-off

      :type: boolean, default False

   .. attribute:: use_multiple_springs

      Every point is effected by multiple springs

      :type: boolean, default False

   .. attribute:: use_object_coords

      Use object/global coordinates for texture

      :type: boolean, default False

   .. attribute:: use_radial_max

      Use a maximum radial distance for the field to work

      :type: boolean, default False

   .. attribute:: use_radial_min

      Use a minimum radial distance for the field's fall-off

      :type: boolean, default False

   .. attribute:: use_root_coords

      Texture coordinates from root particle locations

      :type: boolean, default False

   .. attribute:: use_smoke_density

      Adjust force strength based on smoke density

      :type: boolean, default False

   .. attribute:: z_direction

      Effect in full or only positive/negative Z direction

      :type: enum in ['BOTH', 'POSITIVE', 'NEGATIVE'], default 'BOTH'

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

   * :class:`Object.field`
   * :class:`ParticleSettings.force_field_1`
   * :class:`ParticleSettings.force_field_2`

