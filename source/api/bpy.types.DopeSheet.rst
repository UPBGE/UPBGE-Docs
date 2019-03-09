DopeSheet(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DopeSheet(bpy_struct)

   Settings for filtering the channels shown in animation editors

   .. attribute:: filter_fcurve_name

      F-Curve live filtering string

      :type: string, default "", (never None)

   .. attribute:: filter_group

      Group that included object should be a member of

      :type: :class:`Group`

   .. attribute:: filter_text

      Live filtering string

      :type: string, default "", (never None)

   .. attribute:: show_armatures

      Include visualization of armature related animation data

      :type: boolean, default False

   .. attribute:: show_cameras

      Include visualization of camera related animation data

      :type: boolean, default False

   .. attribute:: show_curves

      Include visualization of curve related animation data

      :type: boolean, default False

   .. attribute:: show_datablock_filters

      Show options for whether channels related to certain types of data are included

      :type: boolean, default False

   .. attribute:: show_expanded_summary

      Collapse summary when shown, so all other channels get hidden (Dope Sheet editors only)

      :type: boolean, default False

   .. attribute:: show_gpencil

      Include visualization of Grease Pencil related animation data and frames

      :type: boolean, default False

   .. attribute:: show_gpencil_3d_only

      Only show Grease Pencil data-blocks used as part of the active scene

      :type: boolean, default False

   .. attribute:: show_hidden

      Include channels from objects/bone that are not visible

      :type: boolean, default False

   .. attribute:: show_lamps

      Include visualization of lamp related animation data

      :type: boolean, default False

   .. attribute:: show_lattices

      Include visualization of lattice related animation data

      :type: boolean, default False

   .. attribute:: show_linestyles

      Include visualization of Line Style related Animation data

      :type: boolean, default False

   .. attribute:: show_materials

      Include visualization of material related animation data

      :type: boolean, default False

   .. attribute:: show_meshes

      Include visualization of mesh related animation data

      :type: boolean, default False

   .. attribute:: show_metaballs

      Include visualization of metaball related animation data

      :type: boolean, default False

   .. attribute:: show_missing_nla

      Include animation data-blocks with no NLA data (NLA editor only)

      :type: boolean, default False

   .. attribute:: show_modifiers

      Include visualization of animation data related to data-blocks linked to modifiers

      :type: boolean, default False

   .. attribute:: show_nodes

      Include visualization of node related animation data

      :type: boolean, default False

   .. attribute:: show_only_errors

      Only include F-Curves and drivers that are disabled or have errors

      :type: boolean, default False

   .. attribute:: show_only_group_objects

      Only include channels from objects in the specified group

      :type: boolean, default False

   .. attribute:: show_only_matching_fcurves

      Only include F-Curves with names containing search text

      :type: boolean, default False

   .. attribute:: show_only_selected

      Only include channels relating to selected objects and data

      :type: boolean, default False

   .. attribute:: show_particles

      Include visualization of particle related animation data

      :type: boolean, default False

   .. attribute:: show_scenes

      Include visualization of scene related animation data

      :type: boolean, default False

   .. attribute:: show_shapekeys

      Include visualization of shape key related animation data

      :type: boolean, default False

   .. attribute:: show_speakers

      Include visualization of speaker related animation data

      :type: boolean, default False

   .. attribute:: show_summary

      Display an additional 'summary' line (Dope Sheet editors only)

      :type: boolean, default False

   .. attribute:: show_textures

      Include visualization of texture related animation data

      :type: boolean, default False

   .. attribute:: show_transforms

      Include visualization of object-level animation data (mostly transforms)

      :type: boolean, default False

   .. attribute:: show_worlds

      Include visualization of world related animation data

      :type: boolean, default False

   .. data:: source

      ID-Block representing source data, usually ID_SCE (i.e. Scene)

      :type: :class:`ID`, (readonly)

   .. attribute:: use_datablock_sort

      Alphabetically sorts data-blocks - mainly objects in the scene (disable to increase viewport speed)

      :type: boolean, default False

   .. attribute:: use_filter_text

      Only include channels with names containing search text

      :type: boolean, default False

   .. attribute:: use_multi_word_filter

      Perform fuzzy/multi-word matching (WARNING: May be slow)

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

   * :class:`SpaceDopeSheetEditor.dopesheet`
   * :class:`SpaceGraphEditor.dopesheet`
   * :class:`SpaceNLA.dopesheet`

