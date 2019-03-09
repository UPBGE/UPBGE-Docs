MetaBall(ID)
============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: MetaBall(ID)

   Metaball data-block to defined blobby surfaces

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: cycles

      Cycles mesh settings

      :type: :class:`CyclesMeshSettings`, (readonly)

   .. data:: elements

      Meta elements

      :type: :class:`MetaBallElements` :class:`bpy_prop_collection` of :class:`MetaElement`, (readonly)

   .. data:: is_editmode

      True when used in editmode

      :type: boolean, default False, (readonly)

   .. data:: materials

      :type: :class:`IDMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. attribute:: render_resolution

      Polygonization resolution in rendering

      :type: float in [0.005, 10000], default 0.0

   .. attribute:: resolution

      Polygonization resolution in the 3D viewport

      :type: float in [0.005, 10000], default 0.0

   .. attribute:: texspace_location

      Texture space location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: texspace_size

      Texture space size

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: threshold

      Influence of meta elements

      :type: float in [0, 5], default 0.0

   .. attribute:: update_method

      Metaball edit update behavior

      * ``UPDATE_ALWAYS`` Always, While editing, update metaball always.
      * ``HALFRES`` Half, While editing, update metaball in half resolution.
      * ``FAST`` Fast, While editing, update metaball without polygonization.
      * ``NEVER`` Never, While editing, don't update metaball at all.

      :type: enum in ['UPDATE_ALWAYS', 'HALFRES', 'FAST', 'NEVER'], default 'UPDATE_ALWAYS'

   .. attribute:: use_auto_texspace

      Adjust active object's texture space automatically when transforming object

      :type: boolean, default False

   .. method:: transform(matrix)

      Transform meta elements by a matrix

      :arg matrix:

         Matrix

      :type matrix: float multi-dimensional array of 4 * 4 items in [-inf, inf]

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.meta_ball`
   * :class:`BlendData.metaballs`
   * :class:`BlendDataMetaBalls.new`
   * :class:`BlendDataMetaBalls.remove`

