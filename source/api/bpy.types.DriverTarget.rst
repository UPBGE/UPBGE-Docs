DriverTarget(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DriverTarget(bpy_struct)

   Source of input values for driver variables

   .. attribute:: bone_target

      Name of PoseBone to use as target

      :type: string, default "", (never None)

   .. attribute:: data_path

      RNA Path (from ID-block) to property used

      :type: string, default "", (never None)

   .. attribute:: id

      ID-block that the specific property used can be found from (id_type property must be set first)

      :type: :class:`ID`

   .. attribute:: id_type

      Type of ID-block that can be used

      :type: enum in ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'GROUP', 'IMAGE', 'KEY', 'LAMP', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD'], default 'OBJECT'

   .. attribute:: transform_space

      Space in which transforms are used

      * ``WORLD_SPACE`` World Space, Transforms include effects of parenting/restpose and constraints.
      * ``TRANSFORM_SPACE`` Transform Space, Transforms don't include parenting/restpose or constraints.
      * ``LOCAL_SPACE`` Local Space, Transforms include effects of constraints but not parenting/restpose.

      :type: enum in ['WORLD_SPACE', 'TRANSFORM_SPACE', 'LOCAL_SPACE'], default 'WORLD_SPACE'

   .. attribute:: transform_type

      Driver variable type

      :type: enum in ['LOC_X', 'LOC_Y', 'LOC_Z', 'ROT_X', 'ROT_Y', 'ROT_Z', 'SCALE_X', 'SCALE_Y', 'SCALE_Z'], default 'LOC_X'

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

   * :class:`DriverVariable.targets`

