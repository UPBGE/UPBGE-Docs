BMesh Utilities (bmesh.utils)
=============================

.. module:: bmesh.utils

This module provides access to blenders bmesh data structures.

.. method:: edge_rotate(edge, ccw=False)

   Rotate the edge and return the newly created edge.
   If rotating the edge fails, None will be returned.

   :arg edge: The edge to rotate.
   :type edge: :class:`bmesh.types.BMEdge`
   :arg ccw: When True the edge will be rotated counter clockwise.
   :type ccw: boolean
   :return: The newly rotated edge.
   :rtype: :class:`bmesh.types.BMEdge`


.. method:: edge_split(edge, vert, fac)

   Split an edge, return the newly created data.

   :arg edge: The edge to split.
   :type edge: :class:`bmesh.types.BMEdge`
   :arg vert: One of the verts on the edge, defines the split direction.
   :type vert: :class:`bmesh.types.BMVert`
   :arg fac: The point on the edge where the new vert will be created [0 - 1].
   :type fac: float
   :return: The newly created (edge, vert) pair.
   :rtype: tuple


.. method:: face_flip(faces)

   Flip the faces direction.

   :arg face: Face to flip.
   :type face: :class:`bmesh.types.BMFace`


.. method:: face_join(faces, remove=True)

   Joins a sequence of faces.

   :arg faces: Sequence of faces.
   :type faces: :class:`bmesh.types.BMFace`
   :arg remove: Remove the edges and vertices between the faces.
   :type remove: boolean
   :return: The newly created face or None on failure.
   :rtype: :class:`bmesh.types.BMFace`


.. method:: face_split(face, vert_a, vert_b, coords=(), use_exist=True, example=None)

   Face split with optional intermediate points.

   :arg face: The face to cut.
   :type face: :class:`bmesh.types.BMFace`
   :arg vert_a: First vertex to cut in the face (face must contain the vert).
   :type vert_a: :class:`bmesh.types.BMVert`
   :arg vert_b: Second vertex to cut in the face (face must contain the vert).
   :type vert_b: :class:`bmesh.types.BMVert`
   :arg coords: Optional argument to define points inbetween *vert_a* and *vert_b*.
   :type coords: sequence of float triplets
   :arg use_exist: .Use an existing edge if it exists (Only used when *coords* argument is empty or omitted)
   :type use_exist: boolean
   :arg example: Newly created edge will copy settings from this one.
   :type example: :class:`bmesh.types.BMEdge`
   :return: The newly created face or None on failure.
   :rtype: (:class:`bmesh.types.BMFace`, :class:`bmesh.types.BMLoop`) pair


.. method:: face_split_edgenet(face, edgenet)

   Splits a face into any number of regions defined by an edgenet.

   :arg face: The face to split.
   :type face: :class:`bmesh.types.BMFace`
   :arg face: The face to split.
   :type face: :class:`bmesh.types.BMFace`
   :arg edgenet: Sequence of edges.
   :type edgenet: :class:`bmesh.types.BMEdge`
   :return: The newly created faces.
   :rtype: tuple of (:class:`bmesh.types.BMFace`)

   .. note::

      Regions defined by edges need to connect to the face, otherwise they're ignored as loose edges.


.. method:: face_vert_separate(face, vert)

   Rip a vertex in a face away and add a new vertex.

   :arg face: The face to separate.
   :type face: :class:`bmesh.types.BMFace`
   :arg vert: A vertex in the face to separate.
   :type vert: :class:`bmesh.types.BMVert`
   :return vert: The newly created vertex or None on failure.
   :rtype vert: :class:`bmesh.types.BMVert`

   .. note::

      This is the same as loop_separate, and has only been added for convenience.


.. method:: loop_separate(loop)

   Rip a vertex in a face away and add a new vertex.

   :arg loop: The loop to separate.
   :type loop: :class:`bmesh.types.BMLoop`
   :return vert: The newly created vertex or None on failure.
   :rtype vert: :class:`bmesh.types.BMVert`


.. method:: vert_collapse_edge(vert, edge)

   Collapse a vertex into an edge.

   :arg vert: The vert that will be collapsed.
   :type vert: :class:`bmesh.types.BMVert`
   :arg edge: The edge to collapse into.
   :type edge: :class:`bmesh.types.BMEdge`
   :return: The resulting edge from the collapse operation.
   :rtype: :class:`bmesh.types.BMEdge`


.. method:: vert_collapse_faces(vert, edge, fac, join_faces)

   Collapses a vertex that has only two manifold edges onto a vertex it shares an edge with.

   :arg vert: The vert that will be collapsed.
   :type vert: :class:`bmesh.types.BMVert`
   :arg edge: The edge to collapse into.
   :type edge: :class:`bmesh.types.BMEdge`
   :arg fac: The factor to use when merging customdata [0 - 1].
   :type fac: float
   :return: The resulting edge from the collapse operation.
   :rtype: :class:`bmesh.types.BMEdge`


.. method:: vert_dissolve(vert)

   Dissolve this vertex (will be removed).

   :arg vert: The vert to be dissolved.
   :type vert: :class:`bmesh.types.BMVert`
   :return: True when the vertex dissolve is successful.
   :rtype: boolean


.. method:: vert_separate(vert, edges)

   Separate this vertex at every edge.

   :arg vert: The vert to be separated.
   :type vert: :class:`bmesh.types.BMVert`
   :arg edges: The edges to separated.
   :type edges: :class:`bmesh.types.BMEdge`
   :return: The newly separated verts (including the vertex passed).
   :rtype: tuple of :class:`bmesh.types.BMVert`


.. method:: vert_splice(vert, vert_target)

   Splice vert into vert_target.

   :arg vert: The vertex to be removed.
   :type vert: :class:`bmesh.types.BMVert`
   :arg vert_target: The vertex to use.
   :type vert_target: :class:`bmesh.types.BMVert`

   .. note:: The verts mustn't share an edge or face.


