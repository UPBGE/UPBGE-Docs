bpy_extras submodule (bpy_extras.mesh_utils)
============================================

.. module:: bpy_extras.mesh_utils

.. function:: mesh_linked_uv_islands(mesh)

   Splits the mesh into connected polygons, use this for seperating cubes from
   other mesh elements within 1 mesh datablock.
   
   :arg mesh: the mesh used to group with.
   :type mesh: :class:`bpy.types.Mesh`
   :return: lists of lists containing polygon indices
   :rtype: list

.. function:: mesh_linked_tessfaces(mesh)

   Splits the mesh into connected faces, use this for seperating cubes from
   other mesh elements within 1 mesh datablock.
   
   :arg mesh: the mesh used to group with.
   :type mesh: :class:`bpy.types.Mesh`
   :return: lists of lists containing faces.
   :rtype: list

.. function:: edge_face_count_dict(mesh)

   :return: dict of edge keys with their value set to the number of
      faces using each edge.
   :rtype: dict

.. function:: edge_face_count(mesh)

   :return: list face users for each item in mesh.edges.
   :rtype: list

.. function:: edge_loops_from_tessfaces(mesh, tessfaces=None, seams=())

   Edge loops defined by faces
   
   Takes me.tessfaces or a list of faces and returns the edge loops
   These edge loops are the edges that sit between quads, so they dont touch
   1 quad, note: not connected will make 2 edge loops,
   both only containing 2 edges.
   
   return a list of edge key lists
   [[(0, 1), (4, 8), (3, 8)], ...]
   
   :arg mesh: the mesh used to get edge loops from.
   :type mesh: :class:`bpy.types.Mesh`
   :arg tessfaces: optional face list to only use some of the meshes faces.
   :type tessfaces: :class:`bpy.types.MeshTessFace`, sequence or or NoneType
   :return: return a list of edge vertex index lists.
   :rtype: list

.. function:: edge_loops_from_edges(mesh, edges=None)

   Edge loops defined by edges
   
   Takes me.edges or a list of edges and returns the edge loops
   
   return a list of vertex indices.
   [ [1, 6, 7, 2], ...]
   
   closed loops have matching start and end values.

.. function:: ngon_tessellate(from_data, indices, fix_loops=True)

   Takes a polyline of indices (fgon) and returns a list of face
   index lists. Designed to be used for importers that need indices for an
   fgon to create from existing verts.
   
   :arg from_data: either a mesh, or a list/tuple of vectors.
   :type from_data: list or :class:`bpy.types.Mesh`
   :arg indices: a list of indices to use this list
      is the ordered closed polyline
      to fill, and can be a subset of the data given.
   :type indices: list
   :arg fix_loops: If this is enabled polylines
      that use loops to make multiple
      polylines are delt with correctly.
   :type fix_loops: bool

.. function:: face_random_points(num_points, tessfaces)

   Generates a list of random points over mesh tessfaces.
   
   :arg num_points: the number of random points to generate on each face.
   :type int:
   :arg tessfaces: list of the faces to generate points on.
   :type tessfaces: :class:`bpy.types.MeshTessFace`, sequence
   :return: list of random points over all faces.
   :rtype: list

