ColorManagedSequencerColorspaceSettings(bpy_struct)
===================================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorManagedSequencerColorspaceSettings(bpy_struct)

   Input color space settings

   .. attribute:: name

      Color space that the sequencer operates in

      * ``Filmic Log`` Filmic Log, Log based filmic shaper with 16.5 stops of latitude, and 25 stops of dynamic range.
      * ``Linear`` Linear, Rec. 709 (Full Range), Blender native linear space.
      * ``Linear ACES`` Linear ACES, ACES linear space.
      * ``Non-Color`` Non-Color, Color space used for images which contains non-color data (i,e, normal maps).
      * ``Raw`` Raw.
      * ``sRGB`` sRGB, Standard RGB Display Space.
      * ``VD16`` VD16, The simple video conversion from a gamma 2.2 sRGB space.
      * ``XYZ`` XYZ.

      :type: enum in ['Filmic Log', 'Linear', 'Linear ACES', 'Non-Color', 'Raw', 'sRGB', 'VD16', 'XYZ'], default 'NONE'

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

   * :class:`Scene.sequencer_colorspace_settings`

