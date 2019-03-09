MaskLayer(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaskLayer(bpy_struct)

   Single layer used for masking pixels

   .. attribute:: alpha

      Render Opacity

      :type: float in [-inf, inf], default 0.0

   .. attribute:: blend

      Method of blending mask layers

      :type: enum in ['MERGE_ADD', 'MERGE_SUBTRACT', 'ADD', 'SUBTRACT', 'LIGHTEN', 'DARKEN', 'MUL', 'REPLACE', 'DIFFERENCE'], default 'ADD'

   .. attribute:: falloff

      Falloff type the feather

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.

      :type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], default 'SMOOTH'

   .. attribute:: hide

      Restrict visibility in the viewport

      :type: boolean, default False

   .. attribute:: hide_render

      Restrict renderability

      :type: boolean, default False

   .. attribute:: hide_select

      Restrict selection in the viewport

      :type: boolean, default False

   .. attribute:: invert

      Invert the mask black/white

      :type: boolean, default False

   .. attribute:: name

      Unique name of layer

      :type: string, default "", (never None)

   .. attribute:: select

      Layer is selected for editing in the Dope Sheet

      :type: boolean, default False

   .. data:: splines

      Collection of splines which defines this layer

      :type: :class:`MaskSplines` :class:`bpy_prop_collection` of :class:`MaskSpline`, (readonly)

   .. attribute:: use_fill_holes

      Calculate holes when filling overlapping curves

      :type: boolean, default False

   .. attribute:: use_fill_overlap

      Calculate self intersections and overlap before filling

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

   * :class:`Mask.layers`
   * :class:`MaskLayers.active`
   * :class:`MaskLayers.new`
   * :class:`MaskLayers.remove`

