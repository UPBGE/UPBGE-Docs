Mesh(ID)
========

.. module:: bpy.types

Mesh Data
+++++++++

The mesh data is accessed in object mode and intended for compact storage,
for more flexible mesh editing from python see :mod:`bmesh`.

Blender stores 4 main arrays to define mesh geometry.

- :class:`Mesh.vertices` (3 points in space)
- :class:`Mesh.edges` (reference 2 vertices)
- :class:`Mesh.loops` (reference a single vertex and edge)
- :class:`Mesh.polygons`: (reference a range of loops)


Each polygon reference a slice in the loop array, this way, polygons do not store vertices or corner data such as UV's directly,
only a reference to loops that the polygon uses.

:class:`Mesh.loops`, :class:`Mesh.uv_layers` :class:`Mesh.vertex_colors` are all aligned so the same polygon loop
indices can be used to find the UV's and vertex colors as with as the vertices.

To compare mesh API options see: :ref:`NGons and Tessellation Faces <info_gotcha_mesh_faces>`


This example script prints the vertices and UV's for each polygon, assumes the active object is a mesh with UVs.

.. literalinclude:: ..\examples\bpy.types.Mesh.py
   :lines: 27-

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Mesh(ID)

   Mesh data-block defining geometric surfaces

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: auto_smooth_angle

      Maximum angle between face normals that will be considered as smooth (unused if custom split normals data are available)

      :type: float in [0, 3.14159], default 3.14159

   .. attribute:: auto_texspace

      Adjust active object's texture space automatically when transforming object

      :type: boolean, default False

   .. data:: cycles

      Cycles mesh settings

      :type: :class:`CyclesMeshSettings`, (readonly)

   .. data:: edges

      Edges of the mesh

      :type: :class:`MeshEdges` :class:`bpy_prop_collection` of :class:`MeshEdge`, (readonly)

   .. data:: has_custom_normals

      True if there are custom split normals data in this mesh

      :type: boolean, default False, (readonly)

   .. data:: is_editmode

      True when used in editmode

      :type: boolean, default False, (readonly)

   .. data:: loops

      Loops of the mesh (polygon corners)

      :type: :class:`MeshLoops` :class:`bpy_prop_collection` of :class:`MeshLoop`, (readonly)

   .. data:: materials

      :type: :class:`IDMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. data:: polygon_layers_float

      :type: :class:`PolygonFloatProperties` :class:`bpy_prop_collection` of :class:`MeshPolygonFloatPropertyLayer`, (readonly)

   .. data:: polygon_layers_int

      :type: :class:`PolygonIntProperties` :class:`bpy_prop_collection` of :class:`MeshPolygonIntPropertyLayer`, (readonly)

   .. data:: polygon_layers_string

      :type: :class:`PolygonStringProperties` :class:`bpy_prop_collection` of :class:`MeshPolygonStringPropertyLayer`, (readonly)

   .. data:: polygons

      Polygons of the mesh

      :type: :class:`MeshPolygons` :class:`bpy_prop_collection` of :class:`MeshPolygon`, (readonly)

   .. data:: shape_keys

      :type: :class:`Key`, (readonly)

   .. attribute:: show_double_sided

      Display the mesh with double or single sided lighting (OpenGL only)

      :type: boolean, default False

   .. attribute:: show_edge_bevel_weight

      Display weights created for the Bevel modifier

      :type: boolean, default False

   .. attribute:: show_edge_crease

      Display creases created for Subdivision Surface modifier

      :type: boolean, default False

   .. attribute:: show_edge_seams

      Display UV unwrapping seams

      :type: boolean, default False

   .. attribute:: show_edge_sharp

      Display sharp edges, used with the Edge Split modifier

      :type: boolean, default False

   .. attribute:: show_edges

      Display selected edges using highlights in the 3D view and UV editor

      :type: boolean, default False

   .. attribute:: show_extra_edge_angle

      Display selected edge angle, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_edge_length

      Display selected edge lengths, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_face_angle

      Display the angles in the selected edges, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_face_area

      Display the area of selected faces, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_indices

      Display the index numbers of selected vertices, edges, and faces

      :type: boolean, default False

   .. attribute:: show_faces

      Display all faces as shades in the 3D view and UV editor

      :type: boolean, default False

   .. attribute:: show_freestyle_edge_marks

      Display Freestyle edge marks, used with the Freestyle renderer

      :type: boolean, default False

   .. attribute:: show_freestyle_face_marks

      Display Freestyle face marks, used with the Freestyle renderer

      :type: boolean, default False

   .. attribute:: show_normal_face

      Display face normals as lines

      :type: boolean, default False

   .. attribute:: show_normal_loop

      Display vertex-per-face normals as lines

      :type: boolean, default False

   .. attribute:: show_normal_vertex

      Display vertex normals as lines

      :type: boolean, default False

   .. attribute:: show_statvis

      Display statistical information about the mesh

      :type: boolean, default False

   .. attribute:: show_weight

      Draw weights in editmode

      :type: boolean, default False

   .. data:: skin_vertices

      All skin vertices

      :type: :class:`bpy_prop_collection` of :class:`MeshSkinVertexLayer`, (readonly)

   .. data:: tessface_uv_textures

      All UV maps for tessellated faces (read-only, for use by renderers)

      :type: :class:`TessfaceUVTextures` :class:`bpy_prop_collection` of :class:`MeshTextureFaceLayer`, (readonly)

   .. data:: tessface_vertex_colors

      All tessellated face colors (read-only, for use by renderers)

      :type: :class:`VertexColors` :class:`bpy_prop_collection` of :class:`MeshColorLayer`, (readonly)

   .. data:: tessfaces

      Tessellated faces of the mesh (derived from polygons)

      :type: :class:`MeshTessFaces` :class:`bpy_prop_collection` of :class:`MeshTessFace`, (readonly)

   .. attribute:: texco_mesh

      Derive texture coordinates from another mesh

      :type: :class:`Mesh`

   .. attribute:: texspace_location

      Texture space location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: texspace_size

      Texture space size

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: texture_mesh

      Use another mesh for texture indices (vertex indices must be aligned)

      :type: :class:`Mesh`

   .. data:: total_edge_sel

      Selected edge count in editmode

      :type: int in [0, inf], default 0, (readonly)

   .. data:: total_face_sel

      Selected face count in editmode

      :type: int in [0, inf], default 0, (readonly)

   .. data:: total_vert_sel

      Selected vertex count in editmode

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: use_auto_smooth

      Auto smooth (based on smooth/sharp faces/edges and angle between faces), or use custom split normals data if available

      :type: boolean, default False

   .. attribute:: use_auto_texspace

      Adjust active object's texture space automatically when transforming object

      :type: boolean, default False

   .. attribute:: use_customdata_edge_bevel

      :type: boolean, default False

   .. attribute:: use_customdata_edge_crease

      :type: boolean, default False

   .. attribute:: use_customdata_vertex_bevel

      :type: boolean, default False

   .. attribute:: use_mirror_topology

      Use topology based mirroring (for when both sides of mesh have matching, unique topology)

      :type: boolean, default False

   .. attribute:: use_mirror_x

      X Axis mirror editing

      :type: boolean, default False

   .. attribute:: use_paint_mask

      Face selection masking for painting

      :type: boolean, default False

   .. attribute:: use_paint_mask_vertex

      Vertex selection masking for painting (weight paint only)

      :type: boolean, default False

   .. attribute:: uv_layer_clone

      UV loop layer to be used as cloning source

      :type: :class:`MeshUVLoopLayer`

   .. attribute:: uv_layer_clone_index

      Clone UV loop layer index

      :type: int in [0, inf], default 0

   .. attribute:: uv_layer_stencil

      UV loop layer to mask the painted area

      :type: :class:`MeshUVLoopLayer`

   .. attribute:: uv_layer_stencil_index

      Mask UV loop layer index

      :type: int in [0, inf], default 0

   .. data:: uv_layers

      All UV loop layers

      :type: :class:`UVLoopLayers` :class:`bpy_prop_collection` of :class:`MeshUVLoopLayer`, (readonly)

   .. attribute:: uv_texture_clone

      UV map to be used as cloning source

      :type: :class:`MeshTexturePolyLayer`

   .. attribute:: uv_texture_clone_index

      Clone UV map index

      :type: int in [0, inf], default 0

   .. attribute:: uv_texture_stencil

      UV map to mask the painted area

      :type: :class:`MeshTexturePolyLayer`

   .. attribute:: uv_texture_stencil_index

      Mask UV map index

      :type: int in [0, inf], default 0

   .. data:: uv_textures

      All UV maps

      :type: :class:`UVTextures` :class:`bpy_prop_collection` of :class:`MeshTexturePolyLayer`, (readonly)

   .. data:: vertex_colors

      All vertex colors

      :type: :class:`LoopColors` :class:`bpy_prop_collection` of :class:`MeshLoopColorLayer`, (readonly)

   .. data:: vertex_layers_float

      :type: :class:`VertexFloatProperties` :class:`bpy_prop_collection` of :class:`MeshVertexFloatPropertyLayer`, (readonly)

   .. data:: vertex_layers_int

      :type: :class:`VertexIntProperties` :class:`bpy_prop_collection` of :class:`MeshVertexIntPropertyLayer`, (readonly)

   .. data:: vertex_layers_string

      :type: :class:`VertexStringProperties` :class:`bpy_prop_collection` of :class:`MeshVertexStringPropertyLayer`, (readonly)

   .. data:: vertex_paint_masks

      Vertex paint mask

      :type: :class:`bpy_prop_collection` of :class:`MeshPaintMaskLayer`, (readonly)

   .. data:: vertices

      Vertices of the mesh

      :type: :class:`MeshVertices` :class:`bpy_prop_collection` of :class:`MeshVertex`, (readonly)

   .. data:: edge_keys

      (readonly)

   .. method:: transform(matrix, shape_keys=False)

      Transform mesh vertices by a matrix (Warning: inverts normals if matrix is negative)

      :arg matrix:

         Matrix

      :type matrix: float multi-dimensional array of 4 * 4 items in [-inf, inf]
      :arg shape_keys:

         Transform Shape Keys

      :type shape_keys: boolean, (optional)

   .. method:: flip_normals()

      Invert winding of all polygons (clears tessellation, does not handle custom normals)


   .. method:: calc_normals()

      Calculate vertex normals


   .. method:: create_normals_split()

      Empty split vertex normals


   .. method:: calc_normals_split()

      Calculate split vertex normals, which preserve sharp edges


   .. method:: free_normals_split()

      Free split vertex normals


   .. method:: split_faces(free_loop_normals=True)

      Split faces based on the edge angle

      :arg free_loop_normals:

         Free Loop Notmals, Free loop normals custom data layer

      :type free_loop_normals: boolean, (optional)

   .. method:: calc_tangents(uvmap="")

      Compute tangents and bitangent signs, to be used together with the split normals to get a complete tangent space for normal mapping (split normals are also computed if not yet present)

      :arg uvmap:

         Name of the UV map to use for tangent space computation

      :type uvmap: string, (optional, never None)

   .. method:: free_tangents()

      Free tangents


   .. method:: calc_tessface(free_mpoly=False)

      Calculate face tessellation (supports editmode too)

      :arg free_mpoly:

         Free MPoly, Free data used by polygons and loops. WARNING: This destructive operation removes regular faces, only used on temporary mesh data-blocks to reduce memory footprint of render engines and export scripts

      :type free_mpoly: boolean, (optional)

   .. method:: calc_smooth_groups(use_bitflags=False)

      Calculate smooth groups from sharp edges

      :arg use_bitflags:

         Produce bitflags groups instead of simple numeric values

      :type use_bitflags: boolean, (optional)
      :return (poly_groups, groups):
         `poly_groups`, Smooth Groups, int array of 1 items in [-inf, inf]

         `groups`, Total number of groups, int in [0, inf]


   .. method:: normals_split_custom_set(normals)

      Define custom split normals of this mesh (use zero-vectors to keep auto ones)

      :arg normals:

         Normals

      :type normals: float multi-dimensional array of 1 * 3 items in [-1, 1]

   .. method:: normals_split_custom_set_from_vertices(normals)

      Define custom split normals of this mesh, from vertices' normals (use zero-vectors to keep auto ones)

      :arg normals:

         Normals

      :type normals: float multi-dimensional array of 1 * 3 items in [-1, 1]

   .. method:: update(calc_edges=False, calc_tessface=False)

      update

      :arg calc_edges:

         Calculate Edges, Force recalculation of edges

      :type calc_edges: boolean, (optional)
      :arg calc_tessface:

         Calculate Tessellation, Force recalculation of tessellation faces

      :type calc_tessface: boolean, (optional)

   .. method:: unit_test_compare(mesh=None)

      unit_test_compare

      :arg mesh:

         Mesh to compare to

      :type mesh: :class:`Mesh`, (optional)
      :return:

         Return value, String description of result of comparison

      :rtype: string, (never None)

   .. method:: validate(verbose=False, clean_customdata=True)

      Validate geometry, return True when the mesh has had invalid geometry corrected/removed

      :arg verbose:

         Verbose, Output information about the errors found

      :type verbose: boolean, (optional)
      :arg clean_customdata:

         Clean Custom Data, Remove temp/cached custom-data layers, like e.g. normals...

      :type clean_customdata: boolean, (optional)
      :return:

         Result

      :rtype: boolean

   .. method:: validate_material_indices()

      Validate material indices of polygons, return True when the mesh has had invalid indices corrected (to default 0)

      :return:

         Result

      :rtype: boolean

   .. method:: from_pydata(vertices, edges, faces)

      Make a mesh from a list of vertices/edges/faces
      Until we have a nicer way to make geometry, use this.
      
      :arg vertices:
      
         float triplets each representing (X, Y, Z)
         eg: [(0.0, 1.0, 0.5), ...].
      
      :type vertices: iterable object
      :arg edges:
      
         int pairs, each pair contains two indices to the
         *vertices* argument. eg: [(1, 2), ...]
      
      :type edges: iterable object
      :arg faces:
      
         iterator of faces, each faces contains three or more indices to
         the *vertices* argument. eg: [(5, 6, 8, 9), (1, 2, 3), ...]
      
      :type faces: iterable object
      
      .. warning::
      
         Invalid mesh data
         *(out of range indices, edges with matching indices,
         2 sided faces... etc)* are **not** prevented.
         If the data used for mesh creation isn't known to be valid,
         run :class:`Mesh.validate` after this function.

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

   * :mod:`bpy.context.mesh`
   * :class:`BlendData.meshes`
   * :class:`BlendDataMeshes.new`
   * :class:`BlendDataMeshes.new_from_object`
   * :class:`BlendDataMeshes.remove`
   * :class:`EditObjectActuator.mesh`
   * :class:`Mesh.texco_mesh`
   * :class:`Mesh.texture_mesh`
   * :class:`Mesh.unit_test_compare`
   * :class:`GameObjectSettings.predefined_bound`
   * :class:`Object.to_mesh`

