BMesh Module (bmesh)
====================

.. module:: bmesh

This module provides access to blenders bmesh data structures.

.. include:: include__bmesh.rst

.. method:: from_edit_mesh(mesh)

   Return a BMesh from this mesh, currently the mesh must already be in editmode.

   :arg mesh: The editmode mesh.
   :type mesh: :class:`bpy.types.Mesh`
   :return: the BMesh associated with this mesh.
   :rtype: :class:`bmesh.types.BMesh`


.. method:: new(use_operators=True)

   :arg use_operators: Support calling operators in :mod:`bmesh.ops` (uses some extra memory per vert/edge/face).
   :type use_operators: bool
   :return: Return a new, empty BMesh.
   :rtype: :class:`bmesh.types.BMesh`


.. method:: update_edit_mesh(mesh, tessface=True, destructive=True)

   Update the mesh after changes to the BMesh in editmode, 
   optionally recalculating n-gon tessellation.

   :arg mesh: The editmode mesh.
   :type mesh: :class:`bpy.types.Mesh`
   :arg tessface: Option to recalculate n-gon tessellation.
   :type tessface: boolean
   :arg destructive: Use when geometry has been added or removed.
   :type destructive: boolean


