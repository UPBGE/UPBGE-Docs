BlendData(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendData(bpy_struct)

   Main data structure representing a .blend file and all its data-blocks

   .. data:: actions

      Action data-blocks

      :type: :class:`BlendDataActions` :class:`bpy_prop_collection` of :class:`Action`, (readonly)

   .. data:: armatures

      Armature data-blocks

      :type: :class:`BlendDataArmatures` :class:`bpy_prop_collection` of :class:`Armature`, (readonly)

   .. data:: brushes

      Brush data-blocks

      :type: :class:`BlendDataBrushes` :class:`bpy_prop_collection` of :class:`Brush`, (readonly)

   .. data:: cache_files

      Cache Files data-blocks

      :type: :class:`BlendDataCacheFiles` :class:`bpy_prop_collection` of :class:`CacheFile`, (readonly)

   .. data:: cameras

      Camera data-blocks

      :type: :class:`BlendDataCameras` :class:`bpy_prop_collection` of :class:`Camera`, (readonly)

   .. data:: curves

      Curve data-blocks

      :type: :class:`BlendDataCurves` :class:`bpy_prop_collection` of :class:`Curve`, (readonly)

   .. data:: filepath

      Path to the .blend file

      :type: string, default "", (readonly, never None)

   .. data:: fonts

      Vector font data-blocks

      :type: :class:`BlendDataFonts` :class:`bpy_prop_collection` of :class:`VectorFont`, (readonly)

   .. data:: grease_pencil

      Grease Pencil data-blocks

      :type: :class:`BlendDataGreasePencils` :class:`bpy_prop_collection` of :class:`GreasePencil`, (readonly)

   .. data:: groups

      Group data-blocks

      :type: :class:`BlendDataGroups` :class:`bpy_prop_collection` of :class:`Group`, (readonly)

   .. data:: images

      Image data-blocks

      :type: :class:`BlendDataImages` :class:`bpy_prop_collection` of :class:`Image`, (readonly)

   .. data:: is_dirty

      Have recent edits been saved to disk

      :type: boolean, default False, (readonly)

   .. data:: is_saved

      Has the current session been saved to disk as a .blend file

      :type: boolean, default False, (readonly)

   .. data:: lamps

      Lamp data-blocks

      :type: :class:`BlendDataLamps` :class:`bpy_prop_collection` of :class:`Lamp`, (readonly)

   .. data:: lattices

      Lattice data-blocks

      :type: :class:`BlendDataLattices` :class:`bpy_prop_collection` of :class:`Lattice`, (readonly)

   .. data:: libraries

      Library data-blocks

      :type: :class:`BlendDataLibraries` :class:`bpy_prop_collection` of :class:`Library`, (readonly)

   .. data:: linestyles

      Line Style data-blocks

      :type: :class:`BlendDataLineStyles` :class:`bpy_prop_collection` of :class:`FreestyleLineStyle`, (readonly)

   .. data:: masks

      Masks data-blocks

      :type: :class:`BlendDataMasks` :class:`bpy_prop_collection` of :class:`Mask`, (readonly)

   .. data:: materials

      Material data-blocks

      :type: :class:`BlendDataMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. data:: meshes

      Mesh data-blocks

      :type: :class:`BlendDataMeshes` :class:`bpy_prop_collection` of :class:`Mesh`, (readonly)

   .. data:: metaballs

      Metaball data-blocks

      :type: :class:`BlendDataMetaBalls` :class:`bpy_prop_collection` of :class:`MetaBall`, (readonly)

   .. data:: movieclips

      Movie Clip data-blocks

      :type: :class:`BlendDataMovieClips` :class:`bpy_prop_collection` of :class:`MovieClip`, (readonly)

   .. data:: node_groups

      Node group data-blocks

      :type: :class:`BlendDataNodeTrees` :class:`bpy_prop_collection` of :class:`NodeTree`, (readonly)

   .. data:: objects

      Object data-blocks

      :type: :class:`BlendDataObjects` :class:`bpy_prop_collection` of :class:`Object`, (readonly)

   .. data:: paint_curves

      Paint Curves data-blocks

      :type: :class:`BlendDataPaintCurves` :class:`bpy_prop_collection` of :class:`PaintCurve`, (readonly)

   .. data:: palettes

      Palette data-blocks

      :type: :class:`BlendDataPalettes` :class:`bpy_prop_collection` of :class:`Palette`, (readonly)

   .. data:: particles

      Particle data-blocks

      :type: :class:`BlendDataParticles` :class:`bpy_prop_collection` of :class:`ParticleSettings`, (readonly)

   .. data:: scenes

      Scene data-blocks

      :type: :class:`BlendDataScenes` :class:`bpy_prop_collection` of :class:`Scene`, (readonly)

   .. data:: screens

      Screen data-blocks

      :type: :class:`BlendDataScreens` :class:`bpy_prop_collection` of :class:`Screen`, (readonly)

   .. data:: shape_keys

      Shape Key data-blocks

      :type: :class:`bpy_prop_collection` of :class:`Key`, (readonly)

   .. data:: sounds

      Sound data-blocks

      :type: :class:`BlendDataSounds` :class:`bpy_prop_collection` of :class:`Sound`, (readonly)

   .. data:: speakers

      Speaker data-blocks

      :type: :class:`BlendDataSpeakers` :class:`bpy_prop_collection` of :class:`Speaker`, (readonly)

   .. data:: texts

      Text data-blocks

      :type: :class:`BlendDataTexts` :class:`bpy_prop_collection` of :class:`Text`, (readonly)

   .. data:: textures

      Texture data-blocks

      :type: :class:`BlendDataTextures` :class:`bpy_prop_collection` of :class:`Texture`, (readonly)

   .. attribute:: use_autopack

      Automatically pack all external data into .blend file

      :type: boolean, default False

   .. data:: version

      Version of Blender the .blend was saved with

      :type: int array of 3 items in [0, inf], default (0, 0, 0), (readonly)

   .. data:: window_managers

      Window manager data-blocks

      :type: :class:`BlendDataWindowManagers` :class:`bpy_prop_collection` of :class:`WindowManager`, (readonly)

   .. data:: worlds

      World data-blocks

      :type: :class:`BlendDataWorlds` :class:`bpy_prop_collection` of :class:`World`, (readonly)

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


   .. method:: user_map([subset=(id1, id2, ...)], key_types={..}, value_types={..})
   
      Returns a mapping of all ID datablocks in current ``bpy.data`` to a set of all datablocks using them.
   
      For list of valid set members for key_types & value_types, see: :class:`bpy.types.KeyingSetPath.id_type`.
   
      :arg subset: When passed, only these data-blocks and their users will be included as keys/values in the map.
      :type subset: sequence
      :arg key_types: Filter the keys mapped by ID types.
      :type key_types: set of strings
      :arg value_types: Filter the values in the set by ID types.
      :type value_types: set of strings
      :return: dictionary of :class:`bpy.types.ID` instances, with sets of ID's as their values.
      :rtype: dict


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

   * :class:`Context.blend_data`
   * :class:`RenderEngine.update`

