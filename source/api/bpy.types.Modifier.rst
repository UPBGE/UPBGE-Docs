Modifier(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ArmatureModifier`, :class:`ArrayModifier`, :class:`BevelModifier`, :class:`BooleanModifier`, :class:`BuildModifier`, :class:`CastModifier`, :class:`ClothModifier`, :class:`CollisionModifier`, :class:`CorrectiveSmoothModifier`, :class:`CurveModifier`, :class:`DataTransferModifier`, :class:`DecimateModifier`, :class:`DisplaceModifier`, :class:`DynamicPaintModifier`, :class:`EdgeSplitModifier`, :class:`ExplodeModifier`, :class:`FluidSimulationModifier`, :class:`HookModifier`, :class:`LaplacianDeformModifier`, :class:`LaplacianSmoothModifier`, :class:`LatticeModifier`, :class:`MaskModifier`, :class:`MeshCacheModifier`, :class:`MeshDeformModifier`, :class:`MeshSequenceCacheModifier`, :class:`MirrorModifier`, :class:`MultiresModifier`, :class:`NormalEditModifier`, :class:`OceanModifier`, :class:`ParticleInstanceModifier`, :class:`ParticleSystemModifier`, :class:`RemeshModifier`, :class:`ScrewModifier`, :class:`ShrinkwrapModifier`, :class:`SimpleDeformModifier`, :class:`SkinModifier`, :class:`SmokeModifier`, :class:`SmoothModifier`, :class:`SoftBodyModifier`, :class:`SolidifyModifier`, :class:`SubsurfModifier`, :class:`SurfaceDeformModifier`, :class:`SurfaceModifier`, :class:`TriangulateModifier`, :class:`UVProjectModifier`, :class:`UVWarpModifier`, :class:`VertexWeightEditModifier`, :class:`VertexWeightMixModifier`, :class:`VertexWeightProximityModifier`, :class:`WarpModifier`, :class:`WaveModifier`, :class:`WireframeModifier`

.. class:: Modifier(bpy_struct)

   Modifier affecting the geometry data of an object

   .. attribute:: name

      Modifier name

      :type: string, default "", (never None)

   .. attribute:: show_expanded

      Set modifier expanded in the user interface

      :type: boolean, default False

   .. attribute:: show_in_editmode

      Display modifier in Edit mode

      :type: boolean, default False

   .. attribute:: show_on_cage

      Adjust edit cage to modifier result

      :type: boolean, default False

   .. attribute:: show_render

      Use modifier during render

      :type: boolean, default False

   .. attribute:: show_viewport

      Display modifier in viewport

      :type: boolean, default False

   .. data:: type

      * ``DATA_TRANSFER`` Data Transfer.
      * ``MESH_CACHE`` Mesh Cache.
      * ``MESH_SEQUENCE_CACHE`` Mesh Sequence Cache.
      * ``NORMAL_EDIT`` Normal Edit.
      * ``UV_PROJECT`` UV Project.
      * ``UV_WARP`` UV Warp.
      * ``VERTEX_WEIGHT_EDIT`` Vertex Weight Edit.
      * ``VERTEX_WEIGHT_MIX`` Vertex Weight Mix.
      * ``VERTEX_WEIGHT_PROXIMITY`` Vertex Weight Proximity.
      * ``ARRAY`` Array.
      * ``BEVEL`` Bevel.
      * ``BOOLEAN`` Boolean.
      * ``BUILD`` Build.
      * ``DECIMATE`` Decimate.
      * ``EDGE_SPLIT`` Edge Split.
      * ``MASK`` Mask.
      * ``MIRROR`` Mirror.
      * ``MULTIRES`` Multiresolution.
      * ``REMESH`` Remesh.
      * ``SCREW`` Screw.
      * ``SKIN`` Skin.
      * ``SOLIDIFY`` Solidify.
      * ``SUBSURF`` Subdivision Surface.
      * ``TRIANGULATE`` Triangulate.
      * ``WIREFRAME`` Wireframe, Generate a wireframe on the edges of a mesh.
      * ``ARMATURE`` Armature.
      * ``CAST`` Cast.
      * ``CORRECTIVE_SMOOTH`` Corrective Smooth.
      * ``CURVE`` Curve.
      * ``DISPLACE`` Displace.
      * ``HOOK`` Hook.
      * ``LAPLACIANSMOOTH`` Laplacian Smooth.
      * ``LAPLACIANDEFORM`` Laplacian Deform.
      * ``LATTICE`` Lattice.
      * ``MESH_DEFORM`` Mesh Deform.
      * ``SHRINKWRAP`` Shrinkwrap.
      * ``SIMPLE_DEFORM`` Simple Deform.
      * ``SMOOTH`` Smooth.
      * ``SURFACE_DEFORM`` Surface Deform.
      * ``WARP`` Warp.
      * ``WAVE`` Wave.
      * ``CLOTH`` Cloth.
      * ``COLLISION`` Collision.
      * ``DYNAMIC_PAINT`` Dynamic Paint.
      * ``EXPLODE`` Explode.
      * ``FLUID_SIMULATION`` Fluid Simulation.
      * ``OCEAN`` Ocean.
      * ``PARTICLE_INSTANCE`` Particle Instance.
      * ``PARTICLE_SYSTEM`` Particle System.
      * ``SMOKE`` Smoke.
      * ``SOFT_BODY`` Soft Body.
      * ``SURFACE`` Surface.

      :type: enum in ['DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'MASK', 'MIRROR', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'WIREFRAME', 'ARMATURE', 'CAST', 'CORRECTIVE_SMOOTH', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANSMOOTH', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID_SIMULATION', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SMOKE', 'SOFT_BODY', 'SURFACE'], default 'DATA_TRANSFER', (readonly)

   .. attribute:: use_apply_on_spline

      Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface

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

   * :class:`Object.modifiers`
   * :class:`ObjectModifiers.new`
   * :class:`ObjectModifiers.remove`
   * :class:`UILayout.template_modifier`

