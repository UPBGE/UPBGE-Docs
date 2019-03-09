FreestyleLineSet(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FreestyleLineSet(bpy_struct)

   Line set for associating lines and style parameters

   .. attribute:: edge_type_combination

      Specify a logical combination of selection conditions on feature edge types

      * ``OR`` Logical OR, Select feature edges satisfying at least one of edge type conditions.
      * ``AND`` Logical AND, Select feature edges satisfying all edge type conditions.

      :type: enum in ['OR', 'AND'], default 'OR'

   .. attribute:: edge_type_negation

      Specify either inclusion or exclusion of feature edges selected by edge types

      * ``INCLUSIVE`` Inclusive, Select feature edges satisfying the given edge type conditions.
      * ``EXCLUSIVE`` Exclusive, Select feature edges not satisfying the given edge type conditions.

      :type: enum in ['INCLUSIVE', 'EXCLUSIVE'], default 'INCLUSIVE'

   .. attribute:: exclude_border

      Exclude border edges

      :type: boolean, default False

   .. attribute:: exclude_contour

      Exclude contours

      :type: boolean, default False

   .. attribute:: exclude_crease

      Exclude crease edges

      :type: boolean, default False

   .. attribute:: exclude_edge_mark

      Exclude edge marks

      :type: boolean, default False

   .. attribute:: exclude_external_contour

      Exclude external contours

      :type: boolean, default False

   .. attribute:: exclude_material_boundary

      Exclude edges at material boundaries

      :type: boolean, default False

   .. attribute:: exclude_ridge_valley

      Exclude ridges and valleys

      :type: boolean, default False

   .. attribute:: exclude_silhouette

      Exclude silhouette edges

      :type: boolean, default False

   .. attribute:: exclude_suggestive_contour

      Exclude suggestive contours

      :type: boolean, default False

   .. attribute:: face_mark_condition

      Specify a feature edge selection condition based on face marks

      * ``ONE`` One Face, Select a feature edge if either of its adjacent faces is marked.
      * ``BOTH`` Both Faces, Select a feature edge if both of its adjacent faces are marked.

      :type: enum in ['ONE', 'BOTH'], default 'ONE'

   .. attribute:: face_mark_negation

      Specify either inclusion or exclusion of feature edges selected by face marks

      * ``INCLUSIVE`` Inclusive, Select feature edges satisfying the given face mark conditions.
      * ``EXCLUSIVE`` Exclusive, Select feature edges not satisfying the given face mark conditions.

      :type: enum in ['INCLUSIVE', 'EXCLUSIVE'], default 'INCLUSIVE'

   .. attribute:: group

      A group of objects based on which feature edges are selected

      :type: :class:`Group`

   .. attribute:: group_negation

      Specify either inclusion or exclusion of feature edges belonging to a group of objects

      * ``INCLUSIVE`` Inclusive, Select feature edges belonging to some object in the group.
      * ``EXCLUSIVE`` Exclusive, Select feature edges not belonging to any object in the group.

      :type: enum in ['INCLUSIVE', 'EXCLUSIVE'], default 'INCLUSIVE'

   .. attribute:: linestyle

      Line style settings

      :type: :class:`FreestyleLineStyle`, (never None)

   .. attribute:: name

      Line set name

      :type: string, default "", (never None)

   .. attribute:: qi_end

      Last QI value of the QI range

      :type: int in [0, inf], default 0

   .. attribute:: qi_start

      First QI value of the QI range

      :type: int in [0, inf], default 0

   .. attribute:: select_border

      Select border edges (open mesh edges)

      :type: boolean, default False

   .. attribute:: select_by_edge_types

      Select feature edges based on edge types

      :type: boolean, default False

   .. attribute:: select_by_face_marks

      Select feature edges by face marks

      :type: boolean, default False

   .. attribute:: select_by_group

      Select feature edges based on a group of objects

      :type: boolean, default False

   .. attribute:: select_by_image_border

      Select feature edges by image border (less memory consumption)

      :type: boolean, default False

   .. attribute:: select_by_visibility

      Select feature edges based on visibility

      :type: boolean, default False

   .. attribute:: select_contour

      Select contours (outer silhouettes of each object)

      :type: boolean, default False

   .. attribute:: select_crease

      Select crease edges (those between two faces making an angle smaller than the Crease Angle)

      :type: boolean, default False

   .. attribute:: select_edge_mark

      Select edge marks (edges annotated by Freestyle edge marks)

      :type: boolean, default False

   .. attribute:: select_external_contour

      Select external contours (outer silhouettes of occluding and occluded objects)

      :type: boolean, default False

   .. attribute:: select_material_boundary

      Select edges at material boundaries

      :type: boolean, default False

   .. attribute:: select_ridge_valley

      Select ridges and valleys (boundary lines between convex and concave areas of surface)

      :type: boolean, default False

   .. attribute:: select_silhouette

      Select silhouettes (edges at the boundary of visible and hidden faces)

      :type: boolean, default False

   .. attribute:: select_suggestive_contour

      Select suggestive contours (almost silhouette/contour edges)

      :type: boolean, default False

   .. attribute:: show_render

      Enable or disable this line set during stroke rendering

      :type: boolean, default False

   .. attribute:: visibility

      Determine how to use visibility for feature edge selection

      * ``VISIBLE`` Visible, Select visible feature edges.
      * ``HIDDEN`` Hidden, Select hidden feature edges.
      * ``RANGE`` QI Range, Select feature edges within a range of quantitative invisibility (QI) values.

      :type: enum in ['VISIBLE', 'HIDDEN', 'RANGE'], default 'VISIBLE'

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

   * :class:`Linesets.active`
   * :class:`Linesets.new`
   * :class:`Linesets.remove`
   * :class:`FreestyleSettings.linesets`

