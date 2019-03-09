BMesh Geometry Utilities (bmesh.geometry)
=========================================

.. module:: bmesh.geometry

This module provides access to bmesh geometry evaluation functions.

.. method:: intersect_face_point(face, point)

   Tests if the projection of a point is inside a face (using the face's normal).

   :arg face: The face to test.
   :type face: :class:`bmesh.types.BMFace`
   :arg point: The point to test.
   :type point: float triplet
   :return: True when the projection of the point is in the face.
   :rtype: bool


