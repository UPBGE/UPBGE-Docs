BakeSettings(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BakeSettings(bpy_struct)

   Bake data for a Scene data-block

   .. attribute:: cage_extrusion

      Distance to use for the inward ray cast when using selected to active

      :type: float in [0, inf], default 0.0

   .. attribute:: cage_object

      Object to use as cage instead of calculating the cage from the active object with cage extrusion

      :type: string, default "", (never None)

   .. attribute:: filepath

      Image filepath to use when saving externally

      :type: string, default "", (never None)

   .. attribute:: height

      Vertical dimension of the baking map

      :type: int in [4, 10000], default 0

   .. data:: image_settings

      :type: :class:`ImageFormatSettings`, (readonly, never None)

   .. attribute:: margin

      Extends the baked result as a post process filter

      :type: int in [0, 32767], default 0

   .. attribute:: normal_b

      Axis to bake in blue channel

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

   .. attribute:: normal_g

      Axis to bake in green channel

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

   .. attribute:: normal_r

      Axis to bake in red channel

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

   .. attribute:: normal_space

      Choose normal space for baking

      * ``OBJECT`` Object, Bake the normals in object space.
      * ``TANGENT`` Tangent, Bake the normals in tangent space.

      :type: enum in ['OBJECT', 'TANGENT'], default 'OBJECT'

   .. data:: pass_filter

      Passes to include in the active baking pass

      :type: enum set in {'NONE', 'AO', 'EMIT', 'DIRECT', 'INDIRECT', 'COLOR', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'}, default {}, (readonly)

   .. attribute:: save_mode

      Choose how to save the baking map

      * ``INTERNAL`` Internal, Save the baking map in an internal image data-block.
      * ``EXTERNAL`` External, Save the baking map in an external file.

      :type: enum in ['INTERNAL', 'EXTERNAL'], default 'INTERNAL'

   .. attribute:: use_automatic_name

      Automatically name the output file with the pass type (external only)

      :type: boolean, default False

   .. attribute:: use_cage

      Cast rays to active object from a cage

      :type: boolean, default False

   .. attribute:: use_clear

      Clear Images before baking (internal only)

      :type: boolean, default False

   .. attribute:: use_pass_ambient_occlusion

      Add ambient occlusion contribution

      :type: boolean, default False

   .. attribute:: use_pass_color

      Color the pass

      :type: boolean, default False

   .. attribute:: use_pass_diffuse

      Add diffuse contribution

      :type: boolean, default False

   .. attribute:: use_pass_direct

      Add direct lighting contribution

      :type: boolean, default False

   .. attribute:: use_pass_emit

      Add emission contribution

      :type: boolean, default False

   .. attribute:: use_pass_glossy

      Add glossy contribution

      :type: boolean, default False

   .. attribute:: use_pass_indirect

      Add indirect lighting contribution

      :type: boolean, default False

   .. attribute:: use_pass_subsurface

      Add subsurface contribution

      :type: boolean, default False

   .. attribute:: use_pass_transmission

      Add transmission contribution

      :type: boolean, default False

   .. attribute:: use_selected_to_active

      Bake shading on the surface of selected objects to the active object

      :type: boolean, default False

   .. attribute:: use_split_materials

      Split external images per material (external only)

      :type: boolean, default False

   .. attribute:: width

      Horizontal dimension of the baking map

      :type: int in [4, 10000], default 0

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

   * :class:`RenderSettings.bake`

