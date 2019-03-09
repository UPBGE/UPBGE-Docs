AnimData(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimData(bpy_struct)

   Animation data for data-block

   .. attribute:: action

      Active Action for this data-block

      :type: :class:`Action`

   .. attribute:: action_blend_type

      Method used for combining Active Action's result with result of NLA stack

      * ``REPLACE`` Replace, Result strip replaces the accumulated results by amount specified by influence.
      * ``ADD`` Add, Weighted result of strip is added to the accumulated results.
      * ``SUBTRACT`` Subtract, Weighted result of strip is removed from the accumulated results.
      * ``MULTIPLY`` Multiply, Weighted result of strip is multiplied with the accumulated results.

      :type: enum in ['REPLACE', 'ADD', 'SUBTRACT', 'MULTIPLY'], default 'REPLACE'

   .. attribute:: action_extrapolation

      Action to take for gaps past the Active Action's range (when evaluating with NLA)

      * ``NOTHING`` Nothing, Strip has no influence past its extents.
      * ``HOLD`` Hold, Hold the first frame if no previous strips in track, and always hold last frame.
      * ``HOLD_FORWARD`` Hold Forward, Only hold last frame.

      :type: enum in ['NOTHING', 'HOLD', 'HOLD_FORWARD'], default 'HOLD'

   .. attribute:: action_influence

      Amount the Active Action contributes to the result of the NLA stack

      :type: float in [0, 1], default 1.0

   .. data:: drivers

      The Drivers/Expressions for this data-block

      :type: :class:`AnimDataDrivers` :class:`bpy_prop_collection` of :class:`FCurve`, (readonly)

   .. data:: nla_tracks

      NLA Tracks (i.e. Animation Layers)

      :type: :class:`NlaTracks` :class:`bpy_prop_collection` of :class:`NlaTrack`, (readonly)

   .. attribute:: use_nla

      NLA stack is evaluated when evaluating this block

      :type: boolean, default False

   .. attribute:: use_tweak_mode

      Whether to enable or disable tweak mode in NLA

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

   * :class:`Armature.animation_data`
   * :class:`CacheFile.animation_data`
   * :class:`Camera.animation_data`
   * :class:`Curve.animation_data`
   * :class:`FreestyleLineStyle.animation_data`
   * :class:`GreasePencil.animation_data`
   * :class:`ID.animation_data_create`
   * :class:`Key.animation_data`
   * :class:`Lamp.animation_data`
   * :class:`Lattice.animation_data`
   * :class:`Mask.animation_data`
   * :class:`Material.animation_data`
   * :class:`Mesh.animation_data`
   * :class:`MetaBall.animation_data`
   * :class:`MovieClip.animation_data`
   * :class:`NodeTree.animation_data`
   * :class:`Object.animation_data`
   * :class:`ParticleSettings.animation_data`
   * :class:`Scene.animation_data`
   * :class:`Speaker.animation_data`
   * :class:`Texture.animation_data`
   * :class:`World.animation_data`

