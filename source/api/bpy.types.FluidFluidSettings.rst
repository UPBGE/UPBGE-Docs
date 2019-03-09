FluidFluidSettings(FluidSettings)
=================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`FluidSettings`

.. class:: FluidFluidSettings(FluidSettings)

   Fluid simulation settings for the fluid in the simulation

   .. attribute:: initial_velocity

      Initial velocity of fluid

      :type: float array of 3 items in [-1000.1, 1000.1], default (0.0, 0.0, 0.0)

   .. attribute:: use

      Object contributes to the fluid simulation

      :type: boolean, default False

   .. attribute:: use_animated_mesh

      Export this mesh as an animated one (slower and enforces No Slip, only use if really necessary [e.g. armatures or parented objects], animated pos/rot/scale F-Curves do not require it)

      :type: boolean, default False

   .. attribute:: volume_initialization

      Volume initialization type (WARNING: complex volumes might require too much memory and break simulation)

      * ``VOLUME`` Volume, Use only the inner volume of the mesh.
      * ``SHELL`` Shell, Use only the outer shell of the mesh.
      * ``BOTH`` Both, Use both the inner volume and the outer shell of the mesh.

      :type: enum in ['VOLUME', 'SHELL', 'BOTH'], default 'VOLUME'

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
   * :class:`FluidSettings.type`

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

