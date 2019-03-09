SpaceUVEditor(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SpaceUVEditor(bpy_struct)

   UV editor data for the image editor space

   .. attribute:: draw_stretch_type

      Type of stretch to draw

      * ``ANGLE`` Angle, Angular distortion between UV and 3D angles.
      * ``AREA`` Area, Area distortion between UV and 3D faces.

      :type: enum in ['ANGLE', 'AREA'], default 'ANGLE'

   .. attribute:: edge_draw_type

      Draw type for drawing UV edges

      * ``OUTLINE`` Outline, Draw white edges with black outline.
      * ``DASH`` Dash, Draw dashed black-white edges.
      * ``BLACK`` Black, Draw black edges.
      * ``WHITE`` White, Draw white edges.

      :type: enum in ['OUTLINE', 'DASH', 'BLACK', 'WHITE'], default 'OUTLINE'

   .. attribute:: lock_bounds

      Constraint to stay within the image bounds while editing

      :type: boolean, default False

   .. attribute:: other_uv_filter

      Filter applied on the other object's UV to limit displayed

      * ``ALL`` All, No filter, show all islands from other objects.
      * ``SAME_IMAGE`` Same Image, Only show others' UV islands whose active image matches image of the active face.

      :type: enum in ['ALL', 'SAME_IMAGE'], default 'SAME_IMAGE'

   .. attribute:: show_faces

      Draw faces over the image

      :type: boolean, default False

   .. attribute:: show_metadata

      Draw metadata properties of the image

      :type: boolean, default False

   .. attribute:: show_modified_edges

      Draw edges after modifiers are applied

      :type: boolean, default False

   .. attribute:: show_normalized_coords

      Display UV coordinates from 0.0 to 1.0 rather than in pixels

      :type: boolean, default False

   .. attribute:: show_other_objects

      Draw other selected objects that share the same image

      :type: boolean, default False

   .. attribute:: show_smooth_edges

      Draw UV edges anti-aliased

      :type: boolean, default False

   .. attribute:: show_stretch

      Draw faces colored according to the difference in shape between UVs and their 3D coordinates (blue for low distortion, red for high distortion)

      :type: boolean, default False

   .. attribute:: show_texpaint

      Draw overlay of texture paint uv layer

      :type: boolean, default False

   .. attribute:: sticky_select_mode

      Automatically select also UVs sharing the same vertex as the ones being selected

      * ``DISABLED`` Disabled, Sticky vertex selection disabled.
      * ``SHARED_LOCATION`` Shared Location, Select UVs that are at the same location and share a mesh vertex.
      * ``SHARED_VERTEX`` Shared Vertex, Select UVs that share mesh vertex, irrespective if they are in the same location.

      :type: enum in ['DISABLED', 'SHARED_LOCATION', 'SHARED_VERTEX'], default 'SHARED_LOCATION'

   .. attribute:: use_live_unwrap

      Continuously unwrap the selected UV island while transforming pinned vertices

      :type: boolean, default False

   .. attribute:: use_snap_to_pixels

      Snap UVs to pixel locations while editing

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

   * :class:`SpaceImageEditor.uv_editor`

