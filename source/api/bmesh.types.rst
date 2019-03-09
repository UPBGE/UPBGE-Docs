BMesh Types (bmesh.types)
=========================

.. module:: bmesh.types

Base Mesh Type
--------------

.. class:: BMesh

   The BMesh data structure

   .. method:: calc_tessface()
   
      Calculate triangle tessellation from quads/ngons.
   
      :return: The triangulated faces.
      :rtype: list of :class:`BMLoop` tuples


   .. method:: calc_volume(signed=False)
   
      Calculate mesh volume based on face normals.
   
      :arg signed: when signed is true, negative values may be returned.
      :type signed: bool
      :return: The volume of the mesh.
      :rtype: float


   .. method:: clear()
   
      Clear all mesh data.


   .. method:: copy()
   
      :return: A copy of this BMesh.
      :rtype: :class:`BMesh`


   .. method:: free()
   
      Explicitly free the BMesh data from memory, causing exceptions on further access.
   
      .. note::
   
         The BMesh is freed automatically, typically when the script finishes executing.
         However in some cases its hard to predict when this will be and its useful to
         explicitly free the data.


   .. method:: from_mesh(mesh, face_normals=True, use_shape_key=False, shape_key_index=0)
   
      Initialize this bmesh from existing mesh datablock.
   
      :arg mesh: The mesh data to load.
      :type mesh: :class:`Mesh`
      :arg use_shape_key: Use the locations from a shape key.
      :type use_shape_key: boolean
      :arg shape_key_index: The shape key index to use.
      :type shape_key_index: int
   
      .. note::
   
         Multiple calls can be used to join multiple meshes.
   
         Custom-data layers are only copied from ``mesh`` on initialization.
         Further calls will copy custom-data to matching layers, layers missing on the target mesh wont be added.


   .. method:: from_object(object, scene, deform=True, render=False, cage=False, face_normals=True)
   
      Initialize this bmesh from existing object datablock (currently only meshes are supported).
   
      :arg object: The object data to load.
      :type object: :class:`Object`
      :arg deform: Apply deformation modifiers.
      :type deform: boolean
      :arg render: Use render settings.
      :type render: boolean
      :arg cage: Get the mesh as a deformed cage.
      :type cage: boolean
      :arg face_normals: Calculate face normals.
      :type face_normals: boolean


   .. method:: normal_update()
   
      Update mesh normals.


   .. method:: select_flush(select)
   
      Flush selection, independent of the current selection mode.
   
      :arg select: flush selection or de-selected elements.
      :type select: boolean


   .. method:: select_flush_mode()
   
      flush selection based on the current mode current :class:`BMesh.select_mode`.


   .. method:: to_mesh(mesh)
   
      Writes this BMesh data into an existing Mesh datablock.
   
      :arg mesh: The mesh data to write into.
      :type mesh: :class:`Mesh`


   .. method:: transform(matrix, filter=None)
   
      Transform the mesh (optionally filtering flagged data only).
   
      :arg matrix: transform matrix.
      :type matrix: 4x4 :class:`mathutils.Matrix`
      :arg filter: set of values in ('SELECT', 'HIDE', 'SEAM', 'SMOOTH', 'TAG').
      :type filter: set


   .. attribute:: edges

      This meshes edge sequence (read-only).
      
      :type: :class:`BMEdgeSeq`


   .. attribute:: faces

      This meshes face sequence (read-only).
      
      :type: :class:`BMFaceSeq`


   .. attribute:: is_valid

      True when this element is valid (hasn't been removed).
      
      :type: boolean


   .. attribute:: is_wrapped

      True when this mesh is owned by blender (typically the editmode BMesh).
      
      :type: boolean


   .. attribute:: loops

      This meshes loops (read-only).
      
      :type: :class:`BMLoopSeq`
      
      .. note::
      
         Loops must be accessed via faces, this is only exposed for layer access.


   .. attribute:: select_history

      Sequence of selected items (the last is displayed as active).
      
      :type: :class:`BMEditSelSeq`


   .. attribute:: select_mode

      The selection mode, values can be {'VERT', 'EDGE', 'FACE'}, can't be assigned an empty set.
      
      :type: set


   .. attribute:: verts

      This meshes vert sequence (read-only).
      
      :type: :class:`BMVertSeq`




Mesh Elements
-------------

.. class:: BMVert

   The BMesh vertex type

   .. method:: calc_edge_angle(fallback=None)
   
      Return the angle between this vert's two connected edges.
   
      :arg fallback: return this when the vert doesn't have 2 edges
         (instead of raising a :exc:`ValueError`).
      :type fallback: any
      :return: Angle between edges in radians.
      :rtype: float


   .. method:: calc_shell_factor()
   
      Return a multiplier calculated based on the sharpness of the vertex.
      Where a flat surface gives 1.0, and higher values sharper edges.
      This is used to maintain shell thickness when offsetting verts along their normals.
   
      :return: offset multiplier
      :rtype: float


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.


   .. method:: copy_from_face_interp(face)
   
      Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).
   
      :arg face: The face to interpolate data from.
      :type face: :class:`BMFace`


   .. method:: copy_from_vert_interp(vert_pair, fac)
   
      Interpolate the customdata from a vert between 2 other verts.
   
      :arg vert_pair: The vert to interpolate data from.
      :type vert_pair: :class:`BMVert`


   .. method:: hide_set(hide)
   
      Set the hide state.
      This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.
   
      :arg hide: Hidden or visible.
      :type hide: boolean


   .. method:: normal_update()
   
      Update vertex normal.


   .. method:: select_set(select)
   
      Set the selection.
      This is different from the *select* attribute because it updates the selection state of associated geometry.
   
      :arg select: Select or de-select.
      :type select: boolean
   
      .. note::
   
         Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex       won't de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.


   .. attribute:: co

      The coordinates for this vertex as a 3D, wrapped vector.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: hide

      Hidden state of this element.
      
      :type: boolean


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :class:`BMElemSeq.index_update`.


   .. attribute:: is_boundary

      True when this vertex is connected to boundary edges (read-only).
      
      :type: boolean


   .. attribute:: is_manifold

      True when this vertex is manifold (read-only).
      
      :type: boolean


   .. attribute:: is_valid

      True when this element is valid (hasn't been removed).
      
      :type: boolean


   .. attribute:: is_wire

      True when this vertex is not connected to any faces (read-only).
      
      :type: boolean


   .. attribute:: link_edges

      Edges connected to this vertex (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMEdge`


   .. attribute:: link_faces

      Faces connected to this vertex (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMFace`


   .. attribute:: link_loops

      Loops that use this vertex (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMLoop`


   .. attribute:: normal

      The normal for this vertex as a 3D, wrapped vector.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: select

      Selected state of this element.
      
      :type: boolean


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: boolean




.. class:: BMEdge

   The BMesh edge connecting 2 verts

   .. method:: calc_face_angle(fallback=None)
   
      :arg fallback: return this when the edge doesn't have 2 faces
         (instead of raising a :exc:`ValueError`).
      :type fallback: any
      :return: The angle between 2 connected faces in radians.
      :rtype: float


   .. method:: calc_face_angle_signed(fallback=None)
   
      :arg fallback: return this when the edge doesn't have 2 faces
         (instead of raising a :exc:`ValueError`).
      :type fallback: any
      :return: The angle between 2 connected faces in radians (negative for concave join).
      :rtype: float


   .. method:: calc_length()
   
      :return: The length between both verts.
      :rtype: float


   .. method:: calc_tangent(loop)
   
      Return the tangent at this edge relative to a face (pointing inward into the face).
      This uses the face normal for calculation.
   
      :arg loop: The loop used for tangent calculation.
      :type loop: :class:`BMLoop`
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.


   .. method:: hide_set(hide)
   
      Set the hide state.
      This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.
   
      :arg hide: Hidden or visible.
      :type hide: boolean


   .. method:: normal_update()
   
      Update edges vertex normals.


   .. method:: other_vert(vert)
   
      Return the other vertex on this edge or None if the vertex is not used by this edge.
   
      :arg vert: a vert in this edge.
      :type vert: :class:`BMVert`
      :return: The edges other vert.
      :rtype: :class:`BMVert` or None


   .. method:: select_set(select)
   
      Set the selection.
      This is different from the *select* attribute because it updates the selection state of associated geometry.
   
      :arg select: Select or de-select.
      :type select: boolean
   
      .. note::
   
         Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex       won't de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.


   .. attribute:: hide

      Hidden state of this element.
      
      :type: boolean


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :class:`BMElemSeq.index_update`.


   .. attribute:: is_boundary

      True when this edge is at the boundary of a face (read-only).
      
      :type: boolean


   .. attribute:: is_contiguous

      True when this edge is manifold, between two faces with the same winding (read-only).
      
      :type: boolean


   .. attribute:: is_convex

      True when this edge joins two convex faces, depends on a valid face normal (read-only).
      
      :type: boolean


   .. attribute:: is_manifold

      True when this edge is manifold (read-only).
      
      :type: boolean


   .. attribute:: is_valid

      True when this element is valid (hasn't been removed).
      
      :type: boolean


   .. attribute:: is_wire

      True when this edge is not connected to any faces (read-only).
      
      :type: boolean


   .. attribute:: link_faces

      Faces connected to this edge, (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMFace`


   .. attribute:: link_loops

      Loops connected to this edge, (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMLoop`


   .. attribute:: seam

      Seam for UV unwrapping.
      
      :type: boolean


   .. attribute:: select

      Selected state of this element.
      
      :type: boolean


   .. attribute:: smooth

      Smooth state of this element.
      
      :type: boolean


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: boolean


   .. attribute:: verts

      Verts this edge uses (always 2), (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMVert`




.. class:: BMFace

   The BMesh face with 3 or more sides

   .. method:: calc_area()
   
      Return the area of the face.
   
      :return: Return the area of the face.
      :rtype: float


   .. method:: calc_center_bounds()
   
      Return bounds center of the face.
   
      :return: a 3D vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_center_median()
   
      Return median center of the face.
   
      :return: a 3D vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_center_median_weighted()
   
      Return median center of the face weighted by edge lengths.
   
      :return: a 3D vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_perimeter()
   
      Return the perimeter of the face.
   
      :return: Return the perimeter of the face.
      :rtype: float


   .. method:: calc_tangent_edge()
   
      Return face tangent based on longest edge.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent_edge_diagonal()
   
      Return face tangent based on the edge farthest from any vertex.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent_edge_pair()
   
      Return face tangent based on the two longest disconnected edges.
   
      - Tris: Use the edge pair with the most similar lengths.
      - Quads: Use the longest edge pair.
      - NGons: Use the two longest disconnected edges.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent_vert_diagonal()
   
      Return face tangent based on the two most distent vertices.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: copy(verts=True, edges=True)
   
      Make a copy of this face.
   
      :arg verts: When set, the faces verts will be duplicated too.
      :type verts: boolean
      :arg edges: When set, the faces edges will be duplicated too.
      :type edges: boolean
      :return: The newly created face.
      :rtype: :class:`BMFace`


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.


   .. method:: copy_from_face_interp(face, vert=True)
   
      Interpolate the customdata from another face onto this one (faces should overlap).
   
      :arg face: The face to interpolate data from.
      :type face: :class:`BMFace`
      :arg vert: When True, also copy vertex data.
      :type vert: boolean


   .. method:: hide_set(hide)
   
      Set the hide state.
      This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.
   
      :arg hide: Hidden or visible.
      :type hide: boolean


   .. method:: normal_flip()
   
      Reverses winding of a face, which flips its normal.


   .. method:: normal_update()
   
      Update face's normal.


   .. method:: select_set(select)
   
      Set the selection.
      This is different from the *select* attribute because it updates the selection state of associated geometry.
   
      :arg select: Select or de-select.
      :type select: boolean
   
      .. note::
   
         Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex       won't de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.


   .. attribute:: edges

      Edges of this face, (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMEdge`


   .. attribute:: hide

      Hidden state of this element.
      
      :type: boolean


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :class:`BMElemSeq.index_update`.


   .. attribute:: is_valid

      True when this element is valid (hasn't been removed).
      
      :type: boolean


   .. attribute:: loops

      Loops of this face, (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMLoop`


   .. attribute:: material_index

      The face's material index.
      
      :type: int


   .. attribute:: normal

      The normal for this face as a 3D, wrapped vector.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: select

      Selected state of this element.
      
      :type: boolean


   .. attribute:: smooth

      Smooth state of this element.
      
      :type: boolean


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: boolean


   .. attribute:: verts

      Verts of this face, (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMVert`




.. class:: BMLoop

   This is normally accessed from :class:`BMFace.loops` where each face loop represents a corner of the face.

   .. method:: calc_angle()
   
      Return the angle at this loops corner of the face.
      This is calculated so sharper corners give lower angles.
   
      :return: The angle in radians.
      :rtype: float


   .. method:: calc_normal()
   
      Return normal at this loops corner of the face.
      Falls back to the face normal for straight lines.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent()
   
      Return the tangent at this loops corner of the face (pointing inward into the face).
      Falls back to the face normal for straight lines.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.


   .. method:: copy_from_face_interp(face, vert=True, multires=True)
   
      Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).
   
      :arg face: The face to interpolate data from.
      :type face: :class:`BMFace`
      :arg vert: When enabled, interpolate the loops vertex data (optional).
      :type vert: boolean
      :arg multires: When enabled, interpolate the loops multires data (optional).
      :type multires: boolean


   .. attribute:: edge

      The loop's edge (between this loop and the next), (read-only).
      
      :type: :class:`BMEdge`


   .. attribute:: face

      The face this loop makes (read-only).
      
      :type: :class:`BMFace`


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :class:`BMElemSeq.index_update`.


   .. attribute:: is_convex

      True when this loop is at the convex corner of a face, depends on a valid face normal (read-only).
      
      :type: boolean


   .. attribute:: is_valid

      True when this element is valid (hasn't been removed).
      
      :type: boolean


   .. attribute:: link_loop_next

      The next face corner (read-only).
      
      :type: :class:`BMLoop`


   .. attribute:: link_loop_prev

      The previous face corner (read-only).
      
      :type: :class:`BMLoop`


   .. attribute:: link_loop_radial_next

      The next loop around the edge (read-only).
      
      :type: :class:`BMLoop`


   .. attribute:: link_loop_radial_prev

      The previous loop around the edge (read-only).
      
      :type: :class:`BMLoop`


   .. attribute:: link_loops

      Loops connected to this loop, (read-only).
      
      :type: :class:`BMElemSeq` of :class:`BMLoop`


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: boolean


   .. attribute:: vert

      The loop's vertex (read-only).
      
      :type: :class:`BMVert`




Sequence Accessors
------------------

.. class:: BMElemSeq

   General sequence type used for accessing any sequence of 
   :class:`BMVert`, :class:`BMEdge`, :class:`BMFace`, :class:`BMLoop`.
   
   When accessed via :class:`BMesh.verts`, :class:`BMesh.edges`, :class:`BMesh.faces` 
   there are also functions to create/remomove items.

   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`BMesh.verts`, :class:`BMesh.edges`, :class:`BMesh.faces`
         works but wont result in each element having a valid index, insted its order in the sequence will be set.




.. class:: BMVertSeq


   .. method:: ensure_lookup_table()
   
      Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg ``bm.verts[index]``.
   
      This needs to be called again after adding/removing data in this sequence.


   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`BMesh.verts`, :class:`BMesh.edges`, :class:`BMesh.faces`
         works but wont result in each element having a valid index, insted its order in the sequence will be set.


   .. method:: new(co=(0.0, 0.0, 0.0), example=None)
   
      Create a new vertex.
   
      :arg co: The initial location of the vertex (optional argument).
      :type co: float triplet
      :arg example: Existing vert to initialize settings.
      :type example: :class:`BMVert`
      :return: The newly created edge.
      :rtype: :class:`BMVert`


   .. method:: remove(vert)
   
      Remove a vert.


   .. method:: sort(key=None, reverse=False)
   
      Sort the elements of this sequence, using an optional custom sort key.
      Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.
   
      :arg key: The key that sets the ordering of the elements.
      :type key: :function: returning a number
      :arg reverse: Reverse the order of the elements
      :type reverse: :boolean:
   
      .. note::
   
         When the 'key' argument is not provided, the elements are reordered following their current index value.
         In particular this can be used by setting indices manually before calling this method.
   
      .. warning::
   
         Existing references to the N'th element, will continue to point the data at that index.


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`BMLayerAccessVert`




.. class:: BMEdgeSeq


   .. method:: ensure_lookup_table()
   
      Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg ``bm.verts[index]``.
   
      This needs to be called again after adding/removing data in this sequence.


   .. method:: get(verts, fallback=None)
   
      Return an edge which uses the **verts** passed.
   
      :arg verts: Sequence of verts.
      :type verts: :class:`BMVert`
      :arg fallback: Return this value if nothing is found.
      :return: The edge found or None
      :rtype: :class:`BMEdge`


   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`BMesh.verts`, :class:`BMesh.edges`, :class:`BMesh.faces`
         works but wont result in each element having a valid index, insted its order in the sequence will be set.


   .. method:: new(verts, example=None)
   
      Create a new edge from a given pair of verts.
   
      :arg verts: Vertex pair.
      :type verts: pair of :class:`BMVert`
      :arg example: Existing edge to initialize settings (optional argument).
      :type example: :class:`BMEdge`
      :return: The newly created edge.
      :rtype: :class:`BMEdge`


   .. method:: remove(edge)
   
      Remove an edge.


   .. method:: sort(key=None, reverse=False)
   
      Sort the elements of this sequence, using an optional custom sort key.
      Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.
   
      :arg key: The key that sets the ordering of the elements.
      :type key: :function: returning a number
      :arg reverse: Reverse the order of the elements
      :type reverse: :boolean:
   
      .. note::
   
         When the 'key' argument is not provided, the elements are reordered following their current index value.
         In particular this can be used by setting indices manually before calling this method.
   
      .. warning::
   
         Existing references to the N'th element, will continue to point the data at that index.


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`BMLayerAccessEdge`




.. class:: BMFaceSeq


   .. method:: ensure_lookup_table()
   
      Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg ``bm.verts[index]``.
   
      This needs to be called again after adding/removing data in this sequence.


   .. method:: get(verts, fallback=None)
   
      Return a face which uses the **verts** passed.
   
      :arg verts: Sequence of verts.
      :type verts: :class:`BMVert`
      :arg fallback: Return this value if nothing is found.
      :return: The face found or None
      :rtype: :class:`BMFace`


   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`BMesh.verts`, :class:`BMesh.edges`, :class:`BMesh.faces`
         works but wont result in each element having a valid index, insted its order in the sequence will be set.


   .. method:: new(verts, example=None)
   
      Create a new face from a given set of verts.
   
      :arg verts: Sequence of 3 or more verts.
      :type verts: :class:`BMVert`
      :arg example: Existing face to initialize settings (optional argument).
      :type example: :class:`BMFace`
      :return: The newly created face.
      :rtype: :class:`BMFace`


   .. method:: remove(face)
   
      Remove a face.


   .. method:: sort(key=None, reverse=False)
   
      Sort the elements of this sequence, using an optional custom sort key.
      Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.
   
      :arg key: The key that sets the ordering of the elements.
      :type key: :function: returning a number
      :arg reverse: Reverse the order of the elements
      :type reverse: :boolean:
   
      .. note::
   
         When the 'key' argument is not provided, the elements are reordered following their current index value.
         In particular this can be used by setting indices manually before calling this method.
   
      .. warning::
   
         Existing references to the N'th element, will continue to point the data at that index.


   .. attribute:: active

      active face.
      
      :type: :class:`BMFace` or None


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`BMLayerAccessFace`




.. class:: BMLoopSeq


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`BMLayerAccessLoop`




.. class:: BMIter

   Internal BMesh type for looping over verts/faces/edges,
   used for iterating over :class:`BMElemSeq` types.



Selection History
-----------------

.. class:: BMEditSelSeq


   .. method:: add(element)
   
      Add an element to the selection history (no action taken if its already added).


   .. method:: clear()
   
      Empties the selection history.


   .. method:: discard(element)
   
      Discard an element from the selection history.
   
      Like remove but doesn't raise an error when the elements not in the selection list.


   .. method:: remove(element)
   
      Remove an element from the selection history.


   .. method:: validate()
   
      Ensures all elements in the selection history are selected.


   .. attribute:: active

      The last selected element or None (read-only).
      
      :type: :class:`BMVert`, :class:`BMEdge` or :class:`BMFace`




.. class:: BMEditSelIter




Custom-Data Layer Access
------------------------

.. class:: BMLayerAccessVert

   Exposes custom-data layer attributes.

   .. attribute:: bevel_weight

      Bevel weight float in [0 - 1].
      
      :type: :class:`BMLayerCollection`


   .. attribute:: deform

      Vertex deform weight :class:`BMDeformVert` (TODO).
      
      type: :class:`BMLayerCollection`


   .. attribute:: float

      Generic float custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: int

      Generic int custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: paint_mask

      Accessor for paint mask layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: shape

      Vertex shapekey absolute location (as a 3D Vector).
      
      :type: :class:`BMLayerCollection`


   .. attribute:: skin

      Accessor for skin layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      type: :class:`BMLayerCollection`




.. class:: BMLayerAccessEdge

   Exposes custom-data layer attributes.

   .. attribute:: bevel_weight

      Bevel weight float in [0 - 1].
      
      :type: :class:`BMLayerCollection`


   .. attribute:: crease

      Edge crease for subsurf - float in [0 - 1].
      
      :type: :class:`BMLayerCollection`


   .. attribute:: float

      Generic float custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: freestyle

      Accessor for Freestyle edge layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: int

      Generic int custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      type: :class:`BMLayerCollection`




.. class:: BMLayerAccessFace

   Exposes custom-data layer attributes.

   .. attribute:: float

      Generic float custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: freestyle

      Accessor for Freestyle face layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: int

      Generic int custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      type: :class:`BMLayerCollection`


   .. attribute:: tex

      Accessor for :class:`BMTexPoly` layer (TODO).
      
      type: :class:`BMLayerCollection`




.. class:: BMLayerAccessLoop

   Exposes custom-data layer attributes.

   .. attribute:: color

      Accessor for vertex color layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: float

      Generic float custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: int

      Generic int custom-data layer.
      
      type: :class:`BMLayerCollection`


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      type: :class:`BMLayerCollection`


   .. attribute:: uv

      Accessor for :class:`BMLoopUV` UV (as a 2D Vector).
      
      type: :class:`BMLayerCollection`




.. class:: BMLayerCollection

   Gives access to a collection of custom-data layers of the same type and behaves like python dictionaries, except for the ability to do list like index access.

   .. method:: get(key, default=None)
   
      Returns the value of the layer matching the key or default
      when not found (matches pythons dictionary function of the same name).
   
      :arg key: The key associated with the layer.
      :type key: string
      :arg default: Optional argument for the value to return if
         *key* is not found.
      :type default: Undefined


   .. method:: items()
   
      Return the identifiers of collection members
      (matching pythons dict.items() functionality).
   
      :return: (key, value) pairs for each member of this collection.
      :rtype: list of tuples


   .. method:: keys()
   
      Return the identifiers of collection members
      (matching pythons dict.keys() functionality).
   
      :return: the identifiers for each member of this collection.
      :rtype: list of strings


   .. method:: new(name)
   
      Create a new layer
   
      :arg name: Optional name argument (will be made unique).
      :type name: string
      :return: The newly created layer.
      :rtype: :class:`BMLayerItem`


   .. method:: remove(layer)
   
      Remove a layer
   
      :arg layer: The layer to remove.
      :type layer: :class:`BMLayerItem`


   .. method:: values()
   
      Return the values of collection
      (matching pythons dict.values() functionality).
   
      :return: the members of this collection.
      :rtype: list


   .. method:: verify()
   
      Create a new layer or return an existing active layer
   
      :return: The newly verified layer.
      :rtype: :class:`BMLayerItem`


   .. attribute:: active

      The active layer of this type (read-only).
      
      :type: :class:`BMLayerItem`


   .. attribute:: is_singleton

      True if there can exists only one layer of this type (read-only).
      
      :type: boolean




.. class:: BMLayerItem

   Exposes a single custom data layer, their main purpose is for use as item accessors to custom-data when used with vert/edge/face/loop data.

   .. method:: copy_from(other)
   
      Return a copy of the layer
   
      :arg other: Another layer to copy from.
      :arg other: :class:`BMLayerItem`


   .. attribute:: name

      The layers unique name (read-only).
      
      :type: string




Custom-Data Layer Types
-----------------------

.. class:: BMLoopUV


   .. attribute:: pin_uv

      UV pin state.
      
      :type: boolean


   .. attribute:: select

      UV select state.
      
      :type: boolean


   .. attribute:: select_edge

      UV edge select state.
      
      :type: boolean


   .. attribute:: uv

      Loops UV (as a 2D Vector).
      
      :type: :class:`mathutils.Vector`




.. class:: BMDeformVert


   .. method:: clear()
   
      Clears all weights.


   .. method:: get(key, default=None)
   
      Returns the deform weight matching the key or default
      when not found (matches pythons dictionary function of the same name).
   
      :arg key: The key associated with deform weight.
      :type key: int
      :arg default: Optional argument for the value to return if
         *key* is not found.
      :type default: Undefined


   .. method:: items()
   
      Return (group, weight) pairs for this vertex
      (matching pythons dict.items() functionality).
   
      :return: (key, value) pairs for each deform weight of this vertex.
      :rtype: list of tuples


   .. method:: keys()
   
      Return the group indices used by this vertex
      (matching pythons dict.keys() functionality).
   
      :return: the deform group this vertex uses
      :rtype: list of ints


   .. method:: values()
   
      Return the weights of the deform vertex
      (matching pythons dict.values() functionality).
   
      :return: The weights that influence this vertex
      :rtype: list of floats




