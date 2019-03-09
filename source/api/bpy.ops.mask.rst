Mask Operators
==============

.. module:: bpy.ops.mask

.. function:: add_feather_vertex(location=(0.0, 0.0))

   Add vertex to feather

   :arg location:

      Location, Location of vertex in normalized space

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: add_feather_vertex_slide(MASK_OT_add_feather_vertex=None, MASK_OT_slide_point=None)

   Add new vertex to feather and slide it

   :arg MASK_OT_add_feather_vertex:

      Add Feather Vertex, Add vertex to feather

   :type MASK_OT_add_feather_vertex: :class:`MASK_OT_add_feather_vertex`, (optional)
   :arg MASK_OT_slide_point:

      Slide Point, Slide control points

   :type MASK_OT_slide_point: :class:`MASK_OT_slide_point`, (optional)

.. function:: add_vertex(location=(0.0, 0.0))

   Add vertex to active spline

   :arg location:

      Location, Location of vertex in normalized space

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: add_vertex_slide(MASK_OT_add_vertex=None, MASK_OT_slide_point=None)

   Add new vertex and slide it

   :arg MASK_OT_add_vertex:

      Add Vertex, Add vertex to active spline

   :type MASK_OT_add_vertex: :class:`MASK_OT_add_vertex`, (optional)
   :arg MASK_OT_slide_point:

      Slide Point, Slide control points

   :type MASK_OT_slide_point: :class:`MASK_OT_slide_point`, (optional)

.. function:: copy_splines()

   Copy selected splines to clipboard

.. function:: cyclic_toggle()

   Toggle cyclic for selected splines

.. function:: delete()

   Delete selected control points or splines

.. function:: duplicate()

   Duplicate selected control points and segments between them

.. function:: duplicate_move(MASK_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate mask and move

   :arg MASK_OT_duplicate:

      Duplicate Mask, Duplicate selected control points and segments between them

   :type MASK_OT_duplicate: :class:`MASK_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: feather_weight_clear()

   Reset the feather weight to zero

.. function:: handle_type_set(type='AUTO')

   Set type of handles for selected control points

   :arg type:

      Type, Spline type

   :type type: enum in ['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE'], (optional)

.. function:: hide_view_clear(select=True)

   Reveal the layer by setting the hide flag

   :arg select:

      Select

   :type select: boolean, (optional)

.. function:: hide_view_set(unselected=False)

   Hide the layer by setting the hide flag

   :arg unselected:

      Unselected, Hide unselected rather than selected layers

   :type unselected: boolean, (optional)

.. function:: layer_move(direction='UP')

   Move the active layer up/down in the list

   :arg direction:

      Direction, Direction to move the active layer

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: layer_new(name="")

   Add new mask layer for masking

   :arg name:

      Name, Name of new mask layer

   :type name: string, (optional, never None)

.. function:: layer_remove()

   Remove mask layer

.. function:: new(name="")

   Create new mask

   :arg name:

      Name, Name of new mask

   :type name: string, (optional, never None)

.. function:: normals_make_consistent()

   Re-calculate the direction of selected handles

.. function:: parent_clear()

   Clear the mask's parenting

.. function:: parent_set()

   Set the mask's parenting

.. function:: paste_splines()

   Paste splines from clipboard

.. function:: primitive_circle_add(size=100.0, location=(0.0, 0.0))

   Add new circle-shaped spline

   :arg size:

      Size, Size of new circle

   :type size: float in [-inf, inf], (optional)
   :arg location:

      Location, Location of new circle

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: primitive_square_add(size=100.0, location=(0.0, 0.0))

   Add new square-shaped spline

   :arg size:

      Size, Size of new circle

   :type size: float in [-inf, inf], (optional)
   :arg location:

      Location, Location of new circle

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: select(extend=False, deselect=False, toggle=False, location=(0.0, 0.0))

   Select spline points

   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg deselect:

      Deselect, Remove from selection

   :type deselect: boolean, (optional)
   :arg toggle:

      Toggle Selection, Toggle the selection

   :type toggle: boolean, (optional)
   :arg location:

      Location, Location of vertex in normalized space

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: select_all(action='TOGGLE')

   Change selection of all curve points

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select curve points using border selection

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_circle(x=0, y=0, radius=25, deselect=False)

   Select curve points using circle selection

   :arg x:

      X

   :type x: int in [-inf, inf], (optional)
   :arg y:

      Y

   :type y: int in [-inf, inf], (optional)
   :arg radius:

      Radius

   :type radius: int in [1, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)

.. function:: select_lasso(path=None, deselect=False, extend=True)

   Select curve points using lasso selection

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_less()

   Deselect spline points at the boundary of each selection region

.. function:: select_linked()

   Select all curve points linked to already selected ones

.. function:: select_linked_pick(deselect=False)

   (De)select all points linked to the curve under the mouse cursor

   :arg deselect:

      Deselect

   :type deselect: boolean, (optional)

.. function:: select_more()

   Select more spline points connected to initial selection

.. function:: shape_key_clear()

   Undocumented

.. function:: shape_key_feather_reset()

   Reset feather weights on all selected points animation values

.. function:: shape_key_insert()

   Undocumented

.. function:: shape_key_rekey(location=True, feather=True)

   Recalculate animation data on selected points for frames selected in the dopesheet

   :arg location:

      Location

   :type location: boolean, (optional)
   :arg feather:

      Feather

   :type feather: boolean, (optional)

.. function:: slide_point(slide_feather=False, is_new_point=False)

   Slide control points

   :arg slide_feather:

      Slide Feather, First try to slide feather instead of vertex

   :type slide_feather: boolean, (optional)
   :arg is_new_point:

      Slide New Point, Newly created vertex is being slid

   :type is_new_point: boolean, (optional)

.. function:: slide_spline_curvature()

   Slide a point on the spline to define it's curvature

.. function:: switch_direction()

   Switch direction of selected splines

