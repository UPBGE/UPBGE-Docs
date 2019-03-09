MaterialSubsurfaceScattering(bpy_struct)
========================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialSubsurfaceScattering(bpy_struct)

   Diffuse subsurface scattering settings for a Material data-block

   .. attribute:: back

      Back scattering weight

      :type: float in [0, 10], default 0.0

   .. attribute:: color

      Scattering color

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: color_factor

      Blend factor for SSS colors

      :type: float in [0, 1], default 0.0

   .. attribute:: error_threshold

      Error tolerance (low values are slower and higher quality)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: front

      Front scattering weight

      :type: float in [0, 2], default 0.0

   .. attribute:: ior

      Index of refraction (higher values are denser)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: radius

      Mean red/green/blue scattering path length

      :type: float array of 3 items in [0.001, inf], default (0.0, 0.0, 0.0)

   .. attribute:: scale

      Object scale factor

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture_factor

      Texture scattering blend factor

      :type: float in [0, 1], default 0.0

   .. attribute:: use

      Enable diffuse subsurface scattering effects in a material

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

   * :class:`Material.subsurface_scattering`

