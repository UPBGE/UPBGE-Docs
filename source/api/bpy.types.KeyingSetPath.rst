KeyingSetPath(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyingSetPath(bpy_struct)

   Path to a setting for use in a Keying Set

   .. attribute:: array_index

      Index to the specific setting if applicable

      :type: int in [-inf, inf], default 0

   .. attribute:: data_path

      Path to property setting

      :type: string, default "", (never None)

   .. attribute:: group

      Name of Action Group to assign setting(s) for this path to

      :type: string, default "", (never None)

   .. attribute:: group_method

      Method used to define which Group-name to use

      :type: enum in ['NAMED', 'NONE', 'KEYINGSET'], default 'NAMED'

   .. attribute:: id

      ID-Block that keyframes for Keying Set should be added to (for Absolute Keying Sets only)

      :type: :class:`ID`

   .. attribute:: id_type

      Type of ID-block that can be used

      :type: enum in ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'GROUP', 'IMAGE', 'KEY', 'LAMP', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD'], default 'OBJECT'

   .. attribute:: use_entire_array

      When an 'array/vector' type is chosen (Location, Rotation, Color, etc.), entire array is to be used

      :type: boolean, default False

   .. attribute:: use_insertkey_needed

      Only insert keyframes where they're needed in the relevant F-Curves

      :type: boolean, default False

   .. attribute:: use_insertkey_override_needed

      Override default setting to only insert keyframes where they're needed in the relevant F-Curves

      :type: boolean, default False

   .. attribute:: use_insertkey_override_visual

      Override default setting to insert keyframes based on 'visual transforms'

      :type: boolean, default False

   .. attribute:: use_insertkey_override_xyz_to_rgb

      Override default setting to set color for newly added transformation F-Curves (Location, Rotation, Scale) to be based on the transform axis

      :type: boolean, default False

   .. attribute:: use_insertkey_visual

      Insert keyframes based on 'visual transforms'

      :type: boolean, default False

   .. attribute:: use_insertkey_xyz_to_rgb

      Color for newly added transformation F-Curves (Location, Rotation, Scale) is based on the transform axis

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

   * :class:`KeyingSet.paths`
   * :class:`KeyingSetPaths.active`
   * :class:`KeyingSetPaths.add`
   * :class:`KeyingSetPaths.remove`

